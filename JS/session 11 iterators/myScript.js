// Iterators

// forEach
{
    const numbers = [5, 33, 1,3,6,7,33,2,4,10]

    numbers.forEach((number, index) => {
      console.log(number, index);
    })
} 
// MAP
{
  const numbers = [5, 33, 1,3,6,7,33,2,4,10];
  const newNumbers = numbers.map((number) => {
    return number*2
  });
  console.log(newNumbers);
}

// Find
// Array'da aradığımız spesifik bir değeri bulmamıza yarıyor
{
  const users = [
    {id: 0, name: "serdar", age: 2},
    {id: 1, name: "ömer", age: 22},
    {id: 2, name: "emre", age: 21},
    {id: 3, name: "ali", age: 32}
  ];

  let myUsers = users.find((user) => user.name === "serdar");
  console.log(myUsers);
  let myUsers2 = users.find((user) => user.age > 20);
  console.log(myUsers2);
  const myUsers3 = users.find((user) => {
    return user.age >20
  })

  console.log(myUsers3);
}

// Filter
{
  const users = [
    {id: 0, name: "serdar", age: 2},
    {id: 1, name: "ömer", age: 22},
    {id: 2, name: "emre", age: 21},
    {id: 3, name: "ali", age: 32}
  ];

  const  myUsers = users.filter((user) => user.age >20)
  console.log(myUsers);
}

// reduce - example 1
console.log("// reduce - example 1  --------------------------")
{
  const numbers = [5, 33, 1,3,6,7,33,2,4,10]
  const result = numbers.reduce((acc, curr) => {
    
  })
  console.log(result);
}

// reduce - example 1
console.log("// reduce - example 1  --------------------------")
{
  const numbers = [5, 33, 1,3,6,77,33,2,4,10]
  const maxNumber = numbers.reduce((acc, curr) => {
    return acc > curr ? acc : curr
  })
  console.log(maxNumber);
}