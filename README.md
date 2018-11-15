# msi
Assignments for the Artificial Intelligence Methods course

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
