'use strict';

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

Ajax.prototype.update = function(callback, elem, checked){
  this.xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/'+elem.id, true);
  this.xhr.setRequestHeader('Content-Type', 'application/json');
  this.xhr.send(JSON.stringify({text: elem.text, completed: checked}));
  this.xhr.onreadystatechange = function ready() {
    if( this.xhr.readyState === XMLHttpRequest.DONE ) {
      var todos = JSON.parse(this.xhr.response);
      callback(todos);
     }
  }.bind(this);
}

Ajax.prototype.del = function(callback, delId){
  this.xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/'+delId);
  this.xhr.send();
  this.xhr.onreadystatechange = function ready() {
    if( this.xhr.readyState === XMLHttpRequest.DONE ) {
      var todos = JSON.parse(this.xhr.response);
      callback(todos);
     }
  }.bind(this);
}

// /////////////////////////////////////////////
function App(){
  this.ajax = new Ajax();
}

App.prototype.get = function(){
  this.ajax.get(this.render.bind(this));
}

App.prototype.add = function(){
  var form = document.querySelector('form')
  form.addEventListener('submit', function(e){
    e.preventDefault();
  });
  var addTaskButton = document.querySelector('.add-button')
  addTaskButton.addEventListener('click', function(){
    var addText = document.querySelector('#add-text')
    this.ajax.add(function(){
      this.ajax.get(this.render.bind(this))
    }.bind(this), addText.value);
  }.bind(this));
}

App.prototype.delete = function(){
  var garbage = document.querySelectorAll('.del-button')
  garbage.forEach(function(t){
    t.addEventListener('click', function(){
      this.ajax.del(function(){
        this.ajax.get(this.render.bind(this))
      }.bind(this), t.id);
    }.bind(this));
  }.bind(this));
}

App.prototype.update = function(todos){
  var elem = {}
  var checkBox = document.querySelectorAll('input[type=checkbox]');
  checkBox.forEach(function(t){
    t.addEventListener('change', function(){
      todos.forEach(function(e){
        if (t.id == e.id){
          elem = e;
        };
      }.bind(this));
      this.ajax.update(function(){
        this.ajax.get(this.render.bind(this))
      }.bind(this),elem, t.checked);
    }.bind(this));
  }.bind(this));
}

App.prototype.render = function(todos){

  var todolist = document.querySelector('ul')
  todolist.innerHTML = '';

  todos.forEach(function(t){
    var todoElem = document.createElement('li');

    var checkLabel = document.createElement('label');
    checkLabel.htmlFor = t.id;
    if (t.text === ''){
      return;
    } else {
      checkLabel.innerText = t.text;
    }
    var checkBox = document.createElement('input');
    checkBox.type = 'checkbox';
    checkBox.id = t.id;
    checkBox.checked = t.completed;

    var checkButton = document.createElement('span');

    var garbage = document.createElement('button');
    garbage.className = 'del-button';
    garbage.id = t.id;
    if (t.completed){
      todoElem.className = 'checked';
      checkButton.className = 'chk';
    } else {
      todoElem.className = 'un-checked';
      checkButton.className = 'un-chk';
    }
    checkLabel.appendChild(checkButton);
    checkLabel.appendChild(checkBox);
    todoElem.appendChild(checkLabel);
    todoElem.appendChild(garbage);
    todolist.appendChild(todoElem);

  }.bind(this));
  this.delete();
  this.update(todos);
}

var application = new App();
application.get();
application.add();
