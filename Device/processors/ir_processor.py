from base_processor import BaseProcessor
import time

ir = BaseProcessor()
ir.start()

print("Processor started for device: "+str(ir._device.ID))

while True:
    time.sleep(1)

print("IR speakers processor...")
ir.stop()
print("IR processor stopped")
