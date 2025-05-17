# API Testing Framework - GitHub Setup Guide

## Repository Setup

1. **Initialize Git Repository**
   ```bash
   git init
   ```

2. **Create .gitignore File**
   Create a `.gitignore` file with the following contents:
   ```
   # Python
   __pycache__/
   *.py[cod]
   *$py.class
   *.so
   .Python
   build/
   develop-eggs/
   dist/
   download/
   eggs/
   .eggs/
   lib/
   lib64/
   parts/
   sdist/
   var/
   wheels/
   *.egg-info/
   .installed.cfg
   *.egg

   # Virtual Environment
   venv/
   env/
   ENV/

   # IDE
   .idea/
   .vscode/
   *.swp
   *.swo

   # Test Reports
   report.html
   .pytest_cache/
   ```

3. **Initial Commit**
   ```bash
   git add .
   git commit -m "Initial commit: API Testing Framework setup"
   ```

4. **Create GitHub Repository**
   - Go to GitHub.com
   - Click "New repository"
   - Name it "api-testing-framework"
   - Don't initialize with README (we already have one)
   - Click "Create repository"

5. **Link Local Repository to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/api-testing-framework.git
   git branch -M main
   git push -u origin main
   ```

## Project Structure
```
api-testing-framework/
├── api_objects/         # Page Object Models for API endpoints
├── config/             # Configuration files
├── tests/              # Test files
├── utils/              # Utility functions
├── requirements.txt    # Project dependencies
├── setup.py           # Package setup file
├── pytest.ini         # Pytest configuration
└── README.md          # Project documentation
```

## Development Workflow

1. **Create a New Branch**
   ```bash
   git checkout -b feature/new-test-case
   ```

2. **Make Changes and Commit**
   ```bash
   git add .
   git commit -m "Add new test case for user API"
   ```

3. **Push Changes**
   ```bash
   git push origin feature/new-test-case
   ```

4. **Create Pull Request**
   - Go to GitHub repository
   - Click "Compare & pull request"
   - Add description of changes
   - Request review if needed
   - Click "Create pull request"

## Running Tests

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Tests**
   ```bash
   pytest
   ```

3. **Generate HTML Report**
   ```bash
   pytest --html=report.html
   ```

## Best Practices

1. **Branch Naming**
   - feature/feature-name
   - bugfix/bug-description
   - hotfix/issue-description

2. **Commit Messages**
   - Use present tense
   - Be descriptive but concise
   - Reference issue numbers if applicable

3. **Code Review**
   - Review all pull requests
   - Ensure tests pass
   - Check code style and documentation

4. **Version Control**
   - Keep commits atomic and focused
   - Don't commit sensitive data
   - Use meaningful commit messages

## CI/CD Setup (Optional)

1. **GitHub Actions**
   Create `.github/workflows/test.yml`:
   ```yaml
   name: API Tests
   on: [push, pull_request]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.9'
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt
       - name: Run tests
         run: |
           pytest
   ```

## Troubleshooting

1. **Merge Conflicts**
   ```bash
   git fetch origin
   git merge origin/main
   # Resolve conflicts
   git add .
   git commit -m "Resolve merge conflicts"
   ```

2. **Reset Changes**
   ```bash
   git reset --hard HEAD
   ```

3. **Update Dependencies**
   ```bash
   pip freeze > requirements.txt
   git add requirements.txt
   git commit -m "Update dependencies"
   ```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 