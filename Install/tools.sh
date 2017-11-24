sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

echo "Configuring remote desktop..."

sudo apt-get install ntpdate 
sudo apt-get install tightvncserver
sudo apt-get install xrdp
sudo apt-get install maven

echo "Configuring ssh..."

sudo sed -i -e 's/#Port 22/Port 2722/g' /etc/ssh/sshd_config
sudo sed -i -e 's/Port 22/Port 2722/g' /etc/ssh/sshd_config
sudo /etc/init.d/ssh restart

echo "Configuring java..."

sudo update-java-alternatives --set jdk-8-oracle-arm32-vfp-hflt

echo "Configuring gpu_mem=128 in /boot/config.txt
sudo sed -i -e '$ a\\ngpu_mem=128' /boot/config.txt

echo "Installing kodi..."
sudo apt-get install kodi

echo "Please reboot now"