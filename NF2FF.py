import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import numpy as np
from reading import timestepreader

#list of field
base = '/home/romain/ara/xfdtdprojects/iceblock2.xf/Simulations/000007/Run0001/output/MultiPoint_beforeice_1_transient_Ey_total_ts'
#base.append(2.bin'
fieldvst = np.array([])
for ts in range(30):
    nameoffile = base + str(ts) + '.bin'
    field = timestepreader(nameoffile)
    fieldvst = np.append(fieldvst,field)

size = np.shape(fieldvst)
t = np.arange(size[0])
plt.plot(t, fieldvst)
plt.show()

