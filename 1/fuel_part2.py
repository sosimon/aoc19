#!/usr/bin/env python

def fuel_required(mass):
    fuel = int(int(mass)/3) - 2
    if int(mass) <= 0 or fuel <= 0:
        return 0
    else:
        return fuel + fuel_required(fuel)

input_lines = []
with open("input.txt", 'r') as file:
    input_lines = [line.rstrip('\n') for line in file]

total_fuel = 0
for mass in input_lines:
    total_fuel += fuel_required(mass)

print(total_fuel)