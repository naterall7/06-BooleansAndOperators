txt = "The quick brown fox jumps over the lazy dog."
t1 = "fox"
t2 = "cat"

###############################################################################
# DONE: 1. (6 pts)
#
#   Write each of the functions below (each that takes two parameters and uses
#   the appropriate operator from the reading) that simply returns the boolean
#   evaluation of those two parameters:
#
#   equal()
#   not_equal()
#   greater_than()
#   less_than()
#   greater_than_or_equal_to()
#   less_than_or_equal_to()
#
#   Now write a line of code for each one using numbers for the parameters that
#   would cause each function to return True. 
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def equal(num1, num2):
    return num1 == num2
print(equal(num1 = 1/2, num2 = 0.5))

def not_equal(num1, num2):
    return num1 != num2
print(not_equal(num1 = 1, num2 = 2))

def greater_than(num1, num2):
    return num1 > num2
print(greater_than(num1 = 2, num2 = 1))

def less_than(num1, num2):
    return num1 < num2
print(less_than(num1 = 1, num2 = 2))

def greater_than_or_equal_to(num1, num2):
    return num1 >= num2
print(greater_than_or_equal_to(num1 = 2, num2 = 2))

def less_than_or_equal_to(num1, num2):
    return num1 <= num2
print(less_than_or_equal_to(num1 = 1, num2 = 2))


###############################################################################
# DONE: 1. (2 pts)
#
#   Write a line of code that returns True if the string
#       t1 (defined above)
#   is contained in the string
#       txt (also defined above)
#   and prints the result.
#
#   Write another line of code that returns True if the string
#       t2
#   is contained in the string
#       txt
#   and prints the result.
#
#   Run your code. Does it return what you expect?
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(t1 in txt)
print(t2 in txt)

###############################################################################
# DONE: 1. (1 pt)
#
#   Now, write a line of code that returns True if the string
#       t1
#   is *not* the same thing as
#       t2
#   and prints the result
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(t1 is not t2)