import math

def write_file(positions, pitch, pad_width = None, radius = None, exposed_copper_length = None, 
               stiffener_length = None, chamfer=False, file_name=None):
    if pad_width is None:
        pad_width = pitch/0.5*0.35
    if radius is None or radius < 0:
        radius = 0
    if exposed_copper_length is None:
        exposed_copper_length = 2.5
    if stiffener_length is None:
        stiffener_length = 3.5
    if file_name is None:
        file_name = f"FPC-{positions}P-{pitch}mm"
    with open(f"{file_name}.kicad_mod", mode="w") as f:
        # preamble point on silk screen
        f.write("(")
        f.write(f"""footprint "{file_name}" (version 20221018) (generator pcbnew) 
  (layer "F.Cu")
  (attr smd)
  (fp_text reference "." (at 0 {stiffener_length-exposed_copper_length/2} unlocked) (layer "F.SilkS")
      (effects (font (size 1 1) (thickness 0.1)))
  )
  (fp_text value "{file_name}" (at 0 1 unlocked) (layer "F.Fab")
      (effects (font (size 1 1) (thickness 0.15)))
  )
""")
    # edge cuts, vertical lines
        f.write(f"""  (fp_line (start {-pitch:.2f} {stiffener_length-exposed_copper_length/2:.2f}) (end {-pitch:.2f} {-exposed_copper_length/2+radius:.2f})
    (stroke (width 0.05) (type default)) (layer "Edge.Cuts"))
""")
    # edge cuts, top line
        f.write(f"""  (fp_line (start {-pitch+radius:.2f} {-exposed_copper_length/2:.2f}) (end {pitch*positions-radius:.2f} {-exposed_copper_length/2:.2f})
    (stroke (width 0.05) (type default)) (layer "Edge.Cuts"))
""")
    # edge suts other vertical line
        f.write(f"""  (fp_line (start {pitch*positions:.2f} {stiffener_length-exposed_copper_length/2:.2f}) (end {pitch*positions:.2f} {-exposed_copper_length/2+radius:.2f})
    (stroke (width 0.05) (type default)) (layer "Edge.Cuts"))
""")
        # edge cuts radius
        if radius>0:
            centre_x1 = -pitch+radius
            centre_x2 = pitch*positions-radius
            centre_y = -exposed_copper_length/2+radius
            spr = radius*math.sin(math.pi/4)
            f.write(f"""  (fp_{"line" if chamfer else "arc"} (start {centre_x1-radius:.2f} {centre_y:.2f}){"" if chamfer else f"( mid {centre_x1-spr:.6f} {centre_y-spr:.6f})"} (end {centre_x1:.2f} {centre_y-radius:.2f})
    (stroke (width 0.05) (type default)) (layer "Edge.Cuts"))
""")
            f.write(f"""  (fp_{"line" if chamfer else "arc"} (start {centre_x2+radius:.2f} {centre_y:.2f}){"" if chamfer else f" (mid {centre_x2+spr:.6f} {centre_y-spr:.6f})"} (end {centre_x2:.2f} {centre_y-radius:.2f})
    (stroke (width 0.05) (type default)) (layer "Edge.Cuts"))
""")
        # stiffener v line
        f.write(f"""  (fp_line (start {-pitch:.2f} {stiffener_length-exposed_copper_length/2:.2f}) (end {-pitch:.2f} {-exposed_copper_length/2+radius:.2f})
    (stroke (width 0.05) (type default)) (layer "User.1"))
""")
        # stiffener, top line
        f.write(f"""  (fp_line (start {-pitch+radius:.2f} {-exposed_copper_length/2:.2f}) (end {pitch*positions-radius:.2f} {-exposed_copper_length/2:.2f})
    (stroke (width 0.05) (type default)) (layer "User.1"))
""")
        # stiffener, bottom line
        f.write(f"""  (fp_line (start {-pitch:.2f} {stiffener_length-exposed_copper_length/2:.2f}) (end {pitch*positions:.2f} {stiffener_length-exposed_copper_length/2:.2f})
    (stroke (width 0.05) (type default)) (layer "User.1"))
""")
        # stiffener other vertical line
        f.write(f"""  (fp_line (start {pitch*positions:.2f} {stiffener_length-exposed_copper_length/2:.2f}) (end {pitch*positions:.2f} {-exposed_copper_length/2+radius:.2f})
    (stroke (width 0.05) (type default)) (layer "User.1"))
""")
        # stiffener corners
        if radius>0:
            centre_x1 = -pitch+radius
            centre_x2 = pitch*positions-radius
            centre_y = -exposed_copper_length/2+radius
            spr = radius*math.sin(math.pi/4)
            f.write(f"""  (fp_{"line" if chamfer else "arc"} (start {centre_x1-radius:.2f} {centre_y:.2f}){"" if chamfer else f" (mid {centre_x1-spr:.6f} {centre_y-spr:.6f})"} (end {centre_x1:.2f} {centre_y-radius:.2f})
    (stroke (width 0.05) (type default)) (layer "User.1"))
""")
            f.write(f"""  (fp_{"line" if chamfer else "arc"} (start {centre_x2+radius:.2f} {centre_y:.2f}){"" if chamfer else f" (mid {centre_x2+spr:.6f} {centre_y-spr:.6f})"} (end {centre_x2:.2f} {centre_y-radius:.2f})
    (stroke (width 0.05) (type default)) (layer "User.1"))
""")
        # old stiffener
        #f.write(f"""  (fp_rect (start {-pitch} {-exposed_copper/2}) (end {pitch*positions} {stiffener-exposed_copper/2})
#    (stroke (width 0.1) (type default)) (fill none) (layer "User.1"))
#""")
        for i in range(positions):
            f.write(f"""  (pad {i+1} smd rect (at {pitch*i} 0 90) (size {exposed_copper_length} {pad_width}) (layers "F.Cu" "F.Paste" "F.Mask"))
""")
        f.write(""")
""")
    return file_name 
