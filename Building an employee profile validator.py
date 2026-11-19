email = 'alice.johnson@company.com'
print(f'Email: {email}')
#Sometimes, you may want to find the position of a specific character inside a string. Python provides the built-in .find() method for this purpose. It returns an integer representing the index (position) of the first occurrence of the given substring.

#Here's an example:

#Example Code
#text = 'hello'
#print(text.find('e'))  # 1 

#Use slicing on email to extract everything before at_position, and store the result in a variable named username.

#Then print username so that the output reads Username: alice.johnson.
at_position = email.find('@')
print(f'Position of @: {at_position}')

#Now that you know the position of @ in the email, you can extract the username, which is placed before the @ sign.

#In the previous workshop, you extracted a portion of a string using slicing. As a reminder, the syntax is:

#Example Code
#text = 'hello world'
#print(text[:5])  # hello
#Use slicing on email to extract everything before at_position, and store the result in a variable named username.

#Then print username so that the output reads Username: alice.johnson.
#This is how we do it

username = email[:at_position]
print(f'Username: {username}')

#You can check whether a substring exists inside a string using the in keyword. It returns True if the substring exists and False otherwise. Here's an example:

#Example Code
#sentence = 'I love Python'
#print('Python' in sentence) # True
#print('Java' in sentence) # False
#Create a variable named has_at that checks if the character @ is in email.

#Then print has_at so that the output reads: Has @ symbol: True.
#has_at = '@' in email
#print(f'Has @ symbol: {has_at}')

#Here is the code

has_at = '@' in email
print(f'Has @ symbol: {has_at}')


#Here is another example
has_com = '.com' in email
print(f'Has .com: {has_com} ')

#.TITLE
#The .title() method capitalizes the first letter of each word. Here is an example:

#Example Code
#lowercase = 'hello world'
#title_case = lowercase.title()
#print(title_case)  # Output: Hello World
#Create a variable named clean_name and assign it the result of calling .title() on messy_name.

#Here is an exapmle

messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

clean_name = messy_name.title()
print(clean_name)

#.STRING
#The .strip() method removes whitespace from both ends of a string.

#Example Code
#messy = '  hello world  '
#clean = messy.strip()
#print(clean)  # Output: hello world
#You can chain .strip() and .title() to remove whitespace from both ends of a string and capitalize the first letter of each word:

#Example Code
#messy = '  hello world  '
#clean = messy.strip().title()
#print(clean)  # Output: Hello World
#Update the value of clean_name to call .strip() on messy_name before .title().

#After that, print clean_name so that the output reads Cleaned name: 'Sarah Davis'.

# Herre is thecode:

clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

#.LOWER

#The .lower() method converts all characters in a string to lowercase. This is useful for normalizing email addresses:

#Example Code
#upperGreet = 'HELLO WORLD'
#lowerGreet = upperGreet.lower()
#print(lowerGreet)  # Output: hello world
#You can call both .strip() and .lower() on a string this way:

#Example Code
#messy = '  HELLO WORLD  '
#clean = messy.strip().lower()
#print(clean)  # Output: hello world
#Create a variable messy_email and assign it the string SARAH.DAVIS@COMPANY.COM with two leading spaces and two trailing spaces.

#Also, call .strip().lower() on messy_email and assign the result to a variable clean_email.

#Then print both so that the output reads:

#Example Code
#Original email: '  SARAH.DAVIS@COMPANY.COM  '
#Cleaned email: 'sarah.davis@company.com'

#Here is the code:

messy_email = '  SARAH.DAVIS@COMPANY.COM  '
print(f"Original email: '{messy_email}'")
clean_email = messy_email.strip().lower()
print(f"Cleaned email: '{clean_email}'")

#The .upper() method converts all characters to uppercase. This is useful for name badges or headings:

#Example Code
#name = 'sarah davis'
#badge = name.upper()
#print(badge)  # Output: SARAH DAVIS
#Create a variable named name_badge and assign it the result of calling the .upper() method on clean_name.

#Then print name_badge so that the output reads: Name badge: SARAH DAVIS.


# Here is the code

#ou already used .find() and slicing on the email variable. Now you will use the same technique on clean_email.

#Find the position of the @ character in clean_email and store it in at_pos. Then use slicing to extract everything before @ and store it in email_user.

#Then print clean_email and email_user so that the output reads:

#Example Code
#Email: sarah.davis@company.com
#Username: sarah.davis

#name_badge = clean_name.upper()
#print(f'Name badge: {name_badge}')

at_pos = clean_email.find('@')

email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')
