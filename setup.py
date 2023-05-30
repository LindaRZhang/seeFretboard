from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='seeFretboard',
    version='0.1.5.3',
    author='Linda Rong Zhang',
    author_email='ronglindaz@gmail.com',
    description='For Release',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LindaRZhang/seeFretboard',
    project_urls={
        "Bug Tracker": "https://github.com/LindaRZhang/seeFretboard/issues"
    },
    license='GNU',
    packages=find_packages(include=['seeFretboard', 'seeFretboard.*']),
    package_data={
        'seeFretboard': ['Images/logo.png',
                         'Outputs/Audios/*',
                         'Outputs/Embeds/*',
                         'Outputs/Images/*',
                         'Outputs/Videos/*'
                        ],
    },
    install_requires=['requests'],
    include_package_data=True
)
