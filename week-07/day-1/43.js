'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function evens(numberList){
  for (var i = 0; i < numberList.length; i++){
    if(numberList[i] % 2 != 0) {
          numberList.splice(numberList[i]);
    }
  }
  return numberList;
}

console.log(evens(numbers));
