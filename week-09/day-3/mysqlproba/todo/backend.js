'use strict';

var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  res.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE');
  next();
});

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

app.post('/todo', function(req, res) {
  connection.query('INSERT INTO todo (text, completed) VALUES ("' + req.body.text + '", 0);', function(err,row){
    if(err) {
      console.log('err.toString()');
      return;
    }
    res.send(row);
  });
});

app.put('/todo/:id', function(req, res) {
  console.log(req.params.id)
  connection.query('UPDATE todo SET completed = NOT completed WHERE id = \'' + req.params.id + '\';', function(err,row){
    if(err) {
      console.log('err.toString()');
      return;
    }
    res.send(row);
  });
});

app.delete('/todo/:id', function(req, res) {
  connection.query('DELETE FROM todo WHERE id = \'' + req.params.id + '\';', function(err,rows){
    if(err) {
      console.log('err.toString()');
      return;
    }
    res.send(rows);
  });
});

app.listen(3000);
