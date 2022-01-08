from sys import exit,argv
from datetime import datetime
from platform import *
f = open(argv[1])
var = {}
lineNum = 0
now = datetime.now()
os = platform.system()
for line in f:
    line = line.replace('\t','')
    line = line.replace('\n','')
    var.update({'filename':f.name})
    var.update({"time":now.strftime("%H:%M")})
    var.update({"date":now.strftime('%d/%m/%Y')})
    var.update({"version":"2.0"})
    var.update({"filename":f.name})
    var.update({"os":os.name})
    tokens = line.split(':')
    lineNum+=1
    if '+' in line:
        a = int(line.split('+')[0])
        b = int(line.split('+')[1])
        op = a+b
        print(op)
    elif '*' in line:
        a = int(line.split('*')[0])
        b = int(line.split('*')[1])
        op = a*b
        print(op)
    elif '-' in line:
        a = int(line.split('-')[0])
        b = int(line.split('-')[1])
        op = a-b
        print(op)
    elif '/' in line:
        a = int(line.split('/')[0])
        b = int(line.split('/')[1])
        op = a/b
        print(op)
    elif '=' in line:
        if '?' in line:
            var.update({line.split('=')[0]:input(line.split('?')[1])})
            var.update({str(line.split('=')[0])+'.type':'<input>'})
        elif '"' in line.split('=')[1]:
            var.update({line.split('=')[0]:str(line.split('"')[1])})
            var.update({str(line.split('=')[0])+'.type':'<string>'})
        elif ':' in line.split('=')[1]:
            var.update({line.split('=')[0]:int(line.split(':')[1])})
            var.update({str(line.split('=')[0])+'.type':'<integer>'})
    elif 'out' in line:
        if '"' in line.split(' ')[1]:
            print(line.split('"')[1])
        else:
            try:
                print(var[line.split(' ')[1]])
            except:
                print('Error at "'+f.name+'" line '+str(lineNum)+':\n   '+line+'\nVariable "'+line.split(' ')[1]+'" is not existent.')
                exit()
    elif 'read' in line:
        if '"' in line.split(' ')[1]:
            try:
                f = open(line.split('"')[1],'r')
                print(f.read())
            except:
                print('Error at "'+f.name+'" line '+str(lineNum)+':\n   '+line+'\nFile "'+line.split('"')[1]+'" is either non existent or not accessible.')
                exit()
        else:
            try:
                f = open(var[line.split(' ')[1]])
                print(f.read())
            except:
                print('Error at "'+f.name+'" line '+str(lineNum)+':\n   '+line+'\nFile "'+var[line.split(' ')[1]]+'" is either non existent or not accessible.')
                exit()
    elif 'append' in line:
        if '"' in line.split(' ')[1]:
            try:
                f = open(line.split('"')[1],'a')
                if '"' in line.split(' ')[1]:
                    f.write(str(line.split('"')[2]).replace(' ','',1))
                else:
                    f.write(var[line.split('"')[1]])
            except:
                print('Error at "'+f.name+'" line '+str(lineNum)+':\n   '+line+'\nFile "'+line.split('"')[1]+'" is either non existent or not accessible.')
                exit()
        else:
            try:
                f = open(var[line.split(' ')[1]],'a')
                if '"' in line.split(' ')[2]:
                    f.write('\n')
                    f.write(line.split('"')[2])
                else:
                    f.write('\n')
                    f.write(var[line.split('"')[1]])
            except:
                print('Error at "'+f.name+'" line '+str(lineNum)+':\n   '+line+'\nFile "'+var[line.split(' ')[1]]+'" is either non existent or not accessible.')
                exit()
    elif line.startswith('::'):
        pass
    elif line == 'debug':
        print('Variables: '+str(var)+',\nFile: '+f.name+',\nLine Number: '+str(lineNum)+',\n')
    else:
        print('Error at "'+f.name+'" line '+str(lineNum)+':\n   '+line+'\nCommand "'+line.split(' ')[0]+'" not identified')
        exit()
