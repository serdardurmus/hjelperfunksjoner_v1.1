
class Player {
    constructor(name, surname, age) {
        this.name = name;
        this.surname = surname;
        this.age = age;
    }
}

let player_1 = new Player("Serdar", "Durmus", 30);
let player_2 = new Player("Tarık", "Demir", 20);
let player_3 = new Player("Emre", "Kaya", 25);
console.log(player_1);
console.log(player_2.surname);
