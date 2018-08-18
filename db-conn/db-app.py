# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:45:03 2018

@author: NEERAJ SUTHAR
"""
import psycopg2
	
try:
    conn  = psycopg2.connect(
        host="localhost",
        database="TutorsPoint",
        user="postgres", 
        password="abcd1234")

except:
    print ("I am unable to connect to the database")
    
cur = conn.cursor();
cur.execute("SELECT version();")
rows = cur.fetchall()

print(rows[0])