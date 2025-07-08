from setuptools import setup

setup(
    name="FileSizeAnalyzerGUI",
    version="1.0",
    description="Gradient-themed file size checker with drag & drop and export features",
    author="Y7X",
    py_modules=["FileSizeAnalyzer"],
    install_requires=[
        "customtkinter",
        "tkinterdnd2",
        "fpdf"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
