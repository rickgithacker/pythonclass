from impala.dbapi import connect
conn = connect(host='impala001.303net.pvt', port=21050)
cursor = conn.cursor()
cursor.execute('SELECT count(*)  FROM qualitylogs.qlog_daily_parquet where year=2015 and month=03 and day=18 and hour=00 LIMIT 100')
print cursor.description # prints the result set's schema
results = cursor.fetchall()
for fred in results:
    print fred
