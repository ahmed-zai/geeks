// Array of planet objects, each with name, color, and number of moons
const planets = [
  { name: "Mercury", color: "#b1b1b1", moons: 0 },
  { name: "Venus", color: "#e6c36d", moons: 0 },
  { name: "Earth", color: "#2e8b57", moons: 1 },
  { name: "Mars", color: "#c1440e", moons: 2 },
  { name: "Jupiter", color: "#f4a460", moons: 79 },
  { name: "Saturn", color: "#deb887", moons: 82 },
  { name: "Uranus", color: "#add8e6", moons: 27 },
  { name: "Neptune", color: "#4169e1", moons: 14 }
];

// Get the section to append planets to
const section = document.querySelector(".listPlanets");

// Create each planet
planets.forEach((planetObj) => {
  const planet = document.createElement("div");
  planet.classList.add("planet");
  planet.style.backgroundColor = planetObj.color;
  planet.textContent = planetObj.name;

  // Position planet with margin
  planet.style.margin = "20px";
  planet.style.display = "inline-block";
  planet.style.color = "white";
  planet.style.lineHeight = "100px";

  // Add moons
  for (let i = 0; i < planetObj.moons; i++) {
    const moon = document.createElement("div");
    moon.classList.add("moon");

    // Position moons in a circle around the planet
    const angle = (i / planetObj.moons) * 2 * Math.PI;
    const radius = 60 + (i % 3) * 10;

    moon.style.left = `${50 + radius * Math.cos(angle)}px`;
    moon.style.top = `${50 + radius * Math.sin(angle)}px`;

    planet.appendChild(moon);
  }

  section.appendChild(planet);
});
