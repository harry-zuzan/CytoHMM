from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import numpy

numpy_inc = numpy.get_include()

extensions = [
	Extension("cytohmm.markov_chain",
			["cytohmm/markov_chain.pyx"],
		include_dirs = [numpy_inc],
		),
	Extension("cytohmm.likelihood",
			["cytohmm/likelihood.pyx"],
		include_dirs = [numpy_inc],
		),
	]


setup(
	name = "Markov chain and likelihood",
	ext_modules = cythonize(extensions),
	packages=['cytohmm',],
	zip_safe=False,
)

