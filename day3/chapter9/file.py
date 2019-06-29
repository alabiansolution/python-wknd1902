f = open('demo.txt', 'a')

f.write('Hello love')

phone = input('Enter Phone: ')
email = input('Enter Email: ')
phone_email = phone + email

f.write(phone_email + '\n')
