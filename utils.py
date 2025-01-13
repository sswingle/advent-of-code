from pathlib import Path
from typing import List, Union, Dict, Tuple
from collections import Counter


def read_input_lines(day: int) -> List[str]:
    """Read input.txt for given day and return list of lines"""
    day_str = str(day).zfill(2)
    with open(f"input/day{day_str}.txt") as f:
        return f.readlines()


def read_input_ints(day: int) -> List[int]:
    """Read input.txt for given day and return list of integers"""
    return [int(line) for line in read_input_lines(day)]


def read_input_int_csv(day: int) -> List[int]:
    """Read input.txt for given day and return list of integers from comma-separated values"""
    day_str = str(day).zfill(2)
    with open(f"input/day{day_str}.txt") as f:
        return [int(x) for x in f.read().split(",")]


class Point:
    """2D point with common operations"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def manhattan_distance(self, other: 'Point' = None) -> int:
        """Calculate Manhattan distance from origin or another point"""
        if other is None:
            return abs(self.x) + abs(self.y)
        return abs(self.x - other.x) + abs(self.y - other.y)


class IntcodeComputer:
    """Computer for running intcode programs"""
    def __init__(self, program: List[int]):
        self.memory = list(program)  # Make a copy to avoid modifying original
        self.ip = 0  # instruction pointer
    
    def get_param_address(self, param_num: int, instruction: int) -> int:
        """Get the address for a parameter based on its mode"""
        mode = (instruction // 10 ** (1 + param_num)) % 10
        if mode == 0:  # position mode
            return self.memory[self.ip + param_num]
        elif mode == 1:  # immediate mode
            return self.ip + param_num
        else:
            raise ValueError(f"Invalid parameter mode: {mode}")
    
    def run(self, inputs: List[int] = None) -> List[int]:
        """Run the program with optional inputs. Returns list of outputs."""
        if inputs is None:
            inputs = []
        input_pointer = 0
        outputs = []
        
        while True:
            instruction = self.memory[self.ip]
            opcode = instruction % 100
            
            if opcode == 1:  # add
                a = self.memory[self.get_param_address(1, instruction)]
                b = self.memory[self.get_param_address(2, instruction)]
                self.memory[self.get_param_address(3, instruction)] = a + b
                self.ip += 4
            elif opcode == 2:  # multiply
                a = self.memory[self.get_param_address(1, instruction)]
                b = self.memory[self.get_param_address(2, instruction)]
                self.memory[self.get_param_address(3, instruction)] = a * b
                self.ip += 4
            elif opcode == 3:  # input
                if input_pointer >= len(inputs):
                    raise ValueError("Not enough inputs provided")
                self.memory[self.get_param_address(1, instruction)] = inputs[input_pointer]
                input_pointer += 1
                self.ip += 2
            elif opcode == 4:  # output
                outputs.append(self.memory[self.get_param_address(1, instruction)])
                self.ip += 2
            elif opcode == 5:  # jump-if-true
                if self.memory[self.get_param_address(1, instruction)] != 0:
                    self.ip = self.memory[self.get_param_address(2, instruction)]
                else:
                    self.ip += 3
            elif opcode == 6:  # jump-if-false
                if self.memory[self.get_param_address(1, instruction)] == 0:
                    self.ip = self.memory[self.get_param_address(2, instruction)]
                else:
                    self.ip += 3
            elif opcode == 7:  # less than
                a = self.memory[self.get_param_address(1, instruction)]
                b = self.memory[self.get_param_address(2, instruction)]
                self.memory[self.get_param_address(3, instruction)] = int(a < b)
                self.ip += 4
            elif opcode == 8:  # equals
                a = self.memory[self.get_param_address(1, instruction)]
                b = self.memory[self.get_param_address(2, instruction)]
                self.memory[self.get_param_address(3, instruction)] = int(a == b)
                self.ip += 4
            elif opcode == 99:  # halt
                break
            else:
                raise ValueError(f"Invalid opcode: {opcode}")
        
        return outputs