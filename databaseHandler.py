import sqlite3

class DB():
    
    def __init__(self):
        self.database = "database.db"
    
    def connect(self):
        self.conn = sqlite3.connect(self.database)
    
    def disconnect(self):
        self.conn.close()
    
    def queryDB(self, query):
        self.connect()
        cur = self.conn.cursor()
        reply = cur.execute(query)
        response = reply.fetchone()
        self.disconnect()
        return response
    
    def queryDBall(self, query):
        self.connect()
        cur = self.conn.cursor()
        response = cur.execute(query)
        response.fetchall()
        self.disconnect()
        return response
    
    def commitDB(self, query):
        self.connect()
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        self.disconnect()
    
    
    
    