"""
cxfreeze script to generate execultable file.
python setup_cx.py build

If recursion depth error => too many modules are being imported.
Need to limit the amount by creating a venv for the freezing process.

"""
import os

from cx_Freeze import setup

from common.file.filenames import findall_ext

DATAPATH_DAMIEN = os.path.join('S:',
                               '205-Caracterisation_Metrologie',
                               '205.00-Stages_Theses_Postdoc',
                               '2023-MONTEIL Damien',
                               'Technique',
                               'Données expérimentales')
INDICES_PATH = os.path.join(DATAPATH_DAMIEN, 'data_indices')
data_files = findall_ext(INDICES_PATH, pattern='.csv')
includes = []
for el in data_files:
    includes.append((el, os.path.split(el)[1]))
# edit this line for your local path
# includes.append(("C:\\Users\\DM274601\\PycharmProjects\\workspace\\thesis\\T_23_damien_monteil\\work\\03-raman_amplification\\cxfreeze\\input_THICKNESS.xlsx", "input_THICKNESS.xlsx"))
includes.append(("C:\\Users\\DM274601\\PycharmProjects\\workspace\\thesis\\T_23_damien_monteil\\work\\03-raman_amplification\\cxfreeze\\input_THICKNESS.xlsx", "input_THICKNESS.xlsx"))

# Dependencies are autmatically detected, but they might need fine-tuning.

build_exe_options = {
    "excludes": [],
    "zip_include_packages": ["matplotlib",
                             "numpy",
                             "pandas",
                             "xlsxwriter",
                             "shiboken6"],
    "include_files": includes,
}

setup(
    name="TMM sim",
    version="0.1",
    description="My GUI application",
    options={"build_exe": build_exe_options},
    executables=[{"script": "run_excel.py", "base": "gui"}],
)
