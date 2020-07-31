"""
helper funtions for non-site specific tasks
"""


"""
finds and returns the union of two arrays
"""
# TODO: fix // make more robust
def getUnion(*lists):
    union = []
    for lst in lists:
        for item in lst:
            if item not in union:
                union.append(item)

    return union


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

    return displayName


"""
parses and returns the tags of a restaurant from a string
"""
def parseTags(string):
    if ' • ' in string:
        return string.split(' • ')
    elif '$' in string:
        return []
    elif 'Featured' in string:
        return []
    elif 'Delivery' in string:
        return []
    else:
        return [string]


"""
helper for dealing with edge cases in rating parsing
"""
def parseRating(string):
    try:
        return float(string)
    except:
        return None
