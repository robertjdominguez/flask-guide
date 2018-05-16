import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib # built-in



conn = sqlite3.connect('database.db')

c = conn.cursor()

email = 'email@addy.com'
first_name = 'First'
last_name = 'Last'
password = 'superSecretBeforeTheHash'

hashed_password = generate_password_hash(password, method='sha256')

values = [email,
          first_name,
          last_name,
          hashed_password
          ]

c.execute('''insert into users(email, first_name, last_name, password) values(?,?,?,?)''', values)

print('Added {} to the db'.format(first_name))

conn.commit()
