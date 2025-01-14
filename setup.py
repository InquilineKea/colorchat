from setuptools import setup, find_packages

setup(
    name="colorchat",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0.0",
        "pycryptodome>=3.10.0",
        "gitpython>=3.1.0",
        "python-dotenv>=0.19.0",
    ],
    python_requires=">=3.8",
)
