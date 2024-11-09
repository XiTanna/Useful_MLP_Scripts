```shell

```

# Documentation of useful MLP scripts

#### **The scripts in the ./MLP_scripts directory are used as follows**

1. **dirct_fractional.py** Converts all POSCAR files in the ./poscar_make directory to fractional coordinates.
2. **singleFrame-outcars2nep-exyz.sh** Converts all OUTCAR files in the current directory and its subdirectories to NEP training format. database Exports to the NEP-dataset folder as NEP-dataset.xyz, with the final database format in exyz.
3. **outcar_check** Checks all OUTCAR files in the current directory and its subdirectories to determine if static self-consistent calculations have converged.
4. **poscar_make** Divides the MLP-MD trajectory into evenly spaced frames and converts these frames to POSCAR files.
5. **vaprun_xyz** Converts vasprun.xml files obtained from VASP AIMD to a database format in exyz.
6. **INCAR_AIMD_ML_NPT INCAR** file for VASP’s on-the-fly AIMD in the NPT ensemble.
7. **INCAR_static_self-consistent** INCAR file for VASP static self-consistent calculations.
7. **Perturbation.py**  Performs 5 structural perturbations, where each perturbation generates a new structure. The simulation box size is perturbed by 5%, and each atom's position is adjusted by 0.1 angstrom.

**Note:** The scripts above are partially derived from the work of other authors and are not entirely original. I extend my sincere gratitude to them for their generous contributions.
