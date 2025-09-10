# import requests
# import mysql.connector
# import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        print("sqlite connected")
        return conn
    except Error as e:
        print(e) 
        
def create_database(conn):
    try:
        cur = conn.cursor() 
        cur.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        cur.execute("""
            CREATE TABLE documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_name TEXT NOT NULL,
                doc_content TEXT,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        cur.execute("""
            CREATE TABLE versions (
                version_id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_id INTEGER,
                doc_content TEXT,
                FOREIGN KEY(doc_id) REFERENCES documents(id)
            )
        """)
        cur.execute("""
            CREATE TABLE shared_docs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_id INTEGER,
                user_id INTEGER,
                permission TEXT CHECK(permission IN ('edit', 'view')),
                FOREIGN KEY(doc_id) REFERENCES documents(id),
                FOREIGN KEY(user_id) REFERENCES users(id) 
            )
        """)
        
        print("tables formed")
    except Error as e:
        print(e)
        
def create_user(conn, username, password):
    try:
        cur = conn.cursor() 
        cur.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
        conn.commit() 
        print("user created")
    except Error as e:
        print(e) 

def login_user(conn, username, password):
    cur = conn.cursor() 
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    rows = cur.fetchall() 
    
    for row in rows:
        return True 
    return False
    
def create_document(conn, doc_name, doc_content, user_id):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO documents(doc_name, doc_content, user_id) VALUES(?, ?, ?)", (doc_name, doc_content, user_id))
        conn.commit()
    except Error as e:
        print(e) 
        
def get_document(conn, doc_id):
    cur = conn.cursor() 
    # cur.execute("SELECT * FROM shared_docs WHERE id=? AND user_id=? AND permission IN ('view', 'edit')", (doc_id, user_id))
    cur.execute("SELECT * FROM documents WHERE id=?", (doc_id,))
    rows = cur.fetchall()
    
    
    
    for row in rows:
        return row
    return None
    
def udpate_document(conn, doc_id, doc_content):
    try:
        cur = conn.cursor() 
        cur.execute("SELECT * FROM documents WHERE id=?", (doc_id,))
        rows = cur.fetchall() 
        for row in rows:
            cur.execute("INSERT INTO versions(doc_id, doc_content) VALUES(?, ?)", (doc_id, row[2]))
            conn.commit() 
        cur.execute("UPDATE documents SET doc_content = ? WHERE id = ?", (doc_content, doc_id))
        conn.commit()
    except Error as e:
        print(e) 
        
def revert_to_version(conn, doc_id, version_id):
    cur = conn.cursor() 
    cur.execute("SELECT * FROM versions WHERE doc_id=? AND version_id=?", (doc_id, version_id))
    rows = cur.fetchall()
    
    for row in rows:
        udpate_document(conn, doc_id, row[2])
        return True 
    return False

def main():
    conn = create_connection()
    create_database(conn)
    create_user(conn, "user1", "password1")
    create_document(conn, "doc1", "content1", 1)
    
    if login_user(conn, "user1", "password1"):
        print("User logged in")
    else:
        print("Invalid credentials")
        
    doc = get_document(conn, 1) 
    print(doc) 
    
    udpate_document(conn, 1, "content2")
    doc = get_document(conn, 1) 
    print(doc) 
    
    revert_to_version(conn, 1, 1)
    doc = get_document(conn, 1) 
    print(doc) 
    
if __name__ == '__main__':
    main() 