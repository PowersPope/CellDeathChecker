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

If there are any problems that arise make sure to generate an issue and I will fix it. I wrote this fairly quickly so someone could get a rough estimate of cells. I am guessing there are errors. If anyone wants/needs to use it feel free to make an issue and I will make it more modular so you can input your own min_cell_area, cell_area_avg, and connected_cell_area.
