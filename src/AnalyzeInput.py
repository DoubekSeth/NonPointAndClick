import Inventory
import Objects
import time

inventory = Inventory.Inventory()

#Seth Doubek
class AnalyzeInput(object):
    currentLocation = "Your Mansion"
    playerStrength = 5
    playerHealth = 20

    def __init__(self, userTyped):
        self.text = str.lower(userTyped)

    #SD
    #This puts the sentence into a list of words
    def analyzeText(self):
        startWord = 0
        endWord = 0
        sentence = []
        for var in range(len(self.text)):
            letterList = self.text[var]
            spacePlace = letterList.count(' ')
            if spacePlace == 0:
                endWord += 1
            else:
                sentence.append(self.text[startWord:endWord])
                startWord = endWord + 1
                endWord += 1
        sentence.append(self.text[startWord:endWord])
        
        #SD
        #This detects the first word
        keyword = sentence[0]
        prefix = ''

        #SD
        #Travel
        if keyword == 'travel':
            prefix = "You are traveling to"
            otherWord = sentence[1:]
            suffix = ''
            #Locations
            #The Courtyard
            currentLocation = ''
            if otherWord == ['the', 'courtyard'] or otherWord == ['to', 'the', 'courtyard']:
                suffix = " to the courtyard.\nThere is an old man and the sword of oof"
                AnalyzeInput.currentLocation = 'courtyard'
            elif otherWord == ['to', 'the', 'academy', 'of', 'alchemy'] or otherWord == ['to', 'academy', 'of', 'alchemy'] or otherWord == ['to', 'the', 'academy', 'of', 'alchemy'] or otherWord == ['academy', 'of', 'alchemy']:
                suffix = " to the Academy of Alchemy.\nThere you see a student, and the professor."
                AnalyzeInput.currentLocation = 'academy of alchemy'
            else:
                suffix = " an incorrect place, try again."

        #SD
        #Location
        elif keyword == 'location':
            prefix = "You are currently in "
            otherWord = sentence[1:]
            suffix = ''
            suffix = AnalyzeInput.currentLocation
            
        #SD           
        #Attack
        elif keyword == 'attack':
            prefix = "You have killed "
            otherWord = sentence[1:]
            suffix = ''
            #NPCS
            if otherWord == ['the', 'old',  'man']:
                suffix = " the old man, RIP"
                enemyStrength = 2
                enemyHealth = 10
                while AnalyzeInput.playerHealth > 0 and enemyHealth > 0:
                    enemyHealth = enemyHealth - AnalyzeInput.playerStrength
                    AnalyzeInput.playerHealth = AnalyzeInput.playerHealth - enemyStrength
                print("Current health: " + str(AnalyzeInput.playerHealth))
            else:
                suffix = "an incorrect entity, try again"
        #SD
        #Examine
        elif keyword == 'examine':
            prefix = ''
            otherWord = sentence[1:]
            suffix = ''
            #Items
            if otherWord == ['sword', 'of', 'oof'] or otherWord == ['the', 'sword', 'of', 'oof'] and 'Sword Of Oof' in inventory.backpack:
                name = 'sword of oof'
                swordOfOof = Objects.Objects('a great sword', name, keyword, 'true', 10, 0)
                swordOfOof.displaySwordOfOof()
            else:
                suffix = 'you entered an incorrect item or tried to examine an item you do not have'

        #GJ
        #Talk
        elif keyword == 'talk':
            prefix = ''
            otherWord = sentence[1:]
            suffix = ''
            #NPCS
            if otherWord == ['to','the', 'old',  'man'] and AnalyzeInput.currentLocation == 'courtyard':
               suffix = 'the old man, he says...'
            
            elif otherWord == ['to','the','professor'] or ['the','professor'] or ['professor'] and AnalyzeInput.currentLocation == 'academy of alchemy':
                print("Why hello there boy, are you here to learn about the magical world of Alchemy?")
                time.sleep(1)
                print("Of course you are, why else would you be here.")
                time.sleep(1)
                print("The world of alchemy is based around equivalent exchange, everything in the world is made up of matter.")
                time.sleep(1)
                print("We alchemists rearrange and reorganize this matter to change what it is fundamentally made of.")
                suffix = ''
            else:
              prefix = "you used an incorrect format or talked to something you can't, please try again."
            
        #GJ
        #Inventory
        elif keyword == 'inventory':
          inventory.addItem(Inventory.Item('Sword', '9', '2', '4', 'Iron'))
          inventory.addItem(Inventory.Item('Head', '0', '8', '6', 'Iron'))
          
          otherWord = sentence[0]
          prefix = 'You check your inventory.'
          suffix = ' You find these! '
          inventory.printItems()
          
        #GJ 
        #Collect
        elif keyword == 'collect':
            prefix = 'you collected'
            otherWord = sentence[1:]
            suffix = ''
            #Quick Guide: inventory.addItem(Inventory.Item(name, attack, armor, weight, level))
            #Rock
            if otherWord == ['a', 'rock'] or otherWord == ['rock'] or otherWord == ['the', 'rock']:
                inventory.addItem(Inventory.Item('Rock', '4', '0', '4', 'Rock'))
                suffix = ' a rock'
            #Sword Of Oof
            elif otherWord == ['sword', 'of', 'oof'] or otherWord == ['the', 'sword', 'of', 'oof'] and AnalyzeInput.currentLocation == 'courtyard':
                inventory.addItem(Inventory.Item('Sword Of Oof', '100', '0', '7', 'Oof'))
                suffix = ' the sword of oof'
            else:
                suffix = ' an entity that does not exist or is in another location, try again'
        #SD
        #Help
        elif keyword == 'help':
            prefix = 'You have just been'
            otherWord = sentence[1:]
            suffix = ' filled in'
            print("Travel - Is used to travel to a new location")
            print("Location - Displays the current location and any other detail")
            print("Attack - Is used to attack a person")
            print("Examine - Displays an item, location, or person")
            print("Talk - Is used to talk to people")
            print("Inventory - Checks your current inventory")
            print("Collect - Picks up an item in the world")
            print("Remeber not to put anything before these key words, and try the objects complete noun when doing something")
        #They Goofed        
        else:
            prefix = "You used an incorrect keyword"
            suffix = ", Try again"
        
        print(prefix + suffix)
