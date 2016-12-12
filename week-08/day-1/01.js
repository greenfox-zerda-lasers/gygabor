'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals(talk){
  this.talk = talk;
}

Animals.prototype.say = function() {
  console.log(this.talk);
}

var frog = new Animals('Brek');
frog.say();

var sheep = new Animals('BEEEEEEEEE');
sheep.say();
