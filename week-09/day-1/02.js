'use strict';

var express = require('express');

var app = express();

app.get('/', function a(req, res) {
  res.send('The request come form: ' + req.url + '\nHey! Fuuuu: ' + new Date());
});

app.listen(3000);
