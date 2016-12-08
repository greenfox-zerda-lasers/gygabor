// fill output1 with the first paragraph's content, text only.
// fill output2 with the first paragraph's content keeping the cat strong.

var firstParagraph = document.querySelector('p');

var secondParagraph = document.getElementsByClassName('output1');

var thirdParagraph = document.getElementsByClassName('output2');

function chngSecond(){
  if (secondParagraph){
    for (var i = 0; i < secondParagraph.length; i++){
      secondParagraph[i].innerText = firstParagraph.innerText;
    }
  }
}

function chngThird(){
  if (thirdParagraph){
    for (var i = 0; i < thirdParagraph.length; i++){
      thirdParagraph[i].innerHTML = firstParagraph.innerHTML;
    }
  }
}

chngSecond();
chngThird();
