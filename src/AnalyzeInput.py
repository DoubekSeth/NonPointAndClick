import Inventory
import Objects
import time
import os

inventory = Inventory.Inventory()

#Seth Doubek
class AnalyzeInput(object):
    currentLocation = "Your Mansion"
    playerStrength = 5
    playerHealth = 20
    specialization = ''
    dust = 0
    talkedToProf = 0
    locationInfo = "This is the starting spot, try to travel to one of the class specific locations"

    #All the dead and alive characters
    oldMan = 1

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
        #VC
            #Locations
            #The Courtyard
            currentLocation = ''
            if otherWord == ['the', 'courtyard'] or otherWord == ['to', 'the', 'courtyard']:
                suffix = " to the courtyard.\nThere is an old man and the sword of oof"
                AnalyzeInput.currentLocation = 'courtyard'
            #VC
            #High Security prison
            elif otherWord == ['the', 'high', 'security', 'prison'] or otherWord == ['high', 'security', 'prison'] or otherWord == ['to', 'the', 'high', 'security','prison']:
                suffix = " to the high security prison. You are imprisoned becasuse you were caught stealing from high ranking nobles You are due to stand trial tommorow where you will most likely be found guilty and be excuted. /n You are currently languishing in your cell. There is a guard outside the door while your cell is completely bare."
                AnalyzeInput.currentLocation = 'high security prison'
                AnalyzeInput.specialization = 'Rogue'
                          #the forest
            elif otherWord == ['the', 'forest']:
                suffix = "to the forest. YOu are being persued by the guards. You flee into the forest\n there are 2 paths one to the left and one to the right.Travel through one of the paths."
                AnalyzeInput.currentLocation = 'forest'
            #the right path
            elif otherWord == ['the', 'right', 'path']:
                suffix = "to the right path. The right path is overgrown with weeds and thorns, and looks unkept. This works to your advantage as it slows the gaurds horses and allows you to slip away."
                AnalyzeInput.currentLocation = 'right path'
            #the left path
            elif otherWord == ['the', 'left', 'path']:
                suffix = "to the left path. As luck would have it, you run into a returnin patrol of soldiers. You are not even given a trial as you are executed on the roadside."
                AnalyzeInput.currentLocation = 'left path'
                AnalyzeInput.playerHealth = 0


                

            #Alchemy
            #The Academy of Alchemy
            elif otherWord == ['to', 'the', 'academy', 'of', 'alchemy'] or otherWord == ['to', 'academy', 'of', 'alchemy'] or otherWord == ['to', 'the', 'academy', 'of', 'alchemy'] or otherWord == ['academy', 'of', 'alchemy']:
                suffix = " to the Academy of Alchemy.\nThere you see a student, and the professor."
                AnalyzeInput.locationInfo = "There is a professor and a student."
                AnalyzeInput.currentLocation = 'academy of alchemy'
                AnalyzeInput.specialization = 'alchemist'
                
            #Outside the Bunker
            elif otherWord == ['to', 'outside','the','bunker'] or otherWord == ['outside','the','bunker']:
                print("You squint your eyes from the oppressive light of the sun")
                time.sleep(3)
                print("As they adjust you start to take in the world around you")
                time.sleep(3)
                print("Very little is left from the blast, the whole place seems to be desolate")
                time.sleep(3)
                print("You notice a 'small town' on the outside of the blast radius")
                time.sleep(3)
                print("It doesn't look like much, but it's a start")
                time.sleep(3)
                prefix = 'You should'
                suffix = ' head there'
                AnalyzeInput.currentLocation = "outside the bunker"

            #Small Town
            elif otherWord == ['to', 'the', 'small', 'town'] or otherWord == ['small', 'town'] or otherWord == ['to','small', 'town'] or otherWord == ['the','small', 'town']:
                print("People:\n    Merchant\n    Woman")
                print("Places:\n    Library\n    Inn")
                prefix = ""
                suffix = ""
                AnalyzeInput.currentLocation = "small town"
                AnalyzeInput.locationInfo = "People:\n    Merchant\n    Woman\nPlaces:\n    Library\n    Inn"
                
            else:
                suffix = " an incorrect place, try again."
        

        #SD
        #Location
        elif keyword == 'location':
            prefix = "You are currently in the "
            otherWord = sentence[1:]
            suffix = ''
            suffix = AnalyzeInput.currentLocation
            print(AnalyzeInput.locationInfo)
            
        #VC SD          
        #Attack
        elif keyword == 'attack':
            prefix = "You have killed "
            otherWord = sentence[1:]
            suffix = ''
            #NPCS
            if otherWord == ['the', 'old',  'man'] and AnalyzeInput.oldMan == 1:
                suffix = " the old man, RIP"
                enemyStrength = 2
                enemyHealth = 10
                print("Health: " + str(AnalyzeInput.playerHealth) + "         Strength: " + str(AnalyzeInput.playerStrength))
                print("Enemy Health: " + str(enemyHealth) + "   Enemy Strength: " + str(enemyStrength))
                fight = str.lower(input("Are you sure you want to fight (Yes/No): "))
                if fight == 'yes' or fight == 'y':
                    while AnalyzeInput.playerHealth > 0 and enemyHealth > 0:
                        enemyHealth = enemyHealth - AnalyzeInput.playerStrength
                        AnalyzeInput.playerHealth = AnalyzeInput.playerHealth - enemyStrength
                    print("Current health: " + str(AnalyzeInput.playerHealth))
                    AnalyzeInput.oldMan = 0
                else:
                    suffix = 'nobody and ran away instead'
            else:
                suffix = "an incorrect entity or someone who is already dead, try again"
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

            #Rogue
            #VC
            #the Guard
            elif otherWord == ['the', 'guard'] or otherWord == ['to', 'the', 'gaurd']:
                suffix = 'the guard.'
                print("Instead of providing helpful diaglogue he merely mocks you about your inpending fate.") 
                time.sleep(3)
                print("Afterwards, he slips what appears to be your meal through the bars. Your last, the guard mocks.") 
                print("Your cell is completely empty except for meal. There is guard outside the door.")
            



            #Alchemist 
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
                AnalyzeInput.talkedToProf = 1
                
            #SD
            #The Student
            elif otherWord == ['the', 'student'] or otherWord == ['student'] or otherWord == ['to','the','student'] and AnalyzeInput.currentLocation == 'academy of alchemy':
                if AnalyzeInput.talkedToProf == 0:
                    prefix = "If you haven't already I would make sure to talk to the professor."
                else:
                    print("You must be new here")
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
                    print("Try to go to the materials section.")
                    time.sleep(1)
                    def codexCheck():
                        check = str.lower(input("You: "))
                        if check == 'codex material' or check == 'codex materials':
                            print("Great job!")
                        else:
                            print("Try again")
                            codexCheck()
                    codexCheck()
                    time.sleep(1)
                    print("I heard they are doing a potion seminar over at apoth...")
                    time.sleep(2)
                    print("What was that?")
                    time.sleep(3)
                    explosion = Objects.Objects()
                    explosion.displayExplosion()
                    time.sleep(5)
                    prefix = "You wake in a new place, take a look around with the 'location' keyword"
                    AnalyzeInput.currentLocation = "bunker"
                    AnalyzeInput.locationInfo = "You are on a cot in the middle of a bunker.\nThere are others all around you.\nYou try and get up but find yourself too weak.\nYou see a potion next to your bed.\nType the 'use' command on the potion."
                    suffix = ""

            #The Merchant in small town
            elif otherWord == ['the', 'merchant'] or otherWord == ['merchant'] or otherWord == ['to','the','merchant'] and AnalyzeInput.currentLocation == 'small town':
                print("What can I do for you?")
                print("| Talk | Buy | Sell |")
                response = str.lower(input("You: "))
                if response == 'talk':
                    print("What would you like to talk about")
                    print("| Who are you | How do I buy stuff | How do I get money |")
                    
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
        #VC updated 3/27/18
        #Help
        elif keyword == 'help':
            prefix = 'There are more class specific commands, '
            otherWord = sentence[1:]
            suffix = 'go back and talk to the people to figure these out in detail or just type help to pull up a list of kewords'
            print("Travel - Use this keyword to travel to a new location")
            print("Location - This keyword displays the current location and any other detail")
            print("Attack - Use this keyword to attack a person")
            print("Examine - This keyword displays an item, location, or person. You can also use this to view the ascci image of an item")
            print("Talk - This keyword is used to talk to people")
            print("Inventory - This keyword checks your current inventory")
            print("Collect - This keyword picks up an item in the world")
            print("Remeber not to put anything before these key words, and try the objects complete noun when doing something")

        #SD
        #Transmute
        elif keyword == 'transmute':
            prefix = 'You just transmuted '
            otherWord = sentence[1:]
            suffix = ''
            if otherWord == ['into', 'a', 'rock'] or otherWord == ['into', 'rock'] or otherWord == ['a','rock'] or otherWord == ['rock']:
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
            else:
                prefix = 'You have entered an incorrect page, try again'
                suffix = ''

        #SD
        #Use
        elif keyword == 'use':
            prefix = ''
            otherWord = sentence[1:]
            suffix = ''
            if otherWord == ['potion'] or otherWord == ['the', 'potion'] or otherWord == ['a', 'potion'] and AnalyzeInput.currentLocation == 'bunker':
                AnalyzeInput.playerHealth = 20
                prefix = 'You have just gained'
                suffix = ' 20 life'
                print("You're feeling so good you think you will go and explore 'outside the bunker'")

        #SD
        #Save
        elif keyword == 'save':
            prefix = 'You have just saved!'
            otherWord = sentence[1:]
            suffix = ''
            os.chdir("/Users/9518588/10th Grade/Programming/Term 3/Non Point and Click/Save/")
            #Current Location
            save = open("currentLocation.txt", "w+")
            save.write(str(AnalyzeInput.currentLocation))
            save.close()
            #Player Strength
            save = open("playerStrength.txt", "w+")
            save.write(str(AnalyzeInput.playerStrength))
            save.close()
            #Player Health
            save = open("playerHealth.txt", "w+")
            save.write(str(AnalyzeInput.playerHealth))
            save.close()
            #Specialization
            save = open("specialization.txt", "w+")
            save.write(str(AnalyzeInput.specialization))
            save.close()
            #Dust
            save = open("dust.txt", "w+")
            save.write(str(AnalyzeInput.dust))
            save.close()
            #Talked To Prof
            save = open("talkedToProf.txt", "w+")
            save.write(str(AnalyzeInput.talkedToProf))
            save.close()
            #Location Info
            save = open("locationInfo.txt", "w+")
            save.write(str(AnalyzeInput.locationInfo))
            save.close()

        #They Goofed        
        else:
            prefix = "You used an incorrect keyword"
            suffix = ", Try again"
        
        print(prefix + suffix)
