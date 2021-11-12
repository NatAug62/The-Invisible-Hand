# C/C++ Conventions
## Naming
### General Info
The convention used here is adapted from the Python conventions. This will cause clashing styles between standard library and windows library conventions, though.

### Naming Styles
* File names - Files should have short, all-lowercase names. Underscores may be used if it improves readability. For example, `utils`
* Class names - Class names should use the CapWords/CamelCase convention. For example, `MyCustomClass`
* Function and Variable names - Function and variable names should be lowercase with words separated by underscores as needed to improve readability. For example, `my_var`
* Constants - Constants are written in all capital letters with underscores separated words. For example, `MAX_VAL` and `TOTAL`

## Docstrings
### General Info
The convention used here is adapted from the Python conventions. This will cause clashing styles between standard library and windows library conventions, though.
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition surrounded by /* and */.
Docstring format differs slightly between single-line and multi-line docstrings.

For example, a single-line docstring would be something like:
```C++
int foo(int a, int b) {
    /*One-line summary*/
```

A multi-line docstring, on the other hand, would be something like:
```C++
int foo(int a, int b) {
    /*One-line summary
    
    Additional details following a blank line
    Closing triple quotes on its own line
    */
```

### File Docstrings
File docstrings will use the following format:
```C++
/*One-line summary

Classes:
    name -- summary
Exceptions:
    name -- summary
Functions:
    name -- summary
Globals:
    name -- type, summary
*/
```

### Class Docstrings
```C++
/*One-line summary

Methods:
    name -- Overrides/Extends foo. Summary
Attributes:
    name -- Overrides/Extends foo. Summary
*/
```

### Function/Method Docstrings
Function/Method docstrings will use the following format:
```C++
/*One-line summary

Long summary (if needed)

Parameters
    name -- type, optional, summary
Returns
    type & value -- summary
Side Effects
    summary
Raises
    exception type -- conditions raised under
Restrictions
    conditions on when to (not) call
*/
```
