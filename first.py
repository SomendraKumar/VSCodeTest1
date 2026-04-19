# /* 1. install python on OS
# //2. install VS Code on OS
# //3. in VS Code terminal install
# // 1. pip install flask
# //2. pip install pyjokes

# print("welcome")
# print("hello ")


# import pyjokes
# joke=pyjokes.get_joke()
# print(joke)


# import math
# print(math.sqrt(67))
# print(math.factorial(8))


# import os
# import random
# print(random.randint(1,8))
# print(os.listdir())



# num=int(input("pls enter a num for the table"))
# for i in range(1,10):
#     print(f"table of {num} X {i} == {num*i}")




# #var/identifiers
# a=90
# b=90.76
# x="som"
# print("int var here == ",a)
# print("float var here == ",b)
# print("str var here == ",x)




# # how do we take input from  the user in python
# var1=int(input("pls enter a int value for the use"))
# print("ur entered value == ",var1)




# # how to perform opeartion/s using different different opeartors
# a=int(input("pls enter 1st val for the calculation\n"))
# b=int(input("pls enter 2nd val for the calculation\n"))
# print("hey ur sum == ",(a+b))
# print("hey ur mul == ",(a*b))
# print("hey ur sub == ",(a-b))
# print("hey ur div == ",(a/b))
# print("hey ur mod == ",(a%b))





# Variables and Data Types Examples
#a = 31
# print(type(a))     # class <int>
# b = "31"
# print(type(b))    # class <str>
# c=90.8
# print(type(c))




# #Type conversion in python
# a=str(31)     # => "31"   (integer to string conversion)
# print("updated value of a == ",a)
# print("updated type of a == ",type(a))
# b=int("32")   # => 32     (string to integer conversion)
# print("updated value of b == ",b)
# print("updated type of b == ",type(b))
# c=float(32)   # => 32.0   (integer to float conversion)
# print("updated value of c == ",c)
# print("updated type of c == ",type(c))


# External Module Example
# #externa module
# import pyjokes
# joke=pyjokes.get_joke()
# print(joke)





# Inbuild Module Example
# #internal modules
# import random
# a=random.randrange(1,9)
# print("rand num bn 1 to 9 == ", a )

# import os
# import random
# print(random.randint(1,8))
# print(os.listdir())



# Inbuild Module Example
# import math
# print(math.sqrt(67))
# print(math.factorial(8))



#Variables and Data Types
# a = 31
# print(type(a))     # class <int>
# b = "31"
# print(type(b))     # class <str>

# a=str(31)     # => "31"   (integer to string conversion)
# print(a)
# print(type(a))
# b=int("32")   # => 32     (string to integer conversion)
# print(b)
# print(type(b))
# c=float(32)   # => 32.0   (integer to float conversion)
# print(c)
# print(type(c))


#





# Taking Input from the user
# num1=int(input("pls enter a num1 "))
# num2=int(input("pls enter a num2 "))
# print("sum == ",(num1+num2))
# print("mul == ",(num1*num2))






# #operators
# #exponential operator
# num=5
# x=3
# print("result of multiply == ",(num*x))
# print("result of exponential == ",(num**x))

# #floor operator
# a=89
# b=9
# #Div
# print("result of div == ",(a/b))
# #floor
# print("result of floor == ",(a//b))



# #different ways to print string
# print("hello world")
# print('hello world of python')
# print(""" hello my friend """)
# print('''hello friends see magic''')


# print("line1 jbbjn       2. line2jnhjkjk nnjn      3. kjvkjd nnvknf      4. nkvddmmmjv")

# print('line1 jbbjn       2. line2jnhjkjk nnjn       3. kjvkjd nnvknf      4. nkvddmmmjv')

# print("""flush=line1 jbbjn
#       2. line2jnhjkjk nnjn
#       3. kjvkjd nnvknf
#       4. nkvddmmmjv""")

# print('''line1 jbbjn
#       2. line2jnhjkjk nnjn
#       3. kjvkjd nnvknf
#       4. nkvddmmmjv''')



# different ways to print string
# print("hey I am line one       hey i am line 2       hey i am line 3       hey i am line4")
# print('hey I am line one       hey i am line 2       hey i am line 3       hey i am line4')
# print("""hey I am line one
#       hey i am line 2
#       hey i am line 3
#       hey i am line4""")
# print('''hey I am line one
#       hey i am line 2
#       hey i am line 3
#       hey i am line4''')


# #String Functions
# text = "hello ha fga jgghhjhjh world bjh hjh"

# print(len(text))                        # 11
# print(text.upper())                     # "HELLO WORLD"
# print(text.lower())                     # "hello world"
# print(text.capitalize())                # "Hello world"
# print(text.title())                     # "Hello World"
# print(text.count("a"))                  # 3
# print(text.find("world"))               # 6
# print(text.replace("world", "somendra"))  # "hello python"
# print(text.endswith("hjh"))           # True
# print(text.startswith("hello"))         # True
# print(text.strip())                     # "hello world" (removes whitespace)
# print(text.split(" "))                  # ['hello', 'world']


