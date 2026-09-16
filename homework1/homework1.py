# File: homework1.py

# Variables and Data Types
a = 10
print(a)
print(type(a)) # a is an integer

b = 1.5
print(b)
print(type(b)) # b is a float

c = 3j
print(c)
print(type(c)) # c is a complex number

d = "hello"
print(d)
print(type(d)) # d is a string

e = [1, 2, 3]
print (e)
print(type(e)) # e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary

g = (1, 2)
print(g)
print(type(g)) # g is a tuple

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list

i = True
print(i)
print(type(i)) # i is a boolean

j = None
print(j)
print(type(j)) # j is a NoneType

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list with mixed data types

l = str(14)
print(l)
print(type(l)) # l is a string

m = 1e4
print(m)
print(type(m)) # m is a float (scientific notation for 10000.0)

# Questions:
# 1. I found nine different data types
# 2. Integer, float, complex number, string, list, dictionary, tuple, boolean, NoneType
# 3. b and m are both floats; d and l are both strings; e and h are both lists
# 4. Using the string command does not treat the numbers as integers, because using quotation marks tells python to treat the numbers as regular text.
# 5. One additional data type is a set

n = {1, 2, 3}
print(n)
print(type(n)) # n is a set

# Booleans

print(10 > 9) # True

print(10 == 9) # False

print(10 <= 9) # False

print(bool("abc")) # True

print(bool(123)) # True

print(bool(["apple", "cherry", "banana"])) # True

print(bool(True)) # True

print(bool(False)) # False

print(bool(0)) # False

print(bool("")) # False

print(bool(" ")) # True

print(bool(())) # False

print(bool([])) # False

print(bool({})) # False

print(bool(True and False)) # False

print(bool(True and True)) # True

print(bool(False and False)) # False

print(bool(True or False)) # True

print(bool(True or True)) # True

print(bool(False or False)) # False

print(bool(not(False))) # True

print(bool(not(True))) # False

# Questions:
# 1. The pattern I noticed about expressions returning true or false is that if the expression is true, it will return true, and if the expression 
# is false, it will return false.
# 2. I was surprised most by the expression that contained apple, cherry, and banana because those are not concrete numbers.
# 3. An expression that will return true is 5 > 3, because 5 is greater than 3.
# 4. An expression that will return false is 2 == 3, because 2 is never equal to 3.

# Operators
#   arithmetic

print(10 + 5) # addition

print(10 - 5) # subtraction

print(2 * 4) # multiplication

print(6 / 3) # division

print(5 % 2) # modulus

print(3 ** 2) # exponentiation

print(15 // 2) # floor division

#   comparison

print(5 == 2) # equal

print(10 != 10) # not equal

print(2 < 5) # less than

print(12 > 5) # greater than

print(5 <= 6) # less than or equal to

print(1 >= 10) # greater than or equal to

#   Assignments Operators

x = 5

x += 5 # x = x + 5

x -= 4 # x = x - 4

x *= 3 # x = x * 3

#   Logical Operators
# 1. The operator and does not return true unless both statements are true
#   an expression that results in true is true and true
# 2. The operator or returns true if one of the statements is true
#   an or exression that results in true is true or false
# 3. The operator not reverses the result, returning false if the result is true and vice versa.
#   an expression that results in true is not false

#   More Questions
# 1. The difference between / and // is that / returns a float, while // returns an integer.
# 2. The difference between % and // is that % returns the remainder of a division, while // returns the integer result of a division.
# 3. The operator you'd use to find the remainder when dividing two numbers is the modulus operator (%).
#   For example, 10 % 3 would return 1, which is the remainder of 10 divided by 3.
# 4. Assignment operators are used to assign values to variables.

# Strings

my_string = "hello"

print(my_string) # prints: hello

print(my_string[0]) # prints: h

print(my_string[1]) # prints: e

print(my_string[2]) # prints: l

print(my_string[3]) # prints: l

print(my_string[4]) # prints: o

print(my_string[-1]) # prints: o

print(my_string[1:3]) # prints: el

print(my_string[0:5:2]) # prints: hlo

print(len(my_string)) # prints: 5

print(my_string + " goodbye") # prints: hello goodbye

print(my_string * 7) # prints: hellohellohellohellohellohellohello

# Questions:
# 1. The term slicing means to extract a portion of a string by specifying a start and end index.
#    The manipulations I sliced were on lines 193 and 195
# 2.
name = "Oski"
print("Hello, my name is", name) # prints: Hello, my name is Oski
# 3.
name = "Oski"
print(f"Hello, my name is {name}") # prints: Hello, my name is Oski
# 4. The difference between the two methods is that the first method uses concatenation to combine strings, while the second method uses f-strings
# to format strings.

# Terminal Commands
# 1. cd
    # changes directories
    # example: cd Desktop

# 2. ls
    # lists the contents of the current directory
    # example: ls

# 3. ls -a
    # lists all contents of the current directory, including hidden files
    # example: ls -a

# 4. mkdir
    # creates a new directory
    # example: mkdir new_directory

# 5. cat
    # displays the contents of a file
    # example: cat file.txt

# 6. pwd
    # prints the current working directory
    # example: pwd

# 7. cd ..
    # moves up one directory level
    # example: cd ..

# 8. cd .
    # stays in the current directory
    # example: cd .

# 9. cd ~
    # moves to the home directory
    # example: cd ~

# 10. cp
    # copies a file or directory
    # example: cp file.txt new_file.txt

# 11. mv
    # moves a file or directory
    # example: mv file.txt new_directory/

# 12. rm
    # removes a file or directory
    # example: rm file.txt

# 13. clear
    # clears the terminal screen
    # example: clear

# 14. grep
    # searches for a specific pattern in a file or output
    # example: grep "pattern" file.txt

# Questions:
# 1. 3 other comands not present are 
#    a. touch - creates a new empty file
#    b. echo - displays a line of text or a variable value
#    c. history - shows the command history
# 2. The difference between ls and ls -a is that ls lists only the visible files and directories in the current directory, while ls -a lists all
#   files and directories
# 3. A hidden file is a file that is not normally visible in the directory listing. It usually starts with a dot (.) and is used for configuration
#   or system purposes. Hidden files are not displayed by default when using the ls command, but they can be viewed using the ls -a command.
# 4. 3 other flags for the ls command are:
#    a. -l: displays detailed information about files and directories in a long format
#    b. -h: displays file sizes in a human-readable format (e.g.,
#    c. -R: lists the contents of directories recursively, including subdirectories
