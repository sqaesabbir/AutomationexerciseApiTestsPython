# API Test Documentation

## Overview
This documentation describes the test cases implemented in the API testing framework using Python, Pytest, and Playwright. The framework follows the Page Object Model (POM) pattern for better organization and maintainability.

## Test Categories

### 1. User API Tests (`tests/test_user_operations.py`)

#### User Registration Tests
1. **Test Successful User Registration**
   - Description: Verifies that a new user can be registered successfully
   - Test Steps:
     1. Create user registration payload
     2. Send POST request to registration endpoint
     3. Verify response status code is 200
     4. Verify response contains success message
     5. Verify user data is returned correctly

2. **Test User Registration with Existing Email**
   - Description: Verifies that registration fails when using an existing email
   - Test Steps:
     1. Create user registration payload with existing email
     2. Send POST request to registration endpoint
     3. Verify response status code is 400
     4. Verify error message indicates email already exists

#### User Login Tests
1. **Test Successful User Login**
   - Description: Verifies that a user can login successfully
   - Test Steps:
     1. Create login payload with valid credentials
     2. Send POST request to login endpoint
     3. Verify response status code is 200
     4. Verify response contains user token
     5. Verify user data is returned correctly

2. **Test Login with Invalid Credentials**
   - Description: Verifies that login fails with invalid credentials
   - Test Steps:
     1. Create login payload with invalid credentials
     2. Send POST request to login endpoint
     3. Verify response status code is 401
     4. Verify error message indicates invalid credentials

### 2. Products and Brands Tests (`tests/test_products_and_brands.py`)

#### Product Tests
1. **Test Get All Products**
   - Description: Verifies that all products can be retrieved
   - Test Steps:
     1. Send GET request to products endpoint
     2. Verify response status code is 200
     3. Verify response contains list of products
     4. Verify each product has required fields

2. **Test Get Product by ID**
   - Description: Verifies that a specific product can be retrieved by ID
   - Test Steps:
     1. Send GET request to product endpoint with specific ID
     2. Verify response status code is 200
     3. Verify response contains correct product data
     4. Verify all product fields are present

3. **Test Search Products**
   - Description: Verifies that products can be searched
   - Test Steps:
     1. Send GET request to search endpoint with search term
     2. Verify response status code is 200
     3. Verify response contains matching products
     4. Verify search results are relevant

#### Brand Tests
1. **Test Get All Brands**
   - Description: Verifies that all brands can be retrieved
   - Test Steps:
     1. Send GET request to brands endpoint
     2. Verify response status code is 200
     3. Verify response contains list of brands
     4. Verify each brand has required fields

2. **Test Get Brand by ID**
   - Description: Verifies that a specific brand can be retrieved by ID
   - Test Steps:
     1. Send GET request to brand endpoint with specific ID
     2. Verify response status code is 200
     3. Verify response contains correct brand data
     4. Verify all brand fields are present

### 3. Response Debug Tests (`tests/test_response_debug.py`)

1. **Test Response Headers**
   - Description: Verifies that response headers are correct
   - Test Steps:
     1. Send request to any endpoint
     2. Verify response contains expected headers
     3. Verify header values are correct

2. **Test Response Time**
   - Description: Verifies that response time is within acceptable limits
   - Test Steps:
     1. Send request to endpoint
     2. Measure response time
     3. Verify response time is within threshold

3. **Test Response Format**
   - Description: Verifies that response format is correct
   - Test Steps:
     1. Send request to endpoint
     2. Verify response is valid JSON
     3. Verify response structure matches expected schema

## Test Data Management

### Test Data Setup
- Test data is managed in the `config/constants.py` file
- Each test category has its own test data section
- Test data includes both valid and invalid scenarios

### Test Data Cleanup
- Tests are designed to be independent
- Each test cleans up after itself
- No test depends on the state from previous tests

## Test Execution

### Running All Tests
```bash
pytest
```

### Running Specific Test Categories
```bash
# Run user tests only
pytest tests/test_user_operations.py

# Run product tests only
pytest tests/test_products_and_brands.py

# Run debug tests only
pytest tests/test_response_debug.py
```

### Running with HTML Report
```bash
pytest --html=report.html
```

## Test Environment

### Required Environment Variables
- `BASE_URL`: Base URL of the API
- `API_KEY`: API key for authentication (if required)
- `TEST_USER_EMAIL`: Test user email
- `TEST_USER_PASSWORD`: Test user password

### Environment Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Best Practices

1. **Test Independence**
   - Each test should be independent
   - Tests should not depend on each other
   - Tests should clean up after themselves

2. **Test Data Management**
   - Use meaningful test data
   - Avoid hardcoding test data in tests
   - Use data factories where appropriate

3. **Assertions**
   - Use specific assertions
   - Verify both positive and negative scenarios
   - Include meaningful assertion messages

4. **Error Handling**
   - Test error scenarios
   - Verify error messages
   - Handle exceptions appropriately

5. **Documentation**
   - Keep test documentation up to date
   - Document test prerequisites
   - Document test data requirements

## Maintenance

### Adding New Tests
1. Create test file in `tests` directory
2. Follow existing naming conventions
3. Add test documentation
4. Update this documentation

### Updating Existing Tests
1. Update test implementation
2. Update test documentation
3. Verify test still passes
4. Update this documentation if needed

## Troubleshooting

### Common Issues
1. **Test Failures**
   - Check test data
   - Verify API is accessible
   - Check environment variables
   - Review test logs

2. **Environment Issues**
   - Verify virtual environment is activated
   - Check dependencies are installed
   - Verify environment variables are set

3. **API Issues**
   - Verify API is running
   - Check API documentation
   - Verify API endpoints are correct

## Support

For any issues or questions:
1. Check the test documentation
2. Review test logs
3. Check API documentation
4. Contact the development team 