import mysql.connector
import getpass

class Myconnession:

    def __init__(self, host, user, database):
        self.connection=None
        self.connection=mysql.connector.connect(host=host, user=user, passwd=getpass.getpass(), port="3306", database=database)
    
    def use_querry(self, query):
        try:
            cursor=self.connection.cursor()
            cursor.execute(query)
        except mysql.connector.errors as er:
            print("ERRORE!")
        else:
            return cursor.fetchall()
    
    def close(self):
        if self.connection != None:
            self.connection.close()

class FilmDB(Myconnession):
    
    def get_all_film(self):
        try:
            result=self.use_querry("select title from film")
            # cursor = self.connection.cursor()                     --- Non ho capito il perchè così mi restituisce il result come NONE         
            # result=cursor.execute("select title from film")
        except mysql.connector.errors as er:
            print(er)
        else:
            print("I film presenti sul database sono:")
            for i in result:
                print(f"{i[0]}")
        
    def get_actor_film(self, first_name, last_name):
        try:
            result=self.use_querry(f"select title from actor inner join film_actor on actor.actor_id=film_actor.actor_id inner join film on film_actor.film_id=film.film_id where actor.first_name=\"{first_name}\" and actor.last_name=\"{last_name}\"")
        except mysql.connector.errors as er:
            print(er)
        else:
            print(f"I film dove recita {first_name} {last_name} sono:")
            for i in result:
             print(f"{i[0]}") 
            
    def get_all_actor(self):
        try:
            result=self.use_querry("select first_name, last_name from actor")
        except mysql.connector.errors as er:
            print(er)
        else:
            print("Tutti gli attori nel database sono:")
            for i in result:
                print(f"{i[0]} {i[1]}") 