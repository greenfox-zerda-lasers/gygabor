// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk

function tour(walk, distance){
  return distance.map(walk);
}

function distance(step){
  var steps = []
    for (var i = 0; i < step; i++){
      steps.push(false);
    }
  return steps;
}

function walk(){
  return true;
}

console.log(tour(walk, distance(4)));
