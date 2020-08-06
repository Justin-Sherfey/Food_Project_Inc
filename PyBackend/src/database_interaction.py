"""
procedure for interacting with the firebase database with some printing to
check for errors
"""

import door_dash_scraping, grub_hub_scraping, helpers, uber_eats_scraping
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Restaurant import Restaurant
import helpers
from functools import reduce


# Use a service account
cred = credentials.Certificate(
        '../../../../Auth files/project-food-5b105-d02a0c57a1eb.json'
        )
firebase_admin.initialize_app(cred)

db = firestore.client()

dd = set([
        door_dash_scraping.parse(x) for x in door_dash_scraping.scrape(
            door_dash_scraping.navigate('92117')
            )
        ])

gh = set([
        grub_hub_scraping.parse(x) for x in grub_hub_scraping.scrape(
            grub_hub_scraping.navigate('92117')
            )
        ])

ue = set([
        uber_eats_scraping.parse(x) for x in uber_eats_scraping.scrape(
            uber_eats_scraping.navigate('92117')
            )
        ])


toSend = reduce(helpers.getUnion, [ue, gh, dd])
for to in toSend:
    print(to)

for rest in toSend:
    docRef = db.collection(u'Restaurants').document(rest.name)
    docRef.set(rest.JSON)

