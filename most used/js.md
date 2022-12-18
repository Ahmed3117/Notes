```javascript
 Output To Screen
  - window.alert()
  - document.write()
  - console.log()
```

```javascript
/*
  Console Methods
  - log
  - error
  - table

  Web API

  Styling Console
  - Directive %c
*/

console.log("Log");
console.error("Error");
console.table(["Osama", "Ahmed", "Sayed"]);

console.log("Hello From %cJS %cFile", "color: red; font-size: 40px", "color: blue; font-size: 40px");
```

```javascript
var myName = "Osama";

console.log("Hello " + myName);
console.log(`Hello ${myName}`);
```

## Data types :

```javascript
/*
  Data Types Intro
  - String
  - Number
  - Array => Object
  - Object
  - Boolean
*/

console.log("Osama Mohamed");
console.log(typeof "Osama Mohamed");
console.log(typeof 5000);
console.log(typeof 5000.99);
console.log(typeof [10, 15, 17]);
console.log(typeof { name: "Osama", age: 17, country: "Eg" });
console.log(typeof true);
console.log(typeof false);
console.log(typeof undefined);
console.log(typeof null);
```

## var, let, const :

```javascript
/*
  Var
  - Redeclare (Yes)
  - Access Before Declare (Undefined)
  - Variable Scope Drama [Added To Window] ()
  - Block Or Scope Function

  Let
  - Redeclare (No => Error)
  - Access Before Declare (Error)
  - Variable Scope Drama ()
  - Block Or Scope Function

  Const
  - Redeclare (No => Error)
  - Access Before Declare (Error)
  - Variable Scope Drama ()
  - Block Or Scope Function
*/
```

## string :

```javascript
console.log('Elzero Web "School"');
console.log("Elzero Web 'School'");
console.log("Elzero Web \"School\"");
console.log('Elzero \\ Web \'School\'');
console.log("Elzero \
Web \
School");
console.log("Elzero\nWeb\nSchool");

/*
  Concatenation
*/

let a = "We Love";
let b = "JavaScript";

document.write(a + " " + b);

console.log(a, b);
```

* Template Literals (Template Strings)

  ```javascript
  /*
    Template Literals (Template Strings)
  */
  
  // First Example
  
  let a = "We Love"; 
  let b = "JavaScript";
  let c = "And";
  let d = "Programming";
  
  console.log(a = " \"\" " + b +
  "\n" + c + " " + d);
  
  console.log(`${a} "" '' \\ ${b}
  ${c} ${d}`);
  
  // Second Example
  
  let title = "Elzero";
  let desc = "Elzero Web School";
   
  let markup = `
    <div class="card">
      <div class="child">
        <h2>${title}</h2>
        <p>${desc}</p>
      </div>
    </div>
  `;
  
  document.write(markup);
  ```

  

## string methods

```javascript
/*
  String Methods
  - Access With Index
  - Access With charAt()
  - length
  - trim()
  - toUpperCase()
  - toLowerCase()
  - Chain Methods
*/

let theName = "  Ahmed  ";

console.log(theName);
console.log(theName[1]);
console.log(theName[5]);

console.log(theName.charAt(1));
console.log(theName.charAt(5));

console.log(theName.length);
console.log(theName.trim());

console.log(theName.toUpperCase());
console.log(theName.toLowerCase());

console.log(theName.trim().charAt(2).toUpperCase());

/*
  String Methods
  - indexOf(Value [Mand], Start [Opt] 0)
  - lastIndexOf(Value [Mand], Start [Opt] Length)
  - slice(Start [Mand], End [Opt] Not Include End)
  - repeat(Times) [ES6]
  - split(Separator [Opt], Limit [Opt])
*/

let a = "Elzero Web School";

console.log(a.indexOf("Web"));
console.log(a.indexOf("Web", 8));
console.log(a.indexOf("o")); // 5
console.log(a.lastIndexOf("o")); // 15

console.log(a.slice(2, 6));
console.log(a.slice(-5, -3));

console.log(a.repeat(5));

console.log(a.split("", 6));

/*
  String Methods
  - substring(Start [Mand], End [Opt] Not Including End)
  --- Start > End Will Swap
  --- Start < 0 It Start From 0
  --- Use Length To Get Last Character
  - substr(Start [Mand], Characters To Extract)
  --- Start >= Length = ""
  --- Negative Start From End
  - includes(Value [Mand], Start [Opt] Default 0) [ES6]
  - startsWith(Value [Mand], Start [Opt] Default 0) [ES6]
  - endsWith(Value [Mand], Length [Opt] Default Full Length) [ES6]
*/

let a = "Elzero Web School";

console.log(a.length);

console.log(a.substring(2, 6));
console.log(a.substring(6, 2));
console.log(a.substring(-10, 6)); // 0 - 6
console.log(a.substring(a.length - 5, a.length - 3));

console.log(a.substr(0, 6));
console.log(a.substr(17));
console.log(a.substr(-3));
console.log(a.substr(-5, 2));

console.log(a.includes("Web"));
console.log(a.includes("Web", 8));

console.log(a.startsWith("E"));
console.log(a.startsWith("E", 2));
console.log(a.startsWith("zero", 2));

console.log(a.endsWith("l"));
```

## Arithmetic Operators

```javascript
/*
  Arithmetic Operators
  + Addition
  - Subtraction
  * Multiplication
  / Division
  ** Exponentiation (ES7)
  % Modulus (Division Remainder)
  ++ Increment [ Post / Pre ]
  -- Decrement [ Post / Pre ]
*/

console.log(10 + 20);
console.log(10 + "Osama");

console.log(10 - 20);
console.log(10 - "Osama"); // NaN
console.log(typeof NaN);

console.log(10 * 20);
console.log(10 * -20);

console.log(20 / 5);
console.log(20 / 3);

console.log(2 ** 4);
console.log(2 * 2 * 2 * 2);

console.log(10 % 2);
console.log(11 % 2); // Remove 1
```

## Unary Plus, Unary Negation

```javascript
/*
  - + Unary Plus [Return Number If Its Not Number]
  - - Unary Negation [Return Number If Its Not Number + Negates It]
  Tests
  - Normal Number
  - String Number
  - String Negative Number
  - String Text
  - Float
  - Hexadecimal Numeral System => 0xFF
  - null
  - false
  - true
*/

console.log(+100);
console.log(+"100");
console.log(+"-100");
console.log(+"Osama");
console.log(+"15.5");
console.log(+0xff);
console.log(+null);
console.log(+false);
console.log(+true);

console.log(-100);
console.log(-"100");
console.log(-"-100");
console.log(-"Osama");
console.log(-"15.5");
console.log(-0xff);
console.log(-null);
console.log(-false);
console.log(-true);

console.log(Number("100"));
```

## Type Coercion (Type Casting)

