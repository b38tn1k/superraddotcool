from os import path, getcwd, listdir
from scBridge import *

class Composer(object):
    def __init__(self, genre, variant, bass_val, mel_val, drum_val, buffer_tracker):
        self.genre = genre
        self.variant = variant
        self.bass_val = bass_val
        self.mel_val = mel_val
        self.drum_val = drum_val
        self.buffer_tracker = buffer_tracker

    def play(self):

        base_directory = getcwd()
        base_directory = path.join(base_directory, 'assets')
        base_directory = path.join(base_directory, self.genre)

        variant_list = [x for x in listdir(base_directory) if path.isdir(path.join(base_directory, x))]
        var_val = self.variant % len(variant_list)
        variant_directory = path.join(base_directory, variant_list[var_val])
        variant_file_list = listdir(variant_directory)

        bass_list = [x for x in variant_file_list if not (x.find("BASS") == -1)]
        drum_list = [x for x in variant_file_list if not(x.find("DRUM") == -1)]
        mel_list = [x for x in variant_file_list if not(x.find("MEL") == -1)]

        if not (len(bass_list) == 0) and not(len(mel_list) == 0) and not(len(drum_list) == 0):
            bass_val = self.bass_val % len(bass_list)
            mel_val = self.mel_val % len(mel_list)
            drum_val = self.drum_val % len(drum_list)

            print 'mod var: {!s}'.format(var_val)
            print 'mod bass: {!s}'.format(bass_val)
            print 'mod mel: {!s}'.format(mel_val)
            print 'mod drum: {!s}'.format(drum_val)

            makeSampler()
            play()

            loadSample(path.join(variant_directory, bass_list[bass_val]))
            loadSample(path.join(variant_directory, drum_list[drum_val]))
            loadSample(path.join(variant_directory, mel_list[mel_val]))
            # setBassBuffer(0)
            # setDrumBuffer(1)
            # setMelBuffer(2)

            setBassBuffer(self.buffer_tracker)
            setDrumBuffer(self.buffer_tracker+1)
            setMelBuffer(self.buffer_tracker+2)
