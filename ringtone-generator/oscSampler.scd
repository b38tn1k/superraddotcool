////////
(// <- DOUBLE CLICK !!! !!! !!!
////////



s = Server.local;
s.boot;
// s.makeWindow;
)

s.reboot;

////////
(// <- DOUBLE CLICK !!! !!! !!!
////////



//PLAY BACK CONTROL

OSCdef('play', {
	"Play!".postln;
	~bassL = Synth.new("Sampler", [\bufnum, 0, \outBus, 1]);
	~bassR = Synth.new("Sampler", [\bufnum, 0, \outBus, 0]);
	~drumL = Synth.new("Sampler", [\bufnum, 1, \outBus, 1]);
	~drumR = Synth.new("Sampler", [\bufnum, 1, \outBus, 0]);
	~melodyL = Synth.new("Sampler", [\bufnum, 2, \outBus, 1, \direct, 0.5]);
	~melodyR = Synth.new("Sampler", [\bufnum, 2, \outBus, 0, \direct, 0.5]);

	~bassL.set(\loopVal, 1);
	~bassR.set(\loopVal, 1);
	~drumL.set(\loopVal, 1);
	~drumR.set(\loopVal, 1);
	~melodyL.set(\loopVal, 1);
	~melodyR.set(\loopVal, 1);

}, "/play");

OSCdef('stop', {
	~bassL.set(\loopVal, 0);
	~bassR.set(\loopVal, 0);
	~drumL.set(\loopVal, 0);
	~drumR.set(\loopVal, 0);
	~melodyL.set(\loopVal, 0);
	~melodyR.set(\loopVal, 0);

	~bassL.free;
	~bassR.free;
	~drumL.free;
	~drumR.free;
	~melodyL.free;
	~melodyR.free;
}, "/stop");

//INSTANTIATE CONTROL

OSCdef ('makeSampler', {
	SynthDef("Sampler", { arg outBus = 0, bufnum, speed=1, direct = 0.3, loopVal = 1;
		var scaledRate, player;
		// Set Playback Speed
		"Create Sampler".postln;
		scaledRate = BufRateScale.kr(bufnum);
		// Create Player
		player = PlayBuf.ar(1, bufnum, speed*scaledRate, loop:loopVal, doneAction:2);
		// Route between two buses
		Out.ar(outBus, player * direct );
	}).add;
}, "/makeSampler");


OSCdef('recordOutput', {
	s.record;
}, "beginRecord");

OSCdef('armRecord', {
	s.prepareForRecord;
}, "armRecord");

OSCdef('stopRecord', {
	s.stopRecording;
}, "stopRecord");

OSCdef('loadSample', {
	arg msg;
	var sample = Buffer.read(s, msg[1]);
	"Load Sample".postln;
	sample
}, "loadSample");

// SAMPLER CONTROL

OSCdef('bassBufferSwap' , {
	arg msg;
	"Set Bass".postln;
	~bassL.set(\bufnum, msg[1]);
	~bassR.set(\bufnum, msg[1]);
}, "/bassSwap");

OSCdef('drumBufferSwap' , {
	arg msg;
	"Set Drum".postln;
	~drumL.set(\bufnum, msg[1]);
	~drumR.set(\bufnum, msg[1]);
}, "/drumSwap");

OSCdef('melBufferSwap' , {
	arg msg;
	"Set Mel".postln;
	~melodyL.set(\bufnum, msg[1]);
	~melodyR.set(\bufnum, msg[1]);
}, "/melSwap");

OSCdef('panic' , {
	s.reboot;
}, "/panic");

OSCdef('quit', {
	s.quit;
}, "/quit")


'You did it! Setup Complete!';

)
