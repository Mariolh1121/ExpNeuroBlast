from setuptools import setup, find_packages

setup(
    name="differential_expression_analysis",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "pydeseq2",
        "logging"
    ],
    entry_points={
        "console_scripts": [
            "prepare-data=analysis.scripts.prepare_data:main",
            "run-deseq2=analysis.scripts.run_deseq2:main",
        ],
    },
)