"use strict"
// DOM

// --------------------------------------------
// document.getElementById
// ID
const element = document.getElementById("user_name");
console.log(element);

// CLASS
const elements = document.getElementsByClassName("user_tag");
console.log(elements);

// TAG
const elements_2 = document.getElementsByTagName("p")
console.log(elements_2);


// --------------------------------------------
console.log("// --------------------------------------------");
// querySellector - querySelectorAll
// ID
const elements_3 = document.querySelector("#user_name");
console.log(elements_3);

// CLASS
const elements_4 = document.querySelector(".user_tag");
console.log(elements_4);
const elements_5 = document.querySelectorAll(".user_tag");
console.log(elements_5);

// TAG
const elements_6 = document.querySelectorAll("p");
console.log(elements_6);

// Hva er foskjellen mellom getElementBy/Id/Tag og querySelector/All
const elements_7 = document.getElementsByClassName("user_tag");
const elements_8 = document.querySelectorAll(".user_tag");

console.log(elements_7);  // HTMLCollection
console.log(elements_8);  // NodeList
/*
    - HTMLCollection
        . Live/Dinamic. Değişiklikleri takip eder. Array'daki metodlara sahip değildir.
    - NodeList
        . Static. O andaki elementlerin durumunu alır, saklar.  
*/