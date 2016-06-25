sudo apt-get update
#Install python boost, python header files and python-pip
sudo apt-get purge python-dev libboost-python-dev python-pip
sudo apt-get install python-dev libboost-python-dev python-pip

#Install ```pi_switch``` using pip:
sudo pip install pi_switch

#install pi-switch
cd pi-switch-python-master
python setup.py install

#get wiringPi
git clone git://git.drogon.net/wiringPi

#build wiring Pi
cd wiringPi
./build