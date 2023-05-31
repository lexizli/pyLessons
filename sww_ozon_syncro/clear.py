import os
import glob

files = glob.glob('./wrk/*.csv')

for f in files:
    print(f)
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

