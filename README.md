MaxLines
========

A python script to count the min and max length of a CSV column

Developed to make importing CSV data into SQL Server easier.  
The MSSQL Data Importer doesn't look at the entire file to determine column lengths.  

So if you have a long CSV file...
where the length of the first cell/column of lines 1-100 is less than 50 characters
and 
where the first cell/column in some line beyond line 100  has a length greater than 50 characters

It will fail the import and you will have no idea what to size your columns to.

That's where this script comes in.

Usage
========

Change 
```python
2: with open('test.csv', 'rb') as f:
```
to be the name of the CSV file relative to the script (or the system root)
- Looking to build some command line args to make this easier.  Suggestions welcome

