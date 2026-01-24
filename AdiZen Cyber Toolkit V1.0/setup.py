from setuptools import setup, find_packages

setup(
    name="AdiZen-Cyber-Toolkit",
    version="1.0.0",
    description="Lightweight Python-based cybersecurity utilities",
    author="Adi Huseinovic",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "adizenauditor=tools.adizenauditor:main",
        ],
    },
)