# #escape sequenvce character
# # Newline
# print("Hello\nWorld")
# # Tab
# print("Hello\tWorld")
# # Quotes inside string
# print("He said \"Hi\"")
# print('It\'s Python')
# # Backslash
# print("Path: C:\\Users\\Documents")
# # Using raw strings (no escape)
# print(r"C:\Users\Documents")




# # String Concatenation and Repetition Copy
# # Concatenation with +
# greeting = "Hellohjmnjk" + "     " + "World"
# print(greeting)
# # Repetition with *
# line = "som \n" * 70
# print(line)
# # f-strings (formatted strings)
# name = "Som"
# age = 20
# print(f"My name is {name} and I am {age} years old.")






# # String Slicing and Indexing 
# name = "peter"
# print(name[0:3])    # "pet" - index 0, 1, 2
# print(name[1:3])    # "et" - index 1, 2
# print(name[-3:])    # "ter" - last 3 characters
# print(name[:-1])    # "pete" - all except last
# print(name[::-1])   # "retep" - reversed string
# # Negative indexing
# print(name[-1])     # "r" - last character
# print(name[-5])     # "p" - first character (same as 0)



#Slicing with Skip Value

# word = "amazing"
# print(word[1:6:2])   # "mzn" - every 2nd char
# print(word[::2])     # "aaig" - every 2nd from start
# print(word[::-1])    # "gnizama" - reversed
# print(word[0:7])     # "amazing" - full string
# print(word[:])       # "amazing" - copy of string




# #conditional expression
# # speed=int(input("pls enter ur speed for test and instruction for the best"))
# # if(speed>180):
# #     print("hey u r in danger")
# # elif((speed>100)and(speed<180)):
# #     print("hey drive safely")
# # elif((speed<100)and(speed>40)):
# #     print("hey u are driving safely")
    
 
# num1=float(input("pls enter a num1 for clculation"))
# num2=float(input("pls enter a num2 for clculation"))
# choice=input("pls enter a choice for calculation of operator +,-,*,%,/,>,< ")
# if choice=='+':
#     print(num1+num2)
# elif(choice=='-'):
#     print(num1-num2)
# elif(choice=='*'):
#     print(num1*num2)
# elif(choice=='%'):
#     print(num1%num2)
# elif(choice=='/'):
#     print(num1/num2)
# elif(choice=='>'):
#     print(num1>num2)
# elif(choice=='<'):
#     print(num1<num2)
# else:
#     print("wrong input, read the msg, Try Again")
    
    

# x=input(" pls enter an I/P1 to test logical operation")#x
# y=input(" pls enter an I/P2 to test logical operation")#y
# z=input(" pls enter an I/P3 to test logical operation")#z
# p=input(" pls enter an I/P4 to test logical operation")#p
# print("ur result == ",((x and y)or(z and p)and((not p)or(not x)) ))



#loops in python

# for i in range(1, 6):
#     input1=input("pls enter ur name\n")
#     print(f" hello {i}. \"{input1}\" thank you ")
    
    
    

# #loops in python
# input1=int(input("pls enter a number to test the loop in python\n"))
# for som in range(1,11):
#     print(f"ur input is in loop {som}. \"{input1}\" thank you")


#loops in python

# for index in range(1,5):
#     input1=input("pls enter ur name to test the loop in python\n")
#     print(f"ur input is in loop {index}. \"{input1}\" thank you")



# for index in range(1,4):
#     name=input("pls enter ur name to test the loop in python\n")
#     age=int(input("pls enter ur age to test the loop in python\n"))
#     marks=float(input("pls enter ur marks to test the loop in python\n"))
#     print(f" {index}. Name == \"{name}\" Age == {age}  Marks == {marks} thank you")






# i = 0
# while i < 5:        # Print "Som" 5 times!
#     print("Som")
#     i = i + 1

# i = 0
# while i < 4:        # Print "Som" 5 times!
#     name=input("pls enter ur name to test the loop in python\n")
#     age=int(input("pls enter ur age to test the loop in python\n"))
#     marks=float(input("pls enter ur marks to test the loop in python\n"))
#     print(f" {i}. Name == \"{name}\" Age == {age}  Marks == {marks} thank you")
#     i = i + 1






# i = 0
# while i < 5:
#     input1=input("pls enter ur a num to test the loop in python\n")      
#     print(f"ur input is in loop {i}. \"{input1}\" thank you")
#     i = i + 1



# i = 0
# while i < 5:
#     input1=input("pls enter ur name to test the loop in python\n")      
#     print(f"ur input is in loop {i}. \"{input1}\" thank you")
#     i = i + 1


# input1=int(input("pls enter a num for even num test"))
# for i in range(1,input1):
#     if(i%2):
#         continue
#     print(f" {i}.  thank you")


# input1=int(input("pls enter a num for Odd num test"))
# for i in range(1,input1):
#     if(i%2==0):
#         continue
#     print(f" {i}.  thank you")
    


#************************

# i = 0
# input1=int(input("pls enter a num to test Odd number\n"))
# while i < input1:
#     if(i%2==0):
#         print(f"{i}. thank you")
#     i = i + 1


