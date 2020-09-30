
// buttons
document.getElementById("submit_btn").addEventListener("click", submitUser);
document.getElementById("list_btn").addEventListener("click", listUsers);

// userlist
const userList = [];

// user of class
class User {
  constructor(userName, userSurname, userAge) {
    this.name = userName;
    this.surname = userSurname;
    this.age = userAge;
  }
}

function submitUser() {
  const name = document.getElementById("name_inp").value;
  const surname = document.getElementById("surname_inp").value;
  const age = document.getElementById("age_inp").value;

  const user = new User(name, surname, age);
  userList.push(user);
}

function listUsers() {
  console.log(userList);
}

/*
class User {
  constructor(name, password, age) {
    this.userName = name;
    this.userPassword = password;
    this.userAge = age;
  }
}

const myUser_1 = new User("Serdar", "EMC2", 25);
const myUser_2 = new User("Thomas", "Tesla2012", 30);
console.log(myUser_1);
console.log(myUser_2);


// JSON
class Car {
  constructor(param) {
    this.name = param.name;
    this.model = param.model;
    this.color = param.color;
  }
  login () {
    console.log(this.name + " logged in!");
  }
}

const car_1 = new Car ({name: "Tesla", model: "2020", color: "black"});
const car_2 = new Car ({name: "BMW", model: "2018", color: "darkblue"});
console.log(car_1);
car_1.login();
car_2.login();
*/