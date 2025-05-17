from setuptools import setup, find_packages

setup(
    name="api_testing_framework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest==8.0.0",
        "pytest-playwright==0.4.4",
        "requests==2.31.0",
        "python-dotenv==1.0.0",
        "pytest-html==4.1.1"
    ],
) 