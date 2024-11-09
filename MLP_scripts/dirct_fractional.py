from pymatgen.io.vasp import Poscar
import glob
import os


poscar_files = glob.glob('./poscar_make/poscar.*')

os.makedirs('./poscar_make/fractional', exist_ok=True)


for poscar_file in poscar_files:

    poscar = Poscar.from_file(poscar_file)


    poscar.structure.to(fmt="POSCAR", filename=poscar_file)


    base_name = os.path.basename(poscar_file)
    new_file_name = os.path.join('./poscar_make/fractional', base_name)


    poscar.write_file(new_file_name)
