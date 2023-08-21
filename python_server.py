import requests


def get_json_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com/posts/1'
    json_data = get_json_data(api_url)

    if json_data:
        print("Received JSON data:")
        print(json_data)
