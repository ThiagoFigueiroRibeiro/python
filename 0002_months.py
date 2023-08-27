# Very simple program where you input the number of the
# month you want and it returns which month it is.
# For instance, you put '7' and it returns 'The month 7 is July'
# It handles ValueError exceptions if you try being funny with your inputs. 

def month():
    months = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    try:
        x = int(input('Type the number of the month (1 to 12) you want: '))
        if x >= 1 and x <= 12:
            print('The month ' + str(x) + ' is ' + str(months[x-1]))
        else:
            print("Please put an integer number between 1 and 12.  Try again.")
            month ()
            
    except ValueError:
        print("That was an invalid number.  Try again.")
        month ()

month()