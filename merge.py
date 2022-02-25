# 26 反向train和正向dev
# 55上的正向train

from ntpath import join


def merge(url,r_url):
    with open(url, 'r+') as f1:
        s1 = f1.read()
        s1 = s1.split('\n')
    with open(r_url, 'r') as f2:
        s2 = f2.read()
        s2 = s2.split('\n')
    res = s1 + s2[::-1]
    with open('enr', 'w') as f:
        f.write('\n'.join(res))

# test
url = '123.txt'
r_url = '234.txt'

with open(url, 'r+') as f1:
    s1 = f1.read()
    s1 = s1.split('\n')
with open(r_url, 'r') as f2:
    s2 = f2.read()
    s2 = s2.split('\n')
res = s1 + s2[::-1]
with open('enr', 'w') as f:
    f.write('\n'.join(res))