from base_processor import BaseProcessor
import time

class LivoloProcessor(BaseProcessor):
    def on_signal_received(self, signal):
        self.sendSignal(signal)
        print("Signal forwarded: "+str(signal.ID)+", "+signal.Name)
            
livolo = LivoloProcessor()
livolo.start()

print("Processor started for device: "+str(livolo._device.ID))

while True:
    time.sleep(1)

print("Stopping livolo processor...")
livolo.stop()
print("Livolo processor stopped")
