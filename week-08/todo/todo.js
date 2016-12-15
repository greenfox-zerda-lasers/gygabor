function Ajax(){
  this.xhr = new XMLHttpRequest();
}

Ajax.prototype.get = function(callback){
  this.xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  this.xhr.send(null);
  this.xhr.onreadystatechange = function ready() {
    if( this.xhr.readyState === XMLHttpRequest.DONE ) {
      var todos = JSON.parse(this.xhr.response);
      callback(todos);
    }
  }.bind(this);
}


function App(){
  this.ajax = new Ajax();
  this.ajax.get(render);

  function render(todos){
    var todolist = document.querySelector('ul')
    todos.forEach(function(t){
      var todoElem = document.createElement('li');
      todoElem.innerText = t.text;
      todolist.appendChild(todoElem);
    })

  }
}

var application = new App();
