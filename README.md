# gift-randomizer

Flask app used to help a group of friends plan a secret santa gift exchange.  
It offers a simple login and registration forms using flask-login and stores the hashed passwords in the sqlite3 database.  
  
Heroku deletes the database every so often, so the passwords are not persistent. Luckily it was not a problem.

🎁 Served its purpose! 🎁

### Usage
```
pip install requirements.txt
python -m flask run
```
### GUI
<img src="https://user-images.githubusercontent.com/59033082/156034715-5490e0d1-799e-4c3d-a1c1-5d981923f6e5.png" height=500>