# i = 0
# input1=int(input("pls enter a num to test Even number\n"))
# while i < input1:
#     if(i%2):
#         print(f"{i}. thank you")
#     i = i + 1




# #Factorial number
# num1=int(input("pls enter a num"))
# result=1
# for i in range(1,num1+1):
#     result*=i    
# print(f"factorial of {num1}=={result}")





# #Fibonicci Series
# num1=int(input("pls enter a num"))
# a, b = 0, 1
# for _ in range(num1):
#     print(a)
#     a, b = b, a + b  # This updates both at the same time!



#Armstrong number()
"""
    Common Examples to Test
3-digit: 153, 370, 371, 407

4-digit: 1634, 8208, 9474

Single digits: 0 through 9 are all technically Armstrong numbers!
   """
# # 1. Get input from user
# num1 = int(input("Enter a number: "))

# # 2. Find the number of digits (the power)
# # We convert to string to easily count characters
# order = len(str(num1))

# # 3. Initialize sum and a temporary variable
# sum_of_powers = 0
# temp = num1

# # 4. Logic to calculate the sum of powers
# while temp > 0:
#     digit = temp % 10          # Get the last digit
#     sum_of_powers += digit ** order  # Raise to power and add to sum
#     temp //= 10                # Remove the last digit

# # 5. Display the result
# if num1 == sum_of_powers:
#     print(f"{num1} is an Armstrong number!")
# else:
#     print(f"{num1} is NOT an Armstrong number.")
    
    


#Palindrome number(121)

# # 1. Get input
# num1 = int(input("Enter a number: "))
# temp = num1
# reverse_num = 0
# # 2. Reverse the number mathematically
# while temp > 0:
#     digit = temp % 10             # Get the last digit
#     reverse_num = (reverse_num * 10) + digit  # Build the reversed number
#     temp //= 10                   # Remove the last digit
# # 3. Compare the original with the reversed
# if num1 == reverse_num:
#     print(f"{num1} is a palindrome!")
# else:
#     print(f"{num1} is NOT a palindrome.")
    
    
    
    
    
    
# # 2nd way/shortcut string way, Palindrome Number check
# #In Python, you can convert the number to a string and use slicing [::-1] to reverse it instantly.
# num = input("Enter a number: ")

# # Check if the string is equal to its reverse
# if num == num[::-1]:
#     print(f"{num} is a palindrome!")
# else:
#     print(f"{num} is NOT a palindrome.")




# #Function in python, without argument/parameter/s
# def sum():
#     print("hey i am print function I can be called n-number of times")

# sum()
# sum()





# #Function in python, with argument/parameter/s
# def sum(a,b):
#     print("hey i am print function I can be called n-number of times")
#     print(f"sum == {a+b}")

# sum(8,9)
# sum(6,4)




# #Function in python, with argument/parameter/s
# #take input from the user
# def sum(a,b):
#     print("hey i am print function I can be called n-number of times")
#     print(f"sum == {a+b}")

# num1=int(input("pls enter a num1"))
# num2=int(input("pls enter a num2"))
# sum(num1,num2)








#Function in python, with argument/parameter/s
#take n number of input from the user

# def sum(a,b):
#     print(f"{i}. sum == {a+b}")

# numIP=int(input("pls enter a number to run the loop "))
# for i in range(1,numIP+1):
#     num1=int(input("pls enter a num1\n"))
#     num2=int(input("pls enter a num2\n"))
#     sum(num1,num2)


# #function in python
# def sum():#def of a fun/sum
#     print("hey i am a sum fun")
# sum()#calling of a fun
# sum()
# sum()    

    
# #function in python
# def sum():#def of a fun/sum
#     print("hey i am a sum fun")
# def div():#def of a fun/sum
#     print("hey i am a div fun")
# def mul():#def of a fun/sum
#     print("hey i am a mul fun")
# div()
# mul()
# sum()#calling of a fun
  

# #function in python
# def sum():#def of a fun/sum
#     print("hey i am a sum fun, I can do sum")
#     print("pls enter 2-nums for sum calculation")
#     num1=int(input("pls enter a num1\n"))
#     num2=int(input("pls enter a num2\n"))
#     print(f" hello, sum of num1 and num2 == {num1+num2}")
    
# sum()




# #function in python
# def sum():#def of a fun/sum
#     print("hey i am a sum fun, I can do sum")
#     print("pls enter 2-nums for sum calculation")
#     num1=int(input("pls enter a num1\n"))
#     num2=int(input("pls enter a num2\n"))
#     print(f" hello{i}., sum of num1 and num2 == {num1+num2}")
# for i in range(1,3):
#     sum()


# #function in python
# def sum():#def of a fun/sum
#     print("hey i am a sum fun, I can do sum")
#     print("pls enter 2-nums for sum calculation")
#     num1=int(input("pls enter a num1\n"))
#     num2=int(input("pls enter a num2\n"))
#     print(f" hello{i}., sum of num1 and num2 == {num1+num2}")
# i=1
# while i<3:
#     sum()
#     i+=1



