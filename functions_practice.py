##----------------------------------------------------------------------------------------------------------------------##

##Functions practice PART 1:
def hello():
    print ("Hello there!")

def pack(a,b,c):
  return[a,c,c]

def eat_lunch(my_list):
    if len(my_list ) ==0:
        print("My lunchbox is empty!")
    else: 
        for i in range(len(my_list)):
            if i ==0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sushi"])
eat_lunch(["rice","avocado","tuna","tomato"])


##----------------------------------------------------------------------------------------------------------------------##


##Functions practice PART 2:

# arb_args — Takes in any number of arguments and prints them one at a time. 

def arb_args(*args):
  for a in args:
    print(a)

# inner_func — Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x,y):
  def inner_1():
    return x+y
  def inner_2():
    return x-y
  print(inner_1()+inner_2())

# lunch_lady — Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="Mystery Meat"):
  print(name, lunch)

# sum_n_product — Accepts two integers and returns both the sum and the product.
def sum_n_product(x,y):
  return x+y,x*y

# alias_arb_args — Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args

# arb_mean — Accepts any number of integers and prints their average.
def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a/len(args))

# arb_longest_string — Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)
      longest = a
  return longest

arb_args(4,3,2,1)
inner_func(3,4)
lunch_lady("Sarah")
sum_n_product(3,5)


##----------------------------------------------------------------------------------------------------------------------##


##Functions Practice Part 3:

# 1. name_args — Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
  for k in kwargs.keys():
    print(f"{k}:{kwargs[k]}")

name_args(name="Jorge", weather="Rainy",location="City",time=5)
# 2. all_true — Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.

def all_true(iter):
  return all(iter)

print(all_true([True,True,True]))
print(all_true((True, False)))

# 3. one_true — Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

def one_true(iter):
  return any(iter)

print(one_true([True,True,True]))
print(one_true([False, False, False]))
print(one_true((True, False)))

# 4. recursive_factorial — Uses recursion to find the factorial of an integer.

def recursive_factorial(n):
  if n <= 1:
    return 1
  else:
    return n * recursive_factorial(n-1)

print(recursive_factorial(6))
print(recursive_factorial(12))

# 5. recursive_deduplicate — Recursively removes all adjacent duplicate letters from a string.

def recursive_deduplicate(my_str,i=0):
  # if our string is empty or only has 1 thing, it's got no duplicates
  # if i is at the end of the string, no duplicates are left
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    # str at current position is same as next position
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      #no duplicate at current position, check next
      return recursive_deduplicate(my_str,i+1)
      
print(recursive_deduplicate("banana"))

# 6. recursive_reverse — Uses recursion to reverse a string.
def recursive_reverse(str, i=0):
  #empty string case
  if len(str)==0:
    return ""
  #base case
  elif i == len(str)-1:
    return str[0]
  else:
    #recursive case
    return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("racecar"))


##----------------------------------------------------------------------------------------------------------------------##


##Python Practice 4

#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
  return([a,b,c])
  
print(max_num(2,4,6))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
  #if the list is empty return 0
  if len(list) == 0:
    return 0
  
  #product starts with first element of the list
  prod = list[0]

  if len(list) > 1:
    for i in list[1:]:
      prod = prod * i
  return prod

print(mult_list([2,4,6,8]))

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_string):
  return my_string[::-1]

print (rev_string("darth vader"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x, a, b):
  return x in range(a,b+1)

print (num_within(10,1,100))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print (triangle[0])
  else:
    #this fills up the correct number of rows in a triangle
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #this creates the correct row, then it add to the triangle (makes it so that the row is 1 longer than the one before)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #the intermediate numbers get added from the prevous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
          #last number is 1
        else: 
          row.append(1)
      triangle.append(row)
      row_number += 1

     #print the triangle
    for row in triangle:
      print(row)

pascal(5)











