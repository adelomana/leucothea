import numpy,matplotlib.pyplot
from mpl_toolkits.basemap import Basemap

# 0. sampled points
lats = [-75.45801,-74.80018,-75.75292,-74.05176,-74.19026,-76.50168,-76.50254,-76.49836]
lons = [168.997,169.3836,168.75947,169.68943,169.5481,170.01464,172.02804,176.00396]
theColors=['orange','cyan','magenta','yellow','yellow','red','red','red']

# 1. building the map
m = Basemap(projection='stere',width=800*1e3,height=800*1e3,lat_0=numpy.mean(lats),lon_0=numpy.mean(lons),resolution='f')

m.bluemarble()
m.drawcoastlines()
m.drawmeridians(meridians=[160,165,170,175,180],zorder=1,color='gray',labels=[0,1,1,0])
m.drawparallels(circles=[-73,-74,-75,-76,-77,-78],zorder=1,color='gray',labels=[0,1,1,0])

# 2. placing the sampling positions
x,y = m(lons, lats)
for i in range(len(lats)):
    m.plot(x[i],y[i],'.',markersize=10,color=theColors[i])

matplotlib.pyplot.savefig('figure.png')
