from kapteyn import maputils
from matplotlib import pyplot as plt

f = maputils.FITSimage("m101.fits")

fig = plt.figure()
frame = fig.add_subplot(1,1,1)

mplim = f.Annotatedimage(frame)
im = mplim.Image()
mplim.plot()

plt.show()

