# Write a function that takes a list, a number, and a string as args
# The string parameter should have a default value
# Use slice to loop through only the first n items in the array, where n = the value of the second argument
# Each item should be prefaced by value of the string argument
# Ex: I have visited the city of San Francisco if "San Francisco" was an item in the list


def cities_visited(city_list, number, string='I have visited the city of '):
    # In the function body, loop over the list and output the items
    city_sublist = city_list[:number]
        for city in city_sublist:
            print(f'{string}{city}')


pauls_cities = [
    'Annapolis',
    'Baltimore',
    'Philadelphia',
    'San Francisco',
    'Portland'
]

cities_visited(pauls_cities, 3, 'It\'s always sunny in ')
