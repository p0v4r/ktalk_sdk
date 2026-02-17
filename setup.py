from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("LICENSE", "r", encoding="utf-8") as fh:
    license_content = fh.read()

setup(
    name="ktalk-sdk",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Python SDK for KTalk API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ktalk-sdk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "httpx>=0.23.0,<1.0.0",
        "pydantic>=1.10.0,<3.0.0",
        "typing-extensions>=3.10.0; python_version < '3.10'",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "pytest-asyncio>=0.18.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
)