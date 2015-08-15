import os
from time import sleep
from mutagen.mp3 import MP3

jack_computer = False

print '\n\nTreeHugger Audio Assets Generator\n\n'

java_array_index_strings = "public int NO_1 = 0;\npublic int NO_2 = 1;\npublic int BLANK_1 = 2;\npublic int BLANK_2 = 3;\npublic int OK_GOOGLE_QUERY = 4;\npublic int OK_GOOGLE_REPLY = 5;\npublic int COPY_ROOT = 6;\n"

asset_list = 'tracklist.md'
root = os.getcwd()
path_to_file = os.path.join(root, asset_list)

if jack_computer is False:
    print 'Creating Index File'
    os.system('gimli')

with open ('audio_assests.json', 'wb') as json:
    json.write('{\n\n')
    with open (path_to_file, 'r') as doc:
        with open ('audio_assets.java', 'wb') as java_lib:
            java_lib.write(java_array_index_strings)
            text = doc.read()
            lines = text.split('\n')
            output_file_name = None
            text_to_say = None
            dir_name = None
            parent_dir = None
            for line in lines:
                if line != '# TreeHugger Audio Assets':
                    if line[0:3] == '## ':
                            output_file_name = None
                            text_to_say = None
                            dir_name = None
                            dir_name = line[3:].replace('-', '_')
                            parent_dir = line[3:].replace('-', '_')
                            if os.path.exists(os.path.join(root, dir_name)) is False:
                                java_lib.write('// {!s}\n'.format(dir_name))
                                os.mkdir(os.path.join(root, dir_name))
                                json.write('\n}},\n"{!s}": {{\n'.format(line[3:].replace('-', '_')))
                            print "Directory Name: {!s}".format(dir_name)
                    elif line[0:4] =='### ':
                        output_file_name = line[4:].replace('-', '_')
                        print "Output File Name: {!s}".format(output_file_name)
                        json.write('\n"{!s}": {{\n"endpoint": "https://storage.googleapis.com/treehugger/{!s}/{!s}.mp3",\n'.format(output_file_name, parent_dir, output_file_name))
                    elif line == '':
                        pass
                    elif line == '---':
                        pass
                    else:
                        text_to_say = line
                        print "Text To Say: {!s}".format(text_to_say)
                        json.write('"text": "{!s}",\n'.format(text_to_say))
                    if dir_name is not None and output_file_name is not None and text_to_say is not None: #lol
                        output = os.path.join(root, dir_name)
                        print 'Output Path: {!s}'.format(output)
                        if os.path.isdir(output) is False:
                            print 'Creating Output Path: {!s}'.format(output)
                            os.mkdir(output)
                        output = os.path.join(output, output_file_name)
                        print 'Absolute Path" {!s}'.format(output)
                        print 'Synthesising Audio: {!s} \n'.format(text_to_say)
                        os.system('say {!s} -o {!s}'.format(text_to_say, output))
                        os.system('lame -m m {!s}.aiff'.format(output))
                        sleep(0.5)
                        os.system('rm {!s}.aiff'.format(output))
                        audio = MP3(output + ".mp3")
                        asset_path = '{!s}/{!s}'.format(parent_dir, output_file_name)
                        java_lib.write('THAudioAsset {!s} = new THAudioAsset("{!s}", {!s});\n'.format(output_file_name, asset_path, 1000*audio.info.length))
                        json.write('"time": "{!s}"\n}},'.format(1000*audio.info.length))
                        text_to_say = None
                        # java_lib.write('public static String {!s}_ASSET_PATH = "{!s}/{!s}.mp3";\n'.format(output_file_name, parent_dir, output_file_name))
                        # java_lib.write('public static long {!s}_DURATION = {!s};\n'.format(output_file_name, 1000*audio.info.length))
    json.write('\n\n}')
