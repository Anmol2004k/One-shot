# print("Anmol Kumar", "Cool Bro")
# age = 23
# name = "Anmol"
# cls = "AIDS"
# Rollnum = 34
# Cgpa = 9.3
# rohit_alive = True
# Rana_ji = False
# hmm = None

# print(Cgpa,name)
# print(name)

# print("My name is",name)
# print("I scored in",Cgpa , "my last Year")

# print(type(age))
# print(type(Cgpa))
# print(type(cls))
# print(type(hmm))
# print(type(Rana_ji))
# print(type(rohit_alive))

                     # #sum

# a = 45
# b = 6
# sum = (a+b)
# print(sum)
# print("Why is this is happen to me")
# print("hello")

             # #start ONE SHOT 
            # #input string
# name = input("Entr your Nmae  ::")
                 # #integer input 
# age = int(input(" Whats your Age :"))
                      # #float input
# height = float(input("What's your Height :"))
# print("My name is",name, "I am ", age, "Years old", "My Height is", height,"Cm.")

                           # COnditional statement (IF Elif ELSE)
# light = input("Enter the color of light >>...")  
# if(light == "red"):
#     print("You need to STOP")
# elif(light == "yellow"):
#     print("You have to Ready and look around ")
# elif(light == "green"):
#     print("You have to goooo..")
# else:
#     print("Your light is brooken")

            # single line Conditional statement 
              # also called terenery operator 
# food = input("food Choice....?")
# eat = "yess" if food == "cake" else "NOOO"
# print(eat)
          #Without declare variable 
# food = input("Enter food..?")
# print("sweet") if food == "cake" or food == "Rasgulla" else print("This is not Sweet")

                       # Clwver if 
# age = int(input("age ..?"))
# vote = ("yes","No") [age<= 18]
# print(vote)

# sal = float(input("Salary..."))
# tax = sal*(0.1, 0.2)[sal<=500]
# print(tax)

               #operators
   #ARTHMATIC OPERATORS 
# a= 10
# b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)
# print(a // b)
               #RELATIONAL OPERATORS 
# a = 50
# b = 20

# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
    #ASSINGMENT OPERATORS
# num = 10
# print(num)
# num = num + 10   # = 20
# print(num)
# num += 10
# print(num)
# num -= 10
# print(num)
# num *= 10
# print(num)
# num /= 10
# print(num)
# num %= 10
# print(num)
# num //= 10
# print(num)
                #LOGICAL OOERATORS
# a = 50
# b = 30
# print(not True)
# print(not False)
# print(a<b)

#    #and 
# val1 = True
# val2 = True
# val3 = False 
# val4 = False
# print("AND Operator",val1 and val2)
# print("AND Operator",val1 and val3)
#        #OR
# print("AND Operator",val1 or  val2)
# print("AND Operator",val1 or val3)
# print("AND Operator",val1 or val4)

                #TYPE CONVERSION    OR     TYPE CASTING
# a =  1
# b = int('23')
# sum = (a + b)
# print(sum)
# e = float(33444)
# print(e)
# r = complex(34)
# print(r)
        # Practice Question
               # QUESTION 1
# a = int(input("Entear a  1st Number"))
# b= int(input("Entear a 2nd Number"))
# sum = (a+b)
# print("The sum is :",sum)

  # QUESTION 2
# side = int(input("Enter the side of the SQUARE"))
# area = side*side
# print("Area of Given Square is: ",area,"Centimeter")

    # QUESTION 3
# a = float(input("Entear a  1st Number"))
# b= float(input("Entear a 2nd Number"))
# avg =( (a+b)/2)
# print("Average of two number is :",avg)

    # QUESTION 4
# a = int(input("Entear a  1st Number"))
# b= int(input("Entear a 2nd Number"))
# print(a>=b)

               #chapter2
         # string and Conditional statement
         #types 

# str1 = "This is string "
# str2 = 'Anmol kumar'
# str3 = """ I am A student"""

         #escape sequence character   \n   for weiting big pharagraph 
# str1 = " i am anmol. \n my age is 21 ."
# print(str1)

           #Basic Operations 
     # concatetation (ADDING) TWO DIFFERNT STRING 
# str1 = "Anmol"
#     # print(len(str1))
# len1 = len(str1) 
# print(len1)  
# str2 = "Kumar"
#      # print(len(str2))
# len2 = len(str2)
# print(len2)
# final = str1+" "+str2     #For space add " "
# print(final)
# print(len(final))  
                # ACCESING ELEMENT OF STRING  BY USING INDEX 
# str1 = "AnmolKumarThakur"
# ch = str1[7]
# print(ch)

          #SLICING (TUKDE KARNA ) [KISI PARTICULAR PART KO ACCES KARNAA]
str1 = "Anmolkumarthakur"
print(str1[2:9])   #exclude end index 9 is not included
print(str1[5:])
print(str1[:5])
print(str1[2:len(str1)])
print(str1[:-6])
print(str1[-13:-3])

        # Other Strin Functions 2:50:23
     #len(): Returns the length of the string.
string = "Hello, World!"
print(len(string))  # Output: 13

     #lower(): Converts the string to lowercase.
string = "Hello, World!"
print(string.lower())  # Output: "hello, world!"
     #upper(): Converts the string to uppercase.
string = "Hello, World!"
print(string.upper())  # Output: "HELLO, WORLD!"
     #strip(): Removes any leading and trailing whitespace characters.
string = "  Hello, World!  "
print(string.strip())  # Output: "Hello, World!"
    #replace(old, new): Replaces all occurrences of the old substring with a new one.
string = "Hello, World!"
print(string.replace("World", "Python"))  # Output: "Hello, Python!"

      #split(): Splits the string into a list of substrings based on a specified delimiter (default is space).
string = "Hello, World!"
print(string.split())  # Output: ['Hello,', 'World!']

      #join(): Joins the elements of an iterable (like a list) into a single string, using the specified string as the delimiter.
words = ['Hello', 'World']
print(" ".join(words))  # Output: "Hello World"

        #find(sub): Returns the index of the first occurrence of the substring, or -1 if not found.
string = "Hello, World!"
print(string.find("World"))  # Output: 7

         #startswith(prefix): Checks if the string starts with the specified prefix.
string = "Hello, World!"
print(string.startswith("Hello"))  # Output: True

         #endswith(suffix): Checks if the string ends with the specified suffix.
string = "Hello, World!"
print(string.endswith("World!"))  # Output: True
