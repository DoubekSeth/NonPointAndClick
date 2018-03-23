import Inventory
import Objects
import time

inventory = Inventory.Inventory()

#Seth Doubek
class AnalyzeInput(object):
    currentLocation = "Your Mansion"
    playerStrength = 5
    playerHealth = 20
    specialization = ''
    dust = 0

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
            prefix = "You are traveling to "
            otherWord = sentence[1:]
            suffix = ''
            #Locations
            #The Courtyard
            currentLocation = ''
            if otherWord == ['the', 'courtyard'] or otherWord == ['to', 'the', 'courtyard']:
                suffix = " to the courtyard.\nThere is an old man and the sword of oof"
                AnalyzeInput.currentLocation = 'courtyard'

            #Alchemy
            #The Academy of Alchemy
            elif otherWord == ['to', 'the', 'academy', 'of', 'alchemy'] or otherWord == ['to', 'academy', 'of', 'alchemy'] or otherWord == ['to', 'the', 'academy', 'of', 'alchemy'] or otherWord == ['academy', 'of', 'alchemy']:
                suffix = " to the Academy of Alchemy.\nThere you see a student, and the professor."
                AnalyzeInput.currentLocation = 'academy of alchemy'
                AnalyzeInput.specialization = 'alchemist'
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
            oldMan = 1
            if otherWord == ['the', 'old',  'man'] and oldMan == 1:
                suffix = " the old man, RIP"
                enemyStrength = 2
                enemyHealth = 10
                while AnalyzeInput.playerHealth > 0 and enemyHealth > 0:
                    enemyHealth = enemyHealth - AnalyzeInput.playerStrength
                    AnalyzeInput.playerHealth = AnalyzeInput.playerHealth - enemyStrength
                print("Current health: " + str(AnalyzeInput.playerHealth))
                oldMan = 0
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
                swordOfOof = Objects.Objects()
                swordOfOof.displaySwordOfOof()
            else:
                suffix = 'you entered an incorrect item or tried to examine an item you do not have'

        #GJ
        #Talk
        elif keyword == 'talk':
            prefix = 'you are currently talking to'
            otherWord = sentence[1:]
            suffix = ''
            #NPCS
            #The old man
            if otherWord == ['to','the', 'old','man'] or otherWord == ['test'] and AnalyzeInput.currentLocation == 'courtyard':
               suffix = 'the old man, he says...'

            #Alchemy 
            #SD
            #The Professor of Alchemy
            elif otherWord == ['the', 'professor'] or otherWord == ['professor'] or otherWord == ['to','the','professor'] and AnalyzeInput.currentLocation == 'academy of alchemy' and AnalyzeInput.specialization == 'alchemist':
                print("Why hello there boy, are you here to learn about the magical world of Alchemy?")
                time.sleep(3)
                print("Of course you do, why else would you be here.")
                time.sleep(3)
                print("The world of alchemy is based around equivalent exchange, everything in the world is made up of matter.")
                time.sleep(3)
                print("We alchemists rearrange this matter to change what it is fundamentally made of.")
                time.sleep(3)
                print("Simply using the command 'transmute' on a pile of covalent dust will turn it into whatever you want")
                time.sleep(3)
                print("Try it now, transmute this dust into a rock")
                AnalyzeInput.dust = 2
                time.sleep(3)
                print("Simply type: 'transmute rock'")
                time.sleep(3)
                prefix = 'Once you are done doing that talk '
                suffix = 'to one of my students to find out more about alchemy'
            #SD
            #The
            elif otherWord == ['the', 'student'] or otherWord == ['student'] or otherWord == ['to','the','student'] and AnalyzeInput.currentLocation == 'academy of alchemy':
                print("If you haven't already I would make sure to talk to the professor.")
                time.sleep(3)
                print("Every student of alchemy needs an alchemical codex.")
                time.sleep(3)
                print("Here I have an extra, take it.")
                time.sleep(3)
                print("This will tell you the amount of dust you need for a certain type and weight of the material.")
                time.sleep(3)
                print("There are some extra sections in it, but they need to be decoded before they can be used.")
                time.sleep(3)
                print("The only section I have decoded is the materials section ('codex materials').")
                time.sleep(3)
                print("I heard they are doing a potion seminar over at apothecary, you should head there.")
                prefix = "She hands you the codex"
                suffix = ""
                
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
            prefix = 'There are more class specific commands, '
            otherWord = sentence[1:]
            suffix = 'go back and talk to the people to figure these out'
            print("Travel - Is used to travel to a new location")
            print("Location - Displays the current location and any other detail")
            print("Attack - Is used to attack a person")
            print("Examine - Displays an item, location, or person")
            print("Talk - Is used to talk to people")
            print("Inventory - Checks your current inventory")
            print("Collect - Picks up an item in the world")
            print("Remeber not to put anything before these key words, and try the objects complete noun when doing something")

        #SD
        #Transmute
        elif keyword == 'transmute':
            prefix = 'You just transmuted '
            otherWord = sentence[1:]
            suffix = ''
            if otherWord == ['into', 'a', 'rock'] or ['into', 'rock'] or ['a','rock'] or ['rock']:
                weight = 2
                if (AnalyzeInput.dust - weight) < 0:
                    prefix = "You don't have enough dust to transmute "
                else:
                    AnalyzeInput.dust -= weight
                    print("You current have " + str(AnalyzeInput.dust) + " grams of dust left")
                    inventory.addItem(Inventory.Item('Rock', '4', '0', '4', 'Rock'))
                suffix = 'a rock'

        #SD
        #Codex
        elif keyword == 'codex' and AnalyzeInput.specialization == 'alchemist':
            prefix = 'page '
            otherWord = sentence[1:]
            suffix = ''
            if otherWord == ['materials']:
                materials = Objects.Objects()
                materials.displayCodexMaterials()
                suffix = '1'
                
                

                
        #They Goofed        
        else:
            prefix = "You used an incorrect keyword"
            suffix = ", Try again"
        
        print(prefix + suffix)
