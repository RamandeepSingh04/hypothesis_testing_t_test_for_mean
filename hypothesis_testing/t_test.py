# t-test of Hypothesis for mean
# Population Distribution - Follows Normal
# Population Variance - Unknown
# Sample Size < 30


import numpy as np
import scipy


def left_tail_t_test(sample_data,alpha,h0_u):
    sample_size = np.size(sample_data)
    sample_mean = np.mean(sample_data)
    sample_standard_dev = np.std(sample_data,ddof=1)
    null_hypothesis_mean = h0_u

    t_stat = (sample_mean - null_hypothesis_mean)*(np.sqrt(sample_size))/(sample_standard_dev)

    p_value = scipy.stats.t.cdf(x=t_stat,df=sample_size-1)

    print(f''' t-test for Mean (Left Tail)
          
          We are testing h0 : u = {h0_u}, against 
                         h1 : u < {h0_u} ''')
    
    print(f'''
            sample size = {sample_size},
            sample mean = {sample_mean},
            sample standard dev = {sample_standard_dev},

              p value = {p_value},
              alpha = {alpha} ''')
    
    if p_value<=alpha:
        print(f'since p_value <= alpha')
        print(f'reject null hypothesis and hence u < {h0_u}')
    else:
        print(f'since p_value > alpha')
        print(f'fail to reject null hypothesis')



def right_tail_t_test(sample_data,alpha,h0_u):
    sample_size = np.size(sample_data)
    sample_mean = np.mean(sample_data)
    sample_standard_dev = np.std(sample_data,ddof=1)
    null_hypothesis_mean = h0_u

    t_stat = (sample_mean - null_hypothesis_mean)*(np.sqrt(sample_size))/(sample_standard_dev)

    p_value = scipy.stats.t.sf(x=t_stat,df=sample_size-1)

    print(f''' t-test for Mean (Right Tail)
          
          We are testing h0 : u = {h0_u}, against 
                         h1 : u > {h0_u} ''')
    
    print(f'''
            sample size = {sample_size},
            sample mean = {sample_mean},
            sample standard dev = {sample_standard_dev},

              p value = {p_value},
              alpha = {alpha} ''')
    
    if p_value<=alpha:
        print(f'since p_value <= alpha')
        print(f'reject null hypothesis and hence u > {h0_u}')
    else:
        print(f'since p_value > alpha')
        print(f'fail to reject null hypothesis')


def two_tail_t_test(sample_data,alpha,h0_u):
    sample_size = np.size(sample_data)
    sample_mean = np.mean(sample_data)
    sample_standard_dev = np.std(sample_data,ddof=1)
    null_hypothesis_mean = h0_u

    t_stat = (sample_mean - null_hypothesis_mean)*(np.sqrt(sample_size))/(sample_standard_dev)

    p_value = 2*(scipy.stats.t.sf(x=np.abs(t_stat),df=sample_size-1))

    print(f''' t-test for Mean (Two Tail)
          
          We are testing h0 : u = {h0_u}, against 
                         h1 : u != {h0_u} ''')
    
    print(f'''
            sample size = {sample_size},
            sample mean = {sample_mean},
            sample standard dev = {sample_standard_dev},

              p value = {p_value},
              alpha = {alpha} ''')
    
    if p_value<=alpha:
        print(f'since p_value <= alpha')
        print(f'reject null hypothesis and hence u != {h0_u}')
    else:
        print(f'since p_value > alpha')
        print(f'fail to reject null hypothesis')




array = np.array([6,5.3,4.9,7.2,3.5,5.5,5.9,2,6.9,8])
alpha = 0.05
assumed_mean = 4

print('''
''')

left_tail_t_test(array,alpha,assumed_mean)

print('''
''')

right_tail_t_test(array,alpha,assumed_mean)

print('''
''')

two_tail_t_test(array,alpha,assumed_mean)