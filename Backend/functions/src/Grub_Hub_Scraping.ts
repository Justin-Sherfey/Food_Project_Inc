//TODO: remove 'open now' tag

const puppeteer = require('puppeteer');

const url = 'https://www.grubhub.com/';

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

async function scrapeGHFeatured() { 
    const browser = await puppeteer.launch(); 
    const page = await browser.newPage(); 
    await page.goto(url);

    const navbar = '#homepage-logged-out-top > ghs-welcome-view > div > div.homepage-inset.s-row.s-col-md-6 > div.s-row.u-flex-align-self-xs--center.s-col-xs-12 > div:nth-child(2) > ghs-start-order-form > div > div.u-stack-y-3.u-padding-left-cancel.s-col-xs-12 > div > ghs-address-input > div > div > div > input';
    await page.type(navbar, '92117');
    const findFood = '#homepage-logged-out-top > ghs-welcome-view > div > div.homepage-inset.s-row.s-col-md-6 > div.s-row.u-flex-align-self-xs--center.s-col-xs-12 > div:nth-child(2) > ghs-start-order-form > div > div:nth-child(2) > button'
    await page.click(findFood)
    sleep(10000);

    let favorites = await page.evaluate(
        () => Array.from(
        document.querySelectorAll("h5.u-text-ellipsis")
        ).map(element => element.textContent)
    );   

    favorites = favorites.slice( 0, 10);
    await browser.close();

    return favorites;
};

async function tryUntilSuccess() {
    let favorites = await scrapeGHFeatured();
    while (favorites.length == 0) {
        favorites = await scrapeGHFeatured();
    };
    console.log(favorites);
};

tryUntilSuccess();
