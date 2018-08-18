# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:12:00 2018

@author: RJ SHARMA
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> str:
    return 'This is the first Web App'

app.run()