# CellDeathCounter

This was designed to help wet-lab scientist be able to count avaiable live cells that are within an image.
Death is signified by red fluorescents, while live are indicated by green fluorescents.

## How to use
First install the conda environment using

```conda env create -f celldeath.yml```

Then you can call from the command line

```python cellcount.py --folder <path-to-images>```


## Output

This will generate a csv file that has the count for each image and a total image at the end as well.
The csv file will be called `counts.csv`


## Problems

If there are any problems that arise make sure to generate an issue and I will fix it. 
