#SD
import AnalyzeInput
#Uncomment these when we are releasing/typing, but otherwise these are annoying
print("Welcome to the world of Non-Point and click")
#name = input("What would you like to be called: ")
#print("My name is %s" % (name)) Just here as a template for what you can do
def occupationChooser():
    occupation = input("Would you like to an alchemist, xxxx, or xxxx: ")
    str.lower(occupation)
    if occupation == 'alchemist':
        print("Alchemists specialize in using potions and creating objects.\nAre you sure you want to be an alchemist?")
        choice = str.lower(input("Yes/No: "))
        if choice == 'yes':
            occupation = 'alchemist'
            print("To begin you adventure, travel to the Academy of Alchemy")
        else:
            occupationChooser()
occupationChooser()

#SD
#This makes it run the analyze keyword after each sentence typed
#Should be put last because it runs on an infinite loop that doesn't close
def analyzeIt():
    userTyped = input("You: ")
    analyzed = AnalyzeInput.AnalyzeInput(userTyped)
    analyzed.analyzeText()
    if analyzed.playerHealth <= 0:
       print("You died, better luck next time")
    else:
       analyzeIt()
analyzeIt()







