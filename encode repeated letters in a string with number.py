from itertools import groupby
s = 'wwwwaaadexxxxxx'
print(''.join('{}{}'.format(c, sum(1 for _ in g)) for c, g in groupby(s)))
