import requests

from rich.console import Console
from rich.table import Table
console = Console()

url = "https://swapi.info/api/planets"
def fetch_swapi_data():
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

data = fetch_swapi_data() #returns a list
#each item on the list is a dictionary

# for planet in data:
#     print(planet)
#     print(type(planet)) #each planet is a dictionary CONFIRMED
#     print(planet.keys())
#     # for names
#     for planet_name in planet["name"]:
#         print(planet_name)
#     # for diameter
#     for planet_diameter in planet["diameter"]:
#         print(planet_diameter)
#     # for population
#     for planet_population in planet["population"]:
#         print(planet_population)


# for planet in data["name"]:
#     print (planet) 
#     #new:: check if planet is an instance of dictionary
#     if isinstance(planet,dict) :
#         print("here")
#         for item in planet:
#             print(f"key: {item}, value: {planet[item]}") #key and value

# print(type(data))

# from rich.console import Console
# from rich.table import Table

# console = Console()

# table = Table(show_header=True)
# table.add_column("NAME", justify="left")
# table.add_column("DIAMETER", justify="left")
# table.add_column("POPULATION", style="dim", justify="left")
# table.add_row(
#     "[red]planet_name[/red]",
#     "planet_diameter", 
#     "planet_population"
# )
# table.add_row(
#     "[purple]May 25, 2018[/purple]",
#     "[red]Solo[/red]: A Star Wars Story",
#     "$275,000,000"
# )
# table.add_row(
#     "[red]Dec 15, 2017[/red]",
#     "Star Wars Ep. VIII: The Last Jedi",
#     "$262,000,000",
# )

# console.print(table)

if data: 
    table = Table(title="Star Wars API Exercise")
    table.add_column("NAME", justify="left", style="#D0429B")
    table.add_column("DIAMETER", justify="left", style ="#3B719E")
    table.add_column("POPULATION", justify="left", style="#197373")

    for planets in data[0:13]:
        name = (planets["name"])
        diameter = (planets["diameter"])
        population = (planets["population"])
       
        table.add_row(name, diameter, population)

console.print(table)