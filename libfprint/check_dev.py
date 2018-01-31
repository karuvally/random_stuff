#!/usr/bin/env python3
# detects the fingerprint reader

# import the serious stuff
import subprocess
import time

initial_run = subprocess.getoutput('dmesg | tail -n 1')
initial_stamp = float(initial_run[initial_run.index('[')+1:initial_run.index(']')].strip())

while True:
    current_run = subprocess.getoutput('dmesg | grep -i 1c7a | tail -n 1')
    
    if current_run != '':
        current_stamp = float(current_run[current_run.index('[')+1:current_run.index(']')].strip())
        
        if current_stamp > initial_stamp:
            subprocess.run(['notify-send', 'Fingerprint reader found!'])
            initial_stamp = current_stamp

    time.sleep(1)
