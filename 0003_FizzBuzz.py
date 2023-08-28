# One solution for the Fizz Buzz Problem.
# If you try anything other than integers as inputs,
# it raises exceptions and finish the program. 

def fizzbuzz():
    
    def exceptions():
        print ('Please, put an integer number. Start over!')
        quit()  #forces the program to end if the input isn't an integer. 

    print('=== Fizz Buzz! ===')
    
    try:
        fizz = int(input('Choose your Fizz: '))
    except:
        exceptions()

    try:
        buzz = int(input('Choose your Buzz: '))
    except:
        exceptions()
        
    try:
        counter = int(input('Should we test fizz buzz until what number? '))
    except:
        exceptions()
    
    
    i = 1
    while i <= counter:
        if i%fizz==0 and i%buzz== 0:
            print(str(i) + ' = FizzBuzz')
        elif i%fizz==0:
            print(str(i) + ' = Fizz')
        elif i%buzz==0:
            print(str(i) + ' = Buzz')        
        i = i+1
        
fizzbuzz()