```javascript
/*
  Type Coercion (Type Casting)
  - +
  - -
  - "" - 2
  - false - true
*/

let a = "100";
let b = 20;
let c = true;

console.log(+a + b + c);
```

## Assignment Operators

```javascript
/*
  Assignment Operators
*/

let a = 10;

a = a + 20;

a = a + 70;

a += 100; // a = a + 100

a -= 50; // a = a - 50

a /= 50; // a = a / 50

// Examples :
/*
  Challenge 1
*/

let a = 10;
let b = "20";
let c = 80;

console.log(++a + +b++ + +c++ - +a++);
console.log(++a + -b + +c++ - -a++ + +a);
console.log(--c + +b + --a * +b++ - +b * a + --a - +true);

/*
  [++a] [+]
  [++a]
  - Value:
  - Explain:
  [+]
  - Explain:
*/

/*
  Challenge 2
*/

let d = "-100";
let e = "20";
let f = 30;
let g = true;

// Only Use Variables Value
// Do Not Use Variable Twice

console.log(); // 2000
console.log(); // 173
```

## comprison opertors

```javascript
/*
  Comparison Operators
  - == Equal
  - != Not Equal

  - === Identical
  - !== Not Identical

  - > Larger Than
  - >= Larger Than Or Equal

  - < Smaller Than
  - <= Smaller Than Or Equal
*/

console.log(10 == "10"); // Compare Value Only
console.log(-100 == "-100"); // Compare Value Only
console.log(10 != "10"); // Compare Value Only

console.log(10 === "10"); // Compare Value + Type
console.log(10 !== "10"); // Compare Value + Type
console.log(10 !== 10); // Compare Value + Type

console.log(10 > 20);
console.log(10 > 10);
console.log(10 >= 10);

console.log(10 < 20);
console.log(10 < 10);
console.log(10 <= 10);

console.log(typeof "Osama" === typeof "Ahmed");
```

## logical operators

```javascript
/*
  Logical Operators
  - ! Not
  - && And
  - || Or
*/

console.log(true);
console.log(!true);

console.log(!(10 == "10"));

console.log(10 == "10" && 10 > 8 && 10 > 50);

console.log(10 == "10" || 10 > 80 || 10 > 50);
```

## Numbers

```javascript
/*
  Number
  - Double Precision
  - Syntactic Sugar "_"
  - e
  - **
  - With Decimal
  - Number + BigInt
  - Number Min Value
  - Number Max Value
*/

console.log(1000000);
console.log(1_000_000);
console.log(1e6);
console.log(10 ** 6);
console.log(10 * 10 * 10 * 10 * 10 * 10);
console.log(1000000.0);

console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.MAX_VALUE);
console.log(Number.MAX_VALUE + 23434343434);

/*
  Number Methods
  - Two Dots To Call A Methods
  - toString()
  - toFixed()
  - parseInt()
  - parseFloat()
  - isInteger() [ES6]
  - isNaN() [ES6]
*/

console.log((100).toString());
console.log(100.10.toString());

console.log(100.554555.toFixed(2));

console.log(Number("100 Osama"));
console.log(+"100 Osama");
console.log(parseInt("100 Osama"));
console.log(parseInt("Osama 100 Osama"));
console.log(parseInt("100.500 Osama"));
console.log(parseFloat("100.500 Osama"));

console.log(Number.isInteger("100"));
console.log(Number.isInteger(100.500));
console.log(Number.isInteger(100));

console.log(Number.isNaN("Osama" / 20));

/*
  Number Challenge
*/

let a = 100;
let b = 2_00.5;
let c = 1e2;
let d = 2.4;

// Find Smallest Number In All Variables And Return Integer
console.log();

// Use Variables a + d One Time To Get The Needed Output
console.log(); // 10000

// Get Integer "2" From d Variable With 4 Methods
console.log();
console.log();
console.log();
console.log();

// Use Variables b + d To Get This Valus
console.log(); // 66.67 => String
console.log(); // 67 => Number
```

## Math

```javascript
/*
  Math Object
  - round()
  - ceil()
  - floor()
  - min()
  - max()
  - pow()
  - random()
  - trunc() [Es6]
*/

console.log(Math.round(99.2));
console.log(Math.round(99.5));

console.log(Math.ceil(99.2));
console.log(Math.floor(99.9));

console.log(Math.min(10, 20, 100, -100, 90));
console.log(Math.max(10, 20, 100, -100, 90));

console.log(Math.pow(2, 4));
console.log(Math.random());
console.log(Math.trunc(99.5));
```

## if

```javascript
let price = 100;
let discount = true;
let discountAmount = 30;
let country = "KSA";

if (discount === true) {
  price -= discountAmount; // price = price - discountAmount
} else if (country === "Egypt") {
  price -= 40;
} else if (country === "Syria") {
  price -= 50;
} else {
  price -= 10;
}

console.log(price);

/*
  Nested If
*/

let price = 100;
let discount = false;
let discountAmount = 30;
let country = "Egypt";
let student = true;

if (discount === true) {

  price -= discountAmount;

} else if (country === "Egypt") {

  if (student === true) {

    price -= discountAmount + 30;

  } else {

    price -= discountAmount + 10;

  }

} else {

  price -= 10;

}

console.log(price);

/*
  Conditional (Ternary) Operator
*/

let theName = "Mona";
let theGender = "Female";
let theAge = 30;

if (theGender === "Male") {
  console.log("Mr");
} else {
  console.log("Mrs");
}

// Condition ? If True : If False

theGender === "Male" ? console.log("Mr") : console.log("Mrs");

let result = theGender === "Male" ? "Mr" : "Mrs";

document.write(result);

console.log(theGender === "Male" ? "Mr" : "Mrs");

console.log(`Hello ${theGender === "Male" ? "Mr" : "Mrs"} ${theName}`);

theAge < 20
  ? console.log(20)
  : theAge > 20 && theAge < 60
  ? console.log("20 To 60")
  : theAge > 60
  ? console.log("Larger Than 60")
  : console.log("Unknown");

/*
  Logical Or ||
  -- Null + Undefined + Any Falsy Value
  Nullish Coalescing Operator ??
  -- Null + Undefined
*/

console.log(Boolean(100));
console.log(Boolean(-100));
console.log(Boolean(0));
console.log(Boolean(""));
console.log(Boolean(null));

let price = 0;

console.log(`The Price Is ${price || 200}`);
console.log(`The Price Is ${price ?? 200}`);

//example
let job = "Manager";
let salary = 0;

if (job === "Manager") {
  salary = 8000;
} else if (job === "IT" || job === "Support") {
  salary = 6000;
} else if (job === "Developer" || job === "Designer") {
  salary = 7000;
} else {
  salary = 4000;
}
```

## switch

