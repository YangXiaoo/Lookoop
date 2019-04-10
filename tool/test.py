import numpy as np 

a = np.arange(5)
hist, bin_edges = np.histogram(a, bins=5, density=True)

ret1 = hist.cumsum()
ret2 = ret1*255 / ret1[-1]
ret = np.interp(a, bin_edges[:-1], ret1)




print("a:{}\nhist:{}\nbin_edges:{}\nret1:{}\nret2:{}\nret:{}".format(a, hist, bin_edges, ret1, ret2, ret))

