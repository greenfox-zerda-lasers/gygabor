'use strict';

var express = require('express');

var app = express();

app.get('/todos', function a(req, res) {
  res.set('Content-Type', 'application/json');
  var jason = [{
    completed: false,
    id: 1,
    text: 'Buy milk'
  },
   {
    completed: false,
    id: 2,
    text: 'Make dinner'
   },
   {
    completed: false,
    id: 3,
    text: 'Save the world'
  }];
  res.end(JSON.stringify(jason));
});

app.listen(3000);
