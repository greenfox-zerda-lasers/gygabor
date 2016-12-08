// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
var king = document.getElementById('b325');
console.log(king);

// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
var conceited = document.getElementsByClassName('b326');
alert(conceited);
console.log(conceited);

// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
businessLamp = document.getElementsByClassName('big');
console.log(businessLamp);

// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
var conceitedKing = document.querySelectorAll('.container .asteroid');
for (var i = 0; i < conceitedKing.length; i++){
  alert(conceitedKing[i].innerText)
};

// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
var noBusiness = document.querySelectorAll('.b329, #b325, .b326');
console.log(noBusiness);

// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.
var allBizniss = document.getElementsByTagName('p');
alert(allBizniss[0].innerText);
console.log(allBizniss);
