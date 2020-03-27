from setuptools import setup

setup(
    name='covidsocial',
    version='0.1',
    packages=['covidsocial'],
    url='',
    license='',
    author='Szu-Min Yu',
    author_email='smy320@nyu.edu',
    description='Covid-19 social and press tracking',
    install_requires = ['numpy', 'pandas','matplotlib','nltk','wordcloud','python-pptx', 'schedule']
)
