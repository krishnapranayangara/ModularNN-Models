# to scrape through all our directories and get packages we used
from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the List of Requirements
    '''
    requirements=[]
    with open('requirements.txt') as f:
        requirements=f.readlines()
        [req.replace("\n"," ")for req in requirements]

        #to remove the -e . we get frm the requirements.txt
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
#basic info of author and project details
name ='modular deep learning models',
version='00.1',
author='Krishna Pranay Angara',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),



)