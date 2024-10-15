import psycopg2

# API Info #
final_balance = 'balance'
address = 'address'
conn = psycopg2.connect(dbname="bitcoin",
                        user='postgres',
                        password='1234', 
                        host='localhost', 
                        port=5432)
cursor = conn.cursor()
table = "hunter"


def GetBTC(addrU):
    try:
        query = "SELECT * FROM " + table + " WHERE address = '" + addrU + "';"
        cursor.execute(query)
        try:
            res = cursor.fetchall()
            return res[0]
        except: 
            return [addrU, '0']
    except:
        return -1