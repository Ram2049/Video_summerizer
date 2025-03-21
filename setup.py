from setuptools import setup,find_packages
from typing import List

def get_requiremnts(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    
    '''
    hypen_e_dot = '-e .'
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if hypen_e_dot in requirements:
           requirements.remove(hypen_e_dot)
    
    return requirements

setup(
    name="Video_Summerizer",                   # Name of the package
    version="0.0.0",                     # Version of the package
    author="Ram",                  # Author name
    author_email="ramsparttakas23@gmail.com",  # Author email
    description="An AI-powered application that summarizes and analyzes video content using Google's Gemini AI model. This tool allows users to upload videos, ask contextual questions, and receive comprehensive AI-generated insights enhanced by real-time web research",  # Short description
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",  # Content type of the long description
    url="https://github.com/Ram2049/Video_summerizer",  # URL of the project repository
    packages=find_packages(),            # Automatically find all packages in the project
    install_requires=get_requiremnts('requirements.txt')                   # Dependencies

)
