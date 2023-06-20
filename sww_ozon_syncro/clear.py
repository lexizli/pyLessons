import os
import glob


def clear():
    files = glob.glob('./wrk/*.csv')

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    files = glob.glob('./out/*.csv')

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
