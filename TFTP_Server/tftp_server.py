import random
import sys
from socket import *
from datetime import datetime, timedelta
import math
from _thread import *
import threading

error_codes = {0: "Error not defined. See error message (if any)",
        1: "File not found",
        2: "Access not permitted",
        3: "Disk full",
        4: "Illegal TFTP operation", 
        5: "Unknown transfer ID",
        6: "File exists",
        7: "User does not exist"
        }


def error(message):
    error = message[3]
    error_message = message[4:len(message)-1].decode()
    print("Error code: " + str(error) + ", " + str(error_message))
    return

def client_ack(ack_record, ack_counter, message_counter, socket, client_address, packet, total, to_send):
    """Loop to accept client acks and ensure correctness"""
    while True:
        cut_off = datetime.now() + timedelta(milliseconds = timeout)
        while datetime.now() < cut_off:
            message, client_address = socket.recvfrom(516)
            op_code = message[1]
            if op_code == 5:
                error(message)
                socket.close()
                return
            elif op_code == 4: 
                client_ack = message[3]
                if client_ack == total:
                    print("Data transmission complete")
                    packet = packet_writer(0, 3, 0, message_counter+1)
                    socket.sendto(packet, client_address)
                    socket.close()
                    return
                elif client_ack not in ack_record:
                    ack_record[client_ack] = 1
                    if client_ack <= total:
                        if client_ack == ack_counter:
                            message_counter += 1
                            packet = packet_writer(0, 3, 0, message_counter, to_send[message_counter-1])
                            socket.sendto(packet,client_address)
                            ack_counter+=1
                elif client_ack in ack_record:
                    message, client = socket.recvfrom(516)
        socket.sendto(packet, client_address)
    return

def rrq(sock, client_address, message):
    """
    Process read requests with inputs of the socket, the client, the data wanted, and the opcodes
    in order for the function to identify the ACKs, determine if there have been errors, and to append
    the DATA opcode and DATA block to the beginning of every block of DATA.
    """
    socket = ephemeral_socket(sock, client_address)

    message_split = message.split(b"\x00")
    filename = message_split[1].split(b"\x01")[1].decode("utf-8")
    with open(filename, "rb") as f:
        file_bytearray = bytearray(f.read())
    
    to_send = []

    for i in range(0, math.ceil(len(file_bytearray)//512)):
        packet = file_bytearray[512*i:512*(i+2)]
        to_send.append(packet)
    
    sent_tracker = len(to_send)
    packet = packet_writer(0, 3, 0, 1, to_send[0])
    ack_counter = 0
    socket.sendto(packet, client_address)
    ack_record = {}
    ack_counter += 1
    message_counter = 1
    
    client_ack(ack_record, ack_counter, message_counter, socket, client_address, packet, sent_tracker, to_send)
    lock_obj.release()

    return


def ephemeral_socket(sock, client_address):
    """Establish an ephemeral socket for the UDP"""
    ephem_socket = socket(AF_INET, SOCK_DGRAM)
    ephem_port = random.randint(2000, 65000)
    host = gethostname()
    ephem_socket.bind((host, ephem_port))
    
    return ephem_socket

def wrq(sock, client_address, message):
    """
    Proccess write requests with inputs of the socket, client address, data, and opcodes. This function
    receives data from the client, sends ACKs in response to the data received in order to get the next 
    data block using the opcodes to decipher whether the server has received a duplicate block, is missing
    a block, or has received an error.
    """
    socket = ephemeral_socket(sock, client_address)

    block_counter = 0
    packet = packet_writer(0, 4, 0, 0)   
    socket.sendto(packet, client_address)

    datablock_counter = 1 # expecting the first data block
    received_datablocks = {}
    message_split = message.split(b"\x00")
    filename = message_split[1].split(b"\x02")[1].decode("utf-8")
    newfile = open(filename, "wb")
    ack_sender(socket, received_datablocks, newfile, datablock_counter)
    
    lock_obj.release()
    return

def ack_sender(socket, received_datablocks, newfile, datablock_counter):
    while True:
        message, client_address = socket.recvfrom(516)
        op_code = message[1]

        if op_code == 5:
            error(message)
            socket.close()
            return

        elif op_code == 3:
            client_datablock = message[3]
            if client_datablock in received_datablocks:
                ack = client_datablock
                packet = packet_writer(0, 4, 0, ack)
                socket.sendto(packet, client_address)
            elif client_datablock not in received_datablocks:
                received_datablocks[client_datablock] = 1
                if len(message) < 516:
                    newfile.write(message[4:])
                    newfile.close()
                    packet = packet_writer(0, 4, 0, ack+1)
                    socket.sendto(packet, client_address)
                    print("All data written")
                    socket.close()
                    return
                else:
                    newfile.write(message[4:])
                    ack = client_datablock
                    packet = packet_writer(0, 4, 0, ack)
                    socket.sendto(packet, client_address)
                    datablock_counter += 1 
    return


def packet_writer(first, second, third, fourth, fifth=None):
    """Make a packet using the inputs"""
    packet = bytearray()
    packet.insert(0, first)
    packet.insert(1, second)
    packet.insert(2, third)
    packet.insert(3, fourth)
    if fifth:
        packet[4:4] = fifth
    return packet


if __name__ == "__main__":
    port = int(sys.argv[1])
    timeout = int(sys.argv[2])

    sock = socket(AF_INET, SOCK_DGRAM)
    host = gethostname()
    sock.bind((host, port))

    print("Server is ready to receive:")

    lock_obj = threading.Lock()

    while True:
    # threading whenever we get a new request
    # assign each new client request to a new thread
        message, client_address = sock.recvfrom(516) 
        op_code = message[1]
        lock_obj.acquire()

        if op_code == 1:
            func = rrq  
            #start_new_thread(func, (sock, client_address, message)
            #rrq(sock, client_address, message)

        elif op_code == 2:
            func = wrq
            #wrq(sock, client_address, message)
        start_new_thread(func, (sock, client_address, message))
    sock.close()
