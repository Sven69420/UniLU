//use double slashes for comments in js, comments should be meaningful
alert("Hello World"); //xyz
/*
This is a line break
https://javascript.info/hello-world
Nothing in between this will be read as code by js 
*/
alert("Goobye World");

// example : let velocity = 25; // m/s

// let defines variable 

let student_id = "023022572B sexy tiger rawwr :*"; 
// variables can't have numbers at the beginning 
// https://javascript.info/variables

alert(student_id);

student_id = 1234556;

alert(student_id);

/*
this is possible because variables are not strongly typed like in other programming languages like C++
*/

const class_id = "webdev1";
// constants dont change duh
alert(class_id);

const body_color = "#FF69B4";

let name = 'Sven';
let msg = `Hello I don't know ${name}`;
alert(msg);

let nameFieldCheck = false;
let ageFieldCheck = true;
alert(ageFieldCheck);
ageFieldCheck = confirm("Are you over 18?");
// confirm opens a confirmation box on the site
alert(nameFieldCheck);
alert(ageFieldCheck);

let coque = "long";
alert(typeof(coque));
// typeof gives you the time of a certain variable

let coqueLength;
coqueLength = prompt("How many inches is your cauque?");
// prompt opens a prompt for the site visitor to enter something
alert(coqueLength);



