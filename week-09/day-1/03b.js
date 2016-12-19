'use strict';

var jason = require('./todos.json');
var express = require('express');

var app = express();

app.get('/todos', function a(req, res) {
  res.send(jason);
});

app.listen(3000);
