"""
restaurant class, main utility is to provide easy access JSON object
and gives an easy way to reference specific Restaurants
"""
class Restaurant:
    """
    init function for any amount of data
    """
    def __init__(self, displayName=None, name=None, tags=None, rating=0.0):
        self.JSON = {
                u'Display_Name': displayName,
                u'name': name,
                u'tags': tags,
                u'rating': rating
                }
        self.name = name
        self.displayName = displayName
        self.tags = tags
        self.rating = rating


    """
    string representation for printing
    """
    def __str__(self):
        return self.name


    """
    repr function for debugging, returns Restaurant name
    """
    def __repr__(self):
        return self.name


    """
    == function to help with finding union
    """
    def __eq__(self, other):
        if self.name in other.name:
            return True
        elif other.name in self.name:
                return True
        else:
            return False


    """
    != function for union
    """
    def __ne__(self, other):
        return not (self == other)


    """
    hash function to make set operations work
    """
    def __hash__(self):
        return hash(self.name)
