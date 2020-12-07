============================================================================================================
To extend a new spider. See the existing spider examples in ./spiders/

1. Create your own spider in ./spiders/spider_robot/spiders like the existing spiders
2. Create your own items in ./spiders/spider_robot/items.py, the item depends on what your original data have.
3. Configure your spider in ./spiders/spider_manager.py  and ./common/constants.py
4. Add your new spider in table spider_configure
    e.g INSERT IGNORE INTO `spider_configure` (`spider_name`) VALUES ('nct');
============================================================================================================
To deploy this python project

1. install sqlite
sudo yum install sqlite-devel -y

3.sudo apt-get install -y libffi libffi-devel libxslt-devel libxml2-devel


7. go to project package/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

10. deploy & run the server
# only first time deploy need to deploy migrate database
python3 weather_manager.py db init
python3 weather_manager.py db migrate
python3 weather_manager.py db upgrade
python3 weather_manager.py deploy

python3 weather_manager.py runserver &


11. install httpie for testing
pip install httpie

e.g testing like
# http GET http://localhost:5002/api/v1.0/get_temperature





