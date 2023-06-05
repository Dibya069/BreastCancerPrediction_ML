from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requires = []
    with open(file_path) as file_obj:
        requires = file_obj.readlines()
        requires = [req.replace("\n", "") for req in requires]

        return requires

setup(
    name="Breast Cancer Prediction",
    author="DIBYA",
    version= "0.0.1",
    author_email= "dibyamohanty069@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
)
