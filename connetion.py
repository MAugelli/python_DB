import mysql.connector
import getpass

class Myconnession:

    def __init__(self):
        self.connection=None
        self.connection=mysql.connector.connect(host = "localhost" , user = "root" , passwd = getpass.getpass() ,port="3306",database="sakila" )
    
    def use_querry(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def close(self):
        if self.connection != None:
            self.connection.close()

class FilmDB(Myconnession):
    
    def get_all_film(self):
        result=self.use_querry("select title from film")
        # cursor = self.connection.cursor()                     --- Non ho capito il perchè così mi restituisce il result come NONE         
        # result=cursor.execute("select title from film")
        print("I film presenti sul database sono:")
        for i in result:
            print(f"{i[0]}")
        
    def get_actor_film(self, first_name, last_name):
        result=self.use_querry(f"select title from actor inner join film_actor on actor.actor_id=film_actor.actor_id inner join film on film_actor.film_id=film.film_id where actor.first_name=\"{first_name}\" and actor.last_name=\"{last_name}\"")
        print(f"I film dove recita {first_name} {last_name}")
        for i in result:
            print(f"{i[0]}") 
            
    def get_all_actor(self):
        result=self.use_querry("select first_name, last_name from actor")
        print("Tutti gli attori nel database sono:")
        for i in result:
            print(f"{i[0]} {i[1]}") 