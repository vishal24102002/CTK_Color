from setuptools import setup, find_packages

setup(
    name="CTK_Color",
    version="0.1.0",
    description="A customizable color tool for CTkinter",
    author="Your Name",
    license="MIT",
    packages=find_packages(),  # This finds CTK_Color/
    include_package_data=True,
    python_requires=">=3.7",
)
