from base_processor import BaseProcessor
import time

speakers = BaseProcessor()
speakers.start()

while True:
    time.sleep(1)

print("Stopping speakers processor...")
speakers.stop()
print("Speakers processor stopped")
