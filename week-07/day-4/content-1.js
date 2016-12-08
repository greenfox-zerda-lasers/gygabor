// 1. Alert the content of the heading.
var head = document.getElementsByTagName('h1');
alert(head[0].innerText);

// 2. Write the content of the first paragraph to the console.
var firstParagraph = document.querySelector('p');
console.log(firstParagraph);

// 3. Alert the content of the second paragraph.
var secondParagraph = document.getElementsByClassName('other');
console.log(secondParagraph);

// 4. Replace the heading's content with 'New content'.
head[0].innerHTML = 'New content'

// 5. Replace the last paragraph's content with the first paragraph's content.
var thirdParagraph = document.getElementsByClassName('result');
thirdParagraph[0].innerHTML = secondParagraph[0].innerText
