'use strict'

var test = require('tape');
var double = require('./01.js');

test('true', function(t) {
  t.equal(true, true);
  t.end();
});

test('test double() gives back doublednumber', function(t){
  t.equal(double(1), 2);
  t.end();
});

test('test double() gives back doublednumber', function(t){
  t.equal(double('1'), 2);
  t.end();
});
