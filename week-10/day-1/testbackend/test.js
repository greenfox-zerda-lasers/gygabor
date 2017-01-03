'use strict';

var test = require('tape');
var request = require('supertest');
var app = require('./server');

// test('First test!', function (t) {
//   t.end();
// });

test('Playlists returned', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('file not found on missingfile', function (t) {
  request(app)
    .get('/missingfile')
    .expect(404)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    })
})

test('unauthorized, send back 401', function (t) {
  request(app)
    .get('/bankinfo')
    .expect(401)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    })
})

test('create new playlist', function (t) {
  request(app)
    .post('/playlists')
    .send({id: '05', name: 'Dubstep'})
    .expect(200)
    .expect('Content-Type', /json/)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    })
})

test('delete playlist', function (t) {
  request(app)
    .delete('/playlists/03')
    // .send({id: '03'})
    .expect(200)
    .expect('Content-Type', /json/)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    })
})

test('get all tracks', function (t) {
  request(app)
    .get('/playlist-tracks')
    .expect(200)
    .expect('Content-Type', /json/)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    })
})

test('get all tracks from a playlist', function (t) {
  request(app)
    .get('/playlist-tracks/01')
    .expect(200)
    .expect('Content-Type', /json/)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    })
})

test('playlist id doesnt exist', function (t) {
  request(app)
    .get('/playlist-tracks/09')
    .expect(404)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    })
})


// GET /playlists
// POST /playlists
// DELETE /playlists/:id
// GET /playlists-tracks
// GET /playlists-tracks/:playlist_id

// POST /playlists-tracks/:playlist_id
// DELETE /playlists-tracks/:playlist_id/:track_id
