<<<<<<< HEAD
import requests

response = requests.get('https://api.github.com/user/octocat')

if response.status_code == 200:
    user_data = response.json()
    
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public Repos: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
=======
import requests

response = requests.get('https://api.github.com/user/octocat')

if response.status_code == 200:
    user_data = response.json()
    
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public Repos: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
>>>>>>> 36e2367c506c94705546caf13817ba0e32d9cbfa
    print("Failed to retrieve data")