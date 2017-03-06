// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

function primeFactor(number){
  let p = 2;

    while (number != 1) {
      if (number % p != 0){
        p++;
        while(!isPrime(p)){
          p++;
        }
      } else {
        number = number / p;
      }
    }
  return p;
}

function isPrime(num) {
  for ( var i = 2; i < num; i++ ) {
    if ( num % i === 0 ) {
      return false;
    }
  }
  return true;
}

console.log(primeFactor(600851475143));
