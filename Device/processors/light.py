from base_processor import BaseProcessor
            
light = BaseProcessor()
light.start()

try:
    input('Light processor started, press any key to exit\r\n')
except:
    pass

print("Stopping light processor...")
light.stop()
print("Light processor stopped")
