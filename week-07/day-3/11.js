'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack(element){
  var elements = element;
  this.size = function(){
    return elements.length;

  };
  this.push = function(elem) {
    elements[elements.length] = elem;
  };
  this.pop = function(){
    var lastElem = elements[elements.length - 1]
    elements.length--
    return lastElem
  }
}

var stack = new Stack([3,4,4,4])
console.log(stack.size())

stack.push(1)
console.log(stack.size())

console.log(stack.pop())
console.log(stack.size())
