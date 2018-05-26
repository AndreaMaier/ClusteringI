# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:41:13 2018

@author: Andrea
"""

import sqlite3
import pandas as pd

def create_Connection():
    conn = sqlite3.connect('../data/cars.sqlite')
    return conn

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars")
 
    rows = cur.fetchall()
    return(rows)

def get_Data():
    conn = create_Connection()
    data = select_all(conn)
    df = pd.DataFrame(data, columns=['MPG','cylinders','displacement','horsepower','weight','acceleration','modelYear','origin','carName'])
    return df
