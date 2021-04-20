# write csv, convert to JSON, then run simulation
import os
import sys
args = sys.argv

def err(m):
    print("Error: " + m); sys.exit(1)

if len(args) < 2:
    err("python3 write_csv [population size] # write tickets going no-where for single universe")

N = 0

try:
    N = int(args[1])
except:
    err("pop size needs to be a whole number")

fn = 'pop' + str(N) +'.csv'
f = open(fn, 'wb')

def w(f, s):
    f.write(s.encode())

w(f, "Population," + str(N) + ",Universe,1,Universe\r\n")
cols = ['pID','sno','ETA', '@U', 'ETD', '>U', '@Role', '@Mx', 'Age', 'FamKey', '23-24', '00-01', '02-05', '05-06', '06-07', '07-08', '08-09', '09-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-00\r\n']

w(f, ','.join(cols))

for i in range(N):
    d = [str(i), str(0), str(0), str(0), str(24), str(0), 'R', str(1.), str(0), 'F00', '', 'U0', 'U0']

    while len(d) < len(cols):
        d = d + ['']

    w(f, ((','.join(d)) + "\r\n"))


f = open('param.csv', 'wb')
w(f, 'Parameters,,\n')
w(f, 'population,' + str(N) + ',\n')
w(f, 'UN,1,Universe\n')
w(f, 'HzR,4,\n')
w(f, 'sizeF,1.5,0\n')
w(f, 'mF,2.6,0\n')
w(f, 'RedDays,11.2,\n')
w(f, 'pop file,pop' + str(N) + '.json,\n')
w(f, 'case file,case5.json,\n')
w(f, 'STOP,350,\n')
f.close()

f = open('case5.csv', 'wb')
w(f, '''Cases,,,,,,
pID,age-Gp,comb-risk,VL,postInfD,role,minglx
0,1,3,2.6,2.2,R,1
1,1,3,2.6,2.2,R,1
2,1,3,2.6,2.2,R,1
3,1,3,2.6,2.2,R,1
4,1,3,2.6,2.2,R,1''')
f.close()

a = os.system('python3 csv_to_json.py')
a = os.system('Rscript run.R > run.txt')
a = os.system('grep prob= run.txt > run.log')
a = os.system('python3 parse.py run.log')
