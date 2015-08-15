
// Server
var http = require('http');
http.createServer(function (req, res) {

  res.writeHead(200, {'Content-Type': 'text/plain'});
  var T = require("timbre");
  res.end('Hello World\n');

  var synth = T("OscGen", {wave:"saw", mul:0.25}).play();
  var keydict = T("ndict.key");
  var midicps = T("midicps");
  T("keyboard").on("keydown", function(e) {
    var midi = keydict.at(e.keyCode);
    if (midi) {
      var freq = midicps.at(midi);
      synth.noteOnWithFreq(freq, 100);
    }
  }).on("keyup", function(e) {
    var midi = keydict.at(e.keyCode);
    if (midi) {
      synth.noteOff(midi, 100);
    }
  }).start();

}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/');
//
