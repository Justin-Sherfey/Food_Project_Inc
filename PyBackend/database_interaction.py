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
    name = helpers.parseName(scrape)
    rest = Restaurant(scrape, name)
    ghFeat.append(rest)

for scrape in ueScrape:
    name = helpers.parseName(scrape)
    rest = Restaurant(scrape, name)
    ueFeat.append(rest)

toSend = helpers.getUnion(ghFeat, ueFeat)
print(toSend)

for rest in toSend:
    docRef = db.collection(u'Restaurants').document(rest.name)
    docRef.set(rest.JSON)


