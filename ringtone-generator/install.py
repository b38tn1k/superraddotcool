import os

print "Installing at {!s}. You will have to enter your password. Good luck".format(os.getcwd())
print

os.system('sudo python {!}'.format(os.path.join(os.getcwd(), 'libraries', 'pyOSC', 'setup.py')))

os.system('sudo cp {!} //usr/bin/sclang'.format(os.path.join(os.getcwd(), 'libraries', 'scripts', 'sclang')))
os.system('sudo cp {!} //usr/bin/scsynth'.format(os.path.join(os.getcwd(), 'libraries', 'scripts', 'scsynth')))

os.system('sudo chmod a+x //usr/bin/sclang')
os.system('sudo chmod a+x //usr/bin/scsynth')
