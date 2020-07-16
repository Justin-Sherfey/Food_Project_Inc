const puppeteer = require('puppeteer');
const url = 'https://www.ubereats.com/';


function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}


async function scrapeFeatured() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);

    const addressBar = '#location-typeahead-home-input';
    await page.click(addressBar);
    sleep(1000);
    await page.type(addressBar, '92117', {delay: 100});
    sleep(3000);
    
    await page.keyboard.press('Enter');
    sleep(8000);

    const featuredNav = 'div.au.aw.et.f2.ba > a';
    await page.click(featuredNav);
    sleep(8000);   

    let featRests = await page.evaluate(
        () => Array.from(
            document.querySelectorAll("h3")
        ).map(element => element.innerText)
    );
    featRests = featRests.slice( 0, 10);

    console.log(featRests);
};

scrapeFeatured();