# #function in python
# def sum():#def of a fun/sum
#     print("hey i am a sum fun, I can do sum")
#     print("pls enter 2-nums for sum calculation")
#     num1=int(input("pls enter a num1\n"))
#     num2=int(input("pls enter a num2\n"))
#     print(f" hello{i}., sum of num1 and num2 == {num1+num2}")
# def mul():#def of a fun/sum
#     print("hey i am a Mul fun, I can do sum")
#     print("pls enter 2-nums for Mul calculation")
#     num1=int(input("pls enter a num1\n"))
#     num2=int(input("pls enter a num2\n"))
#     print(f" hello, Mul of num1 and num2 == {num1*num2}")
# def div():#def of a fun/sum
#     print("hey i am a div fun, I can do sum")
#     print("pls enter 2-nums for div calculation")
#     num1=int(input("pls enter a num1\n"))
#     num2=int(input("pls enter a num2\n"))
#     print(f" hello, div of num1 and num2 == {num1/num2}")
# choice=input("pls enter ur choice from (1. Div 2. Mul 3. Add)")
# if(choice=="div"):
#     div()
# elif(choice=="add"):
#     sum()
# elif(choice=="mul"):
#     mul()
# else:
#     print("entered choice is wrong try again")




    
# # WAP in python to test factorial number using a fun
# def fact1():
#     num1=int(input("pls enter a num"))
#     result=1
#     for i in range(1,num1+1):
#         result*=i
#     print(f"factorial of {num1}=={result}")
# fact1()    


# #function in python
# def sum():
#     print("hey i am inside the function of python")
# sum()
# sum()
# sum()


# #function in python
# def sum():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for sum"))
#     num2=int(input("pls enter a num2 for sum"))
#     print(f"hello ur sum == {num1+num2}, thank you")
# sum()


# #function in python
# def sum():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for sum"))
#     num2=int(input("pls enter a num2 for sum"))
#     print(f"hello {i}. ur sum == {num1+num2}, thank you")
# num11=int(input("pls enter a num for the loop count"))
# for i in range(1,num11):
#     sum()

# #function in python
# def sum():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for sum"))
#     num2=int(input("pls enter a num2 for sum"))
#     print(f"hello {i}. ur sum == {num1+num2}, thank you")
# num11=int(input("pls enter a num for the loop count"))
# i=1
# while i<num11:
#     sum()
#     i+=1



# #function in python
# def sum():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for sum"))
#     num2=int(input("pls enter a num2 for sum"))
#     print(f"hello ur sum == {num1+num2}, thank you")
# def mul():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for mul"))
#     num2=int(input("pls enter a num2 for mul"))
#     print(f"hello ur mul == {num1*num2}, thank you")
# def div():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for div"))
#     num2=int(input("pls enter a num2 for div"))
#     print(f"hello ur sum == {num1/num2}, thank you")
# div()
# mul()
# sum()




# #function in python
# def sum():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for sum\n"))
#     num2=int(input("pls enter a num2 for sum\n"))
#     print(f"hello ur sum == {num1+num2}, thank you")
# def mul():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for sum\n"))
#     num2=int(input("pls enter a num2 for sum\n"))
#     print(f"hello ur mul == {num1*num2}, thank you")
# def div():
#     print("hey i am inside the function of python")
#     num1=int(input("pls enter a num1 for sum\n"))
#     num2=int(input("pls enter a num2 for sum\n"))
#     print(f"hello ur sum == {num1/num2}, thank you")
# choice1=input("pls enter ur choice 1. div 2. mul 3. sum for the calculation\n")
# if(choice1=="div"):
#     div()
# elif(choice1=="mul"):
#     mul()
# elif(choice1=="sum"):
#     sum()
# else:
#     print("u have enterede wrong choice try again:)")
    
    
    
    


# # WAP in python to test factorial number using a function
# def fact1():
#     num1=int(input("pls enter a num"))
#     result=1
#     for i in range(1,num1+1):
#         result*=i
#     print(f"factorial of {num1}=={result}")
# fact1()   
 
 
  
    
# #fibonicci Series using Function
# def fibbo1():
#     num1=int(input("pls enter a num"))
#     a, b = 0, 1
#     for _ in range(num1):
#         print(a)
#         a, b = b, a + b  # This updates both at the same time!
# fibbo1()




#Armstron Number Using Function

"""
    Common Examples to Test
3-digit: 153, 370, 371, 407


4-digit: 1634, 8208, 9474


Single digits: 0 through 9 are all technically Armstrong numbers!
   """
# def armtr1():
#     num1 = int(input("Enter a number: "))
#     order = len(str(num1))
#     sum_of_powers = 0
#     temp = num1
#     while temp > 0:
#         digit = temp % 10          # Get the last digit
#         sum_of_powers += digit ** order  # Raise to power and add to sum
#         temp //= 10                # Remove the last digit
#     if num1 == sum_of_powers:
#         print(f"{num1} is an Armstrong number!")
#     else:
#         print(f"{num1} is NOT an Armstrong number.")
# armtr1()



