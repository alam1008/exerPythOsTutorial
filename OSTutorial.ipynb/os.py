import os
from datetime import datetime

print(dir(os))

print(os.getcwd())

os.chdir('/Users/angela/Desktop/')

#os.mkdir('OS-Demo-2/Sub-Dir-1')
os.makedirs('OS-Demo-2/Sub-Dir-1')

#os.rmdir('OS-Demo-2/Sub-Dir-1')
os.removedirs('OS-Demo-2/Sub-Dir-1')

os.rename('test.txt', 'demo.txt')

print(os.listdir())

print(os.stat('demo.txt').st_size)
print(datetime.fromtimestamp(mod_time))

for dirpath,dirnames, filenames in os.walk('/Users/angela/Desktop/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME') + 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))

print(os.path.dirname('/tmp/test.txt'))

print(os.path.split('/tmp/test.txt'))

print(os.path.exists('/tmp/test.txt'))

print(os.path.isdir('/tmp/fgdfgdf'))

print(os.path.isfile('/tmp/fgdfgdf'))

print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))

# Official Python documentation: https://docs.python.org/3/
# Tutorial on the OS module in the official documentation: https://docs.python.org/3/library/os.html?highlight=os%20module#module-os

