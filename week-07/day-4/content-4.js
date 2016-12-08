// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']

var listElements = ['apple', 'banana', 'cat', 'dog'];

var listToUpdate = document.getElementsByTagName('li');

function update(){
  if (listElements.length === listToUpdate.length){
    for (var i = 0; i < listElements.length; i++){
      listToUpdate[i].innerHTML = listElements[i];
    }
  }
}

update();
