/*
Exercise 2 : Shopping List
Instructions

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

    Add the stock and prices objects to your js file.

    Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

    Create a function called myBill() that takes no parameters.

    The function should return the total price of your shoppingList. In order to do this you must follow these rules:
        The item must be in stock. (Hint : check out if .. in)
        If the item is in stock find out the price in the prices object.

    Call the myBill() function.

    Bonus: If the item is in stock, decrease the item’s stock by 1

*/
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
function addItemStokPrice(obj , stockn, price)  {
    if (!(obj in stock )){
        stock[obj] = stockn;
        prices[obj] = price;
        
    }
    else {
        console.log( `item ${obj} already exists in stock`);
    }

}
function updateprice(obj , price) {
    if (obj in prices) {
        prices[obj] = price;
    }
    else {
        console.log( `item ${obj} not found in price list`);
    }
}
function updatestock(obj, stockn) {
    if (obj in stock) {
        stock[obj] = stockn;
    }
    else {
        console.log( `item ${obj} not found in stock list`);
    }
}

const shoppingList = ["banana", "orange", "apple"];
function myBill() {
    let total = 0;
    for (let item of shoppingList) {
        if (item in stock && stock[item] > 0 ) {
            total += prices[item] ;
            stock[item] -= 1;
        }
    }
     return console.log(`total price of your shoppingList is: ${total}`);
}
addItemStokPrice("Kiwi", 10, 6);
updateprice("Kiwi", 5);
updatestock("Kiwi", 8);

myBill();
console.log(`updated stock: `, stock);