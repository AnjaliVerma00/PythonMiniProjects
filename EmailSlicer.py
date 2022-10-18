email = str(input("enter your email : "))
emlsplit=  email.split('@')
username = emlsplit[0:1]
domain = emlsplit[1:2]
print("Your user name is ", ' '.join(username), " and your domain is", ' '.join(domain))
