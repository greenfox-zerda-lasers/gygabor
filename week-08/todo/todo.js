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

Ajax.prototype.add = function(callback, task){
  this.xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  this.xhr.setRequestHeader('Content-Type', 'application/json');
  this.xhr.send(JSON.stringify({text: task}));
  this.xhr.onreadystatechange = function ready() {
    if( this.xhr.readyState === XMLHttpRequest.DONE ) {
      var todos = JSON.parse(this.xhr.response);
      callback(todos);
     }
  }.bind(this);
}

Ajax.prototype.del = function(callback, delId){
  console.log(delId);
  this.xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/'+delId);
  this.xhr.send();
  this.xhr.onreadystatechange = function ready() {
    if( this.xhr.readyState === XMLHttpRequest.DONE ) {
      var todos = JSON.parse(this.xhr.response);
      callback(todos);
     }
  }.bind(this);
}

function App(){
  this.ajax = new Ajax();
  this.ajax.get(render.bind(this));

  var form = document.querySelector('form')
  form.addEventListener('submit', function(e){
    e.preventDefault();
  });

  var addTaskButton = document.querySelector('.add-button')
  addTaskButton.addEventListener('click', function(){
    var addText = document.querySelector('#add-text')
    this.ajax.add(function(){
      this.ajax.get(render.bind(this))
    }.bind(this), addText.value);
  }.bind(this));

  function render(todos){
    var todolist = document.querySelector('ul')
    todolist.innerHTML = '';
    todos.forEach(function(t){
      var todoElem = document.createElement('li');
      todoElem.innerText = t.text;
      var garbage = document.createElement('button');
      garbage.id = 'del-button';

      garbage.addEventListener('click', function(){
        console.log(this);
        this.ajax.del(function(){
          this.ajax.get(render.bind(this))
        }.bind(this), t.id);
      }.bind(this));

      todoElem.appendChild(garbage);
      todolist.appendChild(todoElem);
    }.bind(this))
  }

}

var application = new App();
