from base_processor import BaseProcessor
import time
            
light = BaseProcessor()
light.start()

light.log("Processor started for device: "+str(light._device.ID))

while True:
   time.sleep(1) 

light.log("Stopping light processor...")
light.stop()
light.log("Light processor stopped")
