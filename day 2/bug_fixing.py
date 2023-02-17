# while True:
#     print("Hello")
#

# greeting = "hello"
# print(greeting.upper())

# countries = []
#
# while True:
#     # Ask user to input a country
#     country = input("Enter the country: ")
#     # Append the given country to the list
#     countries.append(country)
#     # Print the appended list
#     print(countries)


countries = []
while True:
    # Ask user to input a country
    country = input("Enter the country: ")
    country = country.capitalize()
    # Check to see if the country has already been added
    if country in countries:
        print("Country already exists, please enter another one")
    else:
        # Append the given country to the list
        countries.append(country)
        # Print the appended list
        print(countries)
    # Check to see if the user wants to keep adding countries
    response = input("Do you want to add another country? [y/n] ")
    # If the user doesn't want to keep adding countries, exit the loop
    if response == 'n':
        break