```javascript
let day = "A";

switch (day) {
  default:
    console.log("Unknown Day");
    break;
  case 0:
    console.log("Saturday");
    break;
  case 1:
    console.log("Sunday");
    break;
  case 2:
  case 3:
    console.log("Monday");
    break;
}
//example

let holidays = 0;
let money = 0;

switch (holidays) {
  case 0:
    money = 5000;
    console.log(`My Money is ${money}`);
    break;
  case 1:
  case 2:
    money = 3000;
    console.log(`My Money is ${money}`);
    break;
  case 3:
    money = 2000;
    console.log(`My Money is ${money}`);
    break;
  case 4:
    money = 1000;
    console.log(`My Money is ${money}`);
    break;
  case 5:
    money = 0;
    console.log(`My Money is ${money}`);
    break;
  default:
    money = 0;
    console.log(`My Money is ${money}`);
}
```

## Array

```javascript
let myFriends = ["Ahmed", "Mohamed", "Sayed", ["Marwan", "Ali"]];

console.log(`Hello ${myFriends[0]}`);
console.log(`Hello ${myFriends[2]}`);
console.log(`${myFriends[1][2]}`);
console.log(`Hello ${myFriends[3][1]}`);
console.log(`${myFriends[3][1][2]}`);

console.log(myFriends);
myFriends[1] = "Gamal";
console.log(myFriends);
myFriends[3] = ["Sameh", "Ameer"];
console.log(myFriends);

console.log(Array.isArray(myFriends));
//ex1:
let myFriends = ["Ahmed", "Mohamed", "Sayed", "Alaa"];

myFriends.length = 2;

console.log(myFriends);
```

* array methods

  ```javascript
  // ex1:
  let myFriends = ["Ahmed", "Mohamed", "Sayed", "Alaa"];
  
  console.log(myFriends);
  
  myFriends.unshift("Osama", "Nabil");
  
  console.log(myFriends);
  
  myFriends.push("Samah", "Eman");
  
  console.log(myFriends);
  
  let first = myFriends.shift();
  
  console.log(myFriends);
  
  console.log(`First Name Is ${first}`);
  
  let last = myFriends.pop();
  
  console.log(myFriends);
  
  console.log(`Last Name Is ${last}`);
  
  // ex2:
  let myFriends = ["Ahmed", "Mohamed", "Sayed", "Alaa", "Ahmed"];
  
  console.log(myFriends);
  
  console.log(myFriends.indexOf("Ahmed"));
  console.log(myFriends.indexOf("Ahmed", 2));
  
  console.log(myFriends.lastIndexOf("Ahmed"));
  console.log(myFriends.lastIndexOf("Ahmed", -2));
  
  console.log(myFriends.includes("Ahmed"));
  console.log(myFriends.includes("Ahmed", 2));
  
  if (myFriends.lastIndexOf("Osama") === -1) {
    console.log("Not Found");
  }
  
  console.log(myFriends.indexOf("Osama"));
  console.log(myFriends.lastIndexOf("Osama"));
  
  // ex3:
  let myFriends = [10, "Sayed", "Mohamed", "90", 9000, 100, 20, "10", -20, -10];
  
  console.log(myFriends);
  console.log(myFriends.sort().reverse());
  
  // ex4:
  let myFriends = ["Ahmed", "Sayed", "Ali", "Osama", "Gamal", "Ameer"];
  console.log(myFriends);
  console.log(myFriends.slice());
  console.log(myFriends.slice(1));
  console.log(myFriends.slice(1, 3));
  console.log(myFriends.slice(-3));
  console.log(myFriends.slice(1, -2));
  console.log(myFriends.slice(-4, -2));
  console.log(myFriends);
  
  myFriends.splice(1, 2, "Sameer", "Samara");
  
  console.log(myFriends);
  
  //ex5:
  let myFriends = ["Ahmed", "Sayed", "Ali", "Osama", "Gamal", "Ameer"];
  let myNewFriends = ["Samar", "Sameh"];
  let schoolFriends = ["Haytham", "Shady"];
  
  let allFriends = myFriends.concat(myNewFriends, schoolFriends, "Gameel", [1, 2]);
  
  console.log(allFriends);
  
  console.log(allFriends.join());
  console.log(allFriends.join(""));
  console.log(allFriends.join(" @ "));
  console.log(allFriends.join("|"));
  console.log(allFriends.join("|").toUpperCase());
  ```

  

* detructuring array

  ```javascript
  /*
    Destructuring
    " is a JavaScript expression that allows us to extract data from arrays,
      objects, and maps and set them into new, distinct variables. "
    - Destructuring Array
  */
  
  let a = 1;
  let b = 2;
  let c = 3;
  let d = 4;
  
  let myFriends = ["Ahmed", "Sayed", "Ali", "Maysa"];
  
  [a = "A", b, c, d, e = "Osama"] = myFriends;
  
  console.log(a);
  console.log(b);
  console.log(c);
  console.log(d);
  console.log(e);
  
  // console.log(myFriends[4]);
  
  let [, y, , z] = myFriends;
  
  console.log(y);
  console.log(z);
  
  // example :
  let myFriends = ["Ahmed", "Sayed", "Ali", ["Shady", "Amr", ["Mohamed", "Gamal"]]];
  
  // console.log(myFriends[3][2][1]);
  
  // let [, , , [a, , [, b]]] = myFriends;
  
  let [, , , [a, , [, b]]] = myFriends;
  
  console.log(a); // Shady
  console.log(b); // Gamal
  
  //Destructuring Arrays (Swap Variables)
  let book = "Video";
  let video = "Book";
  
  // // Save Book Value In Stash
  // let stash = book; // Video
  
  // // Change Book Value
  // book = video; // Book
  
  // // Change Video Value
  // video = stash; // Video
  
  [book, video] = [video, book];
  
  console.log(book);
  console.log(video);
  ```

## for

```javascript
for (let i = 0; i < 10; i++) {
  console.log(i);
}

// ex1:
let myFriends = [1, 2, "Osama", "Ahmed", 3, 4, "Sayed", 6, "Ali"];

let onlyNames = [];

for (let i = 0; i < myFriends.length; i++) {
  if (typeof myFriends[i] === "string") {
    onlyNames.push(myFriends[i]);
  }
}

console.log(onlyNames);
// ex2:
/*
  Loop
  - Nested Loops
*/

let products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor"];

let colors = ["Red", "Green", "Black"];

let models = [2020, 2021];

for (let i = 0; i < products.length; i++) {
  console.log("#".repeat(15));
  console.log(`# ${products[i]}`);
  console.log("#".repeat(15));
  console.log("Colors: ");
  for (let j = 0; j < colors.length; j++) {
    console.log(`- ${colors[j]}`);
  }
  console.log("Models: ");
  for (let k = 0; k < models.length; k++) {
    console.log(`- ${models[k]}`);
  }
}
// ex3:
/*
  Loop Control
  - Break
  - Continue
  - Label
*/

let products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor"];

let colors = ["Red", "Green", "Black"];

