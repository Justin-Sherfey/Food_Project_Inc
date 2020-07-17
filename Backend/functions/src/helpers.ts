function sleep(milliseconds: number): void {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
};

/**
 *
 */
function union(arr1: Array<string>, arr2: Array<string>): Array<string> {
    const unionArray = Array<string>();
    let item: string;
    for (item in arr1) {
        if (item in arr2) {
            unionArray.push(item);
        };
    };
    return unionArray;
};

function formatRestaurants(array: Array<string>): Array<object> {
    let restaurantDN: string;
    const restaurants = Array<object>();
    for (restaurantDN in array) {
        const restaurant = {
            Display_Name: 'restaurantDN',
            name: null
        };
        restaurants.push(restaurant);
    };
    return restaurants;
};

async function sendToDB(restaurants: Array<any>) {
    let restaurant: any;
    const restCollection = db.collection('Restaurants');
    for (restaurant in restaurants) {
        const restObj = restCollection.doc(restaurant.Display_Name);
        await restObj.set(restaurant);
    };
};

