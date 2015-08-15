This script will create a stack of audio files and a pretty pdf index file:

REQUIREMENTS:
CLI TOOLS

gem install gimli

gimli lets you generate a .pdf from the md file - requires ruby to be installed
otherwise set jack_computer to True

sudo port install lame

lame is a mp3 codec to convert the aif files to mp3

PYTHON LIBRARIES

pip install mutagen

mutagen gets info about audio files
