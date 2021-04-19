import os
import sys
args = sys.argv

if len(args) < 2:
    print("python3 write_csv [population size] # write tickets going no-where for single universe")
    sys.exit(1)

N = 0

try:
    N = int(args[1])
except:
    print("pop size needs to be a number"); sys.exit(1)

fn = 'pop' + str(N) +'.csv'
f = open(fn, 'wb')

def w(f, s):
    f.write(s.encode())

w(f, "Population," + str(N) + ",Universe,1,Universe\r\n")

stuff = ['pID','sno','ETA', '@U', 'ETD', '>U', '@Role', '@Mx', 'Age', 'FamKey', '23-24', '00-01', '02-05', '05-06', '06-07', '07-08', '08-09', '09-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-00\r\n']

w(f, ','.join(stuff))

for i in range(N):
    d = [str(i), str(0), str(0), str(0), str(0), 'R', str(1.), str(0), 'F00', '', 'U0', 'U0']
    while len(d) < len(stuff):
        d = d + ['']

    w(f, ((','.join(d)) + "\r\n"))
