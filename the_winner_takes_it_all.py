import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("The winner takes it all", 0.09),
        ("The loser has to fall", 0.09),
        ("It's simple and it's plain", 0.09),
        ("Why should I complain?", 0.09)
    ]

    # Longer pauses between lines to match musical phrasing
    delays = [1.7, 1.7, 1.7, 2.3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()