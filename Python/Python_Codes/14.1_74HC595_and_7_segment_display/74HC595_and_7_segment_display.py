import time
from my74HC595 import Chip74HC595

lists =[0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8,
        0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]

chip = Chip74HC595(14,12,13)
try:
    while True:
        for count in range(16):
            chip.shiftOut(0,lists[count])
            time.sleep_ms(500)
except:
    pass