#!/usr/bin/env python3
# piper, alpha release
# Pipes the output of any command to libnotify
# Copyright 2017, Aswin Babu Karuvally

# TODO
# Ouput only specific line


# import the serious stuff
import argparse
import subprocess

# the main function
def main():
    # setup the input arguments
    parser = argparse.ArgumentParser(
        description='Pipes the output of a command to desktop notification')
    
    parser.add_argument('-c', '--command')
    arguments = parser.parse_args()
    
    if arguments.command:
        command = subprocess.Popen(arguments.command, stdout = subprocess.PIPE,
            shell = True)
        subprocess.run(['notify-send', command.stdout.readline().rstrip()])
    
    return

main()
