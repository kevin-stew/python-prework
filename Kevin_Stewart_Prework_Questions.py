# Question 1 ----------------------------------------------
# Write a function to print "hello_USERNAME!" USERNAME 
# is the input of the function.

def hello_name(user_name):
    """Prints 'hello_USERNAME'"""
    return f"hello_{user_name.upper()}"

print(hello_name(input("What is your user name?" )))


# Question 2 ----------------------------------------------
# Write a python function, first_odds that prints the odd 
# numbers from 1-100 and returns nothing

def first_odds():
    """Prints only odd numbers from 1 to 100"""
    for n in range(0,101):
        if n % 2 == 1:
            print(n)

# Line below included so that 'returns nothing' (aka None)
print(first_odds())


# Question 3 ----------------------------------------------
# Please write a Python function, max_num_in_list
# to return the max number of a given list.

def max_num_in_list(a_list):
    """Retunrs the maximum value for a given list"""
    max_num = max(a_list)
    return max_num

# A given list of integers:
my_list = [7, 565, 632, 1998, 55]

print(max_num_in_list(my_list))


# Question 4 ----------------------------------------------
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Tests if a user provided year is a leap year"""
    
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                print(f"\n{a_year} year is divisibale by 4, 100, and 400. It is a leap year!")
                return True
            else:
                print(f"\n{a_year} is divisable by 4, 100, but not 400. It is NOT a leap year")
                return False
            
        print(f"\n{a_year} is divisable by 4, it is a Leap Year!")
        return True
    
    else:
        print(f"\n{a_year} is not divisible by 4, it is not a leap year.")
        return False

print(is_leap_year(int(input("\nEnter a year to test if it is a leap year: "))))


# Question 5 ----------------------------------------------
# Write a function to check to see if all numbers in list 
# are consecutive numbers.

def is_consecutive(a_list):
    """Test if a list has consecutive integer values"""

    #creat check list using range() to compare inputted list with
    check_list = list(range(min(a_list), max(a_list) + 1))

    if a_list == check_list:
        print("\nNumbers in list are consecutive :) ")
        return True
    elif a_list != check_list:
        print("\nNumbers in list are not consecutive :( ")
        return False

# A given list with non-consecutive vlaues
my_list = [6, 7, 8, 8, 10, 51]

print(is_consecutive(my_list))
