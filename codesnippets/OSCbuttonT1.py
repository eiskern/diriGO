from gpiozero import Button
from pythonosc import udp_client
from signal import pause

# Initialize the button on GPIO pins with debouncing
buttonA = Button(17, bounce_time=0.01)
buttonB = Button(27, bounce_time=0.01)
buttonC = Button(5, bounce_time=0.01)
buttonD = Button(13, bounce_time=0.01)

# Set up the OSC client
OSC_SERVER_IP = "192.168.100.88"
OSC_SERVER_PORT = 53535
client = udp_client.SimpleUDPClient(OSC_SERVER_IP, OSC_SERVER_PORT)

print("Programm running. Sending to port: ")
print(OSC_SERVER_IP)
print(" on port ")
print(OSC_SERVER_PORT)

# Define actions for each button
def buttonA_pressed():
    try:
        client.send_message("/nechste")
        print("Go to next Cue")
    except Exception as e:
        print(f"Error in buttonA callback: {e}")

def buttonB_pressed():
    try:
        client.send_message("/vorherige")
        print("Go to previous Cue")
    except Exception as e:
        print(f"Error in buttonB callback: {e}")

def buttonC_pressed():
    try:
        client.send_message("/starten")
        print("Play selected Cue")
    except Exception as e:
        print(f"Error in buttonC callback: {e}")

def buttonD_pressed():
    try:
        client.send_message("/stoppen")
        print("Stop All!")
    except Exception as e:
        print(f"Error in buttonD callback: {e}")

# Attach actions to buttons
buttonA.when_pressed = buttonA_pressed
buttonB.when_pressed = buttonB_pressed
buttonC.when_pressed = buttonC_pressed
buttonD.when_pressed = buttonD_pressed

# Keep the program running
pause()
