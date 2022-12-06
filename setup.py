from setuptools import setup

setup(
    name='extorch',
    version='0.1.0',    
    description='A pytorch extension from Sequential model and hypertuning',
    url='https://github.com/denis-spe/extorch',
    author='Den',
    author_email='denisbrian07@gmail.com',
    license='BSD 2-clause',
    packages=['extorch'],
    install_requires=['torch',
                      'numpy',
                      'progress==1.6',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)