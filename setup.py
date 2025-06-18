from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="CTK_Color",
    version="0.1.0",
    description="A customizable color tool for CTkinter",
    author="Vishal Sharma",
    author_email="vishalsharma.pypi@gmail.com",
    long_description=long_description,  # 📝 From README.md
    long_description_content_type="text/markdown",  # 📄 Type of README
    license="MIT",
    packages=find_packages(),  # This finds CTK_Color/
    classifiers=[  # ✅ Optional classifiers for PyPI & users
        "Development Status :: 3 - Alpha",  # or "4 - Beta", "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ],
    include_package_data=True,
    python_requires=">=3.7",
    url="https://github.com/yourusername/CTK_Color",  # 🌐 Project URL
    project_urls={  # 🔗 Additional links
        "Bug Tracker": "https://github.com/yourusername/CTK_Color/issues",
        "Documentation": "https://github.com/yourusername/CTK_Color#readme",
        "Source Code": "https://github.com/yourusername/CTK_Color",
    },
)
