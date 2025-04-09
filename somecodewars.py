#   Conference Traveller (kyu 7 / lists)

def conference_picker(cities_visited, cities_offered):
    if cities_visited:
        for city in cities_offered:
            if city not in cities_visited:
                return city
        return "No worthwhile conferences this year!"
        
    else: return cities_offered[0]