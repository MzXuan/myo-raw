#!/usr/bin/env python
#title           :record_data.py
#description     :This will record data of different gesture, and save to pkl for future classification
#author          :ZHAO Xuan
#date            :2018-05-24
#=============================================================================

from __future__ import print_function
from collections import Counter, deque
import sys
import os
import pickle

import numpy as np

from myo_raw import MyoRaw


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


def write_file(data, file_name):
    # emg: data[1] ; imu: data[2]; cls: data[3]
    print ("write to pkl")
    with open(file_name,'ab') as output:
        pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)
    # TODO:  write file (txt) function



if __name__ == '__main__':
    if HAVE_PYGAME:
        pygame.init()
        w, h = 800, 320
        scr = pygame.display.set_mode((w, h))
        font = pygame.font.Font(None, 30)

    file_path = './data_set/'
    file_name = os.path.join(file_path, 'data.pkl')

    m = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
    hnd = DataHandler(m)
    m.add_emg_handler(hnd.on_emg)
    m.add_imu_handler(hnd.on_imu)
    m.connect()

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
                        elif ev.unicode == 's':
                            write_file(data_list,file_name)
                            data_list[:] = []

                    elif ev.type == KEYUP:
                        if K_0 <= ev.key <= K_9 or K_KP0 <= ev.key <= K_KP9:
                            hnd.recording = -1

    except KeyboardInterrupt:
        pass
    finally:
        m.disconnect()
        print()
