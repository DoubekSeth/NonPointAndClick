#SD
import AnalyzeInput
#Uncomment these when we are releasing/typing, but otherwise these are annoying
print("Welcome to the world of Non-Point and click")
#name = input("What would you like to be called: ")
#print("My name is %s" % (name)) Just here as a template for what you can do

#SD Specialization chooser
def specializationChooser():
    specialization = input("Would you like to be an Alchemist, Rogue, or xxxx: ")
    specialization = str.lower(specialization)
    if specialization == 'alchemist':
        print("Alchemists specialize in using potions and creating objects that are used to solve puzzles.\nAre you sure you want to be an alchemist?")
        choice = str.lower(input("Yes/No: "))
        if choice == 'yes':
            specialization = 'alchemist'
            print("To begin you adventure, travel to the Academy of Alchemy")
        else:
            specializationChooser()
    elif specialization == 'rogue':
        print("Rogues are and clever, and sly, specializing in the art of stealth and deception.\nAre you sure you want to be a Rogue?")
        choice = str.lower(input("Yes/No: "))
        if choice == 'yes':
            specialization = 'rogue'
            print("You begin your adventure, travel to the high security prison.")
        else:
           specializationChooser()
    else:
        print("You typed something in wrong, try again")
        specializationChooser()
specializationChooser()
        

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








