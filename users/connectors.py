import psycopg2
import pymssql


def postgreConnect(hostname, database, user, password, port):
    try:
        conn = psycopg2.connect(
            host=hostname,
            database=database,
            user=user,
            password=password,
            port=port)
        return conn
    except:
        print("connection not established")


# def redshiftAWS():
#     try:
#     conn = redshift_connector.connect(
#         host='examplecluster.abc123xyz789.us-west-1.redshift.amazonaws.com',
#         database='dev',
#         port=5439,
#         user='awsuser',
#         password='my_password')
#         return conn
#     except:
#         print("connection not established")

def sqlServer(hostname, user, password, database):
    try:
        conn = pymssql.connect(server=hostname, user=user,
                               password=password, database=database)
        return conn
    except:
        print("connection not established")
