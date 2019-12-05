#!/usr/bin/env python

import sys

OFFSET = 4
ADD = 1
MULTIPLY = 2
HALT = 99

def process_instruction(opcode, input):
    #print(opcode)
    if opcode[0] == ADD:
        input[opcode[3]] = input[opcode[1]] + input[opcode[2]]
    elif opcode[0] == MULTIPLY:
        input[opcode[3]] = input[opcode[1]] * input[opcode[2]]
    elif opcode[0] == HALT:
        print("opcode 99: program halt")
        sys.exit(0)
    else:
        raise Exception("Unknown opcode: {}".format(opcode))
    return input

# Test cases:
#intcode_input = [1,0,0,0,99]
#intcode_input = [2,3,0,3,99]
#intcode_input = [2,4,4,5,99,0]
#intcode_input = [1,1,1,4,99,5,6,0,99]
intcode_input = []
with open("input.txt", 'r') as file:
    intcode_input = [int(x) for x in file.readline().strip("\n").split(",")]
"""
Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the
"1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program,
replace position 1 with the value 12 and replace position 2 with the value 2
"""
intcode_input[1] = 12
intcode_input[2] = 2

print("Input: {}".format(intcode_input))

input_length = len(intcode_input)
for i in range(0, input_length, 4):
    intcode_input = process_instruction(intcode_input[i:i+OFFSET], intcode_input)
    print(intcode_input)
    