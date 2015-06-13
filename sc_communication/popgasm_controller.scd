s = Server.local;
s.reboot;

j = "this is a voice";
j.speak;

"this is a voice".speak;

Speech.setSpeechPitch(0, 200);

(
OSCdef('speakLyric', {
	arg msg;
	"Word:".postln;
	msg[1].asSymbol.postln;
	"Pitch:".postln;
	msg[2].asSymbol.postln;
}, "speakLyric");
)
