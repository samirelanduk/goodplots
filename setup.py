from setuptools import setup

setup(
 name="goodplots",
 version="0.1.0",
 description="A matplotlib wrapper.",
 url="https://goodplots.samireland.com",
 author="Sam Ireland",
 author_email="mail@samireland.com",
 license="MIT",
 classifiers=[
  "Development Status :: 4 - Beta",
  "Intended Audience :: Science/Research",
  "License :: OSI Approved :: MIT License",
  "Topic :: Scientific/Engineering :: Visualization",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.5",
  "Programming Language :: Python :: 3.6",
 ],
 keywords="charts plots matplotlib data",
 packages=["goodplots"],
 install_requires=["matplotlib==2.2.2",]
)
