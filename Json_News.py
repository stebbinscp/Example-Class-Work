import json
import requests

def articles(request):
       articles = request['articles']
       for i in range(0,9):
              article = articles[i]
              print(f"\n{article['author']} | {article['source']['name']} | {article['title']}")
              print(f"{article['description']}")
              print("- - - - - - - - - - - - - - -")

def choose(user_choice, topic_options):
       """Use the user's choice to determine the articles wanted"""
       if user_choice == "1":
              url2 = ('http://newsapi.org/v2/'
              'top-headlines?'
              'country=us&'
              'apiKey=9e7b0f780ba64aff96d93c04918fd9f0')
              request = requests.get(url2).json() # top headlines
              articles(request)
              # pass # run code to grab top headlines
       elif user_choice == "2":
              for i in range(0,7):
                     print(f"[{i}] {topic_options[i]}")
              topic_choice = input("Please choose from the listed options: ")
              number_options = "0123456"
              # make sure the input is valid
              topic_dict = {"0":"Business", "1":"Entertainment", 
              "2":"General", "3":"Health", "4":"Science", 
              "5":"Sports", "6":"Technology"} # assign each number choice a topic as listed before
              if topic_choice in number_options:
                     # if we go with option search [2]
                     # pull from the dictionary their choice and insert it into the URL
                     url = f'http://newsapi.org/v2/top-headlines?country=us&category={topic_dict[topic_choice]}&apiKey=9e7b0f780ba64aff96d93c04918fd9f0'
                     request = requests.get(url)
                     j_request = request.json()
                     # no idea why but splitting it up seemed to do smth
                     articles(j_request)
              else:
                     print("Sorry, that was not a valid input.")
              # run code to search by category 
              # give a list of categories

def main():
       topic_options = ["Business", "Entertainment", "General", "Health", "Science", "Sports", "Technology"]
       user_choice = input("Please make a choice: [1] Top headlines [2] Search:  ")
       choose(user_choice, topic_options)

if __name__ == "__main__":
       main()
