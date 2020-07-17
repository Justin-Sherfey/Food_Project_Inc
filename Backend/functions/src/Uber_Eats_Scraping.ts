const ueURL = 'https://www.ubereats.com/';

exports.scrapeUEFeatured = async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(ueURL);

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

    await browser.close();
    return featRests;

};

