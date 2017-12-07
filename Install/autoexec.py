import xbmc
import os

os.system('setxkbmap us,ru -option grp:ctrl_shift_toggle')
xbmc.executebuiltin('RunAddon(plugin.video.okino.tv)')