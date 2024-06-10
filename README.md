This is a README FILE for Cron Parser

# Cron Parser

This project provides a command-line utility for parsing and expanding cron expressions. It takes a cron string as input and expands each field to show the times at which it will run. The utility supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Usage

To use the utility, run the `Parsing.py` script with a cron expression as an argument. For example:

## Usage
```
$-python Parsing.py */15 0 1,15 * 1-5 /usr/bin/find
```

This will output the expanded cron expression in a table format:
```
minute	      0 15 30 45
hour	      0
day of month  1 15
month	      1 2 3 4 5 6 7 8 9 10 11 12
day of week	  1 2 3 4 5
command	      /usr/bin/find
```


## Testing

To run the unit tests, navigate to the `test` directory and execute the following command:

```
python -m unittest discover -s test
```

This will run all the test cases defined in the project.

## Files and Folders

- `Parsing.py`: Main script for parsing cron expressions.
- `test`: Directory containing unit test files.
  - `Test_Validation.py`: Test cases for validation of cron expressions.
  - `Test_Parsing.py`: Test cases for parsing and expanding cron expressions.



Idea :

* - means all (regex terms)
/ - per
15  as provided in question this means 15 mins
we need to keep a valid range of values of all the fields
we need to check if the values provided with space separation are valid inputs or not
so it breaks down from starting hour (0) 0, 15, 30, 45 (loops around this)
1,15 day of month (we have comma seperated value so it means it would be 1st and 15th day of month)
month is represented by * so it would be running every month (show 1-12 count)
day of week  1-5 (-) the interval is represented by - sign left value is start and right is the end
command is the last section of the information

We can start with creating a library which contains the meaning of signs 
We would have to set the maximum length of the each field so that we can 
trace the different intervals based on different expressions

* -> all the elements in the range of that field
- -> in the interval of provided len inclusive field values
, -> all the comma separated values
/-> ???
