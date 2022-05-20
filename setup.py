from setuptools import setup

with open("README.MD", "r") as fh:
    long_description = fh.read()

setup(
    name='proxy-email-transfer',
    version='1.0.0',
    description='Send emails, read emails, reply emails through Proxies using Python.',
    py_modules=["proxy_smtp", "proxy_imap"],
    package_dir={'': 'src'},
    requires = ["PySocks"], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nivethithan M",
    author_email="nivethithan@ghostengines.io",
    url="https://github.com/ghostenginesio/proxy-email-transfer"
)
