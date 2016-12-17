sudo apt-get update

#install RabbitMQ
sudo apt-get install rabbitmq-server

#install RabbitMQ python lib
sudo pip install pika

#install python dev tools
sudo apt-get install python-dev -y

#install Wiring Pi and Livolo
bash ../Device/lib/install_livolo.sh

#install Livolo python lib
cd ../Device/lib/livolo
sudo python setup.py install

@install IR python lib
cd ../ir
sudo python setup.py install
