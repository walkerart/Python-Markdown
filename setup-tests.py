from distutils.core import setup
import os

setup_path = os.path.dirname(__file__)

setup(
    name='tests',
    version='1.0',
    description='Python-Markdown testing Framework',
    author='Waylan Limberg',
    author_email='waylan@gmail.com',
    packages=['tests'],
    package_dir={'tests': os.path.join(setup_path, 'tests')},
    package_data={'tests': [os.path.join(setup_path, 'tests/*.txt'), 
                            os.path.join(setup_path,'tests/*.html'), 
                            os.path.join(setup_path, 'tests/*.cfg')]},
    scripts=[os.path.join(setup_path, 'run-tests.py')],
)