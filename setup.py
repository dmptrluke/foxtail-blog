import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("./foxtail_blog/version.py") as fp:
    exec(fp.read(), version)

install_requires = [
    'django>=2.2',
    'django-markdownfield>=0.3',
    'django-taggit',
    'django-versatileimagefield',
    'django-crispy-forms',
    'django-recaptcha',
    'django-csp-helpers',
    'django-published>=0.5.0'
]

setuptools.setup(
    name="foxtail-blog",
    version=version['__version__'],
    author="Luke Rogers",
    author_email="lukeroge@gmail.com",
    description="A blog.",
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmptrluke/foxtail-blog",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
