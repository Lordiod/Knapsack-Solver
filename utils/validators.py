"""
Input Validation Utilities
Contains utility functions for validating user input.

Author: GitHub Copilot
Created: 2025
"""

from typing import List, Tuple, Optional
import re


class InputValidator:
    """
    A class containing validation methods for user input.
    """
    
    @staticmethod
    def validate_input(capacity_text: str, weights_text: str, values_text: str) -> Optional[Tuple[int, List[int], List[int]]]:
        """
        Validate user input and return parsed values.
        
        Args:
            capacity_text: Text input for capacity
            weights_text: Text input for weights
            values_text: Text input for values
        
        Returns:
            Tuple of (capacity, weights, values) if valid, None otherwise
        """
        try:
            # Validate capacity
            capacity_text = capacity_text.strip()
            if not capacity_text:
                raise ValueError("Capacity cannot be empty")
            capacity = int(capacity_text)
            if capacity <= 0:
                raise ValueError("Capacity must be positive")
                
            # Validate weights
            weights_text = weights_text.strip()
            if not weights_text:
                raise ValueError("Weights cannot be empty")
            weights = [int(x.strip()) for x in re.split(r'[,\s]+', weights_text) if x.strip()]
            if not weights:
                raise ValueError("No valid weights found")
            if any(w <= 0 for w in weights):
                raise ValueError("All weights must be positive")
                
            # Validate values
            values_text = values_text.strip()
            if not values_text:
                raise ValueError("Values cannot be empty")
            values = [int(x.strip()) for x in re.split(r'[,\s]+', values_text) if x.strip()]
            if not values:
                raise ValueError("No valid values found")
            if any(v <= 0 for v in values):
                raise ValueError("All values must be positive")
                
            # Check if weights and values have same length
            if len(weights) != len(values):
                raise ValueError(f"Number of weights ({len(weights)}) must equal number of values ({len(values)})")
                
            return capacity, weights, values
            
        except ValueError as e:
            raise ValueError(str(e))
