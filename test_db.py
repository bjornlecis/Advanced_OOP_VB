import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="personendb"
)
#woonplaats = input("geef de woonplaats")
cursor = db.cursor()

def toon_alles_data():
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for item in cursor:
        print(*item)
#cursor.close"""
#update
def voeg_item_toe():
    naam = input("geef naam")
    woonplaats = input("geef woonplaats")
    sql = "INSERT INTO personen(naam,woonplaats) values(%s,%s)"
    cursor.execute(sql,(naam,woonplaats))
    db.commit()

toon_alles_data()
voeg_item_toe()
toon_alles_data()
