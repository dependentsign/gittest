from joblib import Parallel, delayed

Parallel(n_jobs=2)(delayed(str)(i ** 2) for i in range(10))
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

def m(n):
    return n+2


Parallel(n_jobs=6)(delayed(m)(i*2)for i in range(5))