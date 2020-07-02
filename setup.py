from setuptools import setup, find_namespace_packages

setup(
    name="django-cassandra-common",
    version="0.0.1",
    author="Didier Gaona",
    author_email="didiergaona@gmail.com",
    install_requires=["Django>=3.0.6", 'djangorestframework>=3.11.0', 'cassandra-driver>=3.23.0', 'requests>=2.23.0',
                      'django-filter>=2.3.0', 'setuptools>=46.4.0', 'django-cassandra-engine>=1.6.1'],
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src")
)
