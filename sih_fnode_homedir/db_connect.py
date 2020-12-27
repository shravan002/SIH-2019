import MYSQLdb

db = MYSQLdb.connect("localhost","root","lunatics@92","smartlab")
cur = db.cursor()
if cur != null:
    print('Sucessfull')
else:
    print('!sucessfull')
