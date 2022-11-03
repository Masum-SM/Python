import hashlib

email = 'mum@gmail.com'

password = 'babu136masum'

encoded_pass = password.encode()
hashed_pass = hashlib.md5(encoded_pass).hexdigest()

your_eamil = 'mum@gmail.com'
your_password = 'babu136masum'
hashed_your_pass = hashlib.md5(your_password.encode()).hexdigest()
if email == your_eamil and hashed_pass == hashed_your_pass:
    print('You are write user.')
else:
    print('You are a hacker!!!!!')