/*
let birthyear = prompt("Please enter your birth year");
alert(birthyear);
//ask brith year of user

birthyear = Number(birthyear);
//convert string of year into a number

let age = 2023 - birthyear;
alert(age);
//calculate age with converted number

let a = null
alert(Number(undefined));
//convert NaN, not a number

let b = '123abc'
alert(Number(b));
//convert b (string) into a number
*/
/*
let c = 2;
let d = 3;

alert(d + c); // 5
alert(d - c); // 1
alert(d * c); // 6
alert(d ** c); //9 = 3*3
alert(d / c); // 1.5
alert(d % c); // 1
//various calculations 

let e = 6;

e++;

alert(e);
*/
/*
let f = 6;
f += 1; //6 + 1 = 7
alert(f);
//adds 1 to 6 each time f +=1 gets executed

let g = 1;
let h ='2';

'12'

alert(g + h);
//prints 1 as a number and 2 as a string

let i = "hello";
let j = "world";
alert(i + ' ' + j);
//combine 2 lines of strings with whitespace in the middle to create "hello world"

let x = -3;
x = -x; // 3
alert(x);
//converting negative numbers into positive ones
*/
/*
let userAge = prompt("please enter your age");
userAger = Number(userAge);
//ask user for their age

if (userAge >= 18) {
    alert("You are allowed to use our website");
    //if 18 then print...
} else {
    alert("Access denied");
    //if not 18 then print...
}
/*
= x equals y (x = y)
== check if x equals y (x == y)
!= check if x does NOT equal y (x != y)
=== check if x equals y for strings(x === y)
*/
/*
let aa = 3;
let bb = 4;

if (aa ==  bb){
    alert("True");
} else {
    alert("False");
}
//code checks if a equals b

let aaa = 3;

if (aaa < 3){
    alert("low");
} else if (aaa > 5){
    alert("high");
} else {
    alert("med");
}
//combined 2 if statements 
*/
/*
let bbb = 4

if (bbb > 6 && bbb < 9){
    alert("in between 6 and 9");
} else {
    alert("not in between designated numbers");
}
//&& = 'and' in python, basically checks if condition 1 AND 2 are met at the same time

let true_username = 'a21';
let true_password = '1234';

username = prompt("Username");
password = prompt("Password");

if (username === true_username && password === true_password){
    alert("Welcome back big cock slayer 69 420");
} else {
    alert("worng username or password");
}
//asks for username and passowrd and checks against real username and password
*/
/*
let month_number = prompt("Please enter the number of the month");
month_number = Number(month_number);

if (month_number === 1){
    alert("January");
} else if (month_number === 2){
    alert("February");
} else if (month_number === 3){
    alert("March");
} else if (month_number === 4){
    alert("April");
} else if (month_number === 5){
    alert("May");
} else if (month_number === 6){
    alert ("June");
} else if (month_number === 7){
    alert("July");
} else if (month_number === 8){
    alert("August");
} else if (month_number === 9){
    alert("September");
} else if (month_number === 10){
    alert("October");
} else if (month_number === 11){
    alert("November");
} else if (month_number === 12){
    alert("December");
} else {
    alert("Invalid input");
}

//these 2 codes do the same thing, one is more efficient tho

switch(month_number){
    case 1:
        alert("Jan.");
        break
    case 2:
        alert("Feb.");
        break
    case 3:
        alert("Mar.");
        break
    case 4:
        alert("Apr.");
        break
    case 5:
        alert("May");
        break
    case 6:
        alert("Jun.");
        break
    case 7:
        alert("Jul.");
        break
    case 8:
        alert("Aug.");
        break
    case 10:
        alert("Oct.");
        break
    case 11:
        alert("Nov.");
        break
    case 12:
        alert("Dec.");
        break
    case 9:
        alert("Sep.");
        break
}
*/
/*
let age2 = 15;
let message = "";

if (age2 < 18){
    message = "Access denied!";
} else {
    message = "Welcome!";
}
*/
//this code does the same thing in one line:
/*
message = age2 < 18 ? "Access denied!" : "Welcome!";
alert(message);
*/

//for = for repetitive tasks/statements
/*
for(let numb = 0; numb <= 20; numb++){
    console.log(numb);
}
//console.log prints the text or statement in the console
*/
/*
for(let numb = 0; numb <= 20; numb++){
    if (numb%2 == 0){
        console.log(numb);
    }
}
*/
/*
for(let numb = 0; numb <= 20; numb++){
    if (numb%2 == 0){
        console.log(numb);
    }
}
*/