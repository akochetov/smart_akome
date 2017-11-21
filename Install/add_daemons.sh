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
echo "0 0 1 * * $DIR/backup.sh" >> mycron
crontab mycron
rm mycron

echo "Done."