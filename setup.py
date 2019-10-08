from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import numpy

numpy_inc = numpy.get_include()

extensions = [
	Extension("hidden_markov.markov_chain",
			["hidden_markov/markov_chain.pyx"],
		include_dirs = [numpy_inc],
		),
	Extension("hidden_markov.likelihood",
			["hidden_markov/likelihood.pyx"],
		include_dirs = [numpy_inc],
		),
	]


setup(
	name = "Markov chain and likelihood",
	ext_modules = cythonize(extensions),
	packages=['cytohmm',],
	zip_safe=False,
)

