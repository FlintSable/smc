const http = require("http");

http.createServer((request, responce) => {
	responce.writeHead(200, {'Content-Type': 'text/html'});
	responce.write('Hello Node, my name in Nicholas Noochla-or');

}).listen(8001);

console.log('Server running at http://127.0.0.1:8001/');