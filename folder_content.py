# source: https://www.thepythoncode.com/article/using-github-api-in-python

import base64
from github import Github


def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-" * 50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass


# Github username
print("Enter github username:")
username = input()
# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)

for r in user.get_repos():
    print(print_repo(r))

# at this point this code has a problem with the API rate limit for the current IP
