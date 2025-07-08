/*
 Exercise 1 : Find the numbers divisible by 23
Instructions

    Create a function call displayNumbersDivisible() that takes no parameter.

    In the function, loop through numbers 0 to 500.

    Console.log all the numbers divisible by 23.

    At the end, console.log the sum of all numbers that are divisible by 23.

    Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 
    368 391 414 437 460 483
    Sum : 5313


    Bonus: Add a parameter divisor to the function.

    displayNumbersDivisible(divisor)

    Example:
    displayNumbersDivisible(3) : Console.log all the numbers divisible by 3, 
    and their sum
    displayNumbersDivisible(45) : Console.log all the numbers divisible by 45, 
    and their sum




*/
console.log('hello');

function displayNumbersDivisible(divisor) {
    let sum = 0;
    let mySet = new Set();

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
           
            mySet.add(i);
            sum += i;
            
        }
    }
    return { numbers: mySet, sum: sum };
    
} 

function printFunctions(divisor){
    console.log(`Numbers divisible by ${divisor}:` , displayNumbersDivisible(divisor));
    console.log('=======');
}
printFunctions(23);
printFunctions(3);