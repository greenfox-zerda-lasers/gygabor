'use strict';

var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');
var fs = require('fs');
var meta = require('musicmetadata');
var async = require('async');

var app = express();

app.use(bodyParser.json());

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  res.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE');
  next();
});


var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'cookies',
  database: 'foxplayer'
});

connection.connect(function (error){
  if (error) {
    console.log('muhahaha', error);
    console.end;
  } else {
    console.log ('WOOOOWW');
  }
});

app.get('/playlists', function(req, res) {
	connection.query('SELECT * FROM playlists', function(err, rows, fields) {
		if (err) throw err;
  	res.send(rows);
	});
});

app.post('/playlists', function (req, res) {
  connection.query('INSERT INTO playlists (playlist, system) VALUES ("' + req.body.playlist + '", 0);', function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
});

app.delete('/playlists/:id', function (req, res) {
  connection.query('DELETE FROM playlists WHERE id = \'' + req.params.id + '\';', function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
}),

app.get('/playlist-tracks', function (req, res) {
  fs.readdir('./mp3/', function (err, files) {
		var coll = [];
		async.each(
			files,
			function (file, callback){
				meta(fs.createReadStream('./mp3/' + file), { duration: true }, function (err, metadata) {
					metadata.fileName = file;
					coll.push(metadata);
				 	callback();
				});
			},
			function(){
  				res.send(coll);
			}
		);
	});
}),

app.get('/playlist-tracks/:playlist_id', function (req, res) {
  connection.query('SELECT * FROM tracks WHERE playlist_id = \'' + req.params.playlist_id + '\';', function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
}),

app.post('/playlist-tracks', function (req, res) {
  connection.query('INSERT INTO tracks (path, playlist_id) VALUES ("' + req.body.path + '", 0);', function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
}),

app.post('/playlists-tracks/:playlist_id', function (req, res) {
  connection.query('UPDATE tracks SET playlist_id = "' + req.params.playlist_id + '";', function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
}),

app.listen(3000, function(){
	console.log('SERVER IS UP AND RUNNIN on port: 3000')
});
