# Interference_Raman_Amplification

## Installation

```
pip install git+https://github.com/CEA-MetroCarac/Interference_Raman_Amplification.git
```

## Execution

```
raman_ampli
```

then, select a **input_MODEL.xlsx** or similar file.
(Example of such a file is given [here](https://github.com/CEA-MetroCarac/Interference_Raman_Amplification/tree/main/src/assets/input_MODEL.xlsx) to copy/paste into your project directory).

Or, from python scripting:

- using *.xlsx* files:

```
from amplification.main import launcher

launcher(['..../input_MODEL1.xlsx', '..../input_MODEL2.xlsx', ...]) 
```

- without *.xlsx* file : refers to examples [here](https://github.com/CEA-MetroCarac/Interference_Raman_Amplification/tree/main/src/examples)

