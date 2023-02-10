# Data Frame normalization Project

### Purpose
This script receives a numeric DataFrame and sum-normalizes it (each cell divided to the sum of its column).

You can use this script as an easy way to normalize your data.

The input should be a numeric pandas Data-frame.

The output will be the fractions of of each column.


### Example: 

Input dataframe:
```
       S1 S2
 Gene1 30 10
 Gene2 50 45
 Gene3 20 45
```
Output dataframe:
```
      S1  S2
Gene1 0.3 0.1
Gene2 0.5 0.45
Gene3 0.2 0.45
```

### Usage


 To run the script 
 ``` python

 ```

### Development

Ideally I would like to add several different noramlization methods (log scaling, Z-score, scalling to a range) to this module so the user can choose which type he needs.

### tests
To test for code formatting run black --check --diff .