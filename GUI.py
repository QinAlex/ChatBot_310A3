# -*- coding: utf-8 -*-
"""
@author: ALex_Qin
"""
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import generateResponse as gr
import preprocess as pp

def cook():
    sendData = sendB.get()
    accept_data = sendData
    
    if sendData == 'bye':
        box.insert(tk.END, "Bye! take care! See you again!" + "\n")
        box.see(tk.END)
        
    else:
        box.insert(tk.END, "User:" + sendData + "\n")
        box.see(tk.END)
        sendB.delete(0, tk.END)
        
        qrDict, sentenceTokens, ql = answer()
        userInput = pp.sanitize_questions(accept_data.lower())
        accept_data = gr.generateResponse(userInput, sentenceTokens, qrDict, ql)
        
        box.insert(tk.END, "Bot:" + accept_data + "\n")
        box.see(tk.END)
               
def answer():
    content = ""
    with open("corpus.txt") as infile:
        for line in infile:
            content = content + " " + line.lower()
    qrDict = pp. generateConversationTurnDict(content)
    pureQuestions = pp.pureQuestionsText(qrDict)
    sentenceTokens = pp.generateSentenceTokens(pureQuestions)
    ql = []
    for question, response in qrDict.items():
        ql.append(question)
    return qrDict, sentenceTokens, ql

if __name__ == "__main__":
    root = tk.Tk()
    # title
    root.title("Chatbot")
    
    frame1 = tk.Frame(root)
    frame1.pack()
    Label = tk.Label(frame1, text="Hi, I am a chatbot. Type Bye to exit.\n")
    Label.pack(side='left')

    # input and answer:
    frame2 = tk.Frame(root)
    frame2.pack()
    box = ScrolledText(frame2, width=60, height=50)
    box.bind("<KeyPress>", lambda e: "break")
    box.pack(side="bottom", fill='both', expand=True)

    # input "Enter" button:
    frame3 = tk.Frame(root)
    frame3.pack()
    e3 = tk.StringVar()
    sendB = tk.Entry(frame3, textvariable=e3, width=50)
    Btext = tk.StringVar()
    Btext.set('SEND')
    Send = tk.Button(frame3, width=15, textvariable= Btext,command=cook)
    sendB.pack(side="left")
    Send.pack(side="left")
    frame3.pack()
    
    cook()

    root.mainloop()