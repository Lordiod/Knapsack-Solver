# 🎒 Professional Knapsack Problem Solver

A sophisticated GUI application for solving **0/1 Knapsack** and **Fractional Knapsack** problems using dynamic programming and greedy algorithms.

## ✨ Features

- **Dual Algorithm Support**: Solve both 0/1 and Fractional Knapsack problems
- **Professional GUI**: Modern, dark-themed interface built with CustomTkinter
- **Comprehensive Results**: Detailed solution breakdown with item selection details
- **Input Validation**: Robust error handling and user-friendly feedback
- **Example Data**: Quick-load sample data for testing
- **Real-time Results**: Clear, formatted output with visual organization

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Required packages (install via pip):

```bash
pip install customtkinter
```

### Running the Application
```bash
python knapsack.py
```

## 📖 Usage

1. **Enter Input Data**:
   - **Capacity**: Maximum weight the knapsack can hold
   - **Weights**: Comma-separated list of item weights (e.g., `10, 20, 30`)
   - **Values**: Comma-separated list of item values (e.g., `60, 100, 120`)

2. **Load Example**: Click "📋 Load Example" to populate with sample data

3. **Choose Algorithm**:
   - **🔢 0/1 Knapsack**: Items can only be taken completely (0 or 1)
   - **⚖️ Fractional Knapsack**: Items can be taken partially

4. **View Results**: Detailed solution appears in the results panel

## 🧮 Algorithms

### 0/1 Knapsack (Dynamic Programming)
- **Time Complexity**: O(n × W) where n is number of items and W is capacity
- **Space Complexity**: O(n × W)
- **Use Case**: When items cannot be divided

### Fractional Knapsack (Greedy Algorithm)
- **Time Complexity**: O(n log n) due to sorting
- **Space Complexity**: O(1)
- **Use Case**: When items can be divided into fractions

## 🎯 Example

**Input:**
- Capacity: 50
- Weights: 10, 20, 30
- Values: 60, 100, 120

**0/1 Knapsack Output:**
- Maximum Value: 220
- Selected Items: [2, 3]
- Total Weight: 50

**Fractional Knapsack Output:**
- Maximum Value: 240.00
- Items taken: Item 3 (100%), Item 2 (100%), Item 1 (0%)

## 🛠️ Technical Details

### Project Structure
```
Knapsack-Solver/
├── knapsack.py          # Main application file
├── README.md           # Project documentation
```

### Key Classes
- **KnapsackSolver**: Contains the core algorithms
- **KnapsackGUI**: Manages the user interface and user interactions

### Features Implemented
- ✅ Professional error handling
- ✅ Type hints for better code documentation
- ✅ Modular class-based architecture
- ✅ Comprehensive input validation
- ✅ Detailed result formatting
- ✅ Modern UI with CustomTkinter

## 🎨 UI Features

- **Dark Theme**: Professional appearance
- **Responsive Layout**: Adapts to window resizing
- **Clear Organization**: Separate input and results sections
- **Visual Feedback**: Icons and formatted text for better UX
- **Error Messages**: User-friendly error dialogs

## 🧪 Testing

The application includes built-in example data for testing:
- Capacity: 50
- Weights: [10, 20, 30]  
- Values: [60, 100, 120]

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Built with ❤️ using Python and CustomTkinter**
