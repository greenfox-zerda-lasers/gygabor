'use strict';

var mysql = require("mysql");
var express = require('express');

var app = express();

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'cookies',
  database: 'bookstore'
});

connection.connect(function (error){
  if (error) {
    console.log('muhahaha', error);
  } else {
    console.log ('WOOOOWW');
  }
});

// app.get('/', function(req, res) {
//    connection.query('SELECT book_name FROM book_mast;',function(err,rows){
//      if(err) {
//        console.log(err.toString());
//        return;
//      }
//      res.send(rows);
//    });
//  });

app.get('/', function(req, res) {
   connection.query('SELECT book_name, aut_name, cate_descrip, book_price pub_name FROM book_mast INNER JOIN author ON book_mast.aut_id = author.aut_id INNER JOIN category ON book_mast.cate_id = category.cate_id INNER JOIN publisher ON book_mast.pub_id = publisher.pub_id;',function(err,rows){
     if(err) {
       console.log(err.toString());
       return;
     }
     res.send(rows);
   });
 });

 app.listen(3000);
