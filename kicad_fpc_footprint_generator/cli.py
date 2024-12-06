"""
The command-line interface for the generator
"""
import argparse
from .fpc_footprint import write_file

def main():
    parser = argparse.ArgumentParser(
        description="A python tool for genrating fpc board edges"
    )
    parser.add_argument(
        "positions", type=int,
        help="The number of positions on the board edge"
    )
    parser.add_argument(
        "pitch", type=float,
        help="The pitch of the connector"
    )

    parser.add_argument(
        "--pad_width", "-w", type=float, help="The width of the pads in mm, defaults to pitch/0.5*0.35"
    )

    parser.add_argument(
        "--pad_length", "-l", type=float, help="The length of the pads in mm, defaults to 2.5"
    )

    parser.add_argument(
        "--stiffener_length", "-s", type=float, help="The length of the stiffener in mm, in layer User.1, defaults to 3.5"
    )

    parser.add_argument(
        "--radius", "-r", type=float, help="The radius of the fillet/chamfer at the corners in mm"
    )

    parser.add_argument(
        "--chamfer", "-c", action="store_true", help="If set the corners will be chanfered with a distance set by the radius argument"
    )

    parser.add_argument(
        "--filename", "-f",
        help=(r"The filename of the output file, if not supplied the default name 'FPC-{positions}P-{pitch}mm' will be used")
    )
    args = parser.parse_args()

    fn = write_file(args.positions, args.pitch, args.pad_width, args.radius, args.pad_length, args.stiffener_length, args.chamfer, args.filename)

    print(f"File sucessfully written to {fn}")
