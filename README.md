# Kicad_FPC_board_ends
Common board end footprints for FPC connectors and a python script for generating custom versions:

![Example footprint 1](Example1.PNG)

Footprints include an outline for the stiffener on layer User.1 and board edge cuts up to the end of the stiffener

## Common footprints
If you just want to use some common footprints you can download the fpc_board_ends.pretty folder and import it into kicad as normal

These footprints have been generated for:
- 0.5mm pitch, 0.35mm pad width, 2.5mm exposed copper and 3.5mm stiffener, with a 0.2mm radius at the corners 
- 1mm pitch, 0.6mm pad width, 2.5mm exposed copper and 3.5mm stiffener, with a 0.2mm radius at the corners 

If ordering from jlcpcb the User.1 layer with the stiffener on should be renamed to:
B.Stiffener_{material}b_{thickness}

for example:
B.Stiffener_pib_0.2
Would indicate a polyimide stiffener 0.2mm thick on the back side of the board

## Generating your own footprints
This python package can be installed by pip:

`pip install git+https://github.com/mikeWShef/Kicad_FPC_board_ends`

And run from the command line eg:

`fpc_footprint_generator [positions] [pitch] -r [corner radius]`

Will generate a 4 position 0.5mm pitch board end with a corner radius of 0.2mm

The full arguments are:

`fpc_footprint_generator -h:`

positional arguments:
- positions             The number of positions on the board edge
- pitch                 The pitch of the connector

optional arguments:
-  --pad_width, -w The width of the pads in mm, defaults to pitch/0.5*0.35
-  --pad_length, -l The length of the pads in mm, defaults to 2.5
-  --stiffener_length, -s The length of the stiffener in mm, in layer User.1, defaults to 3.5
-  --radius, -r The radius of the fillet/chamfer at the corners in mm
-  --chamfer, -c If set the corners will be chanfered with a distance set by the radius argument
-  --filename , -f The filename of the output file, if not supplied the default name 'FPC-{positions}P-{pitch}mm' will be used