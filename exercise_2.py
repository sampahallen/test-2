'''Checking Usernames:
Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•Make a list of five or more usernames called current_users.
•Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•
Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.


FizzBuzz: 
Write a short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.'''

#CHECKING USERNAMES
usernames = ["kwa_si" , "kwa_me" , "ab_ena" , "ko_bby" , "kw_aku" , "e_si"]
new_users = ["yaw_" , "kwa_si" , "ama_" , "ko_jo" , "ko_fi"]
for new_user in new_users:
    if new_user in usernames:
        print ("This username has been taken, please choose another username.")
    else:
        print ("This username is available")


#FIZZBUZZ
for value in range(1,101):
    if value % 3 == 0 and value % 5 ==0 :
        print ("Fizz Buzz")
    elif value % 5 == 0:
        print("Buzz")
    elif value % 3== 0 :
        print ("Fizz ")
    else:
        print(value)
        