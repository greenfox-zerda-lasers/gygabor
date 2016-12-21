'use strict';

var mysql = require("mysql");
var express = require('express');

var app = express();

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'cookies',
  database: 'todo'
});

connection.connect(function (error){
  if (error) {
    console.log('muhahaha', error);
  } else {
    console.log ('WOOOOWW');
  }
});

app.get('/', function(req, res) {
   connection.query('SELECT * FROM todo',function(err,rows){
     if(err) {
       console.log(err.toString());
       return;
     }
     res.send(rows);
   });
 });

 app.listen(3000);
