import psycopg2
from config import Config

conn = psycopg2.connect(
    dbname=Config.DB_NAME,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    host=Config.DB_HOST,
    port=Config.DB_PORT
)

cur = conn.cursor()
cur.execute("select * from tasks")
tasks = cur.fetchall()
cur.close()
conn.close()