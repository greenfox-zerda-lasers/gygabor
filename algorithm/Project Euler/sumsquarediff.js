// The sum of the squares of the first ten natural numbers is,
//
// 12 + 22 + ... + 102 = 385
// The square of the sum of the first ten natural numbers is,
//
// (1 + 2 + ... + 10)2 = 552 = 3025
// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
//
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

function sumSquareDiff(){
  var numberSquare = 0;
  var sumSquare = 0;
  for (var i = 1; i <= 100; i++){
    numberSquare += i * i;
  }
  for (var i = 1; i <= 100; i++){
    sumSquare += i;
  }
  sumSquare = sumSquare * sumSquare;
  return (sumSquare - numberSquare);
}

console.log(sumSquareDiff())
