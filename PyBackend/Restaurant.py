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
                u'tags': None,
                u'rating': None
            }
        self.name = None

    def __init__(self, displayName, name):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': name,
                u'tags': None,
                u'rating': None
            }
        self.name = name

    def __init__(self, displayName, name, tags):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': name,
                u'tags': tags,
                u'rating': None
            }
        self.name = name

    def __init__(self, displayName, name, tags, rating):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': name,
                u'tags': tags,
                u'rating': rating
                }
        self.name = name

    """
    == function to help with finding union
    """
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

