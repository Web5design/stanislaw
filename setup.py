#!/usr/bin/env python
from distutils.core import setup

setup(name="stanislaw",
      version="0.1",
      description="A basic headless browser testing tool",
      author="Ted Dziuba",
      author_email="tjdziuba@gmail.com",
      url="https://github.com/teddziuba/stanislaw",
      packages=["stanislaw"],
      install_requires = [
        "pyquery>=1.1.1",
        "lxml>=2.3",
        ]
      )
