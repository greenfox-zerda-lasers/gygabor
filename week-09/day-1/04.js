'use strict';

var jason = require('./todos.json');
var express = require('express');

var app = express();

app.get('/todos/:id', function a(req, res) {
  res.send(jason.filter(function (e){
    return parseInt(req.params.id) === e['id'];
  }));
})

app.listen(3000);
