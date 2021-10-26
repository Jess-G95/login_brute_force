# Brute force tool for login pages

This tool was built to practice brute forcing.

```
git clone https://github.com/Jess-G95/login_brute_force.git
cd login_brute_force
python login_brute_force.py -h
```

## Example


```
python .\login_brute_force.py -U http://<ip>/login.php -r "Your Login Name or Password is invalid" -P <password_word_list> -L <users_word_list>
```