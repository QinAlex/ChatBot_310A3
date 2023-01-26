# -*- coding: utf-8 -*-
"""
Created on Wed Apr 9 20:25:05 2019

@author: ALex_Qin
"""

import generateResponse as gr
import preprocess as pp
content="" 
with open("corpus.txt") as infile: 
    for line in infile: 
        content=content+" "+line.lower() 
qrDict= pp.generateConversationTurnDict(content) 
pureQuestions= pp.pureQuestionsText(qrDict) 
sentenceTokens= pp.generateSentenceTokens(pureQuestions) 
ql=[] 
for question,response in qrDict.items(): 
    ql.append(question)

flag = True
print("ROBO: Hello, I am a chatbot. Type Bye to exit")

while flag:
    userInput = input()
    userInput = pp.sanitize_questions(userInput.lower())
    if userInput != 'bye':
        if userInput in ['thanks', 'thank you']:
            flag = False
            print("ROBO: You are welcome..")
        else:
            print("ROBO: "+ gr.generateResponse(userInput, sentenceTokens, qrDict, ql))
            sentenceTokens.remove(userInput)
    else:
        flag = False
        print("ROBO: Bye! take care..")