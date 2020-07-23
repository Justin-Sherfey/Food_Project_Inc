from Uber_Eats_Scraping import scrapeFeatured
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('../../project-food-5b105-d02a0c57a1eb.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

featured = scrapeFeatured()

for displayName in featured:
    restaurant = db.collection(u'Restaurants').document(displayName)
    restaurant.set({
        u'Display_Name': displayName,
        u'name': u'temp'
    })
