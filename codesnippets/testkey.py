"""
Diri-Box OSC-Client
"""
import argparse
import tty, sys, termios #keyboard inputs

#keyboardinputs
filedescriptors = termios.tcgetattr(sys.stdin) 
tty.setcbreak(sys.stdin)

#import pythonosc
from pythonosc import udp_client

#start udpclient
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="192.168.2.203",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

#run key detect loop
x = 0

while 1:
  x=sys.stdin.read(1)[0]
  print("You pressed", x)
  if x == "r":
    client.send_message("/workspace/id/playhead", "next")
    print("If condition is met")
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)
