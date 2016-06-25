VHOST=$1
ADMIN_EMAIL=$2

if [ -z "$VHOST" ]
then
	echo "Please provide vhost. Command syntax: command [vhost] [admin_email]"
	exit
fi
if [ -z "$ADMIN_EMAIL" ]
then
	echo "Please provide admin email. Command syntax: command [vhost] [admin_email]"
	exit
fi

#create virtual host directory
echo "Setting up apache2 vhost for: "$VHOST"..."
DIR="/var/www/"$VHOST
echo "Creating directory "$DIR...
sudo mkdir -p $DIR

#provide permissions to virtual host directory
echo "Setting current user permissions for "$DIR...
sudo chown -R $USER:$USER $DIR

#provide read permissions to /var/www and create /etc/mono/registry
echo "Setting read permissions for /var/www..."
sudo chmod -R 755 /var/www
sudo mkdir /etc/mono/registry
sudo chmod uog+rw /etc/mono/registry

#create config files
echo "Creating config files..."
VHOST_CONF=/etc/apache2/sites-available/$VHOST.conf
sudo cp default.conf $VHOST_CONF
sudo sed -i -e 's!vhost!'$VHOST'!g' $VHOST_CONF
sudo sed -i -e 's!admin_email!'$ADMIN_EMAIL'!g' $VHOST_CONF
sudo sed -i -e 's!vdir!'$DIR'!g' $VHOST_CONF

#turn vhost on
echo "Turning vhost on..."
sudo a2ensite $VHOST

cd /bin/
sudo ln -s mod-mono-server mod-mono-server2

#restart apache
echo "Restarting apache..."
sudo service apache2 restart