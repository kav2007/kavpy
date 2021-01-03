import math

#Basic Arithmetic Functions

#Addition
def add(x,y):
    print('The sum of',x,'and',y,'is',x+y)

#Add multiple numbers
def add_multple(nums):
    sum = 0
    for x in nums:
        sum += x
    return(sum)

#Subtraction
def subtract(x,y):
    print('The difference of',x,'and',y,'is',x-y)

#Multiplication
def multiply(x,y):
    print('The product of',x,'and',y,'is',x*y)

#Multiply multiple numbers
def multiply_multiple(nums):
    product = 0
    for x in nums:
        product *= x
    print(product)

#Division
def divide(x,y):
    print('The quotient of',x,'and',y,'is',x/y)

#Finding remainder on division or Modulus
def remainder(x,y):
    print('The remainder of',x,'and',y,'is',x%y)

#Square
def square(x):
    print('The square of',x,'is',x**2)

#Cube
def cube(x):
    print('The cube of',x,'is',x**3)

#Exponential
def exponential(x,y):
    print('The value of',x,'raisd to the power of',y,'is',x**y)

#Square Root
def sq_root(x):
    x = math.sqrt(x)
    print('The square root of',x,'is',x)

#Cube Root
def cb_root(x):
    print('The cube root of',x,'is',x**1/3)

#Any root
def root(x,y):
    print('The',y,'th root of ',x,'is',x**1/y)

#Percentage
def percentage(x,y):
    print(x,'percent of',y,'is',(x/100)*y)

#End of Basic Arithmetic Operators

#Areas and perimeters of 2D shapes

#Area of Square
def area_square(side):
    print('The area of square with side',side,'is',side*side)

#Perimeter of Square
def peri_square(side):
    print('The perimeter of square with side',side,'is',side*4)

#Area of Rectangle
def area_rectangle(length,breadth):
    print('The area of rectangle with length',length,'and breadth',breadth,'is',length*breadth)

#Perimeter of Rectangle
def peri_rectangle(length,breadth):
    print('The perimeter of recatngle with length',length,'and breadth',breadth,'is',2*(length+breadth))

#Area of Triangle
def area_triangle(base,height):
    print('The area of triangle with base',base,'and height',height,'is',(base*height)/2)

#Perimeter of Triangle
def peri_triangle(side1,side2,side3):
    print('The perimeter of triangle with sides',side1,',',side2,'and',side3,'is',side1+side2+side3)

#Area of Equilateral Triangle
def area_equilateral_triangle(side):
    area_equilateral_triangle = (math.sqrt(3)/4)* side * side
    print('The area of the equilateral triangle with side',side,'is',area_equilateral_triangle)

#Area of Triangle using Heron's Theorem
def area_heron_triangle(side1,side2,side3):
    s = (side1+side2+side3)/2
    area_heron_triangle = (math.sqrt(s*(s-side1)*(s-side2)*(s-side3)))
    print("The area of triangle using heron's theorem with sides",side1,',',side2,'and',side3,'is',area_heron_triangle)

#Area of Parallelogram
def area_parallelogram(base,height):
    print('The area of parallelogram with base',base,'and height',height,'is',base*height)

#Perimeter of Parallelogram
def peri_parallelogram(parallel1,parallel2):
    print('The perimeter of parallelogram with sides',parallel1,'and',parallel2,'is',2*(parallel1+parallel2))

#Area of Rhombus
def area_rhombus(diagonal1,diagonal2):
    print('The area of rhombus with diagonals',diagonal1,'and',diagonal2,'is',(diagonal1*diagonal2)/2)

#Area of Rhombus with parallelogram way
def area_rhombus_parallelogram_way(base,height):
    print('The area of rhombus with base',base,'and height',height,'is',base*height)

#Perimeter of Rhombus
def peri_rhombus(side):
    print('The perimeter of rhombus with side',side,'is',side*4)

#Area of Circle
def area_circle(r):
    area_circle = math.pi * r * r
    print('The area of circle with radius',r,'is',area_circle)

#Circumference of Circle
def circum_circle(r):
    circum_circle = math. pi * 2 * r
    print('The circumference of circle with radius',r,'is',circum_circle)

#Area of Trapezium
def area_trapezium(base1,base2,height):
    area_trapezium = ((base1+base2)/2)*height
    print('The area of trapezium with bases',base1,'and',base2,'is',area_trapezium)

#Perimeter of Trapezium
def peri_trapezium(side1,side2,side3,side4):
    print('The perimeter of trapezium with sides',side1,',',side2,',',side3,'and',side3,'is',side1+side2+side3+side4)

#Area of Kite
def area_kite(diagonal1,diagonal2):
    print('The area of kite with diagonals',diagonal1,'and',diagonal2,'is',(diagonal1*diagonal2)/2)

#Perimeter of Kite
def peri_kite(side1,side2):
    print('The perimeter of kite with sides',side1,'and',side2,'is',2*(side1+side2))

