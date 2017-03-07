from setuptools import setup

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(name='weather-api',
      version='0.0.2',
      description='A Python wrapper for the Yahoo Weather XML RSS feed.',
      long_description=long_descr,
      url='https://github.com/AnthonyBloomer/weather-api',
      author='Anthony Bloomer',
      keywords=['weather', 'api'],
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['weather', 'weather.models'],
      install_requires=[
          'requests',
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          "Topic :: Software Development :: Libraries",
          'Programming Language :: Python :: 2.7'
      ],
      zip_safe=False)
