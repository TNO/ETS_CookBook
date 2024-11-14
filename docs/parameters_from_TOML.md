# Parameters from TOML

## What it does
Reads a TOML parameters file name and returns a dictionary of parameters.




## Inputs
### parameters_file_name
A string containing the path and name of a TOML file.
## Output

###

## Examples
You can then call the values in the following way:
```python
scenario['Level_1']['Level_2']
```
You can also use Box
```python
scenario.Level_1.Level_2
```

Note that if one of the levels is a variable string, then you need to call
it as such 
```python
scenario[Level_1]['Level_2']
```

You can also use Box
```python
scenario.[Level_1].Level_2
```

###

## Tests

###


## Open issues
