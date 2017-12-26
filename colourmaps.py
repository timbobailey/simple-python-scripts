import cubehelix
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import LightSource

from matplotlib.colors import LinearSegmentedColormap

def make_colormap(seq):
    """
    Converts a sequence of RGB tuples containing floats in the interval (0,1).
    For some reason LinearSegmentedColormap cannot take an alpha channel,
    even though matplotlib colourmaps have one.
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return LinearSegmentedColormap('CustomMap', cdict)

from matplotlib.colors import ListedColormap

def add_alpha(cmap, alpha=None):
    """
    Add an alpha channel (opacity) to a colourmap. Uses a ramp by default.
    Pass an array of 256 values to use that. 0 = transparent; 1 = opaque.
    """
    cmap4 = cmap(np.arange(cmap.N))
    if alpha is None:
        alpha = np.linspace(1, 0, cmap.N)
    cmap4[:,-1] = alpha
    return ListedColormap(cmap4)

seabed = np.load('data/Penobscot_Seabed.npy')

# Finesse the hillshade if you want to.
ls = LightSource(azdeg=225, altdeg=140)
bumps = ls.hillshade(seabed)
# bumps = ls.hillshade(seabed)**0.5 # Sqrt backs it off a bit.

# Make the plot.
fig = plt.figure(figsize=(18,8), facecolor='white')
ax = fig.add_subplot(111)

kmap = make_colormap([(0,0,0)])
kmap4 = add_alpha(kmap)

cx=cubehelix.cmap(0.75, -0.75, reverse=True, min_light=0.3)
params = dict(cmap=cx, aspect=0.5, origin='lower')

xlines, inlines = seabed.shape
x, y = np.arange(inlines), np.arange(xlines)
X, Y = np.meshgrid(x, y)

mi, ma = np.floor(np.nanmin(seabed)), np.ceil(np.nanmax(seabed))
levels = np.arange(mi, ma)

# Plot everything.
ax0 = fig.add_subplot(221)
ax0.imshow(seabed, **params)
ax0.axis('off')

ax1 = fig.add_subplot(222)
ax1.imshow(seabed, **params)
ax1.contour(X, Y, seabed, levels=levels, linewidths=0.4, colors=[(0,0,0,0.4)])
ax1.axis('off')

ax2 = fig.add_subplot(223)
ax2.imshow(seabed, **params)
ax2.imshow(bumps, cmap=kmap4, aspect=0.5, origin='lower', alpha=0.67)
ax2.axis('off')

ax3 = fig.add_subplot(224)
ax3.imshow(seabed, **params)
ax3.imshow(bumps, cmap=kmap4, aspect=0.5, origin='lower', alpha=0.67)
ax3.contour(X, Y, seabed, levels=levels, linewidths=0.4, colors=[(0,0,0,0.4)])
ax3.axis('off')

plt.show()

"""
cmap=helix(0.75, -0.75, reverse=True, min_light=0.3)
im = ax.imshow(seabed, cmap, aspect=0.5, origin='lower')
ax.imshow(bumps, cmap=kmap4, aspect=0.5, origin='lower', alpha=0.67)
cb = plt.colorbar(im, label="Two way time")
cb.ax.invert_yaxis()
cb.outline.set_visible(False)
ax.contour(X, Y, seabed, levels=levels, linewidths=0.4, colors=[(0,0,0,0.4)])
ax.set_xlabel("Inline")
ax.set_ylabel("Xline")
ax.grid(color='w', alpha=0.2)

plt.show()
"""



