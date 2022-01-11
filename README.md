# djnStats
Work-in-progress. Python command-line program providing various statistical analysis tools to be performed on datasets in .csv format.

The program assumes that the first row of the .csv files contains the names of the variables, and the other rows contain the (numerical) data associated with each variable.

The program is called as follows:

```
python3 main.py DATA.csv
```

Where `data.csv` is your .csv file. *Please note that Python 3.10 or above must be used* due to the use of match-case statements.
