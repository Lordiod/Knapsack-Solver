"""
Knapsack Problem Solver Algorithms
Contains the core algorithms for solving knapsack problems.

Author: GitHub Copilot
Created: 2025
"""

from typing import List, Tuple


class KnapsackSolver:
    """
    A class containing algorithms for solving knapsack problems.
    """
    
    @staticmethod
    def solve_01_knapsack(capacity: int, weights: List[int], values: List[int]) -> Tuple[int, List[int]]:
        """
        Solve the 0/1 Knapsack problem using dynamic programming.
        
        Args:
            capacity: Maximum weight capacity of the knapsack
            weights: List of item weights
            values: List of item values
            
        Returns:
            Tuple containing (maximum_value, selected_item_indices)
        """
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i - 1] <= w:
                    dp[i][w] = max(
                        values[i - 1] + dp[i - 1][w - weights[i - 1]], 
                        dp[i - 1][w]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]

        # Backtrack to find selected items
        selected_items = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_items.append(i - 1)
                w -= weights[i - 1]

        selected_items.reverse()
        return dp[n][capacity], selected_items

    @staticmethod
    def solve_fractional_knapsack(capacity: int, weights: List[int], values: List[int]) -> Tuple[float, List[Tuple[int, float]]]:
        """
        Solve the Fractional Knapsack problem using greedy approach.
        
        Args:
            capacity: Maximum weight capacity of the knapsack
            weights: List of item weights
            values: List of item values
            
        Returns:
            Tuple containing (maximum_value, selected_items_with_fractions)
        """
        n = len(weights)
        items = [(i, weights[i], values[i], values[i] / weights[i]) for i in range(n)]
        items.sort(key=lambda x: x[3], reverse=True)  # Sort by value-to-weight ratio

        max_value = 0.0
        selected_items = []
        remaining_capacity = capacity

        for item_index, weight, value, ratio in items:
            if remaining_capacity >= weight:
                # Take the whole item
                max_value += value
                selected_items.append((item_index, 1.0))
                remaining_capacity -= weight
            elif remaining_capacity > 0:
                # Take fraction of the item
                fraction = remaining_capacity / weight
                max_value += value * fraction
                selected_items.append((item_index, fraction))
                break

        return max_value, selected_items
