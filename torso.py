# webdriver torso clone in Python, using Tkinter and Pyaudio.
# it's pretty damn slow to be honest, but that's pyaudio for you

from Tkinter import * # canvas

import random         # randomizer
import time           # timing

import pyaudio        # audio

import math           # beep prerequisites
import numpy          # beep prerequisites

# source of audio:
# http://milkandtang.com/blog/2013/02/16/making-noise-in-python/
def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency=440, length=1, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25

    stream.write(chunk.astype(numpy.float32).tostring())

def beep(): # I actually kind of wrote this one... not really
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
  play_tone(stream, random.randint(1, 1000))
  stream.close()
  p.terminate()

def rectangulate():
  # blue coords
  bluex1 = random.randint(1, 600)
  bluey1 = random.randint(1, 300)
  bluex2 = random.randint(1, 700)
  bluey2 = random.randint(1, 350)
  
  # red coords
  redx1 = random.randint(1, 600)
  redy1 = random.randint(1, 300)
  redx2 = random.randint(1, 700)
  redy2 = random.randint(1, 350)
  
  canvas.create_rectangle(bluex1, bluey1, bluex2, bluey2, fill="blue", tag="blue")
  canvas.create_rectangle(redx1, redy1, redx2, redy2, fill="red", tag="red")

window = Tk()
canvas = Canvas(window, width=960, height=480)
canvas.pack()

while True:
  rectangulate()
  beep()
  canvas.update()
  time.sleep(1)
  canvas.delete("all")

window.mainloop()