
const colors = ["red", "blue", "gray", "green", "purple"]

const buttonElement = document.querySelector("#randomColorButton");

buttonElement.addEventListener("click", changeColors);
// buttonElement.addEventListener("click", () => changeColors());
// buttonElement.addEventListener("click", function () {
//     changeColors()
// });

// Vi velger tilfeldig elementet fra Array.
function changeColors () {
    const randomIndex = Math.floor(Math.random() * colors.length);
    document.querySelector("body").style.backgroundColor = colors[randomIndex];

    document.querySelector("#colorName").innerHTML = colors[randomIndex];

    console.log(randomIndex);
}