class Restaurant:

    def __init__(self, displayName):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': None, 
                u'tags': None
            }

        self.displayName = displayName
        self.name = None

    def __init__(self, displayName, name):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': name,
                u'tags': None
            }

        self.displayName = displayName
        self.name = name

    def __init__(self, displayName, name, tags):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': name,
                u'tags': tags
            }
        self.displayName = displayName
        self.name = name
        self.tags = tags

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