# # Palindrome Number uisng function
# def palind1():
#     num = input("Enter a number: ")
#     if num == num[::-1]:
#         print(f"{num} is a palindrome!")
#     else:
#         print(f"{num} is NOT a palindrome.")
# palind1()









# # final code for the choice of 1. Fact, 2. Febo, 3. Armstr, 4. Palin
# # functions using conditional expression to test the app for user choice
# def fact1():
#     num1=int(input("pls enter a num"))
#     result=1
#     for i in range(1,num1+1):
#         result*=i
#     print(f"factorial of {num1}=={result}")
    
# def febbo1():
#     num1=int(input("pls enter a num"))
#     a, b = 0, 1
#     for _ in range(num1):
#         print(a)
#         a, b = b, a + b  # This updates both at the same time!  
 
# def palind1():
#     num = input("Enter a number: ")
#     if num == num[::-1]:
#         print(f"{num} is a palindrome!")
#     else:
#         print(f"{num} is NOT a palindrome.") 
        
# def armtr1():
#     num1 = int(input("Enter a number: "))
#     order = len(str(num1))
#     sum_of_powers = 0
#     temp = num1
#     while temp > 0:
#         digit = temp % 10          # Get the last digit
#         sum_of_powers += digit ** order  # Raise to power and add to sum
#         temp //= 10                # Remove the last digit
#     if num1 == sum_of_powers:
#         print(f"{num1} is an Armstrong number!")
#     else:
#         print(f"{num1} is NOT an Armstrong number.")
        
# choice=input("pls enter ur choice from (1. Fact, 2. Febo, 3. Armstr, 4. Palin)\n")
# if(choice=="Fact" or choice=='1'):
#     fact1()
# elif(choice=="Febo" or choice=='2'):
#     febbo1()
# elif(choice=="Armstr" or choice=='3'):
#     palind1()
# elif(choice=="Palin" or choice=='4'):
#     armtr1()   
# else:
#     print("entered choice is wrong try again")
 
 
 
 
 

# final code for the choice of 1. Fact, 2. Febo, 3. Armstr, 4. Palin
# functions using conditional expression to test the app for user choice
# choice as 1/2/3/4 or 1. Fact, 2. Febo, 3. Armstr, 4. Palin
# def fact1():
#     num1=int(input("pls enter a num"))
#     result=1
#     for i in range(1,num1+1):
#         result*=i
#     print(f"factorial of {num1}=={result}")
    
# def febbo1():
#     num1=int(input("pls enter a num"))
#     a, b = 0, 1
#     for _ in range(num1):
#         print(a)
#         a, b = b, a + b  # This updates both at the same time!  
 
# def palind1():
#     num = input("Enter a number: ")
#     if num == num[::-1]:
#         print(f"{num} is a palindrome!")
#     else:
#         print(f"{num} is NOT a palindrome.") 
        
# def armtr1():
#     num1 = int(input("Enter a number: "))
#     order = len(str(num1))
#     sum_of_powers = 0
#     temp = num1
#     while temp > 0:
#         digit = temp % 10          # Get the last digit
#         sum_of_powers += digit ** order  # Raise to power and add to sum
#         temp //= 10                # Remove the last digit
#     if num1 == sum_of_powers:
#         print(f"{num1} is an Armstrong number!")
#     else:
#         print(f"{num1} is NOT an Armstrong number.")
        
# choice=input("pls enter ur choice from (1. Fact, 2. Febo, 3. Armstr, 4. Palin)\n")
# if(choice=="Fact" or choice=='1'):
#     fact1()
# elif(choice=="Febo" or choice=='2'):
#     febbo1()
# elif(choice=="Armstr" or choice=='3'):
#     palind1()
# elif(choice=="Palin" or choice=='4'):
#     armtr1()   
# else:
#     print("entered choice is wrong try again")
 
 
 
 
 
 
#  # functions with return type and parameters/arguments
 
# def sum1(a,b):
#     return (a+b)
# num1=int(input("pls enter a num1 to do calculation\n"))
# num2=int(input("pls enter a num2 to do calculation\n"))
# print(f" sum of {num1} and {num2} == {sum1(num1,num2)}")



# # recursive function

#function with return type and parameterized/argumented function
# def sum1(a,b):# argumented funtion, u can have n-num of arguments in side the function as parameters
#     return (a+b)
# num1=int(input("pls enter a num1  for the calculation\n"))
# num2=int(input("pls enter a num2  for the calculation\n"))
# print(f"sum of {num1} and {num2} == {sum1(num1,num2)} ")




# def sum1(a,b):# argumented funtion, u can have n-num of arguments in side the function as parameters
#     return (a+b)
# def mul1(a,b):# argumented funtion, u can have n-num of arguments in side the function as parameters
#     return (a*b)
# def mod(a,b):# argumented funtion, u can have n-num of arguments in side the function as parameters
#     return (a%b)
# num1=int(input("pls enter a num1  for the calculation\n"))
# num2=int(input("pls enter a num2  for the calculation\n"))
# print(f"sum of {num1} and {num2} == {sum1(num1,num2)} ")
# print(f"mul of {num1} and {num2} == {mul1(num1,num2)} ")
# print(f"mod of {num1} and {num2} == {mod(num1,num2)} ")




