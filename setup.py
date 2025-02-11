from setuptools import find_packages, setup
from typing import List
hype = "-e ."
def get_requirements(filepath:str):
    reqs = []
    with open(filepath) as file:
        reqs = file.readlines()
    reqs = [req.replace("\n", "") for req in reqs]
    if hype in reqs:
        reqs.remove(hype)
    return reqs

setup(
    name = "mymlproject",
    author= "Abdulsalaam",
    version= "0.0.1",
    author_email= "sa.abdulsalaam@gmail.com",
    packages= find_packages(),
    requires= get_requirements("requirements.txt")
)