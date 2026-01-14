from setuptools import find_packages,setup

from typing import List

hypn_e_dt='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        
        if hypn_e_dt in requirements:
            requirements.remove(hypn_e_dt)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Sudhir',
    author_email='sudhir050702@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)