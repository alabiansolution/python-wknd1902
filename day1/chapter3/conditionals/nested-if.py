firstname = input('Enter firstname: ')
lastname = input('Enter lastname: ')

use_firstname = firstname.strip()
use_lastname = lastname.strip()

if use_firstname != '' or use_lastname != '':
    if len(use_firstname) < 3 or len(use_lastname) < 3:
        print('Please your firstname and lastname should be grater than 3')
    else:
        print(use_lastname+' '+use_firstname)
else:
    print('The firstname and lastname should not be empty')
