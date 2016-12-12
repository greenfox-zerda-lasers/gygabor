'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rockets(consumption){
  this.consumption = consumption;
  this.fuel = 0;
}

Rockets.prototype.fill = function(fuel){
  this.fuel += fuel;
}

Rockets.prototype.launch = function(){
  if (this.fuel > this.consumption){
    this.fuel -= this.consumption;
  }
}

var rocket1 = new Rockets(10);
rocket1.fill(15);
console.log(rocket1.consumption);
console.log(rocket1.fuel);
rocket1.launch();
console.log(rocket1.consumption);
console.log(rocket1.fuel);

var rocket2 = new Rockets(20);
rocket2.fill(10);
console.log(rocket2.consumption);
console.log(rocket2.fuel);
rocket2.launch();
console.log(rocket2.consumption);
console.log(rocket2.fuel);
