CONF_FILE=/etc/init.d/smart_akome
DIR=$(pwd)

echo "Current directory: "$DIR"..."
echo "Creating file: "$CONF_FILE"..."

sudo cp smart_akome /etc/init.d/
sudo chmod +x $CONF_FILE
sudo update-rc.d smart_akome defaults

echo "Setting up pathes to daemon apps..."

sudo sed -i -e 's!{dir}!'$DIR'!g' $CONF_FILE

echo "Done."