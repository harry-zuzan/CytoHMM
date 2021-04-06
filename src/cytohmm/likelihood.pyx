import numpy
cimport numpy

from libc.math cimport exp, sqrt

# gaussian probabilities not fully normalised since they are used
# for likelihoods
def prob_normal_vec(vec, mu, sigma):
	vec1 = (vec - mu)/sigma
	return numpy.exp(-0.5*vec1*vec1)/(sigma*numpy.sqrt(numpy.pi))

# Likelihoods computed below
def gaussian_likelihood(yvec, mu, sigma):
	lhood = numpy.zeros((mu.size,yvec.size), numpy.float64)

	for i in range(mu.size):
		lhood[i,:] = prob_normal_vec(yvec,mu[i],sigma[i])
	lhood /= lhood.sum(0)

	return lhood
