'use strict';

var y = 'season';
var out = 6;
// if the last and the first letter of the string
// are the same double the variable
// called out, if not half it

if (y[0] === y.slice(-1)){
  out *= 2;
} else {
  out /= 2;
}
console.log(out);
