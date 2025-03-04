"""
This module houses the Heuristics class, which provides smart selection strategies for deciding where to place tiles. 
It implements approaches like Minimum Remaining Values (MRV), which prioritizes working with the most restricted areas first. 
By identifying the most constrained squares, these heuristics help make the search process more efficient.
"""

from typing import List
from operator import attrgetter
from Square import Square

class Heuristics:
    """
    This class encapsulates the heuristic strategies for tile placement in the CSP problem.
    """

    def __init__(self, squares: List['Square']):
        """
        Initializes the Heuristics class with a list of Square objects, sorted by the number
        of bushes in descending order.
        
        Args:
            squares (List[Square]): List of Square objects.
        """
        # Sorting squares by NumberOfBushes in descending order
        self.squares = sorted(squares, key=attrgetter('number_of_bushes'), reverse=True)

    def get_mrv(self) -> 'Square':
        """
        Returns the square with the least number of remaining values (tiles) 
        that hasn't been assigned a tile (MRV heuristic).
        
        Returns:
            Square: The square with the least remaining values (tiles).
                    Returns None if no unassigned squares are available.
        """
        # Filter squares that haven't been assigned a tile
        unassigned_squares = [square for square in self.squares if square.assigned_tile is None]

        # If no unassigned squares are found, return None
        if not unassigned_squares:
            return None
        
        # Sort by remaining available tiles, number of bushes (descending), and position
        unassigned_squares.sort(key=lambda square: (len(square.available_tiles), 
                                                    -square.number_of_bushes, 
                                                    square.x, square.y))

        # Return the square with the least available tiles (MRV)
        return unassigned_squares[0]