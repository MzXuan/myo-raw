from __future__ import print_function
from collections import Counter, deque
import sys
import time

import numpy as np

from common import *
from myo_raw import MyoRaw

# from pynput import keyboard
#
#
# class KeyDetection():
#     def __init__(self):
#         self.break_program = False
#
#     def on_press(self,key):
#         print (key)
#         if key == keyboard.Key.enter:
#             print ('enter pressed')
#         if key == keyboard.Key.esc:
#             print ('end pressed')
#             self.break_program = True
#             return False


try:
    import pygame
    from pygame.locals import *
    HAVE_PYGAME = True
except ImportError:
    HAVE_PYGAME = False




#TODO: EMG handler
class DataHandler(object):
    def __init__(self,m):
        # self.recording = -1
        self.m = m
        self.emg = (0,) * 8
        self.quat = (0,) *4

    def on_emg(self, emg, moving):
        self.emg = emg
        # print ('emg: ', self.emg)

    def on_imu(self, quat, acc, gyro):
        self.quat = quat
        # print ('quat: ', quat)

    # TODO: save to file



        # if self.recording >= 0:
        #     self.m.cls.store_data(self.recording, emg)

# def write_file(emg, quat, cls):




if __name__ == '__main__':
    if HAVE_PYGAME:
        pygame.init()
        w, h = 800, 320
        scr = pygame.display.set_mode((w, h))
        font = pygame.font.Font(None, 30)



    m = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
    hnd = DataHandler(m)
    m.add_emg_handler(hnd.on_emg)
    m.add_imu_handler(hnd.on_imu)
    m.connect()

    emg_list = []
    quat_list = []
    cls_list = []

    data_list = []

    try:

        while True:
            m.run()

            if HAVE_PYGAME:
                for ev in pygame.event.get():
                    if ev.type == QUIT or (ev.type == KEYDOWN and ev.unicode == 'q'):
                        raise KeyboardInterrupt()
                    elif ev.type == KEYDOWN:
                        if K_0 <= ev.key <= K_9:
                            temp_data = [hnd.emg,hnd.quat, (ev.key-K_0)]  # type: List[Union[Union[Tuple[int, int, int, int, int, int, int, int], Tuple[int, int, int, int], int], Any]]
                            data_list.append(temp_data)
                            print("recording data: ", temp_data)

                        elif K_KP0 <= ev.key <= K_KP9:
                            temp_data = [hnd.emg, hnd.quat, (ev.key - K_KP0)]
                            data_list.append(temp_data)
                            print("recording data: ", temp_data)

                        # TODO: save data
                        # elif ev.unicode == 's':
                            #hnd.cl.read_data()
                    elif ev.type == KEYUP:
                        if K_0 <= ev.key <= K_9 or K_KP0 <= ev.key <= K_KP9:
                            hnd.recording = -1


    except KeyboardInterrupt:
        pass
    finally:
        m.disconnect()
        print()

    # key = KeyDetection()
    # lis = keyboard.Listener(on_press=key.on_press)
    # lis.start()

    # try:
    #
    #     while True:
    #         m.run()
    #         lis.join()
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     m.disconnect()
    #     print()