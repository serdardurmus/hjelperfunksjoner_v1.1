
console.log("js file loaded");

document.getElementById('mySpan1').addEventListener('click', function() {
    console.log("Hide me");
    document.getElementById("myDiv").style.visibility = "hidden";
});
document.getElementById("mySpan2").addEventListener("click", function() {
    console.log("Show me");
    document.getElementById("myDiv").style.visibility ="";
})

/*
document.getElementById("mySpan").addEventListener("mouseover", function() {
    console.log("Mouseover")
});
document.getElementById("mySpan").addEventListener("mouseout", function() {
    console.log("mouseout")
});*/


document.getElementById("mySpan3").addEventListener("click", function() {
    const result = document.getElementById("myDiv").style.visibility;

    if (result === "hidden") { document.getElementById("myDiv").style.visibility = ""} else {
        document.getElementById("myDiv").style.visibility ="hidden";
    }
})

document.getElementById("mySpan4").addEventListener("click", function() {
    const temp = prompt("Hva er temperaturen med Kelvin?")
    alert(`${temp} Kelvin =  ${temp-273} Celcius`);
})