mainLoop: for (let i = 0; i < products.length; i++) {
  console.log(products[i]);
  nestedLoop: for (let j = 0; j < colors.length; j++) {
    console.log(`- ${colors[j]}`);
    if (colors[j] === "Green") {
      break mainLoop;
  }
}
//ex4:
let products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor", "iPhone"];
let i = 0;

for (;;) {
  console.log(products[i]);
  i++;
  if (i === products.length) break;
}
//ex5:
/*
  Products Practice
*/

let products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor", "iPhone"];
let colors = ["Red", "Green", "Blue"];
let showCount = 3;

document.write(`<h1>Show ${showCount} Products</h1>`);

for (let i = 0; i < showCount; i++) {
  document.write(`<div>`);
  document.write(`<h3>[${i + 1}] ${products[i]}</h3>`);
  for (let j = 0; j < colors.length; j++) {
    document.write(`<p>${colors[j]}</p>`);
  }
  document.write(`<p>${colors.join(" | ")}</p>`);
  document.write(`</div>`);
}
```

## for each

```javascript
<ul>
  <li class="active">One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
<div class="content">
  <div>Div One</div>
  <div>Div Two</div>
  <div>Div Three</div>
</div>

/*
  - forEach
  --- method executes a provided function once for each array element.

  Syntax forEach(callBackFunction(Element, Index, Array) { }, thisArg)
  - Element => The current element being processed in the array.
  - Index => The index of the current element being processed in the array.
  - Array - The Current Array

  Note
  - Doesnt Return Anything [Undefined]
  - Break Will Not Break The Loop
*/

let allLis = document.querySelectorAll("ul li");
let allDivs = document.querySelectorAll(".content div");

allLis.forEach(function (ele) {
  ele.onclick = function () {
    // Remove Active Class From All Elements
    allLis.forEach(function (ele) {
      ele.classList.remove("active");
    });
    // Add Active Class To This Element
    this.classList.add("active");
    // Hide All Divs
    allDivs.forEach(function (ele) {
      ele.style.display = "none";
    });
  };
});

```

## while

```javascript
let products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor", "iPhone"];

let index = 0;

while (index < products.length) {
  console.log(products[index]);
  index += 1;
}
```

## do while

```javascript
let products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor", "iPhone"];

let i = 0;

do {
  console.log(i);
  i++;
} while (false);

console.log(i);
```

## function

```javascript
function sayHello(userName) {
  console.log(`Hi ${userName}`);
}

sayHello("Osama");
sayHello("Sayed");
sayHello("Ali");
// ex1:
function sayHello(userName, age) {
  if (age < 20) {
    console.log(`App is Not Suitable For You`);
  } else {
    console.log(`Hello ${userName} Your Age is ${age}`);
  }
}

sayHello("Osama", 38);
sayHello("Sayed", 40);
sayHello("Ali", 18);

function generateYears(start, end, exclude) {
  for (let i = start; i <= end; i++) {
    if (i === exclude) {
      continue;
    }
    console.log(i);
  }
}

generateYears(1982, 2021, 2020);
// ex2:
function generate(start, end) {
  for (let i = start; i <= end; i++) {
    if (i === 15) {
      return `Interrupting`;
    }
    console.log(i);
  }
}

generate(10, 20);
// ex3:
function sayHello(username = "Unknown", age = "Unknown") {
  // if (age === undefined) {
  //   age = "Unknown";
  // }
  // age = age || "Unknown";
  return `Hello ${username} Your Age Is ${age}`;
}

console.log(sayHello());
// ex4:
/*
  Function
  - Rest Parameters
  - Only One Allowed
  - Must Be Last Element
*/

function calc(...numbers) {
  // console.log(Array.isArray(numbers));
  let result = 0;
  for (let i = 0; i < numbers.length; i++) {
    result += numbers[i]; // result = result + numbers[i]
  }
  return `Final Result Is ${result}`;
}

console.log(calc(10, 20, 10, 30, 50, 30));
// ex5:
function showInfo(us = "Un", ag = "Un", rt = 0, show = "Yes", ...sk) {
  document.write(`<div>`);
  document.write(`<h2>Welcome, ${us}</h2>`);
  document.write(`<p>Age: ${ag}</p>`);
  document.write(`<p>Hour Rate: $${rt}</p>`);
  if (show === "Yes") {
    if (sk.length > 0) {
      document.write(`<p>Skills: ${sk.join(" | ")}</p>`);
    } else {
      document.write(`<p>Skills: No Skills</p>`);
    }
  } else {
    document.write(`<p>Skills Is Hidden</p>`);
  }
  document.write(`</div>`);
}

showInfo("Osama", 38, 20, "No", "Html", "CSS");
// ex6 :
/*
  Function
  - Anonymous Function
  - Calling Named Function vs Anonymous Function
  - Argument To Other Function
  - Task Without Name
  - SetTimeout
*/

let calculator = function (num1, num2) {
  return num1 + num2;
};

console.log(calculator(10, 20));

function sayHello() {
  console.log("Hello Osama");
}

document.getElementById("show").onclick = sayHello;

setTimeout(function elzero() {
  console.log("Good");
}, 2000);

/////////////// return nested functions
// Example 1

function sayMessage(fName, lName) {
  let message = `Hello`;
  // Nested Function
  function concatMsg() {
    message = `${message} ${fName} ${lName}`;
  }
  concatMsg();
  return message;
}

console.log(sayMessage("Osama", "Mohamed"));

// Example 2

function sayMessage(fName, lName) {
  let message = `Hello`;
  // Nested Function
  function concatMsg() {
    return `${message} ${fName} ${lName}`;
  }
  return concatMsg();
}

console.log(sayMessage("Osama", "Mohamed"));

// Example 3

function sayMessage(fName, lName) {
  let message = `Hello`;
  // Nested Function
  function concatMsg() {
    function getFullName() {
      return `${fName} ${lName}`;
    }
    return `${message} ${getFullName()}`;
  }
  return concatMsg();
}

console.log(sayMessage("Osama", "Mohamed"));

// ex7 : Arrow function
let print = function () {
  return 10;
};

let print = () => 10;

let print = function (num) {
  return num;
};

let print = num => num;

let print = function (num1, num2) {
  return num1 + num2;
};

let print = (num1, num2) => num1 + num2;

console.log(print(100, 50));

// scope
//exaple1
var a = 1;
let b = 2;

function showText() {
  var a = 10;
  let b = 20;
  console.log(`Function - From Local ${a}`);
  console.log(`Function - From Local ${b}`);
}

console.log(`From Global ${a}`);
console.log(`From Global ${b}`);

showText();
//example2
var x = 10;

if (10 === 10) {
  let x = 50;
  console.log(`From If Block ${x}`);
}

console.log(`From Global ${x}`);
//example3 (scope static)
function parent() {
  let a = 10;

  function child() {
    console.log(a);
    console.log(`From Child ${b}`);

    function grand() {
      let b = 100;
      console.log(`From Grand ${a}`);
      console.log(`From Grand ${b}`);
    }
    grand();
  }
  child();
}
parent();
// higher order function-map
/*
  Higher Order Functions
  ---> is a function that accepts functions as parameters and/or returns a function.

  - Map
  --- method creates a new array
  --- populated with the results of calling a provided function on every element
  --- in the calling array.

  Syntax map(callBackFunction(Element, Index, Array) { }, thisArg)
  - Element => The current element being processed in the array.
  - Index => The index of the current element being processed in the array.
  - Array => The Current Array

  Notes
  - Map Return A New Array

  Examples
  - Anonymous Function
  - Named Function

*/

let myNums = [1, 2, 3, 4, 5, 6];

let newArray = [];

for (let i = 0; i < myNums.length; i++) {
  newArray.push(myNums[i] + myNums[i]);
}

console.log(newArray);

// Same Idea With Map

// let addSelf = myNums.map(function (element, index, arr) {
//   // console.log(`Current Element => ${element}`);
//   // console.log(`Current Index => ${index}`);
//   // console.log(`Array => ${arr}`);
//   // console.log(`This => ${this}`);
//   return element + element;
// }, 10);

// let addSelf = myNums.map((a) => a + a);

// console.log(addSelf);

function addition(ele) {
  return ele + ele;
}

let add = myNums.map(addition);

console.log(add);
//higher order function - filter
/*
  - Filter
  --- method creates a new array
  --- with all elements that pass the test implemented by the provided function.

  Syntax filter(callBackFunction(Element, Index, Array) { }, thisArg)
  - Element => The current element being processed in the array.
  - Index => The index of the current element being processed in the array.
  - Array => The Current Array
*/

// Get Friends With Name Starts With A
let friends = ["Ahmed", "Sameh", "Sayed", "Asmaa", "Amgad", "Israa"];

let filterdFriends = friends.filter(function (el) {
  return el.startsWith("A") ? true : false;
});

console.log(filterdFriends);

// Get Even Numbers Only
let numbers = [11, 20, 2, 5, 17, 10];

let evenNumbers = numbers.filter(function (el) {
  return el % 2 === 0;
});

console.log(evenNumbers);

// Test Map vs Filter

// let addMap = numbers.map(function (el) {
//   return el + el;
// });

// console.log(addMap);

// let addFilter = numbers.filter(function (el) {
//   return el + el;
// });

// console.log(addFilter);
// filter example:
/*
  Filter
  - Filter Longest Word By Number
*/

// Filter Words More Than 4 Characters
let sentence = "I Love Foood Code Too Playing Much";

let smallWords = sentence
  .split(" ")
  .filter(function (ele) {
    return ele.length <= 4;
  })
  .join(" ");

console.log(smallWords);

// Ignore Numbers
let ignoreNumbers = "Elz123er4o";

let ign = ignoreNumbers
  .split("")
  .filter(function (ele) {
    return isNaN(parseInt(ele));
  })
  .join("");

console.log(ign);

// Filter Strings + Multiply
let mix = "A13BS2ZX";

let mixedContent = mix
  .split("")
  .filter(function (ele) {
    return !isNaN(parseInt(ele));
  })
  .map(function (ele) {
    return ele * ele;
  })
  .join("");

console.log(mixedContent);
// higher order function - reduce
/*
  - Reduce
  --- method executes a reducer function on each element of the array,
  --- resulting in a single output value.

  Syntax
  reduce(callBackFunc(Accumulator, Current Val, Current Index, Source Array) { }, initialValue)
  - Accumulator => the accumulated value previously returned in the last invocation
  - Current Val => The current element being processed in the array
  - Index => The index of the current element being processed in the array.
  ---------- Starts from index 0 if an initialValue is provided.
  ---------- Otherwise, it starts from index 1.
  - Array => The Current Array
*/

let nums = [10, 20, 15, 30];

let add = nums.reduce(function (acc, current, index, arr) {
  console.log(`Acc => ${acc}`);
  console.log(`Current Element => ${current}`);
  console.log(`Current Element Index => ${index}`);
  console.log(`Array => ${arr}`);
  console.log(acc + current);
  console.log(`#############`);
  return acc + current;
}, 5);

console.log(add);
//reduce example :
/*
  Reduce
  - Longest Word
  - Remove Characters + Use Reduce
*/

let theBiggest = ["Bla", "Propaganda", "Other", "AAA", "Battery", "Test", "Propaganda_Two"];

let check = theBiggest.reduce(function (acc, current) {
  console.log(`Acc => ${acc}`);
  console.log(`Current Element => ${current}`);
  console.log(acc.length > current.length ? acc : current);
  console.log(`#############`);
  return acc.length > current.length ? acc : current;
});

console.log(check);

let removeChars = ["E", "@", "@", "L", "Z", "@", "@", "E", "R", "@", "O"];

let finalString = removeChars
  .filter(function (ele) {
    return ele !== "@";
  })
  .reduce(function (acc, current) {
    return `${acc}${current}`;
  });

console.log(finalString);
```

* Destructuring Function Parameters

  ```javascript
  const user = {
    theName: "Osama",
    theAge: 39,
    skills: {
      html: 70,
      css: 80,
    },
  };
  
  showDetails(user);
  
  // function showDetails(obj) {
  //   console.log(`Your Name Is ${obj.theName}`);
  //   console.log(`Your Age Is ${obj.theAge}`);
  //   console.log(`Your CSS Skill Progress Is ${obj.skills.css}`);
  // }
  
  function showDetails({ theName: n, theAge: a, skills: { css: c } } = user) {
    console.log(`Your Name Is ${n}`);
    console.log(`Your Age Is ${a}`);
    console.log(`Your CSS Skill Progress Is ${c}`);
  }  
  ```

## object

```javascript
let user = {
  // Properties
  theName: "Osama",
  theAge: 38,
  // Methods
  sayHello: function () {
    return `Hello`;
  },
};
// Dot Notation vs Bracket Notation
console.log(user.theName);
console.log(user.theAge);
console.log(user.sayHello());

let myVar = "country";

let user = {
  theName: "Osama",
  country: "Egypt",
};

console.log(user.theName);
console.log(user.country); // user.country
console.log(user.myVar); // user.country
console.log(user[myVar]); // user.country
// nested object
let available = true;

let user = {
  name: "Osama",
  age: 38,
  skills: ["HTML", "CSS", "JS"],
  available: false,
  addresses: {
    ksa: "Riyadh",
    egypt: {
      one: "Cairo",
      two: "Giza",
    },
  },
  checkAv: function () {
    if (user.available === true) {
      return `Free For Work`;
    } else {
      return `Not Free`;
    }
  },
};

console.log(user.name);
console.log(user.age);
console.log(user.skills);
console.log(user.skills.join(" | "));
console.log(user.skills[2]); // Access With Index
console.log(user.addresses.ksa);
console.log(user.addresses.egypt.one);
console.log(user["addresses"].egypt.one);
console.log(user["addresses"]["egypt"]);
console.log(user["addresses"]["egypt"]["one"]);

console.log(user.checkAv());
// object with new keyword
let user = new Object({
  age: 20,
});

console.log(user);

user.age = 38;
user["country"] = "Egypt";

user.sayHello = function () {
  return `Hello`;
};

console.log(user);
console.log(user.age);
console.log(user.country);
console.log(user.sayHello());
// this
console.log(this);
console.log(this === window);

myVar = 100;

console.log(window.myVar);
console.log(this.myVar);

function sayHello() {
  console.log(this);
  return this;
}
sayHello();

console.log(sayHello() === window);

document.getElementById("cl").onclick = function () {
  console.log(this);
};

let user = {
  age: 38,
  ageInDays: function () {
    console.log(this);
    return this.age * 365;
  },
};

console.log(user.age);
console.log(user.ageInDays());
//Create Object With Create Method
let user = {
  age: 20,
  doubleAge: function () {
    return this.age * 2;
  },
};

console.log(user);
console.log(user.age);
console.log(user.doubleAge());

let obj = Object.create({});

obj.a = 100;

console.log(obj);

let copyObj = Object.create(user);

copyObj.age = 50;

console.log(copyObj);
console.log(copyObj.age);
console.log(copyObj.doubleAge());
//Create Object With Assign Method
let obj1 = {
  prop1: 1,
  meth1: function () {
    return this.prop1;
  },
};

let obj2 = {
  prop2: 2,
  meth2: function () {
    return this.prop2;
  },
};

let targetObject = {
  prop1: 100,
  prop3: 3,
};

let finalObject = Object.assign(targetObject, obj1, obj2);

finalObject.prop1 = 200;
finalObject.prop4 = 4;

console.log(finalObject);

let newObject = Object.assign({}, obj1, { prop5: 5, prop6: 6 });

console.log(newObject);
```

*  Destructuring Objects

  ```javascript
  const user = {
    theName: "Osama",
    theAge: 39,
    theTitle: "Developer",
    theCountry: "Egypt",
  };
  
  // console.log(user.theName);
  // console.log(user.theAge);
  // console.log(user.theTitle);
  // console.log(user.theCountry);
  
  // let theName = user.theName;
  // let theAge = user.theAge;
  // let theTitle = user.theTitle;
  // let theCountry = user.theCountry;
  
  // console.log(theName);
  // console.log(theAge);
  // console.log(theTitle);
  // console.log(theCountry);
  
  // ({ theName, theAge, theTitle, theCountry } = user);
  const { theName, theAge, theCountry } = user;
  
  console.log(theName);
  console.log(theAge);
  console.log(theCountry);
  
  // example:
  
  const user = {
    theName: "Osama",
    theAge: 39,
    theTitle: "Developer",
    theCountry: "Egypt",
    theColor: "Black",
    skills: {
      html: 70,
      css: 80,
    },
  };
  
  const {
    theName: n,
    theAge: a,
    theCountry,
    theColor: co = "Red",
    skills: { html: h, css },
  } = user;
  
  console.log(n);
  console.log(a);
  console.log(theCountry);
  console.log(co);
  console.log(`My HTML Skill Progress Is ${h}`);
  console.log(`My CSS Skill Progress Is ${css}`);
  
  const { html: skillOne, css: skillTwo } = user.skills;
  
  console.log(`My HTML Skill Progress Is ${skillOne}`);
  console.log(`My CSS Skill Progress Is ${skillTwo}`);
  ```

## Dom

```javascript
let myIdElement = document.getElementById("my-div");
let myTagElements = document.getElementsByTagName("p");
let myClassElement = document.getElementsByClassName("my-span");
let myQueryElement = document.querySelector(".my-span");
let myQueryAllElement = document.querySelectorAll(".my-span");

console.log(myIdElement);
console.log(myTagElements[1]);
console.log(myClassElement[1]);
console.log(myQueryElement);
console.log(myQueryAllElement[1]);

console.log(document.title);
console.log(document.body);
console.log(document.forms[0].one.value);
console.log(document.links[1].href);
//[Get / Set Elements Content And Attributes]:
let myElement = document.querySelector(".js");

console.log(myElement.innerHTML);
console.log(myElement.textContent);

myElement.innerHTML = "Text From <span>Main.js</span> File";
myElement.textContent = "Text From <span>Main.js</span> File";

document.images[0].src = "https://google.com";
document.images[0].alt = "Alternate";
document.images[0].title = "Picture";
document.images[0].id = "pic";
document.images[0].className = "img";

let myLink = document.querySelector(".link");

console.log(myLink.getAttribute("class"));
console.log(myLink.getAttribute("href"));

myLink.setAttribute("href", "https://twitter.com");
myLink.setAttribute("title", "Twitter");
//[Check Attributes]:
console.log(document.getElementsByTagName("p")[0].attributes);

let myP = document.getElementsByTagName("p")[0];

if (myP.hasAttribute("data-src")) {
  if (myP.getAttribute("data-src") === "") {
    myP.removeAttribute("data-src");
  } else {
    myP.setAttribute("data-src", "New Value");
  }
} else {
  console.log(`Not Found`);
}

if (myP.hasAttributes()) {
  console.log(`Has Attributes`);
}

if (document.getElementsByTagName("div")[0].hasAttributes()) {
  console.log(`Has Attributes`);
} else {
  console.log(`Div Has No Attributes`);
}
// create and append elements:
let myElement = document.createElement("div");
let myAttr = document.createAttribute("data-custom");
let myText = document.createTextNode("Product One");
let myComment = document.createComment("This Is Div");

myElement.className = "product";
myElement.setAttributeNode(myAttr);
myElement.setAttribute("data-test", "Testing");

// Append Comment To Element
myElement.appendChild(myComment);

// Append Text To Element
myElement.appendChild(myText);

// Append Element To Body
document.body.appendChild(myElement);

//ex1:Practice Product With Heading And Paragraph
let myMainElement = document.createElement("div");
let myHeading = document.createElement("h2");
let myParagraph = document.createElement("p");

let myHeadingText = document.createTextNode("Product Title");
let myParagraphText = document.createTextNode("Product Description");

// Add Heading Text
myHeading.appendChild(myHeadingText);

// Add Heading To Main Element
myMainElement.appendChild(myHeading);

// Add Paragraph Text
myParagraph.appendChild(myParagraphText);

// Add Paragraph To Main Element
myMainElement.appendChild(myParagraph);

myMainElement.className = "product";

document.body.appendChild(myMainElement);
// deal with childrens :
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>Learn JavaScript</title>
  </head>
  <body>
    <div><!-- Osama -->Hello Div<p>Hello P</p><span>Hello Span</span><!-- Comment -->Hello</div>
    <script src="main.js"></script>
  </body>
</html>

let myElement = document.querySelector("div");

console.log(myElement);
console.log(myElement.children);
console.log(myElement.children[0]);
console.log(myElement.childNodes);
console.log(myElement.childNodes[0]);

console.log(myElement.firstChild);
console.log(myElement.lastChild);

console.log(myElement.firstElementChild);
console.log(myElement.lastElementChild);

// dom events:
/*
  DOM [Events]
  - Use Events On HTML
  - Use Events On JS
  --- onclick
  --- oncontextmenu
  --- onmouseenter
  --- onmouseleave

  --- onload
  --- onscroll
  --- onresize

  --- onfocus
  --- onblur
  --- onsubmit
*/

let myBtn = document.getElementById("btn");

myBtn.onmouseleave = function () {
  console.log("Clicked");
};

window.onresize = function () {
  console.log("Scroll");
};
// validate form and prevent defaults:
/*
  DOM [Events]
  - Validate Form Practice
  - Prevent Default
*/

let userInput = document.querySelector("[name='username']");
let ageInput = document.querySelector("[name='age']");

document.forms[0].onsubmit = function (e) {
  let userValid = false;
  let ageValid = false;

  if (userInput.value !== "" && userInput.value.length <= 10) {
    userValid = true;
  }

  if (ageInput.value !== "") {
    ageValid = true;
  }

  if (userValid === false || ageValid === false) {
    e.preventDefault();
  }
};

document.links[0].onclick = function (event) {
  console.log(event);
  event.preventDefault();
};
//event simulation
/*
  DOM [Events Simulation]
  - click
  - focus
  - blur
*/

let one = document.querySelector(".one");
let two = document.querySelector(".two");

window.onload = function () {
  two.focus();
};

one.onblur = function () {
  document.links[0].click();
};
//classlist object and method:
let element = document.getElementById("my-div");

console.log(element.classList);
console.log(typeof element.classList);
console.log(element.classList.contains("osama"));
console.log(element.classList.contains("show"));
console.log(element.classList.item("3"));

element.onclick = function () {
  element.classList.toggle("show");
};
// css styling:
let element = document.getElementById("my-div");

console.log(element.classList);
console.log(typeof element.classList);
console.log(element.classList.contains("osama"));
console.log(element.classList.contains("show"));
console.log(element.classList.item("3"));

element.onclick = function () {
  element.classList.toggle("show");
};
//Before, After, Prepend, Append, Remove:
let element = document.getElementById("my-div");
let createdP = document.createElement("p");
element.remove();
// traversing:
let span = document.querySelector(".two");

console.log(span.parentElement);

span.onclick = function () {
  span.parentElement.remove();
}
// cloning:
let myP = document.querySelector("p").cloneNode(true);
let myDiv = document.querySelector("div");

myP.id = `${myP.id}-clone`;

myDiv.appendChild(myP);
//addeventlistener
let myP = document.querySelector("p");

// myP.onclick = one;
// myP.onclick = two;

// function one() {
//   console.log("Message From OnClick 1");
// }
// function two() {
//   console.log("Message From OnClick 2");
// }

// window.onload = "Osama";

// myP.addEventListener("click", function () {
//   console.log("Message From OnClick 1 Event");
// });

// myP.addEventListener("click", one);
// myP.addEventListener("click", two);

// myP.addEventListener("click", "String"); // Error

myP.onclick = function () {
  let newP = myP.cloneNode(true);
  newP.className = "clone";
  document.body.appendChild(newP);
};

// let cloned = document.querySelector(".clone"); // Error

// cloned.onclick = function () {
//   console.log("Iam Cloned");
// };

document.addEventListener("click", function (e) {
  if (e.target.className === "clone") {
    console.log("Iam Cloned");
  }
});
```

## Bom:

```javascript
/*
  BOM [Browser Object Model]
  - Introduction
  --- Window Object Is The Browser Window
  --- Window Contain The Document Object
  --- All Global Variables And Objects And Functions Are Members Of Window Object
  ------ Test Document And Console
  - What Can We Do With Window Object ?
  --- Open Window
  --- Close Window
  --- Move Window
  --- Resize Window
  --- Print Document
  --- Run Code After Period Of Time Once Or More
  --- Fully Control The URL
  --- Save Data Inside Browser To Use Later
*/

window.document.title = "Hello JS";
```

*  Alert, Confirm, Prompt :

  ```javascript
  /*
    BOM [Browser Object Model]
    - alert(Message) => Need No Response Only Ok Available
    - confirm(Message) => Need Response And Return A Boolean
    - prompt(Message, Default Message) => Collect Data
  */
  
  // alert("Test");
  // console.log("Test");
  
  // let confirmMsg = confirm("Are You Sure?");
  
  // console.log(confirmMsg);
  
  // if (confirmMsg === true) {
  //   console.log("Item Deleted");
  // } else {
  //   console.log("Item Not Deleted");
  // }
  
  let promptMsg = prompt("Good Day To You?", "Write Day With 3 Characters");
  
  console.log(promptMsg);
  ```

* setTimeout and clearTimeout:

  ```javascript
  /*
    BOM [Browser Object Model]
    - setTimeout(Function, Timeout, Additional Params)
    - clearTimeout(Identifier)
  */
  
  // setTimeout(function () {
  //   console.log("Msg");
  // }, 3000);
  
  // setTimeout(sayMsg, 3000);
  
  // function sayMsg() {
  //   console.log(`Iam Message`);
  // }
  
  // setTimeout(sayMsg, 3000, "Osama", 38);
  
  // function sayMsg(user, age) {
  //   console.log(`Iam Message For ${user} Age Is : ${age}`);
  // }
  
  let btn = document.querySelector("button");
  
  btn.onclick = function () {
    clearTimeout(counter);
  };
  
  function sayMsg(user, age) {
    console.log(`Iam Message For ${user} Age Is : ${age}`);
  }
  
  let counter = setTimeout(sayMsg, 3000, "Osama", 38);
  ```

* setInterval and clearInterval :

  ```javascript
  /*
    BOM [Browser Object Model]
    - setInterval(Function, Millseconds, Additional Params)
    - clearInterval(Identifier)
  */
  
  // setInterval(function () {
  //   console.log(`Msg`);
  // }, 1000);
  
  // setInterval(sayMsg, 1000);
  
  // function sayMsg() {
  //   console.log(`Iam Message`);
  // }
  
  // setInterval(sayMsg, 1000, "Osama", 38);
  
  // function sayMsg(user, age) {
  //   console.log(`Iam Message For ${user} His Age Is: ${age}`);
  // }
  
  let div = document.querySelector("div");
  
  function countdown() {
    div.innerHTML -= 1;
    if (div.innerHTML === "0") {
      clearInterval(counter);
    }
  }
  
  let counter = setInterval(countdown, 1000);
  ```

*  Window Location Object:

  ```javascript
  /*
    BOM [Browser Object Model]
    - location Object
    --- href Get / Set [URL || Hash || File || Mail]
    --- host
    --- hash
    --- protocol
    --- reload()
    --- replace()
    --- assign()
  */
  
  console.log(location);
  console.log(location.href);
  
  // location.href = "https://google.com";
  // location.href = "/#sec02";
  // location.href = "https://developer.mozilla.org/en-US/docs/Web/JavaScript#reference";
  
  // console.log(location.host);
  // console.log(location.hostname);
  
  // console.log(location.protocol);
  
  // console.log(location.hash);
  ```

* Window History Object :

  ```javascript
  /*
    BOM [Browser Object Model]
    - History API
    --- Properties
    ------ length
    --- Methods
    ------ back()
    ------ forward()
    ------ go(Delta) => Position In History
  
    Search [For Advanced Knowledge]
    - pushState() + replaceState()
  */
  
  console.log(history);
  ```

* Scroll, ScrollTo, ScrollBy, Focus, Print, Stop

* ```javascript
  /*
    BOM [Browser Object Model]
    - stop()
    - print()
    - focus()
    - scrollTo(x, y || Options)
    - scroll(x, y || Options)
    - scrollBy(x, y || Options)
  */
  
  // let myNewWindow = window.open("https://google.com", "", "width=500,height=500");
  
  // window.scrollTo({
  //   left: 500,
  //   top: 200,
  //   behavior: "smooth"
  // });
  ```

* Scroll To Top Using ScrollY Practice

* 

* ```javascript
  /*
    BOM [Browser Object Model]
    - Practice => Scroll To Top
    - scrollX [Alias => PageXOffset]
    - scrollY [Alias => PageYOffset]
  */
  
  // console.log(window.scrollX === window.pageXOffset);
  
  let btn = document.querySelector("button");
  
  window.onscroll = function () {
    if (window.scrollY >= 600) {
      btn.style.display = "block";
    } else {
      btn.style.display = "none";
    }
  };
  
  btn.onclick = function () {
    window.scrollTo({
      left: 0,
      top: 0,
      behavior: "smooth",
    });
  };
  ```

* Local Storage

* 

* ```javascript
  /*
    BOM [Browser Object Model]
    Local Storage
    - setItem
    - getItem
    - removeItem
    - clear
    - key
  
    Info
    - No Expiration Time
    - HTTP And HTTPS
    - Private Tab
  */
  
  // Set
  window.localStorage.setItem("color", "#F00");
  window.localStorage.fontWeight = "bold";
  window.localStorage["fontSize"] = "20px";
  
  // Get
  console.log(window.localStorage.getItem("color"));
  console.log(window.localStorage.color);
  console.log(window.localStorage["color"]);
  
  // Remove One
  // window.localStorage.removeItem("color");
  
  // Remove All
  // window.localStorage.clear();
  
  // Get Key
  console.log(window.localStorage.key(0));
  
  // Set Color In Page
  document.body.style.backgroundColor = window.localStorage.getItem("color");
  
  console.log(window.localStorage);
  console.log(typeof window.localStorage);
  
  ///////////////////////////////////////////
  //Local Storage Color App Practice
  
  // html :
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Learn JavaScript</title>
      <link rel="stylesheet" href="main.css" />
      <style>
        body {
          background-color: #eee;
        }
        ul {
          padding: 0;
          margin: 0;
          background-color: #ddd;
          margin: 20px auto;
          padding: 20px;
          width: 400px;
          list-style: none;
          display: flex;
          justify-content: space-between;
        }
        ul li {
          width: 60px;
          height: 60px;
          border: 2px solid transparent;
          opacity: 0.4;
          cursor: pointer;
          transition: 0.3s;
        }
        ul li.active,
        ul li:hover {
          opacity: 1;
        }
        ul li:first-child {
          background-color: red;
        }
        ul li:nth-child(2) {
          background-color: green;
        }
        ul li:nth-child(3) {
          background-color: blue;
        }
        ul li:nth-child(4) {
          background-color: black;
        }
        .experiment {
          background-color: red;
          width: 600px;
          height: 300px;
          margin: 20px auto;
        }
      </style>
    </head>
    <body>
      <ul>
        <li class="active" data-color="red"></li>
        <li data-color="green"></li>
        <li data-color="blue"></li>
        <li data-color="black"></li>
      </ul>
      <div class="experiment"></div>
      <script src="main.js"></script>
    </body>
  </html>
  
  // js :
  
  /*
    BOM [Browser Object Model]
    Local Storage Practice
  */
  
  let lis = document.querySelectorAll("ul li");
  let exp = document.querySelector(".experiment");
  
  if (window.localStorage.getItem("color")) {
    // If There Is Color In Local Storage
    // [1] Add Color To Div
    exp.style.backgroundColor = window.localStorage.getItem("color");
    // [2] Remove Active Class From All Lis
    lis.forEach((li) => {
      li.classList.remove("active");
    });
    // [3] Add Active Class To Current Color
    document.querySelector(`[data-color="${window.localStorage.getItem("color")}"]`).classList.add("active");
  }
  
  lis.forEach((li) => {
    li.addEventListener("click", (e) => {
      // console.log(e.currentTarget.dataset.color);
      // Remove Active Class From all Lis
      lis.forEach((li) => {
        li.classList.remove("active");
      });
      // Add Active Class To Current Element
      e.currentTarget.classList.add("active");
      // Add Current Color To Local Storage
      window.localStorage.setItem("color", e.currentTarget.dataset.color);
      // Change Div Background Color
      exp.style.backgroundColor = e.currentTarget.dataset.color;
    });
  });
  ```

* Session Storage And Use Cases

* 

* ```javascript
  // html
  <form action="">
    <input type="text" class="name" />
  </form>
  // js
  /*
    BOM [Browser Object Model]
    Session Storage
    - setItem
    - getItem
    - removeItem
    - clear
    - key
  
    Info
    - New Tab = New Session
    - Duplicate Tab = Copy Session
    - New Tab With Same Url = New Session
  */
  
  // window.localStorage.setItem("color", "red");
  // window.sessionStorage.setItem("color", "blue");
  
  document.querySelector(".name").onblur = function () {
    // console.log(this.value);
    window.localStorage.setItem("input-name", this.value);
  };
  ```

* destructuring mixed content :

* ```javascript
  const user = {
    theName: "Osama",
    theAge: 39,
    skills: ["HTML", "CSS", "JavaScript"],
    addresses: {
      egypt: "Cairo",
      ksa: "Riyadh",
    },
  };
  
  const {
    theName: n,
    theAge: a,
    skills: [, , three],
    addresses: { egypt: e },
  } = user;
  
  console.log(`Your Name Is: ${n}`);
  console.log(`Your Age Is: ${a}`);
  console.log(`Your Last Skill Is: ${three}`);
  console.log(`Your Live In: ${e}`);
  ```