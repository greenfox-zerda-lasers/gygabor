// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

function sum(){
  var three = 0;
  var five = 0;

  for (var i = 3; i <= 999; i += 3){
    three = three + i;
  }
  for (var i = 5; i <= 995; i += 5){
    if (i % 3 !== 0){
      console.log(i)
      five = five + i;
    }
  }
  return (three + five);
}

console.log(sum());
