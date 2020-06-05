from setuptools import setup


setup(
    name='flask-color-extended',
    version='0.1',
    url='https://github.com/Alveona/flask-color-extended',
    license='MIT',
    author='Alveona',
    author_email='pomavau@yandex.ru',
    description='flask-color-extended is an extension for Flask that improves the built-in web server with colors when debugging.',
    long_description=__doc__,
    packages=['flask_color_extended'],
    namespace_packages=['flask_color_extended'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
