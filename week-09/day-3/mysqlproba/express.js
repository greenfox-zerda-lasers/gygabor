'use strict';

var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');


var app = express();

app.use(bodyParser.json());

var urlencodedParser = bodyParser.urlencoded({ extended: false });

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

app.get('/todo', function(req, res) {
   connection.query('SELECT * FROM todo',function(err,rows){
     if(err) {
       console.log(err.toString());
       return;
     }
     res.send(rows);
   });
 });

app.post('/todo', urlencodedParser, function(req, res) {
  console.log(req.body);
  connection.query('INSERT INTO todo (task, completed) VALUES ("'+req.body.task+'");', function(err,rows){
    if(err) {
      console.log('err.toString()');
      return;
    }
    res.send('req.body.task');
  });
});

app.listen(3000);
