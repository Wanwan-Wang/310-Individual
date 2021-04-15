# 310-Individual
![ChatbotImage](https://s3-eu-west-1.amazonaws.com/userlike-cdn-blog/do-i-need-a-chatbot/header-chat-box.png)

## About the project
This repository contains a programming project code for a chatbot that simulates a conversation between friends. 
A specific topic about soccer and some scattered topics are covered. Moreover, after the individual project our chatbot
can use Google Static Maps API to embeds images into conversation. And use Google Geocoding API to convert urban addresses 
and display them in a meaningful way in your program.

## Prepare stage
before we start running this code we need to download several libraries
```bash
pip install nltk
pip install -U spacy
python -m spacy download en_core_web_lg
pip install pyspellchecker
pip install -U textblob
```

## How to run the code
First, set up the libraries, and open the folder.

Second, click on the socket_server.py and run it.

Third, while the Terminal shows the chatbot is ready,
you can enter "python chatbox.py" in command line or anaconda
to open GUI of chatbox.

## Some features
1. The system can clean all punctuations in the sentence and convert sentence to lower case

2. The system can remove suffixes (e.g.playing and play) and 
convert all the words back to root form (e.g. apples and apple)

3. The system can clean all the words with not much meaning in the sentence (e.g. 'a', 'is')

4. The system can perform sentiment analysis （e.g. good and bad)

5. A simple GUI so that the user is typing into a nicer interface and can view a recent history of the conversation

6. New topics about basketball is added to improve the conversation of agent

7. A feature enables agent to give at least 5 different reasonable responses when the user enters something beyond the two topics

8. A feature enables the system to handle spelling mistakes of the words to improve the fluency of conversation
 
9. A feature to use Google Static Maps API to embeds images into conversation (new)

10. A feature to use Google Geocoding API to convert urban addresses and display them in a meaningful way in your program (new)
## Sample output
```bash
Input:what is chemistry??  
the science of mixing chemicals.
```
```bash
Input:tell me about chemistry  
the science of mixing chemicals.
```
```bash
Input:what is chemitry
the science of mixing chemicals.
```
```bash
Input:you are a good robot
Thank you!!!
```
```bash
Input:you are not a good robot
I'm sorry QAQ!
```
```bash
...
```

## GUI and Examples
<img src="https://raw.githubusercontent.com/COSC310-A2-Team10/COSC310-Friend-ChatBot-A3/main/GUI(1).jpg" width="500" height="700">
