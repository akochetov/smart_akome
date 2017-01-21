sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install ntpdate 
sudo apt-get install tightvncserver
sudo apt-get install xrdp
sudo apt-get install maven

echo "Installing kodi..."
sudo apt-get install kodi

echo "Configuring gpu_mem=128 in /boot/config.txt
sudo sed -i -e '$ a\\ngpu_mem=128' /boot/config.txt

echo "Please reboot now"