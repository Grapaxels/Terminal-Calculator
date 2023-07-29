print('-------------------------------')
print('     --------oo---------       ')
print('----------calculator-----------')
print('     --------oo---------       ')
print('-------------------------------')
print('-----Designed by Grapaxels-----')
print('     --------oo---------       ')
print('-------------------------------')

sign=input('Enter the Code eg : ( + , - , * , / , % , sqrt , date) : ')

if sign==("+"):
    a=input("Enter your first number : ")
    b=input("Enter your second number : ")
    sum=int(a)+int(b)
    print('Answer is:',sum)

elif sign==("-"):
    a=input("Enter your first number : ")
    b=input("Enter your second number : ")
    sum=int(a)-int(b)
    print('Answer is:',sum)

elif sign==("*"):
    a=input("Enter your first number : ")
    b=input("Enter your second number : ")
    sum=int(a)*int(b)
    print('Answer is:',sum)

elif sign==("/"):
    a=input("Enter your first number : ")
    b=input("Enter your second number : ")
    sum=int(a)/int(b)
    print('Answer is:',sum)

elif sign==("%"):
    a=input("Enter your first number : ")
    b=input("Enter your second number : ")
    sum=int(a)%int(b)
    print('Answer is:',sum)

elif sign==("sqrt"):
    a=input("Enter your number : ")
    sum=int(a)*int(a)
    print('Answer is:',sum)

elif sign==("date"):
    days=input('Enter the month : ( 1 , 2 , 2Leap , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 : ) ')

    if days==('1'):
        print('Month is : January')
        a=input("Enter today's Date : ")
        if a<=('31'):
           sum=int('31')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')     

    elif days==('2'):
        print('Month is : February')
        a=input("Enter today's Date : ")
        if a<=('28'):
           sum=int('28')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists in This Month !!') 

    elif days==('2Leap'):
        print('Month is : February ( Leap Year )')
        a=input("Enter today's Date : ")
        if a<=('29'):        
           sum=int('29')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists in This Month !!')    

    elif days==('3'):
        print('Month is : March')
        a=input("Enter today's Date : ")
        if a<=('31'):
           sum=int('31')-int(a)
           print('Pending days in this month:',sum) 
        else:
           print('Are you mad! This Date Never Exists !! ')    

    elif days==('4'):
        print('Month is : April')
        a=input("Enter today's Date : ")
        if a<=('30'):
           sum=int('30')-int(a)
           print('Pending days in this month:',sum) 
        else:
           print('Are you mad! This Date Never Exists !! ')       
    
    elif days==('5'):
        print('Month is : May')
        a=input("Enter today's Date : ")
        if a<=('31'):
           sum=int('31')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')    

    elif days==('6'):
        print('Month is : June')
        a=input("Enter today's Date : ")
        if a<=('30'):
           sum=int('30')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')      

    elif days==('7'):
        print('Month is : July')
        a=input("Enter today's Date : ")
        if a<=('31'):
           sum=int('31')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')      

    elif days==('8'):
        print('Month is : August')
        a=input("Enter today's Date : ")
        if a<=('31'):
           sum=int('31')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')      

    elif days==('9'):
        print('Month is : September')
        a=input("Enter today's Date : ")
        if a<=('30'):
           sum=int('30')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')      

    elif days==('10'):
        print('Month is : October')
        a=input("Enter today's Date : ")
        if a<=('31'):
           sum=int('31')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')    

    elif days==('11'):
        print('Month is : November')
        a=input("Enter today's Date : ")
        if a<=('30'):
           sum=int('30')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')      

    elif days==('12'):
        print('Month is : December')
        a=input("Enter today's Date : ")
        if a<=('31'):
           sum=int('31')-int(a)
           print('Pending days in this month:',sum)
        else:
           print('Are you mad! This Date Never Exists !! ')      

else:
    print('Command not found')
print('Follow Grapaxels For More')
x=input('Press Enter to exit')  
print('Exited Successfully')
