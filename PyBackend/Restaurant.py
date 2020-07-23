class Restaurant:

    def __init__(self, displayName):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': u'none'
            }

        self.displayName = displayName
        self.name = None

    def __init__(self, displayName, name):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': name 
            }

        self.displayName = displayName
        self.name = name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
