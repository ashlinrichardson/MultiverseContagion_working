import os
import sys
args = sys.argv

if len(args) < 2:
    print("python3 csv_to_json.py [csv file] #convert pop file to json in expected way")
    sys.exit(1)

d = open(args[1]).read()

dat = '{"x":"' + d + '")'

open(args[1] + ".json", "wb").write(dat.encode())






