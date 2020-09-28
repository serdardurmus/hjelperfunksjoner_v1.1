class User {
    constructor(firstName, lastName, credits) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.credits = credits;
    }
    getFullname() {
        let fullName = `${this.firstName} ${this.lastName} is my full name`;
        return fullName;
    }
    editName(newname) {
        let editName = newname.split(" ");
        this.firstName = editName[0];
        this.lastName = editName[1];
    }
}

const john = new User("Serdar", "Durmus", 34);
console.log(john.firstName)
console.log(john.getFullname());

john.editName("Emre Kaya");
console.log(john.getFullname());