#Area of Ellipse
def area_ellipse(axis1,axis2):
    area_ellipse = math.pi * axis1 * axis2
    print('The area of ellpise with axes',axis1,'and',axis2,'is',area_ellipse)

#End of areas and perimeters of 2D shapes

#Volumes and Surface areas of 3D shapes

#Volume of Cube
def volume_cube(edge):
    print('The volume of cube with edge',edge,'is',edge**3)

#Surface area of Cube
def surface_area_cube(edge):
    print('The surface area of cube with edge',edge,'is',6*(edge**2))

#Lateral Surface Area of Cube
def lateral_surface_area_cube(edge):
    print('The lateral surface area of cube with edge',edge,'is',4*(edge**2))

#Volume of Cuboid
def volume_cuboid(length,breadth,height):
    print('The volume of cuboid with length',length,',breadth',breadth,'and height',height,'is',length*breadth*height)

#Surface Area of Cuboid
def surface_area_cuboid(length,breadth,height):
    surface_area_cuboid = 2*((length*breadth)*(length*height)*(breadth*height))
    print('The surface area of cuboid with length',length,',breadth',breadth,'and height',height,'is',surface_area_cuboid)

#Lateral Surface Area of Cuboid
def lateral_surface_area_cuboid(length,breadth,height):
    lateral_surface_area_cuboid = 2 * height * (length+breadth)
    print('The lateral surface area of cuboid with length',length,',breadth',breadth,'and height',height,'is',lateral_surface_area_cuboid)

#Volume of Cylinder
def volume_cylinder(r,height):
    volume_cylinder = math.pi * (r**2) * height
    print('The volume of cylinder with radius',r,'and height',height,'is',volume_cylinder)

#Total Surface Area of Cylinder
def surface_area_cylinder(r,height):
    surface_area_cylinder = (2 * math.pi * r)*(r + height)
    print('The total surface area of cylinder with radius',r,'and height',height,'is',surface_area_cylinder)

#Curved Surface Area of Cylinder
def curved_surface_area_cylinder(r,height):
    curved_surface_area_cylinder = (2 * math.pi * r * height)
    print('The curved surface area of cylinder with radius',r,'and height',height,'is',curved_surface_area_cylinder)

#Volume of Cone
def volume_cone(r, height):
    volume_cone = (1/3)* math.pi * (r**2) * height
    print('The volume of cone with radius',r,'and height',height,'is',volume_cone)

#Total Surface Area of Cone
def surface_area_cone(slant_height,r):
    surface_area_cone = math.pi * r * (slant_height + r)
    print('The total surface area of cone with radius',r,'and slant height',slant_height,'is',surface_area_cone)

#Curved Surface Area of Cone
def curved_surface_area_cone(slant_height,r):
    curved_surface_area_cone = math.pi * r * slant_height
    print('The curved surface area of cone with radius',r,'and slant height',slant_height,'is',curved_surface_area_cone)

#Volume of Sphere
def volume_sphere(r):
    volume_sphere = (4/3)*math.pi*(r**3)
    print('The volume of sphere with radius',r,'is',volume_sphere)

#Surface Area of Sphere
def surface_area_sphere(r):
    surface_area_sphere = 4 * math.pi * (r**2)
    print('The surface area of sphere with radius',r,'is',surface_area_sphere)

#Volume of Hemisphere
def volume_hemishphere(r):
    volume_hemishphere = (2/3)*math.pi*(r**3)
    print('The volume of hemisphere with radius',r,'is',volume_hemishphere)

#Total surface area of Hemisphere
def surface_area_hemisphere(r):
    surface_area_hemisphere = 3 * math.pi * (r**2)
    print('The total surface area of hemishphere with radius',r,'is',surface_area_hemisphere)

#Curved Surface Area of Hemisphere
def curved_surface_area_hemisphere(r):
    curved_surface_area_hemisphere = 2 * math.pi * (r**2)
    print('The curved surface area of hemishphere with radius',r,'is',curved_surface_area_hemisphere)

#End of volume and surface area of 3D shapes

#Playing with numbers

#LCM: Lowest Common Multiple
def lcm(nums):
    lcm = math.lcm(nums)
    print(lcm)

#HCF: Highest Common Factor or GCD: Greatest Common Divisor
def hcf(nums):
    hcf = math.gcd(nums)
    print(hcf)

#Fining if a number is prime or not
def prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print('The number',num,'is not a prime number')
                break
            else:
                print('The number',num,'is a prime number')
    elif num == 1:
        print('1 is a special number that is neither prime or composite')
    else:
        print('Please enter a valid positive number')

#Finding if a number is an armstrong number or not
def armstrong(num):
    num_str = str(num)
    num_list = list()
    sq_list = list()
    for i in num_str:
        i = int(i)
        num_list.append(i)
    for i in num_list:
        sq_list.append(i**3)
    sum = add_multple(sq_list)
    if sum == num:
        print('The number',num,'is an armstrong number')
    else:
        print('The number',num,'is not an armstrong num')

