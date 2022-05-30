import time

# kgr1 = kgr
import kg_robot as kgr

tstart = time.time()
# 这个代码不好用，别用！！！！一直连接不上， whj 20210716
burt = kgr.kg_robot(port=30010, db_host="169.254.1.1")

# burt.movel([-0.335845, 0.0547358-3*0.024, 0.180464, 1.27118, 2.84003, 0.111631],0.05, 0.05)
#
# burt.movel([-0.368331, 0.0395556, 0.173028, -1.31259, -2.80238, -       0.413307],0.05, 0.03)
start_position = burt.getl()
print(start_position)

Az = -0.12 #z displacement (m)
hold_time = 1
up_acc = 0.3
up_velo = 0.3

position_array = []
position_array.append(start_position)

# while(1):
for i in range(100):
    burt.translatel_rel([0, 0, Az, 0, 0, 0],up_acc, up_velo)
    # current_position = burt.getl()
    # position_array.append(current_position)
    time.sleep(hold_time)
    burt.movel(start_position)

print("done testing at....")
print(position_array)
print(position_array.__sizeof__())

# # deg2rad = 36.5
# Az = 0.20 #z displacement (m)
# # angle = 5/deg2rad
# up_acc = 5
#
# up_velo = 10
#
# key_width = 24*0.001
#
# # go_acc = 1
# # go_velo = 1
#
# down_acc = 5
# down_velo = 10
#
# hold_time = 0
#
# for i in range(3):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(hold_time)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],up_acc, up_velo)
#     time.sleep(0)
#
# burt.movel(start_position)
# print(burt.getl())

# burt.translatel_rel([0, key_width*4, 0, 0, 0, 0],go_acc, go_velo)
#
# for i in range(2):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(0)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, velo)
#     time.sleep(0)
#
# burt.translatel_rel([0, key_width*1, 0, 0, 0, 0],go_acc, go_velo)
#
# for i in range(2):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(0)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, velo)
#     time.sleep(0)
#
# burt.translatel_rel([0, key_width*-1, 0, 0, 0, 0],go_acc, go_velo)
#
# for i in range(1):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(1)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, velo)
#     time.sleep(0)
#
# burt.translatel_rel([0, key_width*-1, 0, 0, 0, 0],go_acc, go_velo)
# for i in range(2):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(0)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, velo)
#     time.sleep(0)
#
# burt.translatel_rel([0, key_width*-1, 0, 0, 0, 0],go_acc, go_velo)
# for i in range(2):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(0)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, velo)
#     time.sleep(0)
#
# burt.translatel_rel([0, key_width*-1, 0, 0, 0, 0],go_acc, go_velo)
# for i in range(2):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(0)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, velo)
#     time.sleep(0)
#
# burt.translatel_rel([0, key_width*-1, 0, 0, 0, 0],go_acc, go_velo)
# for i in range(1):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],down_acc, down_velo)
#     time.sleep(2)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, velo)
#     time.sleep(0)


#
# for i in range(1):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],acc, 2*velo)
#     time.sleep(0)
#     burt.translatel_rel([0, 0, Az, 0, 0, 0],acc, 2*velo)
#     time.sleep(2)



# slide_dis = 0.025*7+0.005
# for i in range(1):
#     burt.translatel_rel([0, 0, -1*Az, 0, 0, 0],acc, velo)
#     burt.translatel_rel([0, slide_dis, 0, 0, 0, 0],acc, velo)
#
#     time.sleep(0.5)
#     burt.translatel_rel([0, 0, 10 * Az, 0, 0, 0], acc, 0.05)
#     time.sleep(2)


# burt.movel([-0.335845, 0.0547358-3*0.024, 0.180464, 1.27118, 2.84003, 0.111631],0.05, 0.05)

burt.close()

