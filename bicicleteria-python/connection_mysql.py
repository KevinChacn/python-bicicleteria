import mysql.connector

config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'kevin_parcial_3'
}

db= mysql.connector.connect(**config)
cursor = db.cursor()