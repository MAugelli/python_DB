from connetion import FilmDB
import mysql.connector

try:
    test=FilmDB("localhost", "root", "sakila")
    test.get_all_film()
    print("\n" + "-"*40 + "\n")
    test.get_actor_film("PENELOPE","GUINESS")
    print("\n" + "-"*40 + "\n")
    test.get_all_actor()
    test.close()
except mysql.connector.errors as er:
    print("ERRORE!")
    print(er)