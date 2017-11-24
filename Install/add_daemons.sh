CONF_FILE=/etc/init.d/smart_akome
DIR=$(pwd)

echo "Current directory: "$DIR"..."
echo "Creating file: "$CONF_FILE"..."

sudo cp smart_akome /etc/init.d/
sudo chmod +x $CONF_FILE
sudo update-rc.d smart_akome defaults

echo "Creating directory: "$DIR/logs"..."
sudo mkdir $DIR/../Device/logs
sudo chmod 777 $DIR/../Device/logs

echo "Setting up pathes to daemon apps..."

sudo sed -i -e 's!{dir}!'$DIR'!g' $CONF_FILE

echo "Adding backup job..."
crontab -l > mycron
echo "0 4 1 * * $DIR/../System/backup.sh > $DIR/../System/logs/backup$today.log" >> mycron
crontab mycron
rm mycron

echo "Adding disks check job..."
crontab -l > mycron
echo "30 2 * * * sudo shutdown -rF now" >> mycron
crontab mycron
rm mycron

echo "Creating system job logs directory: "$DIR/../System/logs"..."
sudo mkdir $DIR/../System/logs
sudo chmod 777 $DIR/../System/logs

echo "Configuring gpu_mem=128 in /boot/config.txt"
sudo sed -i -e '$ a\\ngpu_mem=128' /boot/config.txt

echo "Setting up fsck to fix errors automatically"
sudo sed -i -e 's/FSCKFIX=no/FSCKFIX=yes/g' /lib/init/vars.sh
sudo bash /lib/init/vars.sh

echo "Done."