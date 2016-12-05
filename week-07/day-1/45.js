'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortest(nameList){
  var short = nameList[0];
  for (var i = 0; i < nameList.length; i++){
    if (short.length > nameList[i].length){
      short = nameList[i];
    }
  }
  return short;
}

console.log(shortest(names));
