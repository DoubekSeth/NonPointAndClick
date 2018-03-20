#GJ
class Item(object):
    def __init__(self, name, attack, armor, weight, level):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.level = level
        

class Inventory(object):
    def __init__(self):
        self.backpack = {}

    def addItem(self, item):
        self.backpack[item.name] = item

    def printItems(self):
        #SD, Stole this off of stack overflow, link: https://stackoverflow.com/questions/39032720/formatting-lists-into-columns-of-a-table-output-python-3
        names = []
        attacks = []
        armors = []
        weights = []
        levels = []
        for item in self.backpack.values():
            names.append(item.name)
            attacks.append(item.attack)
            armors.append(item.armor)
            weights.append(item.weight)
            levels.append(item.level)

        titles = ['name', 'attack', 'armor', 'weight', 'level']
        data = [titles] + list(zip(names, attacks, armors, weights, levels))

        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(12) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))
