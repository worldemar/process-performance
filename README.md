![Python test and lint](https://github.com/worldemar/process-performance/workflows/Python%20test%20and%20lint/badge.svg)
[![codecov](https://codecov.io/gh/worldemar/process-performance/branch/master/graph/badge.svg?token=W8XKDQ2YIC)](https://codecov.io/gh/worldemar/process-performance)

# Process performance analysis tool

## What

Python-based tool to facilitate finding optimal parameters for executable.

## Why

There are situations when optimal parameters of certain process is unclear. Notable examples are:
- Packing firmware for embedded devices
  
  - There are several options that control both speed of compression and final firmware size
  
  - For production environment it may be beneficial to have smallest possible firmware in order to reduce flashing time, but wasting hours of CI time for it may not be desirable
  
  - For development environment it may be beneficial to have shortest packaging time to reduce testing time, but resulting firmware could be too big to efficiantly handle
  
  All of those factors require finding "sweet spot" within all possible compression flags combinations.

- Archiving specific content
  
  There is no guarantee that archiver will find best possible algorithm for compressing your data and meet requrements of compression time and file size.

- Compiling specific code
  
  Since there are many options for optimising C/C++ code, it may be time consuming to find optimal ones for your specific code. As an example, try to answer "When `-O3` is better than `-Os`?".

## How it works

(write this once refactor is complete)

## Usage example

(example usage here)
