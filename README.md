# msi
Assignments for the Artificial Intelligence Methods course

## Installation guide

In order to reproduce the project you will need to have conda installed and use the following commands:
```bash
conda create -n msi
source activate msi
conda install --file requirements.txt
python setup.py install
```

Now to check if everything is working properly run
```bash
pytest src/tests
```

## Basic usage
The resolution method solver is ready to use in form of a python command. There is also an example input file in the repository. In order to perform the resolution method on the sample input just use the following command:

```bash
python main.py example.txt --visualize
```

Notice the `--visualize` option, it specifies whether the resolution tree should be displayed.

## Input format
The input clauses and the thesis are stored in a .txt file line by line. The thesis should be separated from the knowledge by a line containg the `---` symbol. The content of a sample input file is presented below:

```
~PIES(x) | WYJE(x)
~POSIADA(x,y) | ~KOT(y) | ~POSIADA(x,z) | ~MYSZ(z)
~KIEPSKO_SYPIA(x) | ~POSIADA(x,y) | ~WYJE(y)
POSIADA(Janek,x) & KOT(x) | PIES(x)
---
KIEPSKO_SYPIA(Janek) & POSIADA(Janek,z) & MYSZ(z)
```
