# t test for difference btween two means in case of independent samples 
# compare x1bar and x2bar

# if we assume that random samples are independently selected from two populations and the populations are normally distributed, then for small sample size, we can use t-test

# H0: u1=u2 or u1>=u2 or u1<=u2, against
# H1: u1!=u2 or u1<u2 or u1>u2


# t_stat = ((x1bar - x2bar) - (u1-u2))/((S^2*((1/n1)+(1/n2)))^0.5)
# u1-u2 = 0 since by H0 : u1=u2

# S^2 is the pooled variance 
# S^2 = ((n1-1)*S1^2 + (n2-1)S2^2)/(n1+n2-2)

# S1^2 and S2^2 are the sample variance
# degree of freedom = n1+n2-2

# note : this is a two-sample independent t-test with pooled variance
# this test assumes: Equal population variances i.e. sigma1^2 = sigma2^2
# In real-world data, this is often false.

# Welch’s t-test is a version of the two-sample t-test that: does NOT assume equal variances between the two populations

