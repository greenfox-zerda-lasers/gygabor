'use strict';

// create a function that returns it's input factorial

function factorial(number){
  var fac = 1;
  for (var i=1; i <= number; i++){
    fac *= i;
  }
  return fac;

}

console.log(factorial(5));
