from kapteyn import maputils
import numpy
from service import *

fignum = 29
fig = plt.figure(figsize=figsize)
frame = fig.add_axes(plotbox)
title = r"""Zenith equal area projection (ZEA) oblique with:
$\alpha_p=0$, $\delta_p=30$ and $\phi_p=180$. (Cal. fig.33a)"""
header = {'NAXIS' : 2, 'NAXIS1': 100, 'NAXIS2': 80,
          'CTYPE1' : 'RA---ZEA',
          'CRVAL1' :0.0, 'CRPIX1' : 50, 'CUNIT1' : 'deg', 'CDELT1' : -3.5,
          'CTYPE2' : 'DEC--ZEA',
          'CRVAL2' : 30.0, 'CRPIX2' : 40, 'CUNIT2' : 'deg', 'CDELT2' : 3.5,
         }
X = numpy.arange(0,360,15.0)
Y = numpy.arange(-90,90,15.0)
Y[0]= -dec0
f = maputils.FITSimage(externalheader=header)
annim = f.Annotatedimage(frame)
grat = annim.Graticule(axnum= (1,2), wylim=(-90,90.0), wxlim=(0,360),
                       startx=X, starty=Y)
grat.setp_lineswcs0(0, lw=2)
grat.setp_lineswcs1(0, lw=2)
lon_world = range(0,360,30)
lat_world = [-60, -30, 30, 60]
labkwargs0 = {'color':'r', 'va':'center', 'ha':'center'}
labkwargs1 = {'color':'b', 'va':'bottom', 'ha':'right'}
doplot(frame, fignum, annim, grat, title,
       lon_world=lon_world, lat_world=lat_world,
       labkwargs0=labkwargs0, labkwargs1=labkwargs1,
       markerpos=markerpos)