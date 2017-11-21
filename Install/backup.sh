sudo apt-get install ntfs-3g
dir=$(findmnt -n -o TARGET /dev/sda1)
echo "Creating SD card backup to: $dir."
today="$(date '+%Y-%m-%d')"
sudo mkdir $dir/test
sudo dd bs=4M if=/dev/mmcblk0 | sudo gzip > $dir/raspbian.backup$today.img
