/*

    Add the code above, to your HTML file

    Using Javascript:
        Retrieve the div and console.log it
        Change the name “Pete” to “Richard”.
        Delete the second <li> of the second <ul>.
        Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)

    Using Javascript:
        Add a class called student_list to both of the <ul>'s.
        Add the classes university and attendance to the first <ul>.

    Using Javascript:
        Add a “light blue” background color and some padding to the <div>.
        Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
        Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
        Change the font size of the whole body.

    Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).



*/


// 1. Retrieve the div and console.log it
const containerDiv = document.getElementById("container");
console.log(containerDiv);

// 2. Change "Pete" to "Richard"
const firstUl = document.querySelectorAll(".list")[0];
firstUl.children[1].textContent = "Richard";

// 3. Delete the second <li> of the second <ul>
const secondUl = document.querySelectorAll(".list")[1];
secondUl.removeChild(secondUl.children[1]); // removes "Sarah"

// 4. Change the name of the first <li> of each <ul> to your name
const ulLists = document.querySelectorAll(".list");
ulLists.forEach((ul) => {
  ul.children[0].textContent = "Ahmed"; // change to your name
});

// 5. Add a class called student_list to both <ul>'s
ulLists.forEach((ul) => {
  ul.classList.add("student_list");
});

// 6. Add classes university and attendance to the first <ul>
firstUl.classList.add("university", "attendance");

// 7. Add "light blue" background and padding to the <div>
containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";

// 8. Hide the <li> that contains "Dan"
const allLi = document.querySelectorAll("li");
allLi.forEach((li) => {
  if (li.textContent.trim() === "Dan") {
    li.style.display = "none";
  }
});

// 9. Add a border to the <li> that contains "Richard"
allLi.forEach((li) => {
  if (li.textContent.trim() === "Richard") {
    li.style.border = "2px solid red";
  }
});

// 10. Change the font size of the whole body
document.body.style.fontSize = "18px";

// BONUS: Alert if background is light blue
if (containerDiv.style.backgroundColor === "lightblue") {
  const names = [];
  const nameLis = document.querySelectorAll(".list li");
  nameLis.forEach((li) => {
    names.push(li.textContent.trim());
  });
  alert(`Hello ${names.join(" and ")}`);
}
