# t test for difference btween two means in case of independent samples 
# compare x1bar and x2bar

# if we assume that random samples are independently selected from two populations and the populations are normally distributed, then for small sample size, we can use t-test

# H0: u1=u2 or u1>=u2 or u1<=u2, against
# H1: u1!=u2 or u1<u2 or u1>u2


# t_stat = ((x1bar - x2bar) - (u1-u2))/((S^2*((1/n1)+(1/n2)))^0.5)
# u1-u2 = 0 since by H0 > u1=u2

# S^2 is the pooled variance 
# S^2 = ((n1-1)*S1^2 + (n2-1)S2^2)/(n1+n2-2)

# S1^2 and S2^2 are the sample variance
# degree of freedom = n1+n2-2

import numpy as np
import scipy

def left_tail_t_test_two_indep_samples(x1,x2,alpha):
    
    x1bar = np.mean(x1)
    
    x2bar = np.mean(x2)
    
    u1 = 0
    u2 = 0
    n1 = np.size(x1)
    n2 = np.size(x2)
    S1_square = np.var(x1,ddof=1)
    S2_square = np.var(x2,ddof=1)
    S_square= ((n1-1)*S1_square + (n2-1)*S2_square)/(n1+n2-2)

    t_stat  = ((x1bar - x2bar) - (u1-u2))/((S_square*((1/n1)+(1/n2)))**0.5)
    
    p_value = scipy.stats.t.cdf(x = t_stat, df = n1+n2-2 )

    print(''' we are testing 
          H0: u1 >= u2 against 
          H1: u1<u2
          ''')
    print(f'mean of sample 1 is {x1bar}')
    print(f'mean of sample 2 is {x2bar}')
    print(f't statistic is {t_stat}')
    print(f'p value is {p_value}')

    if p_value<=alpha:
        print(f'since p_value <= alpha')
        print(f'reject null hypothesis and hence u1 < u2')
    else:
        print(f'since p_value > alpha({alpha})')
        print(f'fail to reject null hypothesis')

# x1 is the delivery time of pizza company x1 in minutes
# x2 is the delivery time of pizza company x2 in minuteds
x1 = np.array([11.5,6.8,5.6,8.2,5.9,26,10,12.1,8.7,6.9])
x2 = np.array([22,15.2,18.7,15.6,20.8,19.5,17,19.5,16.5,24])

left_tail_t_test_two_indep_samples(x1,x2,0.05)



def right_tail_t_test_two_indep_samples(x1,x2,alpha):
    
    x1bar = np.mean(x1)
    
    x2bar = np.mean(x2)
    
    u1 = 0
    u2 = 0
    n1 = np.size(x1)
    n2 = np.size(x2)
    S1_square = np.var(x1,ddof=1)
    S2_square = np.var(x2,ddof=1)
    S_square= ((n1-1)*S1_square + (n2-1)*S2_square)/(n1+n2-2)

    t_stat  = ((x1bar - x2bar) - (u1-u2))/((S_square*((1/n1)+(1/n2)))**0.5)
    
    p_value = scipy.stats.t.sf(x = t_stat, df = n1+n2-2 )

    print(''' we are testing 
          H0: u1 <= u2 against 
          H1: u1>u2
          ''')
    print(f'mean of sample 1 is {x1bar}')
    print(f'mean of sample 2 is {x2bar}')
    print(f't statistic is {t_stat}')
    print(f'p value is {p_value}')

    if p_value<=alpha:
        print(f'since p_value <= alpha')
        print(f'reject null hypothesis and hence u1 > u2')
    else:
        print(f'since p_value > alpha({alpha})')
        print(f'fail to reject null hypothesis')

# x1 is the delivery time of pizza company x1 in minutes
# x2 is the delivery time of pizza company x2 in minuteds
x1 = np.array([11.5,6.8,5.6,8.2,5.9,26,10,12.1,8.7,6.9])
x2 = np.array([22,15.2,18.7,15.6,20.8,19.5,17,19.5,16.5,24])
print(''' 
''')
right_tail_t_test_two_indep_samples(x1,x2,0.05)


def two_tail_t_test_two_indep_samples(x1,x2,alpha):
    
    x1bar = np.mean(x1)
    
    x2bar = np.mean(x2)
    
    u1 = 0
    u2 = 0
    n1 = np.size(x1)
    n2 = np.size(x2)
    S1_square = np.var(x1,ddof=1)
    S2_square = np.var(x2,ddof=1)
    S_square= ((n1-1)*S1_square + (n2-1)*S2_square)/(n1+n2-2)

    t_stat  = ((x1bar - x2bar) - (u1-u2))/((S_square*((1/n1)+(1/n2)))**0.5)
    
    p_value = 2*(scipy.stats.t.sf(x = np.abs(t_stat), df = n1+n2-2 ))

    print(''' we are testing 
          H0: u1 = u2 against 
          H1: u1!=u2
          ''')
    print(f'mean of sample 1 is {x1bar}')
    print(f'mean of sample 2 is {x2bar}')
    print(f't statistic is {t_stat}')
    print(f'p value is {p_value}')

    if p_value<=alpha:
        print(f'since p_value <= alpha')
        print(f'reject null hypothesis and hence u1 != u2')
    else:
        print(f'since p_value > alpha({alpha})')
        print(f'fail to reject null hypothesis')

# x1 is the delivery time of pizza company x1 in minutes
# x2 is the delivery time of pizza company x2 in minuteds
x1 = np.array([11.5,6.8,5.6,8.2,5.9,26,10,12.1,8.7,6.9])
x2 = np.array([22,15.2,18.7,15.6,20.8,19.5,17,19.5,16.5,24])
print(''' 
''')
two_tail_t_test_two_indep_samples(x1,x2,0.05)


# note : this is a two-sample independent t-test with pooled variance
# this test assumes: Equal population variances i.e. sigma1^2 = sigma2^2
# In real-world data (like the pizza example), this is often false.

# Welch’s t-test is a version of the two-sample t-test that: does NOT assume equal variances between the two populations


# Welch’s t-test
# import scipy.stats as stats
# ******************************************************************
#  **t_stat, p_value = stats.ttest_ind(x1, x2, equal_var=False)**