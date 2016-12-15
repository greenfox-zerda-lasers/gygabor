'use strict'

var test = require('tape');
var addA = require('./02.js');

test('addA() gives back string', function(t) {
  t.equal(typeof addA('string'), 'string' );
  t.end();
});

test('addA() gives back string + a', function(t) {
  t.equal(addA('string'), 'stringa' );
  t.end();
});
