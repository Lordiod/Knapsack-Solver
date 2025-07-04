# 🎒 Professional Knapsack Problem Solver

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI/CD](https://github.com/yourusername/Knapsack-Solver/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/yourusername/Knapsack-Solver/actions)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

*A sophisticated GUI application for solving **0/1 Knapsack** and **Fractional Knapsack** problems using dynamic programming and greedy algorithms.*

[Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing) • [Documentation](#-documentation)

</div>

---

## ✨ Features

- **🔢 Dual Algorithm Support**: Solve both 0/1 and Fractional Knapsack problems
- **🎨 Professional GUI**: Modern, dark-themed interface built with CustomTkinter
- **🏗️ Modular Architecture**: Clean separation of concerns with organized code structure
- **📊 Comprehensive Results**: Detailed solution breakdown with item selection details
- **✅ Input Validation**: Robust error handling and user-friendly feedback
- **📋 Example Data**: Quick-load sample data for testing
- **⚡ Real-time Results**: Clear, formatted output with visual organization
- **🌐 Cross-platform**: Works on Windows, macOS, and Linux

## 📁 Project Structure

```
Knapsack-Solver/
├── main.py                 # Entry point for the application
├── models/                 # Core algorithms and data models
│   ├── __init__.py
│   └── knapsack_solver.py  # Knapsack solving algorithms
├── utils/                  # Utility functions and validators
│   ├── __init__.py
│   └── validators.py       # Input validation logic
├── gui/                    # GUI components
│   ├── __init__.py
│   └── knapsack_gui.py     # Main GUI application
├── knapsack_original.py    # Original monolithic version (backup)
├── requirements.txt
└── README.md
```

## 🎬 Demo

<!-- Add a GIF or screenshot here when available -->
<div align="center">
  <img src="docs/images/demo.png" alt="Knapsack Solver Demo" width="800"/>
  <br>
  <em>Professional GUI interface showing knapsack problem solving in action</em>
</div>

> **Note**: Demo images will be added in future releases. The application features a modern dark-themed interface with real-time results display.

## 🚀 Quick Start

### Option 1: Direct Download and Run
```bash
# Clone the repository
git clone https://github.com/yourusername/Knapsack-Solver.git
cd Knapsack-Solver

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 2: Install as Package
```bash
# Install from source
pip install git+https://github.com/yourusername/Knapsack-Solver.git

# Or install in development mode
git clone https://github.com/yourusername/Knapsack-Solver.git
cd Knapsack-Solver
pip install -e .
```

## 📋 Installation

### Prerequisites
- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **Git** (optional) - [Download Git](https://git-scm.com/downloads)

### Step-by-Step Installation

1. **Clone or Download**:
   ```bash
   git clone https://github.com/yourusername/Knapsack-Solver.git
   cd Knapsack-Solver
   ```

2. **Create Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```
```

### Alternative: Running the Original Version
```bash
python knapsack_original.py
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

## 🏗️ Architecture

### Modular Design
The application follows a clean, modular architecture:

- **`models/`**: Contains core business logic and algorithms
  - `KnapsackSolver`: Implements 0/1 and Fractional Knapsack algorithms
- **`utils/`**: Utility functions and validation logic
  - `InputValidator`: Handles input validation and parsing
- **`gui/`**: User interface components
  - `KnapsackGUI`: Main GUI application with all interface logic
- **`main.py`**: Application entry point

### Key Classes
- **KnapsackSolver**: Contains the core algorithms using dynamic programming and greedy approaches
- **InputValidator**: Handles robust input validation with detailed error messages
- **KnapsackGUI**: Manages the user interface and user interactions

### Benefits of Modular Structure
- ✅ **Separation of Concerns**: Each module has a single responsibility
- ✅ **Maintainability**: Easy to modify individual components
- ✅ **Testability**: Components can be tested independently
- ✅ **Reusability**: Algorithms can be used without GUI
- ✅ **Scalability**: Easy to extend with new features

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

## 🧪 Testing

Run the test suite to verify everything works correctly:

```bash
# Run module tests
python test_modules.py

# Test individual components
python -c "from models import KnapsackSolver; print('✅ Models working')"
python -c "from utils import InputValidator; print('✅ Utils working')"
python -c "from gui import KnapsackGUI; print('✅ GUI working')"
```

## 🐛 Troubleshooting

### Common Issues

**ImportError: No module named 'customtkinter'**
```bash
pip install customtkinter
```

**GUI doesn't appear on Linux**
```bash
# Install tkinter if missing
sudo apt-get install python3-tk
```

**Performance issues with large datasets**
- The application is optimized for educational use
- For very large datasets (>1000 items), consider using the algorithms programmatically

## 📚 Documentation

- [Algorithm Explanation](docs/algorithms.md) *(Coming Soon)*
- [API Reference](docs/api.md) *(Coming Soon)*
- [Contributing Guide](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## 🏆 Features Roadmap

### Planned Features
- [ ] 🎨 Light/Dark theme toggle
- [ ] 📊 Algorithm performance visualization
- [ ] 📁 Save/Load problem configurations
- [ ] 📈 Batch processing multiple problems
- [ ] 🌐 Web-based version
- [ ] 📱 Mobile-responsive design
- [ ] 🔧 Advanced algorithm variants

### Completed Features
- [x] ✅ 0/1 Knapsack algorithm
- [x] ✅ Fractional Knapsack algorithm
- [x] ✅ Professional GUI interface
- [x] ✅ Input validation
- [x] ✅ Modular architecture
- [x] ✅ Cross-platform compatibility

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🐛 Report Bugs**: [Create an issue](https://github.com/yourusername/Knapsack-Solver/issues/new?template=bug_report.md)
2. **💡 Suggest Features**: [Request a feature](https://github.com/yourusername/Knapsack-Solver/issues/new?template=feature_request.md)
3. **🔧 Submit Code**: [Create a pull request](https://github.com/yourusername/Knapsack-Solver/compare)

Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and development process.

## 📞 Support

- 📖 [Documentation](https://github.com/yourusername/Knapsack-Solver#readme)
- 🐛 [Issue Tracker](https://github.com/yourusername/Knapsack-Solver/issues)
- 💬 [Discussions](https://github.com/yourusername/Knapsack-Solver/discussions)

## 👥 Contributors

Thanks to all contributors who have helped make this project better!

<!-- Contributors list will be auto-updated -->
<a href="https://github.com/yourusername/Knapsack-Solver/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yourusername/Knapsack-Solver" />
</a>

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/Knapsack-Solver&type=Date)](https://star-history.com/#yourusername/Knapsack-Solver&Date)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CustomTkinter** - For the modern GUI framework
- **Python Community** - For the amazing ecosystem
- **Contributors** - For making this project better

---

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

[Report Bug](https://github.com/yourusername/Knapsack-Solver/issues) • [Request Feature](https://github.com/yourusername/Knapsack-Solver/issues) • [Contribute](CONTRIBUTING.md)

**Built with ❤️ using Python and CustomTkinter**

</div>
