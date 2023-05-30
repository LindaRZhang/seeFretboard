from setuptools import setuptools, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='seeFretboard',
    version='0.1.1',
    author='Linda Rong Zhang',
    author_email='ronglindaz@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LindaRZhang/seeFretboard',
    project_urls = {
        "Bug Tracker": "https://github.com/LindaRZhang/seeFretboard/issues"
    },
    license='MIT',
    packages=find_packages(include=['seeFretboard', 'seeFretboard.*']),
    install_requires=['requests'],
    include_package_data=True
)