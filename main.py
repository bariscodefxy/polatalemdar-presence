import time
import pypresence

RPC = pypresence.Presence('883688743310098432') # dont touch here
RPC.connect()

print(RPC.update(
state="polat alemdar", 
details="polat alembar",
large_image="large-image",
small_image="small-image"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds