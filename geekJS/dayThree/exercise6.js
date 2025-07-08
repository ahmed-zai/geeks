/*
Exercise 6 : Change the navbar
Instructions

Create a new structured HTML file and a new Javascript file

<div id="navBar">
    <ul>
        <li><a href="#">Profile</a></li>
        <li><a href="#">Home</a></li>
        <li><a href="#">My Friends</a></li>
        <li><a href="#">Messenger</a></li>
        <li><a href="#">My Pics</a></li>
    </ul>
</div>


    Add the code above, to your HTML file

    Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

    We are going to add a new <li> to the <ul>.
        First, create a new <li> tag (use the createElement method).
        Create a new text node with “Logout” as its specified text.
        Append the text node to the newly created list node (<li>).
        Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

    Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).

*/


// 1. Change the id from "navBar" to "socialNetworkNavigation"
const navDiv = document.getElementById("navBar");
navDiv.setAttribute("id", "socialNetworkNavigation");

// 2. Create a new <li> element
const newLi = document.createElement("li");

// 3. Create a text node with "Logout"
const logoutText = document.createTextNode("Logout");

// 4. Append the text node to the <li>
newLi.appendChild(logoutText);

// 5. Append the <li> to the <ul>
const ul = document.querySelector("#socialNetworkNavigation ul");
ul.appendChild(newLi);

// 6. Use firstElementChild and lastElementChild to get <li>s
const firstLi = ul.firstElementChild;
const lastLi = ul.lastElementChild;

// 7. Display the text content of both
console.log("First link text:", firstLi.textContent);
console.log("Last link text:", lastLi.textContent);
