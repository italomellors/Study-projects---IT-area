from time import sleep
# Make a program that shows on the screen
# A countdown to the pop and fireworks,
# Going from 10 to 0, with a 1 second pause between them.
# USING LOOP NOW
import time
print('Countdown:')
for i in range(10, 0, -1):
    print(f'{i} seconds...')
    time.sleep(1)
print('Happy New Year!!!')