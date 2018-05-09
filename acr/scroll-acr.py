#!/usr/bin/env python

import sys
import time

import scrollphat


scrollphat.set_brightness(2)
text = "HELLO"

scrollphat.write_string(text, 11)

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
