This is a README FILE for Cron Parser

# Cron Parser

This project provides a command-line utility for parsing and expanding cron expressions. It takes a cron string as input and expands each field to show the times at which it will run. The utility supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Usage

To use the utility, run the `Parsing.py` script with a cron expression as an argument. For example:

## Usage
```
python Parsing.py */15 0 1,15 * 1-5 /usr/bin/find
```

This will output the expanded cron expression in a table format:
```
minute       0 15 30 45
hour	       0
day of month 1 15
month	       1 2 3 4 5 6 7 8 9 10 11 12
day of week	 1 2 3 4 5
command	     /usr/bin/find
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


