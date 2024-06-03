import os
import sys
if len(sys.argv) < 3:
    print("Usage: python3 main.py <identifier> <folder>")
    exit(1)

identifier = sys.argv[1]
folder = sys.argv[2]

def upload(directory, remote_directory):
    for filename in os.listdir(directory):
        if os.path.isfile(directory + '/' + filename):
            r = '--remote-name="'
            q = '"'
            print(f'ia upload {identifier} "{directory + "/" + filename}" {(r + remote_directory + "/" + filename + q) if remote_directory else ""}')
            #os.system(f"ia upload {identifier} {directory + '/' + filename} {(remote_directory + '/' + filename) if remote_directory else ''}")
        elif os.path.isdir(directory + '/' + filename):
            upload(directory + '/' + filename, (remote_directory + '/' + filename) if remote_directory else filename)
upload(folder, '')