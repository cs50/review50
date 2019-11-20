from setuptools import setup

setup(
    author="CS50",
    author_email="sysadmins@cs50.harvard.edu",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    description="This is review50, with which you can initiate code reviews.",
    install_requires=["natsort", "requests", "termcolor"],
    keywords=["review", "review50"],
    name="review50",
    scripts=["review50"],
    url="https://github.com/cs50/review50",
    version="0.1.0"
)
