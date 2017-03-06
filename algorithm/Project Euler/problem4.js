// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.
'use strict';

function palindrome(){
  let a = 999;
  let b = 999;
  let find = false;
  let d = 0;


  while (a > 100) {
    let c = a * b;
    if (c === reverseNumber(c)){
      if (c > d) {
        d = c;
      }
      a--;
      b = a;
    } else {
      b--;
    }
  }
  return d;
}

function reverseNumber(c){
  let reversed = 0;
  while (c > 0){
    reversed *= 10;
    reversed += c % 10;
    c = Math.floor(c / 10);
  }
  return reversed;
}

console.log(palindrome());
