def getUnion(restaurantArr1, restaurantArr2):
    union = []

    for rest in restaurantArr1:
        union.append(rest)

    for rest in restaurantArr2:
        match = False
        for comp in union:
            if comp == rest:
                match = True
        if match:
            continue
        else:
            union.append(rest)

    return union


def parseName(displayName):
    if '- ' in displayName:
        end = displayName.index('- ')
        displayName = displayName[0:end]
    elif '(' in displayName:
        end = displayName.index('(')
        displayName = displayName[0:end]

    return displayName


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
