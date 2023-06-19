import sqlite3
import re


db = sqlite3.connect('orgs_Counts.sqlite')
cr = db.cursor()
cr.execute('DROP TABLE  IF EXISTS Counts')
cr.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
fname = input('File: ').strip()
fh = open(fname)
for line in fh:
    if  not line.startswith('From '):
        continue
    
    org = re.findall('@(\S+)', line)[0]

    cr.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    counter = cr.fetchone()
    if counter is None:
        cr.execute('INSERT INTO Counts VALUES (?, 1)', (org,))
    else:
        cr.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

db.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cr.execute(sqlstr):
    print(str(row[0]), row[1])
cr.close()
fh.close()

