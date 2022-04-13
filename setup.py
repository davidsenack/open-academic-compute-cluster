import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="oacc",
    version="0.1.0",
    description="The Open Academic Compute Cluster: Simplified HPC in the AWS Cloud",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/davidsenack/open-academic-compute-cluster",
    author="David Senack",
    author_email="david.senack@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Clustering",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["aws-parallelcluster", "aws-parallelcluster-node"],
    entry_points={
        "console_scripts": [
            "oacc=oacc.oacc:main",
        ]
    },
)