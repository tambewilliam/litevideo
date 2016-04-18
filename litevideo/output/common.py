from litex.gen import *

from litex.soc.interconnect import stream

hbits = 12
vbits = 12

bpp = 16
bpc = 8
pixel_layout_s = [
    ("cb_cr", bpc),
    ("y", bpc)
]

def pixel_layout(pack_factor):
    return [("p"+str(i), pixel_layout_s) for i in range(pack_factor)]

bpc_phy = 8

def phy_description(pack_factor):
    param_layout = [("hsync", 1), ("vsync", 1)]
    payload_layout = [("data", 2*bpc_phy*pack_factor)]
    return stream.EndpointDescription(payload_layout, param_layout)
