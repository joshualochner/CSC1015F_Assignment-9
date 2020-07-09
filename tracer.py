import re
print('***** Program Trace Utility *****')
fileName = input('Enter the name of the program file: ')

try:
    r = open(fileName,'r')
    linesToRead = []
    linesToWrite = []
    for line in r:
        linesToRead.append(line.strip('\n'))

    containsDebug = False
    for i in linesToRead:
        if("""DEBUG""" in i):
            containsDebug = True
            break

    if(containsDebug):
        for x in linesToRead:
            if("""DEBUG""" not in x):
                linesToWrite.append(x)
            
        print('Program contains trace statements')
        
    else:
        linesToWrite.append('"""DEBUG"""')
        
        for x in linesToRead:
            linesToWrite.append(x)
            if(x[0:3]=='def'):
                functionDefinition = re.split(' |\(',x)
                linesToWrite.append('    """DEBUG""";print(\''+functionDefinition[1]+'\')')
    r.close() 
    
    w = open(fileName,'w')
    w.write('\n'.join(linesToWrite))
    w.close()
    if(containsDebug):
        print('Removing...Done')
    else:
        print('Inserting...Done')
    
except:
    
    pass
