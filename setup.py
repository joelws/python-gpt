import setuptools


setuptools.setup(
    include_package_data=True,
    name='python_gpt',
    version='0.1.0',
    description='Python GPT Wrapper for terminal or script use',
    url='https://github.com/joelws/python-gpt',
    author_email='joel.w.simmons@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['openai',],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Linux/Unix, MacOS :: MacOS',
    ]
)