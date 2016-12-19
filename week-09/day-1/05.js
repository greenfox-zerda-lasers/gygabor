'use strict';

var jason = require('./todos.json');
var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());

var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.get('/todos', function a(req, res) {
  res.send(jason);
});

app.get('/todos/:id', function a(req, res) {
  res.send(jason.filter(function (e){
    return parseInt(req.params.id, 10) === e['id'];
  }));
});

app.post('/todos', urlencodedParser, function a(req, res) {
  console.log(req.body);
  var todo = {
    completed: Boolean(req.body.completed),
    id: jason.length + 1,
    text: req.body.text,
  };
  jason.push(todo);
  res.send(JSON.stringify(todo));
});

app.listen(3000);
