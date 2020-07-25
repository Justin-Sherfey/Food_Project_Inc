"""
restaurant class, main utility is to provide easy access JSON object
and gives an easy way to reference specific Restaurants
"""
class Restaurant:

    """
    series of init functions for any amount of data
    """
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

    
    """
    == function to help with finding union
    """
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
