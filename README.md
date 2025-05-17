# API Testing Framework with Python, Pytest, and Playwright

A comprehensive API testing framework for testing the Automation Exercise API using Python, Pytest, and Playwright.

## 🚀 Features

- Page Object Model (POM) pattern implementation
- Comprehensive test coverage
- HTML test reports
- CI/CD integration with GitHub Actions
- Environment-based configuration
- Detailed logging and debugging

## 📋 Test Cases

### 1. User API Tests
#### Registration Tests
- ✅ Test successful user registration
- ✅ Test registration with existing email
- ✅ Test registration with invalid data

#### Login Tests
- ✅ Test successful user login
- ✅ Test login with invalid credentials
- ✅ Test login with non-existent user

### 2. Products and Brands Tests
#### Product Tests
- ✅ Test get all products
- ✅ Test get product by ID
- ✅ Test search products
- ✅ Test product details validation

#### Brand Tests
- ✅ Test get all brands
- ✅ Test get brand by ID
- ✅ Test brand details validation

### 3. Response Debug Tests
- ✅ Test response headers
- ✅ Test response time
- ✅ Test response format
- ✅ Test error handling

## 🛠️ Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/sqaesabbir/AutomationexerciseApiTestsPython.git
cd AutomationexerciseApiTestsPython
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test Categories
```bash
# Run user tests
pytest tests/test_user_operations.py

# Run product tests
pytest tests/test_products_and_brands.py

# Run debug tests
pytest tests/test_response_debug.py
```

### Generate HTML Report
```bash
pytest --html=report.html
```

## 📁 Project Structure
```
api-testing-framework/
├── api_objects/         # Page Object Models
│   ├── user_api.py
│   ├── products_api.py
│   └── brands_api.py
├── config/             # Configuration files
│   └── constants.py
├── tests/              # Test files
│   ├── test_user_operations.py
│   ├── test_products_and_brands.py
│   └── test_response_debug.py
├── utils/              # Utility functions
│   └── api_helpers.py
├── requirements.txt    # Project dependencies
└── pytest.ini         # Pytest configuration
```

## 🔧 Environment Variables

Create a `.env` file in the root directory with:
```
BASE_URL=https://automationexercise.com/api
TEST_USER_EMAIL=your_test_email@example.com
TEST_USER_PASSWORD=your_test_password
```

## 📊 Test Reports

After running tests, view the HTML report:
1. Open `report.html` in your browser
2. View detailed test results
3. Check test execution time
4. Review any failures or errors

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Sabbir Hossain** - *Initial work* - [sqaesabbir](https://github.com/sqaesabbir)

## 🙏 Acknowledgments

- Automation Exercise API for providing the test environment
- Python community for excellent testing tools
- Playwright team for the amazing automation framework 