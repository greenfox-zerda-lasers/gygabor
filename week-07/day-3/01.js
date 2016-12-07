'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

var numberName = ['zero', 'one', 'two', 'three', 'four', 'five'];

function stringBack(number){
  if (number in numberName){
    return numberName[number];
  }
}

console.log(stringBack(0))
