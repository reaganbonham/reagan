# 2.1 VOCABULARY REVIEW
#   1. Git is a tool used to track code changes, and GitHub is an online platform with Git repositories
#   2. The Terminal allows you to interact directly with your computer and the command line is tex-based
#   3. A local repository is a computer folder with all the files and a remote repository is a copy of the local repository on GitHub
#   4. Version control records changes to a file over time so you can recall versions later
#   5. A staging area is the place where you can prepare a file before committing it
#   6. Git add adds a file to the staging area
#   7. Git commit saves changes in the staging area
#   8. Git push sends the changes to the remote repository
#   9. Git pull downloads changes from the remote repository
#   10. pwd shows which directory you're in
#   11. ls lists the files in the current directory
#   12. cd changes the current directory
#   13. nano allows you to edit files in the terminal
#   14. touch creates a new file
#   15. mv moves a file to a new location
#   16. rm deletes a file
#   17. cat displays the contents of a file

# 2.2 A DIRECTORY TREE
#   1. pwd
#   2. ls
#   3. git pull
#   4. mv homework.py homework/
#   5. cd homework.py
#   6. cat homework.py
#   7. git add homework.py
#        git commit -m "added homework.py"
#        git push origin main

#   8. git pull origin main and then git push origin main
#   9. cd Recents

# 3.1 DATA TYPES

def check_data_type(value):
    return type(value)

print(check_data_type(5))

# 3.2 CONDITIONALS
def check_condition(value):
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "zero"

print(check_condition(5))

# 4 LOOPS
def sumwithloop(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sumwithloop([1, 2, 3, 4, 5]))

# 5.1 LISTS

def duplicate_list(lst):
    return [x for item in lst for x in (item, item)]

print(duplicate_list(["a", "b", "c"]))

def square(num):
    return num * num
# the original had no colon after the function

print(square(5))

# My favorite function was the first one at the top