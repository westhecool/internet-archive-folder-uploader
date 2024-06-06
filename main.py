import os
import sys
import subprocess
if len(sys.argv) < 3:
    print('Usage: python3 main.py <identifier> <folder>')
    exit(1)

identifier = sys.argv[1]
folder = sys.argv[2]

def upload(directory, remote_directory):
    for filename in os.listdir(directory):
        if os.path.isfile(directory + '/' + filename):
            print(f'Uploading {directory + "/" + filename} to {(remote_directory + "/" + filename) if remote_directory else filename}')
            subprocess.run(['ia', 'upload', '--no-backup', identifier, directory + '/' + filename, f'--remote-name="{(remote_directory + "/" + filename) if remote_directory else filename}'])
        elif os.path.isdir(directory + '/' + filename):
            upload(directory + '/' + filename, (remote_directory + '/' + filename) if remote_directory else filename)
upload(folder, '')