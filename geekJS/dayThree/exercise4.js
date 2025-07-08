
/*

Exercise 4 : Vacations Costs
Instructions

Let’s create functions that calculate your vacation’s costs:

    Define a function called hotelCost().
        It should ask the user for the number of nights they would like to stay in the hotel.
        If the user doesn’t answer or if the answer is not a number, ask again.
        The hotel costs $140 per night. The function should return the total price of the hotel.

    Define a function called planeRideCost().
        It should ask the user for their destination.
        If the user doesn’t answer or if the answer is not a string, ask again.
        The function should return a different price depending on the location.
            “London”: 183$
            “Paris” : 220$
            All other destination : 300$

    Define a function called rentalCarCost().
        It should ask the user for the number of days they would like to rent the car.
        If the user doesn’t answer or if the answer is not a number, ask again.
        Calculate the cost to rent the car. The car costs $40 everyday.
            If the user rents a car for more than 10 days, they get a 5% discount.
        The function should return the total price of the car rental.

    Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
    Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
    Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

    Call the function totalVacationCost()

    Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

*/
//  before use that code don't forget to install prompt-sync package 
const prompt = require("prompt-sync")({sigint: true});



function hotelCost(nightinput) {
    //let nightinput = require("how many nights will you stay at the hotel?");
    let nights = parseInt(nightinput);
    while (isNaN(nights) || nights <= 0) {
        nightinput = prompt("invalid input please enter a valid number of nights:");
        nights = parseInt(nightinput);

    }

    return nights * 140;
}

function planeRideCost(destination) {
    //let destination = require("where are you flying to?");
    while (!destination || typeof destination !== 'string') {
        destination = prompt("invalid input please enter a valid destination");

    }

    switch (destination.toLowerCase().trim()) {
        case "london":
            return 183;
        case "paris":
            return 220;
        default:
            return 300;
    }
    
}

function rentalCarCost(days) {
    //let days = parseInt(require("How many days will you rent the car? "));
    while (isNaN(days) || days <= 0) {
        days = parseInt(prompt("Invalid input. Please enter a valid number of days: "));
    }
    let cost = days * 40;
    if (days > 10) cost *= 0.95;
    return cost;
}
function totalVacationCost() {
    let nights = prompt("How many nights will you stay at the hotel?");
    let destination = prompt("where are you flying to?");
    let days = prompt("how many days will you rent the car?");

    let x = hotelCost(nights);
    let y = planeRideCost(destination);
    let z = rentalCarCost(days);
    return  `The hotel cost : $${x}, the plane tickets cost: $${y}, the car cost: $${z}, total cost: $${x + y + z}.`;

}
// call function to se the result 
console.log(totalVacationCost());
