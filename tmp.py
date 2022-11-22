import sqlite3
connection = sqlite3.connect('accounts.db')
cursor = connection.cursor()

cursor.execute('SELECT id FROM accounts WHERE username = "%s" and pin = %d' % (username,  pin))
row = cursor.fetchone()

if row:
    print('Hello #%d' % row[0])
else:
    print('Error')