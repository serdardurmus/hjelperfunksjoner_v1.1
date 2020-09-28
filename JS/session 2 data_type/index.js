function myFunctionString() {
    var firstName, lastName, fullName;

    firstName = prompt("Skriv firstName");
    lastName = prompt("Skriv lastName");

    fullName = firstName + " " + lastName;

    alert("Hei "+ fullName);
    document.querySelector("#inp-btn-1").value = fullName
}

function myFunctionNumber() {
    var firstName, lastName, fullName;

    firstNummer = prompt("Skriv nummer 1");
    secondNummer = prompt("Skriv nummer 2");

    total = parseInt(firstNummer) + parseInt(secondNummer);

    alert("Hei "+ total);
    document.querySelector("#inp-btn-2").value = "Total: "+total
    let num1 = 4;
    document.querySelector("#area").innerHTML = num1;

}

// JS Operators
let num1 = 4;
console.log(num1++);  // 4
console.log(num1);  // 5