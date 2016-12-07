'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements
var elements = [1, 2, 3]

function each(arr, funct){
  arr.forEach(function(element, index, array){
    funct(element, array)
  });
}

each(elements, console.log)