#Recursive function to test Factorial number , input from the user

# def factorial(n):
#     if n == 0 or n == 1:    # base condition
#         return 1
#     else:
#         return n * factorial(n - 1)  # function calling itself
# num1=int(input("pls enter anum for factorial number\n"))
# print(f" factorial of {num1} == {factorial(num1)}")










#Exception Handling in Python
# try:
#     result = 10 / 0
# # except ZeroDivisionError:
# except ZeroDivisionError:    
#     print("Cannot divide by zero!")



#user input
# try:
#     numer1=int(input("pls enter a num for numerator1\n"))
#     Dnumer1=int(input("pls enter a num for Dnumer1\n"))
#     result = numer1 / Dnumer1
#     print(f"hey ur result == {result}")
# # except ZeroDivisionError:
# except ZeroDivisionError:    
#     print("Cannot divide by zero!")





#exception inside a function
# def excepTest1():    
#     try:
#         numer1=int(input("pls enter a num for numerator1\n"))
#         Dnumer1=int(input("pls enter a num for Dnumer1\n"))
#         result = numer1 / Dnumer1
#         print(f"hey ur result == {result}")
#     # except ZeroDivisionError:
#     except ZeroDivisionError:    
#         print("Cannot divide by zero!")
# excepTest1()



# def excepTest1(a,b):    
#     try:        
#         result = a / b
#         return result
#     # except ZeroDivisionError:
#     except ZeroDivisionError:    
#         print("Cannot divide by zero!")
# numer1=int(input("pls enter a num for numerator1\n"))
# Dnumer1=int(input("pls enter a num for Dnumer1\n"))
# print(f"hey ur result == {excepTest1(numer1,Dnumer1)}")



# #Exception Handling in Python, from user Input
# try:
#     numer1=int(input("pls enter a number for numerator\n"))
#     Dnumer1=int(input("pls enter a number for Dnumer1\n"))
#     result = numer1 / Dnumer1
#     print(f"result == {result} ")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")





# def tesEcxep1():
#     #Exception Handling in Python, from user Input
#     try:
#         numer1=int(input("pls enter a number for numerator\n"))
#         Dnumer1=int(input("pls enter a number for Dnumer1\n"))
#         result = numer1 / Dnumer1
#         print(f"result == {result} ")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
# tesEcxep1()







# def tesEcxep1(a,b):
#     #Exception Handling in Python, from user Input
#     try:       
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
# numer1=int(input("pls enter a number for numerator\n"))
# Dnumer1=int(input("pls enter a number for Dnumer1\n"))
# print(f"result == {tesEcxep1(numer1,Dnumer1)} ")






# Handling a ZeroDivisionError
# try:
#     numerator = int(input("pls enter a num for numerator"))
#     denominator = int(input("pls enter a num for denominator"))
#     result = numerator / denominator
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero!")

# print("Program continues normally...")




#Catching Multiple Exceptions
# Handling different exception types
# def divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         print("Error: Division by zero!")
#     except TypeError:
#         print("Error: Invalid data types for division!")
# # Test cases
# print("Test 1:", divide(10, 2))
# print("Test 2:", divide(10, 0))
# print("Test 3:", divide("10", 2))



# def divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         print("Error: Division by zero!")
#     except TypeError:
#         print("Error: Invalid data types for division!")
# # Test cases
# num1=int(input("pls enter a num1\n"))
# num2=int(input("pls enter a num2\n"))
# print("Test 1:", divide(num1, num2))
# num1=input("pls enter a num1\n")
# num2=input("pls enter a num2\n")
# print("Test 1:", divide(num1, num2))





# def divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         print("Error: Division by zero!")
#     except TypeError:
#         print("Error: Invalid data types for division!")

# # Test cases
# num1=int(input("pls enter a num1\n"))
# num2=int(input("pls enter a num2\n"))
# print("Test 1:", divide(num1, num2))
# num1=int(input("pls enter a num1\n"))
# num2=int(input("pls enter a num2\n"))
# print("Test 2:", divide(num1, num2))
# str1=input("pls enter a str\n")
# num2=int(input("pls enter a num2\n"))
# print("Test 3:", divide(str1, num2))









#using function, understand, Try, Except, Else and Finally 
# def read_number():
#     try:
#         num = int(input("Enter a number: "))  # May raise ValueError
#         result = 100 / num                     # May raise ZeroDivisionError
#     except ValueError:
#         print("That's not a valid number!")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
#     else:
#         print(f"100 / {num} = {result}")
#     finally:
#         print("--- Operation Complete ---")
# read_number()



# def read_number(x):
#     try:
#         result = 100 / x                     # May raise ZeroDivisionError
#         return result
#     except ValueError:
#         print("That's not a valid number!")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
#     else:
#         print(f"100 / {num} = {result}")
#     finally:
#         print("--- Operation Complete ---")
# num = int(input("Enter a number: "))  # May raise ValueError
# print(f"result of fun call == {read_number(num)} ")





