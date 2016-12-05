'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10];
// write your own sum function
var sum = 0;
function summa(numberList){
  for (var i=0; i < numberList.length; i++){
    sum += numberList[i];

  }
  return sum;
}

console.log(summa(numbers));
