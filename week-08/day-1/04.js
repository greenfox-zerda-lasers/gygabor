'use strict';
// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function Aircraft(type){
  if (type === 'F16'){
    this.type = type;
    this.ammo = 0;
    this.maxAmmo = 8;
    this.baseDamage = 30;
  } else if (type === 'F35'){
    this.type = type;
    this.ammo = 0;
    this.maxAmmo = 12;
    this.baseDamage = 50;
  } else {
    return 'This Type doesn\'t exist!'
  }
  this.allDamage = this.maxAmmo * this.baseDamage;
}

Aircraft.prototype.fight = function(){
  var causedDamage = this.ammo * this.baseDamage;
  this.ammo = 0;
  return causedDamage;
}

Aircraft.prototype.refill = function(roundAmmo){
  for (var i = 0; roundAmmo > 0 && i < this.maxAmmo; i++){
    if (this.ammo < this.maxAmmo) {
      this.ammo++;
      roundAmmo--;
    }
  }
  return roundAmmo;
}

// ****************CARRIER*********************

function Carrier(){
  this.plane = [];
  this.totalAmmo = 100;
  this.health = 3000;
  this.totalDamage = 0;
}

Carrier.prototype.addAircraft = function(plane){
  this.plane.push(plane);
  this.totalDamage += plane.allDamage;
}

Carrier.prototype.fill = function(){
  this.plane.forEach(function(plane){
    if (plane.maxAmmo > this.totalAmmo){
      var fillAmount = this.totalAmmo;
    } else {
      var fillAmount = this.totalAmmo;
    }
    if (this.totalAmmo <= 0) {
      this.totalAmmo = 0;
      throw Error('No more Fuel');
    }
    var remainAmmo = plane.refill(fillAmount);
    this.totalAmmo -= plane.maxAmmo-remainAmmo;
  }, this);
}

var plane1 = new Aircraft('F16');
var plane2 = new Aircraft('F35');
var carrier = new Carrier();
carrier.addAircraft(plane1);
carrier.addAircraft(plane2);
carrier.fill()
// console.log(plane1.fight());
// console.log(plane1.refill(5));
// console.log(plane1);
