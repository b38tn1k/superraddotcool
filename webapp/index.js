var icecast = require("icecast"), // I'll talk about this module later
    lame = require("lame");

var encoder = lame.Encoder({channels: 2, bitDepth: 16, sampleRate: 44100});
encoder.on("data", function(data) {
  console.log("encoding data");
  sendData(data);
});
var decoder = lame.Decoder();
decoder.on('format', function(format) {
  console.log("decoding data");
  decoder.pipe(encoder);
});

var url = 'http://192.168.2.6:8000/listen.m3u'
icecast.get(url, function(res) {
  res.on('data', function(data) {
    console.log("got data");
    decoder.write(data);
  });
});

var clients = []; // consider that clients are pushed to this array when they connect

function sendData(data){
  clients.forEach(function(client) {
      client.write(data);
  });
}

setTimeout(function () {
    console.log('hello');
}, 10000);
