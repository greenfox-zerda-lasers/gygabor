'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function minimalElement(numberList){
  var min = numberList[0];
  for (var i = 0; i < numberList.length; i++){
    if (min > numberList[i]){
      min = numberList[i];
    }
  }
  return min;
}

console.log(minimalElement(numbers));
