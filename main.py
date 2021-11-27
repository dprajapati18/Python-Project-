import os
import os.path
import shutil
import gui

source = gui.source
destination = gui.destination

source += '/'
destination += '/'

for filename in os.listdir(source):

    split_tup = os.path.splitext(filename)
    ex=split_tup[1] #----->ex = extension
    ex=ex[1:]

    if ex == '':
        continue

    temp = destination + ex

    if not(os.path.isdir(temp)):
        path=os.path.join(destination, ex)
        os.mkdir(path)

    s = source + filename
    d = destination + ex + '/' + filename

    if os.path.exists(d):
        print(filename, " already exists")
        continue

    shutil.move(s, d)