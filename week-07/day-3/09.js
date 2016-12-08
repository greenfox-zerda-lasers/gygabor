'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function countLetter(string){
  var count = {}
  for (var i = 0; i < string.length; i++){
    var character = string.charAt(i);
      if (count[character]) {
        count[character]++;
      } else {
        count[character] = 1;
      }
  }
  return count;
}

console.log(countLetter('apple'));
