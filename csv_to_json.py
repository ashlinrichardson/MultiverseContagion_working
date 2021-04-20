'''convert all csv files in the present folder, to the json form expected by CovidSIM
'''
import os
import sys
args = sys.argv

if len(args) < 2:
    files = os.popen('ls -1 *.csv').readlines()
    if len(files) < 1:
        print("python3 csv_to_json.py [csv file] #convert pop file to json in expected way")
        sys.exit(1)
    else:
        files = [x.strip() for x in files]
        for f in files:
            a = os.system('python3 csv_to_json.py ' + f)
        sys.exit(0)

fn = args[1]
d = open(fn).read()
dat = '{"x":"' + d + '")'
open(fn[:-4] + ".json", "wb").write(dat.encode())
