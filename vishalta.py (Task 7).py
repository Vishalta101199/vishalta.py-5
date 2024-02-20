A python program which will do the following:(https://restcountries.com/v3.1/all)
import requests

class CountryData:
    def _init_(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data.")
            return None

    def display_country_info(self, data):
        print("Country Information:")
        for country in data:
            print(f"Country: {country['name']['common']}")
            print(f"Currency: {', '.join(country['currencies'].keys())}")
            print(f"Currency Symbol: {', '.join(country['currencies'].values())}")
            print("")

    def countries_with_dollar_currency(self, data):
        print("Countries with Dollar Currency:")
        for country in data:
            if 'USD' in country['currencies']:
                print(country['name']['common'])

    def countries_with_euro_currency(self, data):
        print("Countries with Euro Currency:")
        for country in data:
            if 'EUR' in country['currencies']:
                print(country['name']['common'])

# Usage example:
url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
data = country_data.fetch_data()
if data:
    country_data.display_country_info(data)
    country_data.countries_with_dollar_currency(data)
    country_data.countries_with_euro_currency(data)

Write a python Program which will do the following (https://www.openbrewerydb.org/)
import requests

class BreweryData:
    def _init_(self, states):
        self.base_url = "https://api.openbrewerydb.org/breweries"
        self.states = states

    def fetch_breweries(self, state):
        url = f"{self.base_url}?by_state={state}&per_page=50"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch breweries in {state}.")
            return []

    def list_breweries_in_states(self):
        breweries_in_states = {}
        for state in self.states:
            breweries = self.fetch_breweries(state)
            brewery_names = [brewery['name'] for brewery in breweries]
            breweries_in_states[state] = brewery_names
        return breweries_in_states

    def count_breweries_in_states(self):
        breweries_count_in_states = {}
        for state in self.states:
            breweries = self.fetch_breweries(state)
            breweries_count_in_states[state] = len(breweries)
        return breweries_count_in_states

    def count_types_in_cities(self, state):
        breweries = self.fetch_breweries(state)
        types_in_cities = {}
        for brewery in breweries:
            city = brewery['city']
            brewery_type = brewery['brewery_type']
            types_in_cities[city] = types_in_cities.get(city, {})
            types_in_cities[city][brewery_type] = types_in_cities[city].get(brewery_type, 0) + 1
        return types_in_cities

    def count_websites_in_states(self):
        websites_count_in_states = {}
        for state in self.states:
            breweries = self.fetch_breweries(state)
            websites_count = sum(1 for brewery in breweries if brewery['website_url'])
            websites_count_in_states[state] = websites_count
        return websites_count_in_states

# Define the states
states = ['Alaska', 'Maine', 'New York']

# Create BreweryData object
brewery_data = BreweryData(states)

# Task 1: List the names of all breweries present in states of Alaska, Maine, and New York
breweries_in_states = brewery_data.list_breweries_in_states()
for state, breweries in breweries_in_states.items():
    print(f"Breweries in {state}:")
    print('\n'.join(breweries))
    print()

# Task 2: Count the number of breweries in each of the states mentioned above
breweries_count_in_states = brewery_data.count_breweries_in_states()
print("Count of breweries in each state:")
for state, count in breweries_count_in_states.items():
    print(f"{state}: {count}")

# Task 3: Count the number of types of breweries present in individual cities of the states mentioned above
print("\nNumber of types of breweries in cities:")
for state in states:
    print(f"{state}:")
    types_in_cities = brewery_data.count_types_in_cities(state)
    for city, types_count in types_in_cities.items():
        print(f"- {city}:")
        for brewery_type, count in types_count.items():
            print(f"  {brewery_type}: {count}")
    print()

# Task 4: Count and list how many breweries have a website in the states of Alaska, Maine, and New York
websites_count_in_states = brewery_data.count_websites_in_states()
print("Count of breweries with websites in each state:")
for state, count in websites_count_in_states.items():
    print(f"{state}: {count}")