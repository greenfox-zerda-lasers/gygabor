'use strict';

var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'cookies',
  database: 'todo'
});

connection.connect(function (error){
  if (error) {
    console.log('muhahaha', error);
    console.end;
  } else {
    console.log ('WOOOOWW');
  }
});
