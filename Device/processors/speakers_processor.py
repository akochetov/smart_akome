from base_processor import BaseProcessor
import time

speakers = BaseProcessor()
speakers.start()

speakers.log("Processor started for device: "+str(speakers._device.ID))

while True:
    time.sleep(1)

speakers.log("Stopping speakers processor...")
speakers.stop()
speakers.log("Speakers processor stopped")
