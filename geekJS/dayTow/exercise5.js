/* 
Exercise 5 : Family
Instructions

    Create an object called family with a few key value pairs.
    Using a for in loop, console.log the keys of the object.
    Using a for in loop, console.log the values of the object.



*/
const family = {
    father: "Jhon", 
    mother: "Jane",
    son: "jack",
    doughter: "jill"

}
// log keys of the object 
for (let key in family) {
    console.log(key);

}
// log values of the object 
for (let key in family) {
    console.log(family[key]);
    
}