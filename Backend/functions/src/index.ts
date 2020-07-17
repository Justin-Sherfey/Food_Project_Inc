// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require('firebase-functions');

// The Firebase Admin SDK to access Cloud Firestore.
const admin = require('firebase-admin');
admin.initializeApp();
const db = admin.firestore();

// dependencies
const puppeteer = require('puppeteer');

//functions dependencies
const UE = require('./Uber_Eats_Scraping');
const GH = require('./Grub_Hub_Scraping');


//functions///////////////////////////////////////////////////////////////////

//featured section
exports.updateFeatured = functions.pubsub.schedule('every day').onRun(
    async (context: any) => {
        const featuredArray = union(UE.scrapeUEFeatured(), GH.scrapeGHFeatured());
        const featuredRestaurants = formatRestaurants(featuredArray);
        await sendToDB(featuredRestaurants);
    }
)
