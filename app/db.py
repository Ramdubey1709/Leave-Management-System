import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    database = "LMS_db",
    user = "postgres",
    password = "Ram@205261"
)
cursor =conn.cursor()