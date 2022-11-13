# Database functions will go here
import os
from flask import Flask, render_template, request, flash, redirect
import psycopg2


def get_db_connection():
        conn = psycopg2.connect("dbname=sandman user=postgres password=password")
        return conn


def reset_tables():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS employee")       
        cur.execute("CREATE TABLE IF NOT EXISTS employee (id integer PRIMARY KEY NOT NULL, pass varchar, manager integer, name varchar, pay integer, hours integer)")
        cur.execute("INSERT INTO employee (id, pass, manager, name, pay, hours) VALUES (%s, %s, %s, %s, %s, %s)",(1234, 'John1234', 1, 'Johnathon Dillbury', 24, 60))
        cur.execute("INSERT INTO employee (id, pass, manager, name, pay, hours) VALUES (%s, %s, %s, %s, %s, %s)",(4321, 'Fred4321', 0, 'Fred Mackentire', 8, 40))
        
        conn.commit()
        cur.close()
        conn.close()
        return

