f = open('file_content.txt', 'a')

# f.write('Hello my people')

phone = input('Enter Phone: ')
email = input('Enter Email: ')
phone_email = phone + email

f.write(phone_email + '\n')
