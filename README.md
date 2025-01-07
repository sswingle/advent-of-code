# Advent of Code Solutions

This repository contains my solutions to [Advent of Code](https://adventofcode.com/) challenges. Advent of Code is an annual programming event where participants solve two coding puzzles each day from December 1st to December 25th.

## Repository Structure

Solutions are organized by day, with each solution in its own Python file:
- `day01.py` contains solutions for Day 1
- `day02.py` contains solutions for Day 2
- etc.

Some days might have multiple solution files (e.g., `day18.py` and `day18b.py`) representing different approaches or iterations of the solution.

Each solution file typically contains code for both Part 1 and Part 2 of that day's challenge.

## Dependencies

The solutions use various Python libraries including:
- Standard libraries:
  - `heapq`
  - `itertools`
- Third-party libraries:
  - `networkx`
  - `more_itertools`

To install the required third-party libraries:
```bash
pip install networkx more-itertools
```

## Running the Solutions

1. Make sure you have Python installed
2. Install the required dependencies
3. Download your puzzle input from the Advent of Code website
4. Save your input as `input.txt` in the same directory as the solution
5. Run the solution for a specific day:
   ```bash
   python dayXX.py
   ```
   Replace `XX` with the day number (e.g., `day01.py` for Day 1)

## Input Files

Each puzzle requires a personal input file that you can get from the Advent of Code website. These input files are not included in this repository as they are unique to each participant. Save your input as `input.txt` in the same directory as the solution you want to run.

## Solution Complexity

The solutions vary in complexity:
- Earlier days (like Day 1) tend to be straightforward and use basic Python features
- Later days often involve more complex algorithms and data structures, using libraries like `networkx` for graph problems
- Some days have multiple solution attempts or optimizations (e.g., Day 18)

## About Advent of Code

[Advent of Code](https://adventofcode.com/) is an annual coding event created by Eric Wastl. Each day from December 1st through December 25th, participants are presented with two puzzles that can be solved using programming skills. The puzzles get progressively more challenging as the month goes on.

The event is free to participate in and is a great way to:
- Practice problem-solving skills
- Learn a new programming language
- Compete with friends and colleagues
- Have fun with programming challenges