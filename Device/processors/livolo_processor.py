from base_processor import BaseProcessor
import time

class LivoloProcessor(BaseProcessor):
    def on_signal_received(self, signal):
        self.sendSignal(signal)
        self.log("Signal processed: "+str(signal.ID)+", "+signal.Name)
            
livolo = LivoloProcessor()
livolo.start()

livolo.log("Processor started for device: "+str(livolo._device.ID))

while True:
    time.sleep(1)

livolo.log("Stopping livolo processor...")
livolo.stop()
livolo.log("Livolo processor stopped")
