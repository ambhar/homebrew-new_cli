import setuptools


setuptools.setup(
     name='add_cli',
     version='0.1',
     scripts=['add_cli.py'] ,
     author="ashima",
     author_email="ashima@snakescript.com",
     description="A Docker and AWS utility package",
     long_description_content_type="text/markdown",
     url="https://github.com/ambhar/new_cli/add_cli",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
