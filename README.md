# Data Frame normalization Project

### Purpose
The script main.py enables the user to run different kinds of normalization type on a numeric matrix using normData module. 
normData module provides several types of normalization for your matrix.

The input file should be a numeric matrix.

When running this the script, the user should choose the normalization type.


### Usage

install requirements
``` 
pip install -r requirements.txt
```

// how to run

For sum-normaliziation over columns, run:
``` 
python main.py sum <Path_Of_Csv>
```

for scaled normalization over columns, run:
``` 
python main.py scaling_range <Path_Of_Csv>
```


### Development

Ideally I would like to add several different noramlization methods (log scaling, Z-score, scalling to a range) to this module so the user can choose which type he needs.

### Tests
To test for code formatting run black --check --diff .