# Contributing to Knapsack Problem Solver

Thank you for your interest in contributing to the Knapsack Problem Solver! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

1. **Bug Description**: Clear and concise description of the bug
2. **Steps to Reproduce**: Step-by-step instructions to reproduce the issue
3. **Expected Behavior**: What you expected to happen
4. **Actual Behavior**: What actually happened
5. **Environment**: Python version, OS, and package versions
6. **Screenshots**: If applicable, add screenshots to help explain the problem

### Suggesting Enhancements

We welcome enhancement suggestions! Please create an issue with:

1. **Enhancement Description**: Clear description of the proposed feature
2. **Use Case**: Explain why this enhancement would be useful
3. **Proposed Implementation**: If you have ideas on how to implement it
4. **Alternatives Considered**: Any alternative solutions you've considered

### Pull Requests

1. **Fork the Repository**: Create a fork of the project
2. **Create a Branch**: Create a feature branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Changes**: Implement your changes following the coding standards
4. **Test Your Changes**: Ensure all tests pass and add new tests if needed
5. **Commit Changes**: Use clear, descriptive commit messages
6. **Push to Fork**: Push your changes to your fork
7. **Create Pull Request**: Submit a pull request with a clear description

## 📋 Development Setup

### Prerequisites

- Python 3.7 or higher
- Git

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Knapsack-Solver.git
   cd Knapsack-Solver
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

6. **Run tests**:
   ```bash
   python test_modules.py
   ```

## 🎨 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to all classes and functions
- Use type hints where applicable
- Maximum line length: 88 characters (Black formatter standard)

### Code Structure

- **models/**: Core algorithms and business logic
- **utils/**: Utility functions and helpers
- **gui/**: User interface components
- **tests/**: Test files (when added)

### Commit Message Convention

Use clear, descriptive commit messages:

```
type(scope): description

Examples:
feat(gui): add dark/light theme toggle
fix(algorithm): correct fractional knapsack calculation
docs(readme): update installation instructions
refactor(models): improve algorithm efficiency
```

### Testing

- Add tests for new functionality
- Ensure existing tests continue to pass
- Test on multiple Python versions if possible
- Verify GUI functionality manually

## 🎯 Areas for Contribution

We welcome contributions in these areas:

### 🚀 Features
- [ ] Light/Dark theme toggle
- [ ] Export results to CSV/PDF
- [ ] Algorithm performance visualization
- [ ] Multiple knapsack variants
- [ ] Batch processing of multiple problems
- [ ] Save/Load problem configurations

### 🐛 Bug Fixes
- [ ] Input validation edge cases
- [ ] GUI responsiveness improvements
- [ ] Cross-platform compatibility issues

### 📚 Documentation
- [ ] API documentation
- [ ] Tutorial videos or GIFs
- [ ] Algorithm explanation articles
- [ ] Code examples and use cases

### 🧪 Testing
- [ ] Unit tests for algorithms
- [ ] GUI integration tests
- [ ] Performance benchmarks
- [ ] Cross-platform testing

### 🎨 UI/UX Improvements
- [ ] Accessibility features
- [ ] Improved error messages
- [ ] Better result visualization
- [ ] Mobile-responsive design (if web version)

## 📞 Getting Help

If you need help or have questions:

1. Check existing issues and documentation
2. Create a new issue with the `question` label
3. Be specific about what you're trying to achieve
4. Include relevant code snippets or error messages

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special thanks for major features or bug fixes

Thank you for helping make the Knapsack Problem Solver better! 🎒✨
