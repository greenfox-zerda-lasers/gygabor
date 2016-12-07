'use strict';

var numbers = [2, 3, 5, 7, 8];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isPrime(numbers){
  return numbers.every(function(num){
    for (var i = 2; i <= Math.floor(Math.sqrt(num)); i++){
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  });

}

console.log(isPrime(numbers));
