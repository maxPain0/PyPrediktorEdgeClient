from setuptools import find_packages, setup
setup(
    name='pyprediktoredgeclient',
    packages=find_packages(include=['pyprediktoredgeclient']),
    setup_requires=[
        "pythonnet>=2.5.2"
        ],
    package_data={
        "": ["dlls/*.dll"]
    },
    version='0.5.0',
    description='A Python library to talk to Prediktor APIS/EDGE',
    author='Prediktor',
    license='MIT'
)