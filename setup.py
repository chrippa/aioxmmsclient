#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name="aioxmmsclient",
      version="0.1.0",
      description="A asyncio (PEP 3156) connector for xmmsclient.",
      author="Christopher Rosell",
      author_email="chrippa@tanuki.se",
      license="MIT",
      py_modules=["aioxmmsclient"]
)

