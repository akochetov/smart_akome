from base_processor import BaseProcessor
import time

ir = BaseProcessor()
ir.start()

ir.log("IR Processor started for device: "+str(ir._device.ID))

while True:
    time.sleep(1)

ir.stop()
ir.log("IR processor stopped")
