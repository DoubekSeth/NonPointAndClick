import Objects
#Seth Doubek 3/8/18
class AnalyzeInput(object):
    currentLocation = "Starting place"

    def __init__(self, userTyped):
        self.text = str.lower(userTyped)
    
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
        
        #This detects the first word
        keyword = sentence[0]
        prefix = ''
        
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
                AnalyzeInput.currentLocation = 'courtyard'
            else:
                suffix = "an incorrect place, try again"

        #Location
        elif keyword == 'location':
            prefix = "You are currently in "
            otherWord = sentence[1:]
            suffix = ''
            suffix = AnalyzeInput.currentLocation
            
            
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

        #Examine
        elif keyword == 'examine':
            prefix = ''
            otherWord = sentence[1:]
            suffix = ''
            #Items
            if otherWord == ['sword', 'of', 'oof'] or otherWord == ['the', 'sword', 'of', 'oof']:
                name = 'sword of oof'
                examinedObject = Objects.Objects(name, keyword)
                examinedObject.displaySwordOfOof
            else:
                suffix = 'you entered an incorrect item'
        
        #They Goofed         
        else:
            prefix = "You used an incorrect keyword"
            suffix = ", Try again"
            
        #Objects
        print(prefix + suffix)
