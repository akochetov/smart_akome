sudo apt-get install lirc liblircclient-dev
sudo lircd -d /dev/lirc0 /home/pi/lircd.conf

#add to  /etc/modules
lirc_dev
lirc_rpi gpio_in_pin=4,gpio_out_pin=24