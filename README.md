# Project 2 – CSP –Tile Placement Task Description
Given
You are given a landscape on which certain “bushes” grow, marked by colors: 1, 2, 3, 4.
The landscape is of square shape, so, it might be 100 x 100 or 200 x 200 etc.
You are given a set of “tiles” which are of three different shapes. The tiles are 4 x 4.  One tile only covers part of the landscape.  Here are the shapes :

Full Block: A “full block” tile covers the full 4 x 4 area, and no bush is then visible in that patch.
An “outer boundary” tile covers the outer boundary of the 4 x 4 area, and any bush in the middle part is visible.
An “EL” shaped tile covers only two sides of the area.
You are given a “target” of which bushes should be visible after you have finished placing the tiles.
Observations
The total tiles cover the entire landscape.  However, depending on which tiles are placed where, different parts of the landscape, and hence different bushes are visible.
The number of tiles equals the size of the area divided by the size of tile.  So, for 20 x 20 landscape, you are given 25 tiles.
Input Files
Structure of the input file is as follows.

Landscape is given in a space delimited, new line separated.
Tiles in terms of counts by different shapes.
Target of how many different bushes should be visible.
Many input files can be found at 
`https://github.com/amrinderarora/ai/tree/master/src/main/resources/csp/tileplacement`

More input files can be generated using `https://github.com/amrinderarora/ai/blob/master/src/main/java/edu/gwu/cs/ai/csp/tileplacement/TilePlacementProblemGenerator.java`

Algorithm
Write a CSP algorithm to solve this problem.  The CSP algorithm should have the following components:

Search algorithm to solve the CSP
Heuristics (min remaining values, least constraining value, tie breaking rules)
Constraint propagation using AC3.

# Tile Placement CSP Solution

## Overview
This repository implements an advanced constraint satisfaction problem (CSP) solver designed specifically for tile placement challenges. The system efficiently arranges tiles of specific dimensions (4×4) on a landscape while ensuring that predefined bush visibility requirements are met for each color.

## Project Architecture

### State Management (`State.py`)
This module contains the `State` class which manages the current configuration of the 4×4 grid segments. Key features include:
- State initialization with reference pointers
- Deep and shallow copy mechanisms for state preservation during backtracking
- State transition handling for the solver algorithm

### Environment Representation (`Landscape.py`)
The `Landscape` class serves as the foundation for the problem environment:
- Input parsing and validation capabilities
- Grid construction and segmentation into 4×4 squares
- Bush distribution tracking across the landscape
- Section management for tile placement operations

### Grid Segments (`Square.py`)
The `Square` class represents individual 4×4 segments of the landscape:
- Bush counting and visibility tracking
- Implementation of the Least Constraining Value (LCV) heuristic
- Neighboring segment relationship management
- Constraint validation for potential tile placements

### Solution Engine (`Solver.py`)
The `Solver` class implements the core solution algorithm:
- Backtracking search with forward checking
- Constraint propagation mechanisms
- Tile assignment and validation procedures
- Solution path reconstruction

### Search Optimization (`Heuristics.py`)
The `Heuristics` class provides performance-enhancing algorithms:
- Minimum Remaining Values (MRV) implementation for variable ordering
- Domain reduction techniques
- Decision optimization for the backtracking process

## Algorithmic Approach

### Primary Solution Method
The solver employs a sophisticated backtracking algorithm enhanced with modern CSP techniques:

1. **Variable Selection Strategy**  
   The system dynamically selects the next grid segment using the MRV heuristic, prioritizing segments with the most restricted options to reduce branching.

2. **Value Ordering Optimization**  
   For each selected segment, the LCV heuristic determines the optimal tile placement by evaluating which placement least restricts future assignments.

3. **Constraint Propagation**  
   Arc consistency (AC-3) is implemented to proactively identify and eliminate invalid assignments before they're fully explored, dramatically reducing the search space.

4. **Decision Resolution Protocol**  
   When multiple equally valid options exist, specialized tie-breaking procedures ensure deterministic behavior while maintaining solution optimality.

## Usage Instructions

### Executing the Solver
To run the solver with an input specification:
```bash
python src/main.py input/input1.txt
```
The output will be directed to the `output` directory with a corresponding filename.

### Testing Framework
Comprehensive testing is available through the unit test suite:
```bash
python -m unittest src/test_csp.py
```
This validates the correct operation of individual components and their interactions.

## Performance Considerations
- The implementation prioritizes search efficiency through strategic heuristic application
- Memory usage is optimized through careful state management
- The solution scales effectively with increasing problem complexity
