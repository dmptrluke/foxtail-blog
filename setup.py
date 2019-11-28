import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="foxtail-blog",
    version="0.4.0",
    author="Luke Rogers",
    author_email="lukeroge@gmail.com",
    description="A blog.",
    install_requires=['django>=2.2', 'bleach', 'bleach_whitelist', 'markdown', 'django-taggit',
                      'django-versatileimagefield', 'django-crispy-forms', 'django-recaptcha'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmptrluke/foxtail-blog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
