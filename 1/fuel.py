#!/usr/bin/env python

input_lines = []
with open("input.txt", 'r') as file:
    input_lines = [line.rstrip('\n') for line in file]

total_fuel = 0
for mass in input_lines:
    fuel_required = int(int(mass)/3) - 2
    total_fuel += fuel_required

print(total_fuel)