const myArray_1 = [3, 66, 45, 101, 71, 15, 37]
const myArray_2 = ["Oslo", "Trondheim", "Bergen", "Lier", "Asker"]
const myArray_3 = ["Et ord", " et nummer" , 3, false, "", [1,3,5]]
const myArray_4 = {nummer_1: 1, nummer_2:2, nummer_3:3, nummer_4: 4};
const nummeret = 1;
const et_ord = "String";

myArray_1[0]= 12;
console.log(myArray_1);
console.log(myArray_2[0]);
console.log("nummer_1: " + myArray_4["nummer_1"]);

// length og sort
{
    console.log("myArray_1.length : " + myArray_1.length);
    console.log("myArray_4.length : " + myArray_4.length); // undefined
    console.log(myArray_1.sort()); // !
    console.log(myArray_2.sort()); // Den fungerer godt
    console.log(myArray_4.sort); // undefined
}

// push - unshift // pop - shift
myArray_2.push("Gjøvik");
myArray_3.unshift("Setning");
myArray_2.pop();  // bak
myArray_1.shift();  // foran
console.log(myArray_2);  // bak
console.log(myArray_3);  // foran
console.log(myArray_1);  // foran


// Array.isArray
console.log(Array.isArray(myArray_2));  // true 
console.log(Array.isArray(myArray_4)); // false
console.log(myArray_3 instanceof Array); // true

// example
const myMath = [3, 66, 45];
let sElement = 0;
let dElement = 1 ;
function sumFunction() {
    for (let i = 0; i < myMath.length; i++) {
        sElement += myMath[i];
    }
    return sElement;
}
function dFunction() {
    for (let i = 0; i < myMath.length; i++) {
        dElement *= myMath[i];        
    }
    return dElement;
}

console.log(sumFunction());
console.log(dFunction());