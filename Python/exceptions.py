

def funct():
    try:
        x= int(input("Please enter a number: ") )
    except ValueError:
        print ('Invalid number, try again')


funct()
