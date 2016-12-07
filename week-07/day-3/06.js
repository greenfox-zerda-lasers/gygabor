'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function letterInString(string, letter){
  return string.indexOf(letter) === 0;
}

console.log(letterInString('abc', 'd'))
