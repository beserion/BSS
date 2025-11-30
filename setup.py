from setuptools import setup, find_packages

setup(
    name="bss-sast",
    version="0.1.0",
    description="BSS — Big Security Solution: lightweight SAST toolkit",
    packages=find_packages(),
    install_requires=[
        "radon", "bandit", "jinja2", "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "bss-sast=sast:main"
        ]
    }
)
