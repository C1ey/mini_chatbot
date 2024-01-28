# Created by Cleon Simpson

import sys
import os
import socket
import time

def chatbot():
    Password = "Password1"
    Greeting= input("Password: ")
    if Greeting != Password:
        print("Incorrect Password, Access Denied!")
        exit()
    else:
        if Greeting == Password:
            print("Preparing Resources...")
            time.sleep(3)

#Define a dictionary of responses
            responses = {
                "default":"I am not sure how to respond to that",
                "hello":"Hello, how may I assist you?", 
                "What are you able to assist me with":"I can help you with general knowledge inquiries", 
                "goodbye":"Goodbye!"
            }
#Function to generate a response
            def generate_response(user_input):
                #convert th euser input to lowercase for case-insensitive matching
                user_input = user_input.lower()
                #Look for a response in the dictionary, use "default" if not found
                return responses.get(user_input, responses["default"])
            #Main chat loop
            print("Chatbot: Hello! Type 'goodbye' to exit.")
            while True:
                user_input = input("You: ")
                if user_input.lower() !="goodbye":
                    response = generate_response(user_input)
                    print("Chatbot: ", response)
                else:
                    print("Chatbot: Goodbye!")
                    break

if __name__ == "__main__":
    chat_bot=chatbot()
    print (chat_bot)