import time

values = [i for i in range(1000) if i%2 == 0]
print(values)

def generateData(values):
    for x in values:
        yield x**2

for val in values:
    print (val)
    time.sleep(0.5)

##def fakeGenerator(n):
##    for i in range(n):
##        
