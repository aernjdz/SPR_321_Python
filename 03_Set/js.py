#N1
players = {}


add_player = lambda name, height: players.update({name: height})
remove_player = players.pop
find_player = players.get
update_player = lambda name, new_height: players.update({name: new_height})


add_player("Michael Jordan", 198)
add_player("LeBron James", 206)
remove_player("Michael Jordan")
print(f"Find: {find_player('LeBron James')}")
update_player("LeBron James", 207)
print(players) 


#N2
countries = {}

add_country = lambda country, capital: countries.update({country: capital})
remove_country = countries.pop
find_country = countries.get
update_country = lambda country, new_capital: countries.update({country: new_capital})


add_country("Ukraine", "Kyiv")
add_country("France", "Paris")

print(f"Find: {find_country('Ukraine')}")
print(f"Find: {find_country('France')}")

update_country("Ukraine", "Kyiv City")
print(countries) 

remove_country("France")
print(countries) 
