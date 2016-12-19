'use strict';

var express = require('express');

var app = express();

app.get('/', function (request, respond) {
  respond.send('Hey! How are you?');
});

app.post('/', function (request, respond) {
  respond.send('Posted');
});

app.listen(3000);
