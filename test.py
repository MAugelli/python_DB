from connetion import FilmDB

test=FilmDB()
test.get_all_film()
print("\n" + "-"*40 + "\n")
test.get_actor_film("PENELOPE","GUINESS")
print("\n" + "-"*40 + "\n")
test.get_all_actor()
test.close()