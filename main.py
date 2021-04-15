import random
import generate as gen
import preprocessing as prep
from googleMapUtil import openMap, getGooglePlaces

question,answer=prep.loadCorpora()

print("preparing system.....")
embeddingList=gen.wordEmbedding(question)
print("The chatbot is ready, Enter 'bye' to exit the system")
print("Hi I'm your chatbot let's chat!!")

def makereply(userinput):

    if userinput =="bye":
        #print("bye")
        listBye = ['see you','bye','bye-bye','good bye']
        replyBye = random.choice(listBye)
        return replyBye
    elif userinput=="hi" or userinput=="hello":
        #print("Hi!!")
        listHi = ['Hi!!','Hello!!','good to see you!','Hi there!']
        replyHi = random.choice(listHi)
        return replyHi
    elif userinput.lower().startswith("show map"):
        userinput=userinput.replace("show map","").replace(" ","")
        openMap(userinput)
        return "Opening map at "+userinput
    elif userinput.lower().startswith("get location"):
        userinput=userinput.replace("get location","").replace(" ","")
        return "location maybe at "+getGooglePlaces(userinput)
    else:
        return gen.generate(userinput,embeddingList,answer)

