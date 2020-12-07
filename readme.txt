============================================================================================================
============================================================================================================
To deploy this python project

1. install mysql
sudo apt install mariadb-server

2.
sudo mysql -uroot
CREATE DATABASE 'homebase';

3. create db user

CREATE USER 'homebase'@'localhost' IDENTIFIED BY 'keeshan';
GRANT ALL PRIVILEGES ON 'homebase'.* TO 'homebase'@'localhost';
FLUSH PRIVILEGES; 

3. create python virtual environment
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

4.  only first time deploy need to deploy migrate database
python3 weather_manager.py db init
python3 weather_manager.py db migrate
python3 weather_manager.py db upgrade

5. run the app
python3 hb_homebase_manage.py runserver &

=======================================================================
# curl  "http://localhost:5002/api/v1.0/get_temperature"





