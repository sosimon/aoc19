#!/usr/bin/env python

import sys

OFFSET = 4
ADD = 1
MULTIPLY = 2
HALT = 99

def process_instruction(opcode, input):
    if opcode[0] == ADD:
        input[opcode[3]] = input[opcode[1]] + input[opcode[2]]
    elif opcode[0] == MULTIPLY:
        input[opcode[3]] = input[opcode[1]] * input[opcode[2]]
    elif opcode[0] == HALT:
        return input
    else:
        raise Exception("Unknown opcode: {}".format(opcode))
    return input

def run(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    for i in range(0, len(memory), 4):
        if i+OFFSET > len(memory):
            break
        memory = process_instruction(memory[i:i+OFFSET], memory)
    print(memory[0])

# Test cases:
#intcode_input = [1,0,0,0,99]
#intcode_input = [2,3,0,3,99]
#intcode_input = [2,4,4,5,99,0]
#intcode_input = [1,1,1,4,99,5,6,0,99]
intcode_input = []
with open("input.txt", 'r') as file:
    intcode_input = [int(x) for x in file.readline().strip("\n").split(",")]

for noun in range(0,100):
    for verb in range(0,100):
        print("noun: {}, verb: {}".format(noun, verb))
        memory = intcode_input.copy()
        run(memory, noun, verb)
    