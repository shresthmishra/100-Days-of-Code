# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print Lille
print(travel_log['France'][1])

nested_list = ["A", "B",["C", "D"]]

# Print C
print(nested_list[2][0])


# Nested Dictionary
travel_log_nested = {
    "India": {
        "cities_visited": ["Singrauli", "Sidhi", "Noida"],
        "total_visits": 7
    }
}

# Print Singrauli
print(travel_log_nested["India"]["cities_visited"][0])