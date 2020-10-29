const checkButton = document.querySelector("#checkButton");
checkButton.addEventListener("click", check);
const num = document.getElementById("numberPreCheck");
const result = document.getElementById("result");
function check() {
    var romanNumeral = "";
    let value = num.value;
    let j = findBigger(value)
    if(j===-1) alert("Değer gir...");
    while (j!= -1) {
        console.log(romanNum[j])
        value -= dNum[j];
        romanNumeral += romanNum[j];
        j = findBigger(value)
    }
    result.innerHTML = `${num.value} converted as ${romanNumeral}`;
    num.value = "";
}
// roman numeral
var romanNum = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];
// decimal number
var dNum = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
function findBigger(value){
    let x = dNum.findIndex(num => value>=num)
    console.log(x);
    return x;
}