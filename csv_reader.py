import random

def read_csv(filename):
    with open(filename, 'r') as f:
        pairs = f.readlines()
    pair_dict = {}
    for i in pairs:
        pair = i.strip()
        if i[0] == '"':
            comma_index = pair.find('"', 1) + 1
            key = pair[1:comma_index - 1]
        else:
            comma_index = pair.find(',')
            key = pair[:comma_index]
        val = pair[comma_index + 1:]
        if ((key != 'Job Class') & (val != 'Job Class')):
            pair_dict[key] = val
    return pair_dict

occupations = read_csv("occupations.csv")
#print (occupations)


keys = occupations.keys()
values = occupations.values()


def randomOccupation():
    randomInt = random.uniform(0.0,99.7) #99.8 sometimes may break, this is guaranteed to work
    dictIterator = 0
    dictTotal = 0
    while (dictIterator < len(keys) - 1):
        if ((values[dictIterator] != '99.8') & (values[dictIterator] != 'Percentage') & (keys[dictIterator] != 'Job Class')):
            dictTotal += float(values[dictIterator])
            dictIterator += 1
            #print (dictTotal)
        else:
            dictIterator += 1
        if (randomInt < dictTotal):
            print ("Your random occupation is: " + keys[dictIterator - 1] + ".")
            return (occupations.keys()[occupations.values().index(occupations.values()[dictIterator])])



j = 0
while (j < 10000):
    randomOccupation()
    j += 1
























##def randomOccupation():
##    randomInt = random.uniform(0.0,99.8)
##    randomInt = 0.7
##    dictIterator = 0
##    dictTotal = 0
##    while (dictIterator < len(occupations) - 1):
##        if ((occupations.values() [dictIterator] != '99.8') & (occupations.values() [dictIterator] != 'Percentage')):
##            dictTotal += float( occupations.values() [dictIterator] [0: len(occupations.values() [dictIterator])])
##            dictIterator += 1
##            print (dictTotal)
##        else:
##            dictIterator += 1
##        if (randomInt < dictTotal):
##            print ("Your random occupation is: " + occupations.keys().index([occupations.values().index(occupations.values()[dictIterator - 1])]) + ".")
##            #return (occupations.keys()[occupations.values().index(occupations.values()[dictIterator])])
            
