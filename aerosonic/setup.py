from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aerosonic-weather",
    version="1.0.0",
    author="Hugo Paquete",
    author_email="hugopaquete@ua.pt",
    description="Simple weather client for developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HugoPaquete/Aerosonic-weather-client",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=["requests>=2.28.0"],
)
