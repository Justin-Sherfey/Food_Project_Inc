"""
helper funtions for non-site specific tasks
"""
from Restaurant import Restaurant

"""
finds and returns the union of two arrays
"""
# TODO: make more effecient
def getUnion(set1, set2):
    union = set1.union(set2)
    temp1 = set()
    temp2 = set()
    for item in set1:
        for thing in union:
            if item == thing:
                item = combine(thing, item)
        temp1.add(item)
    for item in set2:
        for thing in union:
            if item == thing:
                item = combine(thing, item)
        temp2.add(item)
    return temp1.union(temp2)


"""
parses and returns the name of a restaurant from its displayName
"""
def parseName(displayName):
    if '- ' in displayName:
        end = displayName.index('- ')
        displayName = displayName[0:end]
    elif '(' in displayName:
        end = displayName.index('(')
        displayName = displayName[0:end]

    if '/' in displayName:
        split = displayName.index('/')
        first = displayName[0:split]
        last = displayName[split+1::]
        displayName = first + ' & ' + last

    if ' and ' in displayName:
        split = displayName.index('and')
        first = displayName[0:split]
        last = displayName[split+3::]
        displayName = first + ' & ' + last

    if 'Barbecue' in displayName:
        split = displayName.index('Barbecue')
        first = displayName[8:split]
        last = displayName[split+1::]
        displayName = first + 'BBQ' + last


    return displayName


"""
parses and returns the tags of a restaurant from a string
"""
def parseTags(string):
    if ' • ' in string:
        return set(string.split(' • '))
    elif '$' in string:
        return set()
    elif 'Featured' in string:
        return set()
    elif 'Delivery' in string:
        return set()
    else:
        return {string}


"""
helper for dealing with edge cases in rating parsing
"""
def parseRating(string):
    try:
        return float(string)
    except:
        return 0.0


"""
combiner function for getting a Restaurant object with the most data
during union operation
"""
def combine(rest1, rest2):
    name = rest1.name
    displayName = rest1.displayName
    tags = rest1.tags.union(rest2.tags)
    rating = max([rest1.rating, rest2.rating])

    return Restaurant(displayName, name, tags, rating)

