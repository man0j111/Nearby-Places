import requests
import time

def get_nearby_restaurants(api_key, location, radius=1000, keyword='restaurant', max_results=60):
    endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': location,
        'radius': radius,
        'keyword': keyword,
        'key': api_key,
    }

    results = []

    while len(results) < max_results:
        response = requests.get(endpoint, params=params)
        data = response.json()
        new_results = data.get('results', [])
        results.extend(new_results)

        # Check if there is another page of results
        next_page_token = data.get('next_page_token')

        if not next_page_token:
            break

        # Wait for a while before making the next request
        time.sleep(2)

        # Use a new API request without the pagetoken
        params = {'location': location, 'radius': radius, 'keyword': keyword, 'key': api_key}

    return results[:max_results]

def main():
    api_key = 'YOUR API KEY'
    locations = ['11.0168,76.9558', '11.0176,76.9495', '11.0122,76.9662']  # List of coordinates

    all_restaurants = []

    for location in locations:
        restaurants = get_nearby_restaurants(api_key, location, max_results=100)
        all_restaurants.extend(restaurants)

    if all_restaurants:
        print("List of nearby restaurants:")
        for i, restaurant in enumerate(all_restaurants, 1):
            print(f"{i}. {restaurant['name']} - {restaurant.get('vicinity', 'Address not available')}")
    else:
        print("No restaurants found nearby.")

if __name__ == "__main__":
    main()
