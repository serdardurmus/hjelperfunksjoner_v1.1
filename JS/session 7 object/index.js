var player1 = {
    name: "serdar",
    surname: "durmus",
    age: 35,
    cars: ["Volvo", "Opel"],
    mail: function() {
        return this.name+this.surname+"@gmail.com";
    },
    fullname: function() {
        return this.name+" "+this.surname;
    }
}

console.log(player1);
console.log(player1.name);
console.log(player1.fullname());
console.log(player1.mail());