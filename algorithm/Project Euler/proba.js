var a = 2, b = { c: 4 };
var x = a, y = b;
x = 5;
y.c = 6;
console.log(a, b);
console.log(a + b.c);
