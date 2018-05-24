

from pynput import keyboard
import time


break_program = False
def on_press(key):
    global break_program
    print (key)

    if key == keyboard.Key.enter:
        print ('enter pressed')
    if key == keyboard.Key.esc:
        print ('end pressed')
        break_program = True
        return False

with keyboard.Listener(on_press=on_press) as listener:
    # while break_program == True:
        #print ('program running')
        # time.sleep(5)
    listener.join()



# import sys
# from pynput.keyboard import Key, Listener
# import time
# def on_press(key):
#     print('{0} pressed'.format(
#         key))
#
# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False
#
#
#     # Collect events until released
#     with Listener(
#             on_press=on_press,
#             on_release=on_release) as listener:
#         listener.join()


    # with Listener(
    #         on_press=on_press,
    #         on_release=on_release) as listener:
    #     try:
    #         listener.join()
    #     except KeyboardInterrupt:
    #         print ('keyboard interrupt')
    #         sys.exit(0)
