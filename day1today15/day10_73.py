def my_function():
    return 3*2

#output = my_function()

#print(output)

def format_name(f_name,l_name):
    """Take a first and last name and format it to return the 
    title case of the name
    
    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

output = format_name("CLIVE","BROOM")
print(output)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False        
    

print(is_leap_year(2000))
print(is_leap_year(2020))
print(is_leap_year(2024))
print(is_leap_year(2400))
print(is_leap_year(1700))
print(is_leap_year(1989))
print(is_leap_year(2100))

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))