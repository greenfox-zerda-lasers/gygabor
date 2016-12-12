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
    return 'This Type doesn\'t exist!';
  }
  this.allDamage = this.maxAmmo * this.baseDamage;
}

Aircraft.prototype.fight = function(){
  var causedDamage = this.ammo * this.baseDamage;
  this.ammo = 0;
  this.allDamage = this.maxAmmo * this.baseDamage;
  return causedDamage;
}

Aircraft.prototype.refill = function(roundAmmo){
  for (var i = 0; roundAmmo > 0 && i < this.maxAmmo; i++){
    if (this.ammo < this.maxAmmo) {
      this.ammo++;
      roundAmmo--;
      this.allDamage = this.maxAmmo * this.baseDamage;
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
}

Carrier.prototype.fill = function(){
  this.totalDamage = 0;
  this.plane.forEach(function(plane){
    var fillAmount = 0
    if (plane.maxAmmo > this.totalAmmo){
      fillAmount = this.totalAmmo;
    } else {
      fillAmount = plane.maxAmmo;
    }
    if (this.totalAmmo <= 0) {
      this.totalAmmo = 0;
      throw Error('No more Fuel');
    }
    var remainAmmo = plane.refill(fillAmount);
    this.totalAmmo -= fillAmount-remainAmmo;
    this.totalDamage += plane.allDamage;
  }, this);
}

Carrier.prototype.planeFight = function(){
  this.plane.forEach(function(plane){
    var damage = plane.fight();
    this.totalDamage -= damage
  }, this);
}

Carrier.prototype.status_report = function(){
  console.log('Aircraft count: '+ this.plane.length +', Ammo Storage: '+ this.totalAmmo +', Total damage: '+ this.totalDamage + ', Health Remaining: '+ this.health);
  console.log('Aircrafts:');
  this.plane.forEach(function(plane){
    console.log('Type '+ plane.type + ', Ammo: ' + plane.ammo + ', Base Damage: '+ plane.baseDamage + ', All Damage: '+ plane.allDamage);
  });
  if (this.health <= 0) {
    return 'It\'s dead Jim :(';
  }
}

var plane1 = new Aircraft('F16');
var plane2 = new Aircraft('F35');
var carrier = new Carrier();
carrier.addAircraft(plane1);
carrier.addAircraft(plane2);
carrier.fill();
carrier.planeFight();
var jim = carrier.status_report();
