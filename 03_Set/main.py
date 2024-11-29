# N1
countries = set()
add_country = countries.add
remove_country = countries.discard
search_country = lambda substring: {c for c in countries if substring.lower() in c.lower()}
is_country_present = countries.__contains__


add_country("Ukraine")
add_country("Canada")
add_country("Germany")
remove_country("Canada")
print(f"Search: {' '.join(search_country('ge'))}")
print(f"Is 'Ukraine' present: {'Yes' if is_country_present('Ukraine') else 'No'}")


# N2–N5:
cities1 = {"Kyiv", "Lviv", "Odesa", "Kharkiv"}
cities2 = {"Odesa", "Kharkiv", "Dnipro", "Zaporizhzhia"}

print(f"Common cities: {' '.join(cities1 & cities2)}")
print(f"Unique to cities1: {' '.join(cities1 - cities2)}")
print(f"Unique to cities2: {' '.join(cities2 - cities1)}")
print(f"Unique cities from both sets: {' '.join(cities1 ^ cities2)}")
