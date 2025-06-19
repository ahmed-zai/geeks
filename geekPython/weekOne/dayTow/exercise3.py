""" Exercise 3: Zara

Key Python Topics:

    Creating dictionaries
    Accessing and modifying dictionary elements
    Dictionary methods like .pop() and .update()


Instructions

Create and manipulate a dictionary that contains information about the Zara brand.


Brand Information:

name: Zara
creation_date: 1975
creator_name: Amancio Ortega Gaona
type_of_clothes: men, women, children, home
international_competitors: Gap, H&M, Benetton
number_stores: 7000
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green


    Create a dictionary called brand with the provided data.
    Modify and access the dictionary as follows:
        Change the value of number_stores to 2.
        Print a sentence describing Zara’s clients using the type_of_clothes key.
        Add a new key country_creation with the value Spain.
        Check if international_competitors exists and, if so, add “Desigual” to the list.
        Delete the creation_date key.
        Print the last item in international_competitors.
        Print the major colors in the US.
        Print the number of keys in the dictionary.
        Print all keys of the dictionary.


Bonus:

Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
"""
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}


     
brand ["number_stores"] = 2 
print(brand["type_of_clothes"])
brand["ountry_creation"] = "Spain"
if "international_competitors" in brand :
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")
print("last item is ", brand["international_competitors"][-1])
print("the major colors in us is ", brand["major_color"]["US"][0:2])
print(len(brand))
#print(brand.keys())

for key in brand.keys():
    print(key)