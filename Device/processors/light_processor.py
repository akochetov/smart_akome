from base_processor import BaseProcessor
import time
            
light = BaseProcessor()
light.start()

print("Processor started for device: "+str(light._device.ID))

while True:
   time.sleep(1) 

print("Stopping light processor...")
light.stop()
print("Light processor stopped")
