# Raman Amplification

## Installation

```
pip install git+https://github.com/CEA-MetroCarac/raman_ampli.git
```

## Execution

```
raman_ampli
```

then, select a **input_MODEL.xlsx** or similar file.
(Example of such a file is given [here](https://github.com/CEA-MetroCarac/raman_ampli/tree/main/raman_ampli/assets/input_MODEL.xlsx) to copy/paste into your project directory).

Or, from python scripting:

- using *.xlsx* files:

```
from raman_ampli.main import launcher

launcher(['..../input_MODEL1.xlsx', '..../input_MODEL2.xlsx', ...]) 
```

- without *.xlsx* file : refers to examples [here](https://github.com/CEA-MetroCarac/raman_ampli/tree/main/raman_ampli/examples)

## Acknowledgements

Part of this work, carried out on the CEA - Platform for Nanocharacterisation (PFNC), was supported by the “Recherche Technologique de Base” program of the French National Research Agency (ANR).
