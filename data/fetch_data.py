import requests

FLIC_TOKEN = "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
HEADERS = {"Flic-Token": FLIC_TOKEN}

API_ENDPOINTS = {
    "viewed": "https://api.socialverseapp.com/posts/view?page={page}&page_size=1000",
    "liked": "https://api.socialverseapp.com/posts/like?page={page}&page_size=1000",
    "inspired": "https://api.socialverseapp.com/posts/inspire?page={page}&page_size=1000",
    "rated": "https://api.socialverseapp.com/posts/rating?page={page}&page_size=1000",
    "posts": "https://api.socialverseapp.com/posts/summary/get?page={page}&page_size=1000",
    "users": "https://api.socialverseapp.com/users/get_all?page={page}&page_size=1000",
}

def fetch_paginated_data(api_url):
    data = []
    page = 1
    while True:
        response = requests.get(api_url.format(page=page), headers=HEADERS)
        if response.status_code != 200 or not response.json():
            break
        data.extend(response.json())
        page += 1

        # Add a limit to prevent infinite loop
        if page > 10:  # Limit to 10 pages for testing
            break
    return data

# def fetch_all_data():
#     return {key: fetch_paginated_data(url) for key, url in API_ENDPOINTS.items()}

# using this for testing

def fetch_all_data():
    return {
        "viewed": [],
        "liked": [],
        "inspired": [],
        "rated": [],
        "posts": [{"id": 1, "title": "Sample Video"}, {"id": 2, "title": "Another Video"}],
        "users": [{"id": 1, "name": "Test User"}]
    }