#Reversing a number
def reverse(num):
    num_str = str(num)
    num_list = list()
    for i in num_str:
        num_list.append(i)
    print('The reverse of ',num,' is ',*num_list[::-1], sep='')

#Sum of the digits of the number
def sum_digits(num):
    num_str = str(num)
    num_list = list()
    sum = 0
    for i in num_str:
        i = int(i)
        num_list.append(i)
        sum += i
    print('The sum of digits of the number',num,'is',sum)

#Finding if a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print('The number',num,'is an even number')
    else:
        print('The number',num,'is an odd number')

#Finding Prime Factors
def prime_factors(num):
    while num % 2 == 0:
        print(2)
        num /= 2
    for i in range(3,int(math.sqrt(num)+1),2):
        while num % i == 0:
            print(i)
            num /= i
    if num > 2:
        print(num)

#Finding the greatest number in a list
def greatest_number(nums):
    greatest_number = None
    for num in nums:
        if greatest_number == None:
            greatest_number = num
        elif num > greatest_number:
            greatest_number = num
    if greatest_number is None:
        print('The Numbers provided were wrong. Please provide valid numbers')
        quit() 
    print('The greatest number is',greatest_number)

#Finding the lowest number in a list
def lowest_number(nums):
    lowest_number = None
    for num in nums:
        if lowest_number == None:
            lowest_number = num
        elif num < lowest_number:
            lowest_number = num
    if lowest_number is None:
        print('The Numbers provided were wrong. Please provide valid numbers')
        quit() 
    print('The lowest number is',lowest_number)

#Finding if a number is in a list or not
def find_number(num,num_list):
    for i in num_list:
        if i == num:
            place = num_list.index(num)
            print('The number',num,'was found in the list at the',place,'index')

#Number of numbers in a list
def how_many_numbers(num_list):
    count = 0
    for i in num_list:
        count += 1
    return(count)

#Average of numbers
def average(num_list):
    sum = add_multple(num_list)
    count = how_many_numbers(num_list)
    average = sum/count
    print('The average of numbers is',average)

#End of Playing with numbers
    
#Word related functions

#Most common letter in a string
def common_letter(text):
    letter_list = list(text)
    counts = dict()
    for letter in letter_list:
        counts[letter] = counts.get(letter, 0) + 1
    biggest_count = None
    common_letter = None
    for letter,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_letter = letter
    print('The most common letter was',common_letter,'and its count was',biggest_count)

#Most common letter in file
def common_letter_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    letter_list = list(handle.read().strip("\n"))
    counts = dict()
    for letter in letter_list:
        counts[letter] = counts.get(letter, 0) + 1
    biggest_count = None
    common_letter = None
    for letter,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_letter = letter
    print('The most common letter was',common_letter,'and its count was',biggest_count)

#Number of Letters in a string
def letter_count(text):
    letter_list = list(text)
    count = 0
    for letter in letter_list:
        count += 1
    print('The number of letters in the text were',count)

#Number of Letters in a file
def letter_count_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    letter_list = list(handle.read().strip("\n"))
    count = 0
    for letter in letter_list:
        count += 1
    print('The number of letters in the file were',count)

#Most common word in a string
def common_word(text):
    counts = dict()
    for line in text:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    biggest_count = None
    common_word = None
    for word,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_word = word
    print('The most common word was',common_word,'and its count was',biggest_count)
    print(counts)

#Most common word in a file
def common_word_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    biggest_count = None
    common_word = None
    for word,count in counts.items():
        if biggest_count is None or count > biggest_count:
            biggest_count = count
            common_word = word
    print('The most common word was',common_word,'and its count was',biggest_count)

#Number of Words in a string
def word_count(text):
    count = len(text.split())
    print('The number of words in text were ' + str(count))

#Number of words in a file
def word_count_file(file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    count = 0
    for line in handle:
        words = line.split()
        for word in words:
                count += 1
    print('The number of words in the text were',count)

#Finding if a word is in a file or not
def find_word(word_to_be_found,file):
    try:
        handle = open(file)
    except:
        print('Enter a valid file. Make sure the file is in the same directory as your python program')
        quit()
    for line in handle:
        words = line.split()
        for word in words:
            if word == word_to_be_found:
                print("The word '",word_to_be_found,"' was found in the text file")

#End of word related function

#Fun
def name():
    name = input("What's your name: ")
    print('Your name',name,'is really gud')

def election(name, age):
    if int(age) >= 18:
        print('You are old enough to vote, big man',name)
        vote = input("Who'll you vote for? big man "+ name+ ":")
        if vote == 'BJP': 
            print('You are a good decision maker',name,'.')
        else: 
            print('You suck at decision making',name,'.')
    else: 
        print('Grow faster small man',name,'.')

