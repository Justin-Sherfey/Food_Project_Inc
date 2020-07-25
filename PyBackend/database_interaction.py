"""
procedure for interacting with the firebase database with some printing to
check for errors
"""


import Grub_Hub_Scraping, Uber_Eats_Scraping
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import helpers
from Restaurant import Restaurant

# Use a service account
cred = credentials.Certificate('../../project-food-5b105-d02a0c57a1eb.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

ghScrape = Grub_Hub_Scraping.scrapeFeatured()
ueScrape = Uber_Eats_Scraping.scrapeFeatured()

ghFeat = []
ueFeat = []

for scrape in ghScrape:
    tup = Grub_Hub_Scraping.parse(scrape)
    rest = Restaurant(tup[0], tup[1], tup[2])
    ghFeat.append(rest)

for scrape in ueScrape:
    tup = Uber_Eats_Scraping.parse(scrape)
    rest = Restaurant(tup[0], tup[1], tup[2])
    ueFeat.append(rest)

toSend = helpers.getUnion(ueFeat, ghFeat)[1::]
for to in toSend:
    print(to.name)

for rest in toSend:
    docRef = db.collection(u'Restaurants').document(rest.name)
    docRef.set(rest.JSON)


