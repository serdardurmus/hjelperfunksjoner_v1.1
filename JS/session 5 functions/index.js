// metod 1
function findX (v, t) {
    var x = v*t
    return x;
}

console.log("findX(3) " + findX(3));
console.log("findX(3, 4) " + findX(3, 4));
// alert(findX(3,4));

// --------------------
// metod 2

var findHipotenus = function(a, b) {
    var hipotenus = (a**2 +b**2) ** (0.5)
    return hipotenus
}

console.log("Hipotebus: " + findHipotenus(3,4));


// --------------------
// nested - anbefales ikke
function findX (v, t) {
    var x = v*t
    return sub_func(x);
}

function sub_func(rslt) {
    return rslt + 10;
}
console.log("findX(3, 4) " + findX(3, 4, "sub_func"));


// --------------------------
// Scope
var x;  // Global variable
function sampleFunction () {
    x = 55;
    return x
}

console.log(sampleFunction());

// Example 1

const r = 10;
const pi = 3.14

function calculate(r) {
    // alert("2*pi*r => " + parseInt(2 * pi * r)); // 62.800000 => 62
    // alert("pi r * r => " + parseInt(pi * (r ** 2)));
    return r;
}

calculate(r);


// example 2

const element = 10;
function if_loop(number) {
    for (let i = 0; i < number; i++) {
        if (i == 5) { continue;}
        if (i == 7 ) { break;}
        console.log(i)
}
}
// console.log(if_loop(element));
if_loop(element);