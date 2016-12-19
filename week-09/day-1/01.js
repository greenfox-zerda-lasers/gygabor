var http = require('http');

var server = http.createServer(function a(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('The request come form: ' + req.url + 'Req Method: ' + req.method + '\nHey! Fuuuu: ' + new Date());
});

server.listen(3000, '127.0.0.1');
