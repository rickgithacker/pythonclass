from impala.dbapi import connect
conn = connect(host='impala001.303net.pvt', port=21050)
cur = conn.cursor()
cur.execute('SHOW TABLES')
