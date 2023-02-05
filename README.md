This script receives a numric DataFrame and sum-normalizes it (each cell divided to the sum of its column).

You can use this script as an easy way to normalize your data.

The input should be a numeric pandas Dataframe.

The output will be the fractions of of each column.

example: 

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
