from bs4 import BeautifulSoup as bs
import requests

# User input
github_user = input('Input Github Username: ')
url = f'https://github.com/'+github_user

# Send request to GitHub
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = bs(response.content, 'html.parser')

    # Find the profile image tag using updated class selector
    image_tag = soup.find('img', {'alt': 'Avatar'})

    if image_tag:
        profile_image = image_tag['src']
        print("Profile image URL:", profile_image)
    else:
        print("❌ Profile image not found. Username may be incorrect or GitHub layout changed.")
else:
    print("❌ Failed to retrieve the page. Please check the username or your internet connection.")
