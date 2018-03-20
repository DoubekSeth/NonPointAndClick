#SD
import AnalyzeInput
#Uncomment these when we are releasing/typing, but otherwise these are annoying
#print("First exposition dump")
#name = input("What would you like to be called: ")
#print("My name is %s" % (name)) Just here as a template for what you can do
#print("Second exposition dump")

#SD
playerStrength = 5
playerHealth = 20

#SD
#This makes it run the analyze keyword after each sentence typed
#Should be put last because it runs on an infinite loop that doesn't close
def analyzeIt():
    userTyped = input("You: ")
    analyzed = AnalyzeInput.AnalyzeInput(userTyped)
    analyzed.analyzeText()
    analyzeIt()
analyzeIt()





