import socket
import binascii
import CameraController
import time
import json

with open("config.json", "r") as configFile:
    cfg = json.load(configFile)

buffer_size = 1

camera = CameraController.PTZOptics20x(cfg['camera']['socket'], cfg['camera']['port'])
print(camera._tcp_host, camera._tcp_port)
camera.init()

#camera.home()

# camera.left(2)
# time.sleep(1)
# camera.stop()
# camera.right(8)
# time.sleep(2)
# camera.stop()
# camera.end()

print('Pan left - speed 6')
camera.left(6)
time.sleep(2)
print('Camera stop')
camera.stop()
time.sleep(2)
print('Pan right - speed 6')
camera.right(6)
time.sleep(2)
print('Camera stop')
camera.stop()
time.sleep(2)
print('Camera home')
camera.home()
time.sleep(2)
print('Pan right 25')
camera.gotoIncremental(25, 0, 5)
time.sleep(2)
print('Pan left 25')
camera.gotoIncremental(-25, 0, 5)
time.sleep(2)
#camera.reset()
#time.sleep(1)
camera.autofocus()
time.sleep(2)
#camera.focus('variable', False, 5)
camera.focus_lock(True)

#~ while 1:
    #~ camera.get_zoom_position()
    #~ camera.get_pan_tilt_position()
    #~ time.sleep(2)
