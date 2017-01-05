'use strict';

var mysql = require("mysql");
var express = require('express');
var bodyParser = require('body-parser');
var fs = require('fs');
var jsmediatags = require("jsmediatags");

var app = express();

var readTrackData = (function () {
  var mp3Folder = './mp3/';
  var files = [];
  var metaData = [];

  function readDir(track){
    if (track === 'all'){
      fs.readdir(mp3Folder, function (err, fileNames) {
        if (err) {
          throw err;
        }
        fileNames.forEach(function(f) {
          files.push(f);
          // metaData.push(readMeta(f));
          // console.log(files);
        });
        // console.log(files)
        return (files);
      });
    }
  }

  function readMeta(track){

    jsmediatags.read(''+ mp3Folder + track + '', {
      onSuccess: function(tag) {
        var data = []
        data.push(tag)
        console.log(data)
        return (data);
      },
      onError: function(error) {
        console.log(error);
      }
    });

  }
  return {
    readDirectory: readDir,
    // file: files,
    // metaData: metaData
  };
})();
readTrackData.readDirectory('all')

app.use(bodyParser.json());

// app.use(function(req, res, next) {
//   res.header("Access-Control-Allow-Origin", "*");
//   res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//   res.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE');
//   next();
// });


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
  connection.query('SELECT * FROM tracks', function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
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

app.listen(3000);
