# Cron Parser

This project provides a command-line utility for parsing and expanding cron expressions. It takes a cron string as input and expands each field to show the times at which it will run. The utility supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Clone the repository:
```bash
git clone https://github.com/quertify/Cron_Parser.git
cd Cron_Parser
```

## Usage
To use the utility, run the `main.py` script with a cron expression as an argument. For example:

### Usage in Windows
```
python main.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```
### Usage in Linux
```
python3 main.py "*/15 0 1,15 * 1-5 /usr/bin/find"
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
### You can now see the next five iterations of the parsed expression
note : We will make it better looking in the next version

```
minute         0 5 10 15 20 25 30 35 40 45 50 55
hour           0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /path/to/command
Next cron iteration would be at: 2024-07-15 00:00:12
Next cron iteration would be at: 2024-07-15 00:05:12
Next cron iteration would be at: 2024-07-15 00:10:12
Next cron iteration would be at: 2024-07-15 00:15:12
Next cron iteration would be at: 2024-07-15 00:20:12
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
```
cronparser/
├── __init__.py
├── constants.py
├── interfaces.py
├── validators.py
├── parsers.py
├── schedulers.py
├── printers.py
├── cron_expression.py
tests/
├── __init__.py
├── test_cron_expression.py
├── test_default_cron_validator.py
├── test_default_cron_parser.py
main.py
```
## Assumptions and Limitations

- Standard Cron Format: The project assumes that the input cron expressions adhere to the standard cron format, including five time fields (minute, hour, day of month, month, day of week) followed by a command.
- The cron expression follows the standard format with five time fields (minute, hour, day of month, month, and day of week) plus a command.
    Each field has a specific range:
    - `Minutes: 0 to 59`
    - `Hours: 0 to 23`
    - `Day of Month: 1 to 31`
    - `Month: 1 to 12, also accepts [JAN-DEC]`
    - `Day of Week: 0 to 6 (Sunday to Saturday) also accepts [MON - SUN]`
    - `Year: 1990 to 2090`
- No Special Time Strings: The project doesn't handle special time strings such as "@yearly" or "@daily".
- Valid Input: It assumes that users provide valid cron expressions as input. The program doesn't extensively validate the input beyond basic syntax checks.
- No External Dependencies: The project assumes that it doesn't require any external dependencies beyond the standard Python libraries.
- Command-Line Interface: It's assumed that users interact with the program via the command line, providing cron expressions as arguments.
- Single Cron Expression: The project processes a single cron expression at a time.
- Output Formatting: The output is formatted as a table with each field name followed by the corresponding times at which it will run. The output format adheres to the specifications provided.
- Python Version Compatibility: The project is assumed to be compatible with Python 3.x versions

## Further Enhancements:
- Next step is to make it better looking
- Add more tests
- Add features like arguments
- accept multiple cron expressions
- allow to switch off the next iteration part
