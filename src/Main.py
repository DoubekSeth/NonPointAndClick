#SD
import AnalyzeInput
#Uncomment these when we are releasing/typing, but otherwise these are annoying
#print("First exposition dump, get on this grey")
#name = input("What would you like to be called: ")
#print("My name is %s" % (name)) Just here as a template for what you can do
#print("Welcome to THE WEEB-ENING, PUT THE EXPOSITION DUMP HERE")

#SD
#Character stats, modify them whenever we need to in response to an item being
#picked up, shouldn't be modified here
playerStrength = 5
playerHealth = 20
inventory = ['dull blade', ] #If we have one

#SD
#This makes it run the analyze keyword after each sentence typed
#Should be put last because it runs on an infinite loop that doesn't close
def analyzeIt():
    userTyped = input("You: ")
    analyzed = AnalyzeInput.AnalyzeInput(userTyped)
    analyzed.analyzeText()
    analyzeIt()
analyzeIt()



