/* 
Exercise 4 : Building Management
Instructions:

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}


Review about objects

    Copy and paste the above object to your Javascript file.

    Console.log the number of floors in the building.

    Console.log how many apartments are on the floors 1 and 3.

    Console.log the name of the second tenant and the number of rooms he has in his apartment.

    Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.



*/

// Exercise 4: Building Management

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
};

// 1. Console.log the number of floors in the building.
console.log("Number of floors:", building.numberOfFloors);

// 2. Console.log how many apartments are on the 1st and 3rd floors.
const floor1 = building.numberOfAptByFloor.firstFloor;
const floor3 = building.numberOfAptByFloor.thirdFloor;
console.log("Apartments on 1st and 3rd floor:", floor1 + floor3);

// 3. Console.log the name of the second tenant and the number of rooms he has.
const secondTenant = building.nameOfTenants[1];  // "Dan"
const numberOfRooms = building.numberOfRoomsAndRent.dan[0];
console.log(`${secondTenant} has ${numberOfRooms} rooms.`);

// 4. Check if Sarah’s and David’s rent > Dan’s rent. If so, increase Dan’s rent to 1200.
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log("Dan's rent increased to 1200.");
} else {
    console.log("No change to Dan's rent.");
}
