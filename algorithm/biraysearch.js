'use strict';

const numbers = [1,2,3,4,5,6,3,4,2,1,2,546554,4432,2];

function binarySearch(array, number){
  var respond = false;
  var array = sortArray(array);
  var mid = Math.floor(array.length / 2);

  while (mid != 0 && respond != true){
    if (number === array[mid]){
      respond = true;
    } else if (number > array[mid]){
      array = array.splice(mid, array.length / 2);
      mid = Math.floor(array.length / 2);
    } else if (number < array[mid]){
      array = array.splice(0, mid);
      mid = Math.floor(array.length / 2);
    }
  }
  return respond;
}

function sortArray(array) {
  return (array.sort(compareNumbers));
}

function compareNumbers(a, b) {
  return a - b;
}

console.log(binarySearch(numbers, 112));
