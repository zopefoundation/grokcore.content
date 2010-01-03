from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = "%s\n%s\n" % (read('README.txt'), read('CHANGES.txt'))

install_requires = [
    'setuptools',
    'grokcore.component >= 1.5, < 2.0',
    'zope.annotation'
    ],

setup(
    name='grokcore.content',
    version = '1.0dev',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://pypi.python.org/pypi/grokcore.content',
    description='Base content types for Grok',
    long_description=long_description,
    license='ZPL',
    install_requires = install_requires
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data = True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Framework :: Zope3'],
)
