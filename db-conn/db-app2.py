# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:45:03 2018

@author: RJ SHARMA
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
cur.execute('SELECT * FROM "tutorSchema"."Records";')
rows = cur.fetchall()

if not rows:
    print ("cannot get data")
else:
    print(rows[0])