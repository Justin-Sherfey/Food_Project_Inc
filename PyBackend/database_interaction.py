"""
procedure for interacting with the firebase database with some printing to
check for errors
"""


import door_dash_scraping, grub_hub_scraping, uber_eats_scraping 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import helpers
from Restaurant import Restaurant

# Use a service account
cred = credentials.Certificate('../../../Auth files/project-food-5b105-d02a0c57a1eb.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

dd = [
        door_dash_scraping.parse(x) for x in door_dash_scraping.scrape(
            door_dash_scraping.navigate(door_dash_scraping.URL, '92117')
            )
        ]

gh = [
        grub_hub_scraping.parse(x) for x in grub_hub_scraping.scrape( 
            grub_hub_scraping.navigate('92117')
            )
        ]


ue = [
        uber_eats_scraping.parse(x) for x in uber_eats_scraping.scrape( 
            uber_eats_scraping.navigate('92117')
            )
        ]

dd = list(map(lambda r: Restaurant(r[0], r[1], r[2], r[3]), dd))

ue = list(map(lambda r: Restaurant(r[0], r[1], r[2], r[3]), ue))

gh = list(map(lambda r: Restaurant(r[0], r[1], r[2], r[3]), gh))

toSend = helpers.getUnion(ue, dd, gh)
for to in toSend:
    print(to.name)

for rest in toSend:
    docRef = db.collection(u'Restaurants').document(rest.name)
    docRef.set(rest.JSON)


