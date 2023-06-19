# This application will read roster data in JSON format, parse the file
# then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

import json
import sqlite3

db = sqlite3.connect('json_to_db.sqlite')
cur = db.cursor()

file_name = input('JSON File Name - ')
fhand= open(file_name)
file_data = fhand.read()
cur.executescript('''
DROP TABLE IF EXISTS User ;
DROP TABLE IF EXISTS Course ;
DROP TABLE IF EXISTS Member ;
CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT UNIQUE,
    
    name TEXT UNIQUE
);
CREATE TABLE Member(
    user_id INTEGER NOT NULL,
    course_id INTGER NOT NULL,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
)
''')

data = json.loads(file_data)
fhand.close()

for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    # print(f'Name: {name} | Course: {course} Role: {"Instructor "if role != 0 else "Student"}.')
    cur.execute('INSERT OR IGNORE INTO Course(name) VALUES(?)', (title, ))
    cur.execute('INSERT OR IGNORE INTO User(name) VALUES(?)', (name, ))
    user_id = cur.execute('SELECT id FROM User WHERE name = ?', (name, )).fetchone()[0]
    course_id = cur.execute('SELECT id FROM Course WHERE name = ?', (title, )).fetchone()[0]
    cur.execute('INSERT OR REPLACE INTO Member(user_id, course_id, role) VALUES(?, ?, ?)', (user_id, course_id, role))


db.commit()

cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.name || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
''')
print(cur.fetchone()[0])
cur.close()
db.close()

