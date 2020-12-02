import setuptools

# Readme Configuration
with open("README.md", "r") as fh:
    long_description = fh.read()

    # Setup Credentials
    setuptools.setup(
        name="GoogleFormsHack",
        version="1.0.0",
        author="Ashkan Ebtekari",
        author_email="ashkanebtekari@gmail.com",
        description="Hack Google Forms User Data Entries",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="GoogleForms GitHub Url",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',

    )
