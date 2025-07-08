// 1. Array of books
const allBooks = [
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://m.media-amazon.com/images/I/91b0C2YNSrL._AC_UF1000,1000_QL80_.jpg",
    alreadyRead: true
  },
  {
    title: "1984",
    author: "George Orwell",
    image: "https://covers.openlibrary.org/b/id/7222246-L.jpg",
    alreadyRead: false
  }
];

// 2. Get the section where books will be added
const bookSection = document.querySelector(".listBooks");

// 3. Loop through books and create HTML for each
allBooks.forEach(book => {
  // Create the container div
  const bookDiv = document.createElement("div");
  bookDiv.style.marginBottom = "20px";

  // Create and style title + author text
  const bookInfo = document.createElement("p");
  bookInfo.textContent = `${book.title} written by ${book.author}`;
  if (book.alreadyRead) {
    bookInfo.style.color = "red";
  }

  // Create and style the image
  const bookImg = document.createElement("img");
  bookImg.src = book.image;
  bookImg.style.width = "100px";
  bookImg.style.display = "block";
  bookImg.style.marginTop = "5px";

  // Append elements
  bookDiv.appendChild(bookInfo);
  bookDiv.appendChild(bookImg);
  bookSection.appendChild(bookDiv);
});
