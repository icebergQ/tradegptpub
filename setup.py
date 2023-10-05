from setuptools import setup, find_packages

# Package metadata
NAME = "tradegptpub"
VERSION = "0.0.1"
DESCRIPTION = "tradegptpub"
AUTHOR = "Kai Qin, He Zhang, Hui Mao, Gordon Chen, Zhuo Ren, Benji Benzyl"
EMAIL = "teachaitradetogether@gmail.com"
URL = "https://tradegptusa.com"


# Package configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(include=["tradegptpub", "tradegptpub.*"]),
)