# 310 ChatBot

Alex Qin

### Introduction: 

This is a simple chatbot program. The most fundamental theory that this program relies on is text similarity. 

The following steps decribe the logic of this program:
* Clean text, including remove punctuation, duplicate whitespace.
* Divide text into multiple independent conversaiton turns.
* Based on such conversation turns, create a dictionary whose key is the question and value is the response.
* Combine only questions, then tokenlizing and lemmatization them.
* Vectorize those sentence tokens and compare the user input with them.
* Find the most similar question and use it as key to retrieve answer from training corpus.
* Output answer/response.
* Having the solution for the question that can not handle

The training corpus used in our project comes from this [Repo](https://github.com/gunthercox/chatterbot-corpus)

### A3 features:
Implemented a GUI to make it looks good and can talk with human smoothly with at least 30 turns.

![30_output with new topic](https://user-images.githubusercontent.com/43220166/55991117-54bf1180-5c5e-11e9-8d06-913b427e40fc.PNG)

Add two new topics: cook and books

![30_output_rest](https://user-images.githubusercontent.com/43220166/55991287-c008e380-5c5e-11e9-8f56-e879fc4b838c.PNG)

Handling the miss-spelling or spell the wrong words by using traind model.

![handlemistakes](https://user-images.githubusercontent.com/43220166/55991396-09593300-5c5f-11e9-8c43-9946f85e6ab8.PNG)

Generate 5 random answer for the question that is outside the scope.

![GUI 5randomAnswer](https://user-images.githubusercontent.com/43220166/55991594-74a30500-5c5f-11e9-876f-083d7553c2c3.PNG)



### How to use this program:
* Using python eniroment
* Make sure training corpus and the program are in the same folder
* Run from command line `python main.py`



