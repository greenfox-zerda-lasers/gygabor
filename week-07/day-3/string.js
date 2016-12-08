// Create an object that has several converter methods:
//
// float2string(num) it should convert a float number to a string, for example 12.24 -> '12.24'
// string2float(str) it should convert a string to a float number, for example '12.24' -> 12.24
// int2roman(number) it should convert an int number to a roman number as a string, for example 12 -> 'XII'
// roman2int(number) it should convert a roman number as a string to an int, for example 'XII' -> 12 please try to avoid using the built in conversion methods

var stringMethods = {
  float2string : function(num){
    return num.toString();
  },
  string2float : function(str){
    return parseFloat(str);
  }
}

console.log(typeof stringMethods.float2string(12.23));
console.log(typeof stringMethods.string2float('12.23'));
