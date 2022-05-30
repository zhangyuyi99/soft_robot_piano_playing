import time
import kg_robot as kgr
from piano import Piano

# all moving distances in meter

def move(note):

    ready_position_l = note.position
    burt.movel(ready_position_l)
    time.sleep(2)

tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")

# go to start position every time for caliberation (rigid finger)
# set the finger at central C, at the height of piano key and the wrist flat before running
start_position_l = [-0.602168, -0.0656458, 0.121373, 2.15931, -2.27794, 0.0549882]
start_position_j = [-0.119586, -1.25544, 2.04127, -2.33096, -1.54294, 3.07975]
burt.movej(start_position_j)
burt.movel(start_position_l)

# set the piano
p = Piano(central_C_position=start_position_l, key_width=[0,0.023,0,0,0,0])

time.sleep(4)
for key, value in p.keys.items():
    move(value)

burt.movel(start_position_l)