# #without exception same above expl
# def read_number():   
#         num = int(input("Enter a number: "))  # May raise ValueError
#         result = 100 / num                     # May raise ZeroDivisionError    
#         return result
# print(f" result of ur input == {read_number()}")





# 2nd way
# #without exception same above expl
# def read_number():   
#         num = int(input("Enter a number: "))  # May raise ValueError
#         result = 100 / num                     # May raise ZeroDivisionError    
#         print(f" result of ur input == {result}")
# read_number()





# #The raise Statement
# def set_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative!")
#     if age > 150:
#         raise ValueError("Age seems unrealistic!")
#     print(f"Age set to {age}")

# try:
#     num1=int(input("pls enter an input\n"))
#     set_age(num1)
# except ValueError as e11:
#     print(f"Error: {e11}")




# #Guess Number Test/Game
# import random
# def guess_the_number():
#     # The computer picks a random number between 1 and 100
#     secret_number = random.randint(1, 100)
#     attempts = 0    
#     print("I'm thinking of a number between 1 and 100.")
#     while True:
#         try:
#             # Get the user's guess
#             guess = int(input("Take a guess: "))
#             attempts += 1

#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Bullseye! You found the number in {attempts} attempts.")
#                 break 
#         except ValueError:
#             print("Please enter a valid whole number.")

# guess_the_number()

###############################

#Module-2

#List, Tuples, Sets & Dictionary

# Lists can store mixed data types
# friends = ["apple", "akash", "rohan", 7, False]
# print(friends)
# print(type(friends))

# # # Indexing
# fruits = ["apple", "banana", "cherry", "date"]
# print(fruits[0])      # "apple"
# print(fruits[-1])     # "date"
# print(fruits[1:3])    # ["banana", "cherry"]
# print(len(fruits))    # 4
# print(type(fruits))






#expl-2, List functions, done
# numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# print(f"unsorted data is here: {numbers}")
# numbers.sort()
# print(f"sorted data is here: {numbers}")

# # sort() - sorts in place
# numbers.sort()
# print("Sorted List:", numbers)

# reverse() - reverses in place
# print(f"not reverse data is here: {numbers}")
# numbers.reverse()
# print("Reversed:", numbers)

# append() - add at end
# print(f"before append data is here: {numbers}")
# numbers.append(7)
# print("After append(7):", numbers)

# # insert() - add at specific index
# print(f"before insert fun data is here: {numbers}")
# numbers.insert(0, 100)
# print("After insert(0, 100):", numbers)

# pop() - remove by index, returns value
# print(f"before pop data is here: {numbers}")
# removed = numbers.pop(0)
# print(f"Popped: {removed}, List: {numbers}")

# remove() - remove first occurrence of value
# print(f"before remove fun data is here: {numbers}")
# numbers.remove(9)
# print("After remove(9):", numbers)










# # List Operations

# # List concatenation
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print("Concatenation:", c)

# # List repetition
# d = [23] * 5
# print("Repetition:", d)

# # Check membership
# print(3 in a)        # True
# print(10 in a)       # False

# # Nested lists
# matrix = [[1, 2], [3, 4], [5, 6]]
# print(matrix[1][0])  # 3
# matrix = [[1, 2,3], [3, 4,9], [5, 6,8]]
# print(matrix[2][1])  # 4/6/5/









# # taking input from user and fill the list
# fruits = []
# for i in range(5):    
#     f1 = input("Enter Fruit name: ")
#     fruits.append(f1)
#     print(fruits)



# range1=int(input("pls enter a range for the loop\n"))
# fruits = []
# for i in range(range1):    
#     f1 = input("Enter Fruit name: ")
#     fruits.append(f1)
#     print(fruits)




# def frutTest1():    
#     range1=int(input("pls enter a range for the loop\n"))
#     fruits = []
#     for i in range(range1):    
#         f1 = input("Enter Fruit name: ")
#         fruits.append(f1)
#         print(fruits)
# frutTest1()




# f2 = input("Enter Fruit name: ")
# fruits.append(f2)
# f3 = input("Enter Fruit name: ")
# fruits.append(f3)
# f4 = input("Enter Fruit name: ")
# fruits.append(f4)
# f5 = input("Enter Fruit name: ")
# fruits.append(f5)
# f6 = input("Enter Fruit name: ")
# fruits.append(f6)
# f7 = input("Enter Fruit name: ")
# fruits.append(f7)
# print(fruits)



# taking input from user and fill the list
# using loops

# fruits = []
# for i in range(1,5):    
#     f1 = input("Enter Fruit name: ")
#     fruits.append(f1)
# print(fruits)



# #expl-2, range also from the user
# range1=int(input("pls enter a range for the loop\n"))
# fruits = []
# for i in range(range1):    
#     f1 = input("Enter Fruit name: ")
#     fruits.append(f1)
# print(fruits)




# range1=int(input("pls enter a range for the loop\n"))
# numbers1 = []
# for i in range(range1):    
#     f1 = input("Enter Fruit name: ")
#     numbers1.append(f1)
# print(numbers1)
# searchme1=int(input("pls enter a number to  for the search\n"))
# for i in range(range1):
#     if(searchme1==numbers1[i]):
#         print(f"I got the element at {i}th index {numbers1[i]} ")
#     else:
#         print("element not found in the list")  
    



