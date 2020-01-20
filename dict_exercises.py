# Set 1
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
# Print Elizabeth's phone number.
if 'Elizabeth' in phonebook_dict:
    print('Elizabeth\'s phone number is: ', phonebook_dict['Elizabeth'])

# Add an entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict.update({'Kareem': '938-489-1234'})
print('Updated dictionary with Kareem\'s phone number: ', phonebook_dict)

# Delete Alice's phone entry
if 'Alice' in phonebook_dict:
    del phonebook_dict['Alice']
print('Here is the dictionary with Alice removed: ', phonebook_dict)

# Change Bob's phone number to '968-345-2345'.
if 'Bob' in phonebook_dict:
    phonebook_dict.update(Bob='968-345-2345')
print('Here is the dictionary with Bob\'s new phone number: ', phonebook_dict)

# Print all the phone entries.
print('Updated phone entries: ', phonebook_dict)
print('************************************')

# Set 2
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

# Write a python expression that gets the email address of Ramit.
print('Ramit\'s email address is :', ramit['email'])

# Write a python expression that gets the first of Ramit's interests.
print('Ramit\'s number one interest is: ', ramit['interests'][0])

# Write a python expression that gets the email address of Jasmine.
print('The email address of Ramit\'s friend Jasmine is: ',
      ramit['friends'][0]['email'])

# Write a python expression that gets the second of Jan's two interests.
print('Ramit\'s friend Jan\'s second favorite interest is: ',
      ramit['friends'][1]['interests'][1])
