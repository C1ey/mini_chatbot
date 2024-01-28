# Created by Cleon Simpson

import sys
import os
import socket
import time


waiting = 2
time.sleep(waiting)
test = ["*" for i in range(3)]

def chatbot():
    Password = "Password1"
    Greeting= input("Password: ")
    if Greeting != Password:
        print("Incorrect Password, Access Denied!")
        exit()
    else:
        if Greeting == Password:
            print(test)

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
    return responses.get(user.input, responses["default"])
        #Main