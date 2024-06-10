# Cron Parser

This project provides a command-line utility for parsing and expanding cron expressions. It takes a cron string as input and expands each field to show the times at which it will run. The utility supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Clone the repository:
```bash
git clone https://github.com/quertify/Cron_Parser.git
cd Cron_Parser
```

## Usage
To use the utility, run the `Parsing.py` script with a cron expression as an argument. For example:

### Usage in Windows
```
python Parsing.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```
### Usage in Linux
```
python3 Parsing.py "*/15 0 1,15 * 1-5 /usr/bin/find"
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

To run the unit tests, navigate to the `Cron_Parser` directory and execute the following command:

### Usage in Windows
```
python -m unittest discover -s test
```
### Usage in Linux
```
python3 -m unittest discover -s test
```

This will run all the test cases defined in the project.

## Files and Folders

- `Parsing.py`: Main script for parsing cron expressions.
- `test`: Directory containing unit test files.
  - `test_validation.py`: Test cases for validation of cron expressions.
  - `test_parsing.py`: Test cases for parsing and expanding cron expressions.


## Limitations
1. Special strings such as @yearly @annually etc are not handled
2. String notations of weekdays and month names like MON, TUE .. and JAN, FEB.. are also not handled
3. Some special characters such as L, W are also beyond scope of this cron parser