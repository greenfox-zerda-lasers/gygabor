'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(sideA, sideB){
  this.sideA = sideA
  this.sideB = sideB
}

Rectangles.prototype.getArea = function(){
  return this.sideA * this.sideB
}

Rectangles.prototype.getCircumference = function(){
  return 2*(this.sideA + this.sideB)
}

var rect1 = new Rectangles(2, 3)
console.log(rect1.getArea())

var rect2 = new Rectangles(4, 5)
console.log(rect2.getArea())
