from setuptools import setup, find_packages 

setup(
    name="vertica_ui",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ipywidgets>=7.0.0",
        "verticapy>=3.1.0",
        "voila>=0.2.0",
        "jupyterlab>=3.0.0"
    ],
    author="Umar Farooq Ghumman",
    author_email="your.email@example.com",
    description="A JupyterLab extension for viewing Vertica database tables",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="jupyter vertica database viewer",
    classifiers=[
        "Framework :: Jupyter",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)