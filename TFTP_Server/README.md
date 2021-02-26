The premisis of the RRQ adn WRQ functions is that there will always be one of four cases. Either there will be an error sent, resulting in an opcode of of 5. This crashes the program and sends a message detailing the error. 

The other cases are similar for RRQ and WRQ. 

(1) The ACK is not received in the case of the RRQ and the timeout is taken into play: if the timeout runs out, a datablock is resent and the while loop continues. 

(1) In the case of the WRQ, the client handles this. 

(2) If we have already received an ACK, and we check this by heading into our ack dictionary, we continue to wait to receive from the client. If the client does not send within the timeout, we send the datablock again.

(2) In the WRQ, if we have received the datablock already, we send the same ACK back.

(3) If the ACK is new in a RRQ, we send the next data block. If we are at our last datablock, we send an empty byte file, or the partially filled data block.

(3) If the datablock is new in WRQ, we send the ACK. If the databloack is less than 512 + 4 bytes long, the final ACK is sent and the server is closed. 

To run the program, run a proxy tftp client to communicate to the server. The server takes as arguments the host name, port number and time out, the first two which you must then communicate to the client. This program transfers a maximum of 256 blocks of data, handles packet loss, and implements the given timeout.