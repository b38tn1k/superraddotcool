s = Server.local;
s.reboot;
"this is a voice".speak;
Speech.setSpeechPitch(0, 200);

(
OSCdef('speak', {
	arg msg;
	'i tried'.postln;
}, "speak");
)
