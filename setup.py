from setuptools import setup, find_packages

setup(
    name="adizen-cyber-toolkit",
    version="1.0.0",
    description="Modular Python toolkit for cybersecurity auditing, automation, and inspection",
    author="AdiZenWorks Inc.",
    author_email="security@adizenworks.com",
    url="https://github.com/AdiZen369/AdiZen-Cyber-Toolkit",
    packages=find_packages(),
    install_requires=["requests>=2.28.0", "beautifulsoup4>=4.12.0"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
)