# #expl-3, same but using function
# def listTest():    
#     range1=int(input("pls enter a range for the loop\n"))
#     fruits = []
#     for i in range(range1):    
#         f1 = input("Enter Fruit name: ")
#         fruits.append(f1)
#     print(fruits)
# listTest()





# # expl-4, same but using function, and conditional expression
# # search app
# def listTest():    
#     range1=int(input("pls enter a range for the loop\n"))
#     fruits = []
#     for i in range(range1):    
#         f1 = input("Enter Fruit name: ")
#         fruits.append(f1)
#         print(fruits)
#     #search fruit from the list
#     searchF=input("Enter Fruit name: ")
#     for i in range(range1):
#         if(searchF==fruits[i]):
#             print("yes, I got the fruit")
#             break
#         else:
#             print(f"ohhh, Fruit is not in the list's index {i}")
# listTest()






# Tuples**********
# a = ()        # empty tuple
# print("output : ",a)
# print(type(a))
# a = (1,)      # tuple with only one element (comma is needed!)
# print("output1 : ",a)
# print(type(a))
# a = (1, 7, 2) # tuple with more than one element
# print("output2 : ",a)
# print(type(a))
# a = (1, "eat", 2) # tuple with more than one element
# print("output2 : ",a)
# print(type(a))







#Dictionary
# a = {
#     "key": "value",
#     "peter": "code",
#     "marks": 100,
#     "list": [1, 2, 9]
# }
# print(a["peter"])    # Output: "value"
# print(a["marks"])   # Output: [1, 2, 9]





#Set
# s = set()     # empty set (NOT {}, that's a dict!)
# s.add(1)
# s.add(2)
# print(s)
# print(type(s))
# # or s = {1, 2}



# fruits=[]
# f2 = input("Enter Fruit name: ")
# fruits.append(f2)
# print(fruits)

# f3 = input("Enter Fruit name: ")
# fruits.append(f3)
# print(fruits)



# # list using loops
# fruits=[]
# for i in range(5):      
#     f2 = input("Enter Fruit name: ")
#     fruits.append(f2)
#     print(fruits)
    
    
    
    

# # list using loops, dynamic range
# range1=int(input("pls enter a num for the range1\n"))
# fruits=[]
# for i in range(range1):      
#     f2 = input("Enter Fruit name: ")
#     fruits.append(f2)
#     print(fruits)






# list using loops, dynamic range, with a function
# def testList1():    
#     range1=int(input("pls enter a num for the range1\n"))
#     fruits=[]
#     for i in range(range1):      
#         f2 = input("Enter Fruit name: ")
#         fruits.append(f2)
#         print(fruits)
# testList1()



# search app
# def testList1():    
#     range1=int(input("pls enter a num for the range1\n"))
#     number1=[]
#     for i in range(range1):      
#         f2 = input("Enter num in the list: ")
#         number1.append(f2)
#         print(number1) 
#     search1=int(input("pls enter a number to be searched\n"))   
#     for i in range(range1):      
#         if(search1==number1[i]):
#             print(f"hey I got the element at {i}th index")
#             break
#         else:
#             print(f"element not found at index{i}")
# testList1()




# #dictionary
# a = {
#     "key": "value",
#     "peter": "code",
#     "marks": 100,
#     "list": [1, 2, 9],
#     "name": "Som",
#     "usn": 123
# }
# print(a["key"])    # Output: "value"
# print(a["list"])   # Output: [1, 2, 9]
# print(a["name"])    #
# print(a["usn"])   # 





# #dictionary functions
# a = {"name": "peter", "from": "india", "marks": [92, 98, 96]}
# #1. function
# print(a.items())
# #2. function
# print(a.keys())
# #3. function
# print(a.values())
# #4. function
# a.update({"friends":["symon"]})
# print(a.items())
# #5. function
# print(a.get("name"))




# all about set, operation and methods
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# # Set operations
# print("Union:", a.union(b))               # {1,2,3,4,5,6,7,8}
# print("Intersection:", a.intersection(b)) # {4, 5}
# print("Difference (a-b):", a - b)         # {1, 2, 3}
# print("Difference (b-a):", b - a)         # {6, 7, 8}
# print("Symmetric Diff:", a.symmetric_difference(b))  # {1,2,3,6,7,8}

# # Set methods
# s = {1, 2, 3}
# s.add(4)
# print("After add(4):", s)
# s.remove(2)
# print("After remove(2):", s)
# print("Length:", len(s))





# Sets automatically remove duplicates
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# Converting list to set removes duplicates
my_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique = set(my_list)
print(f"List: {my_list}")
print(f"Unique: {unique}")

# Important: 20 and 20.0 are equal!
s = set()
s.add(20)
s.add(20.0)    # Not added (20 == 20.0)
s.add("20")    # Added (different type)
print(f"Set: {s}, Length: {len(s)}")