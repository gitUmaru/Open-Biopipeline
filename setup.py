import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="open_biopipeline", # Replace with your own username
    version="0.0.4",
    author="Muhammad Umar Ali",
    author_email="umaruali@student.ubc.ca",
    description="Welcome to Open Biopipeline, an open source gene exploration tool!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitUmaru/Open-Biopipeline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       "biopython",
       "uniprot",
       "requests",
       "matplotlib",
       "beautifulsoup4"
   ]
)
