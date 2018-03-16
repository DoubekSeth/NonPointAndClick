import Inventory
import Objects

inventory = Inventory.Inventory()

#Seth Doubek
class AnalyzeInput(object):
    currentLocation = "Your Mansion"

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
                suffix = " to the courtyard, good luck!"
                
                AnalyzeInput.currentLocation = 'the courtyard'
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
            prefix = "You are attacking "
            otherWord = sentence[1:]
            suffix = ''
            #NPCS
            if otherWord == ['the', 'old',  'man']:
                suffix = " the old man, RIP"
            else:
                suffix = "an incorrect entity, try again"
        #SD
        #Examine
        elif keyword == 'examine':
            prefix = ''
            otherWord = sentence[1:]
            suffix = ''
            #Items
            if otherWord == ['sword', 'of', 'oof'] or otherWord == ['the', 'sword', 'of', 'oof'] and inventory.backpack.keys().find('Sword Of Oof') != -1:
                name = 'sword of oof'
                swordOfOof = Objects.Objects('a great sword', name, keyword, 'true', 10, 0)
                swordOfOof.displaySwordOfOof()
            else:
                suffix = 'you entered an incorrect item or tried to examine an item you do not have'

        #GJ
        #Talk
        elif keyword == 'talk':
          prefix = 'you talk to '
          otherWord = sentence[1:]
          suffix = ''
          #NPCS
          if otherWord == ['to','the', 'old',  'man']:
            suffix = 'the old man, he says...'
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
            elif otherWord == ['sword', 'of', 'oof'] or otherWord == ['the', 'sword', 'of', 'oof']:
                inventory.addItem(Inventory.Item('Sword Of Oof', '100', '0', '7', 'Oof'))
                suffix = ' the sword of oof'
            else:
                suffix = ' an entity that does not exist, try again'
          
        #They Goofed         
        else:
            prefix = "You used an incorrect keyword"
            suffix = ", Try again"
        
        print(prefix + suffix)
