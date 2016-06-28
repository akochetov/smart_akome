from pi_switch import RCSwitchSender

rcpin = 6

sender = RCSwitchSender()
sender.enableTransmit(rcpin)

for i in range (0,3):#send 3 times
    sender.sendDecimal(6400,16)
    sender.sendDecimal(120,16)
