"""
Professional GUI for the Knapsack Problem Solver.
Contains the main GUI application class.

Author: GitHub Copilot
Created: 2025
"""

import customtkinter as ctk
from tkinter import messagebox
from typing import List, Tuple

from models import KnapsackSolver
from utils import InputValidator


class KnapsackGUI:
    """
    Professional GUI for the Knapsack Problem Solver.
    """
    
    def __init__(self):
        self.solver = KnapsackSolver()
        self.validator = InputValidator()
        self.setup_gui()
        
    def setup_gui(self):
        """Initialize and configure the GUI components."""
        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Main window
        self.window = ctk.CTk()
        self.window.title("Professional Knapsack Problem Solver")
        self.window.geometry("800x700")
        self.window.resizable(False, False)
        
        # Configure grid weights
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        
        self.create_header()
        self.create_main_content()
        self.create_footer()
        
    def create_header(self):
        """Create the application header."""
        header_frame = ctk.CTkFrame(self.window)
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        title_label = ctk.CTkLabel(
            header_frame, 
            text="🎒 Knapsack Problem Solver",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=20)
        
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Solve 0/1 and Fractional Knapsack problems with dynamic programming",
            font=ctk.CTkFont(size=14)
        )
        subtitle_label.pack(pady=(0, 10))
        
    def create_main_content(self):
        """Create the main content area."""
        main_frame = ctk.CTkFrame(self.window)
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        main_frame.grid_columnconfigure((0, 1), weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Input section
        self.create_input_section(main_frame)
        
        # Results section
        self.create_results_section(main_frame)
        
    def create_input_section(self, parent):
        """Create the input section."""
        input_frame = ctk.CTkFrame(parent)
        input_frame.grid(row=0, column=0, sticky="ew", padx=(20, 10), pady=20)
        input_frame.grid_columnconfigure(1, weight=1)
        
        # Section title
        input_title = ctk.CTkLabel(
            input_frame, 
            text="📝 Input Parameters",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        input_title.grid(row=0, column=0, columnspan=2, pady=(20, 15))
        
        # Capacity input
        ctk.CTkLabel(input_frame, text="Knapsack Capacity:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, sticky="w", padx=(20, 10), pady=10
        )
        self.capacity_entry = ctk.CTkEntry(input_frame, placeholder_text="e.g., 50")
        self.capacity_entry.grid(row=1, column=1, sticky="ew", padx=(0, 20), pady=10)
        
        # Weights input
        ctk.CTkLabel(input_frame, text="Item Weights:", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, sticky="w", padx=(20, 10), pady=10
        )
        self.weights_entry = ctk.CTkEntry(input_frame, placeholder_text="e.g., 10, 20, 30")
        self.weights_entry.grid(row=2, column=1, sticky="ew", padx=(0, 20), pady=10)
        
        # Values input
        ctk.CTkLabel(input_frame, text="Item Values:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, sticky="w", padx=(20, 10), pady=10
        )
        self.values_entry = ctk.CTkEntry(input_frame, placeholder_text="e.g., 60, 100, 120")
        self.values_entry.grid(row=3, column=1, sticky="ew", padx=(0, 20), pady=10)
        
        # Example button
        example_btn = ctk.CTkButton(
            input_frame, 
            text="📋 Load Example",
            command=self.load_example,
            width=120
        )
        example_btn.grid(row=4, column=0, columnspan=2, pady=15)
        
        # Action buttons
        button_frame = ctk.CTkFrame(input_frame)
        button_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 20))
        button_frame.grid_columnconfigure((0, 1), weight=1)
        
        self.btn_01 = ctk.CTkButton(
            button_frame,
            text="🔢 Solve 0/1 Knapsack",
            command=lambda: self.calculate_knapsack(False),
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.btn_01.grid(row=0, column=0, padx=(0, 5), pady=10, sticky="ew")
        
        self.btn_fractional = ctk.CTkButton(
            button_frame,
            text="⚖️ Solve Fractional Knapsack",
            command=lambda: self.calculate_knapsack(True),
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.btn_fractional.grid(row=0, column=1, padx=(5, 0), pady=10, sticky="ew")
        
    def create_results_section(self, parent):
        """Create the results section."""
        results_frame = ctk.CTkFrame(parent)
        results_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)
        results_frame.grid_rowconfigure(1, weight=1)
        
        # Section title
        results_title = ctk.CTkLabel(
            results_frame, 
            text="📊 Results",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        results_title.grid(row=0, column=0, pady=(20, 15))
        
        # Results display
        self.results_text = ctk.CTkTextbox(
            results_frame,
            wrap="word",
            font=ctk.CTkFont(family="Courier", size=12),
        )
        self.results_text.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.results_text.configure(state="disabled")  # Start in disabled state
        
        # Clear button
        clear_btn = ctk.CTkButton(
            results_frame,
            text="🗑️ Clear Results",
            command=self.clear_results,
            width=120
        )
        clear_btn.grid(row=2, column=0, pady=(0, 20))
        
    def create_footer(self):
        """Create the application footer."""
        footer_frame = ctk.CTkFrame(self.window)
        footer_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(10, 20))
        
        footer_label = ctk.CTkLabel(
            footer_frame,
            text="Professional Knapsack Solver | Built with CustomTkinter",
            font=ctk.CTkFont(size=12)
        )
        footer_label.pack(pady=10)
        
    def append_result(self, text):
        """Append text to results display with proper state management."""
        self.results_text.configure(state="normal")  # Enable editing
        self.results_text.insert("end", text)
        self.results_text.configure(state="disabled")  # Disable editing again
        
    def load_example(self):
        """Load example data for demonstration."""
        self.capacity_entry.delete(0, 'end')
        self.capacity_entry.insert(0, "50")
        
        self.weights_entry.delete(0, 'end')
        self.weights_entry.insert(0, "10, 20, 30")
        
        self.values_entry.delete(0, 'end')
        self.values_entry.insert(0, "60, 100, 120")
        
    def validate_input(self):
        """
        Validate user input and return parsed values.
        
        Returns:
            Tuple of (capacity, weights, values) if valid, None otherwise
        """
        try:
            capacity_text = self.capacity_entry.get()
            weights_text = self.weights_entry.get()
            values_text = self.values_entry.get()
            
            return self.validator.validate_input(capacity_text, weights_text, values_text)
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return None
            
    def calculate_knapsack(self, is_fractional: bool):
        """
        Calculate knapsack solution and display results.
        
        Args:
            is_fractional: True for fractional knapsack, False for 0/1 knapsack
        """
        # Validate input
        validation_result = self.validate_input()
        if validation_result is None:
            return
            
        capacity, weights, values = validation_result
        
        try:
            # Clear previous results
            self.clear_results()
            
            # Display problem details
            problem_type = "Fractional Knapsack" if is_fractional else "0/1 Knapsack"
            self.append_result(f"🎯 {problem_type} Solution\n")
            self.append_result("=" * 40 + "\n\n")
            
            self.append_result(f"📦 Knapsack Capacity: {capacity}\n")
            self.append_result(f"📝 Number of Items: {len(weights)}\n\n")
            
            # Display items table
            self.append_result("📋 Items Information:\n")
            self.append_result("-" * 40 + "\n")
            self.append_result(f"{'Item':<6} {'Weight':<8} {'Value':<8} {'Ratio':<8}\n")
            self.append_result("-" * 40 + "\n")
            
            for i in range(len(weights)):
                ratio = values[i] / weights[i]
                self.append_result(f"{i+1:<6} {weights[i]:<8} {values[i]:<8} {ratio:<8.2f}\n")
            
            self.append_result("\n")
            
            # Solve the problem
            if is_fractional:
                max_value, selected_items = self.solver.solve_fractional_knapsack(capacity, weights, values)
                self.display_fractional_results(max_value, selected_items, weights, values)
            else:
                max_value, selected_items = self.solver.solve_01_knapsack(capacity, weights, values)
                self.display_01_results(max_value, selected_items, weights, values)
                
        except Exception as e:
            messagebox.showerror("Calculation Error", f"An error occurred during calculation: {str(e)}")
            
    def display_01_results(self, max_value: int, selected_items: List[int], weights: List[int], values: List[int]):
        """Display results for 0/1 knapsack."""
        self.append_result("🏆 SOLUTION RESULTS:\n")
        self.append_result("-" * 40 + "\n")
        self.append_result(f"💰 Maximum Value: {max_value}\n")
        self.append_result(f"📦 Selected Items: {[i+1 for i in selected_items]}\n")
        
        total_weight = sum(weights[i] for i in selected_items)
        self.append_result(f"⚖️  Total Weight: {total_weight}\n\n")
        
        if selected_items:
            self.append_result("📋 Selected Items Details:\n")
            self.append_result("-" * 40 + "\n")
            self.append_result(f"{'Item':<6} {'Weight':<8} {'Value':<8}\n")
            self.append_result("-" * 40 + "\n")
            
            for i in selected_items:
                self.append_result(f"{i+1:<6} {weights[i]:<8} {values[i]:<8}\n")
        else:
            self.append_result("ℹ️  No items selected (capacity too small)\n")
            
    def display_fractional_results(self, max_value: float, selected_items: List[Tuple[int, float]], weights: List[int], values: List[int]):
        """Display results for fractional knapsack."""
        self.append_result("🏆 SOLUTION RESULTS:\n")
        self.append_result("-" * 40 + "\n")
        self.append_result(f"💰 Maximum Value: {max_value:.2f}\n")
        
        total_weight = sum(weights[i] * fraction for i, fraction in selected_items)
        self.append_result(f"⚖️  Total Weight: {total_weight:.2f}\n\n")
        
        if selected_items:
            self.append_result("📋 Selected Items Details:\n")
            self.append_result("-" * 50 + "\n")
            self.append_result(f"{'Item':<6} {'Weight':<8} {'Value':<8} {'Fraction':<10}\n")
            self.append_result("-" * 50 + "\n")
            
            for item_index, fraction in selected_items:
                weight_taken = weights[item_index] * fraction
                value_taken = values[item_index] * fraction
                percentage = fraction * 100
                
                self.append_result(f"{item_index+1:<6} {weight_taken:<8.2f} {value_taken:<8.2f} {percentage:<10.1f}%\n")
        else:
            self.append_result("ℹ️  No items selected (capacity too small)\n")
            
    def clear_results(self):
        """Clear the results display."""
        self.results_text.configure(state="normal")
        self.results_text.delete("1.0", "end")
        self.results_text.configure(state="disabled")
        
    def run(self):
        """Start the GUI application."""
        self.window.mainloop()
