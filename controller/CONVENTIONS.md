# Python Conventions
## Naming
## Documentation
### Docstrings
#### General Info
The convention used here is based on [PEP 257](https://www.python.org/dev/peps/pep-0257/).
As defined, "a docstring is a string literal that occurs as the first statement in a module, function, class, or method definition" surrounded by triple quotes.
Docstring format differs slightly between single-line and multi-line docstrings.

For example, a single-line docstring would be something like:
```Python
def foo(a, b):
    """One-line summary"""
```

A multi-line docstring, on the other hand, would be something like:
```Python
def foo(a, b):
    """One-line summary
    
    Additional details following a blank line
    Closing triple quotes on its own line
    """
```

#### Module Docstrings
As explained in PEP 257, "the docstring for a module should generally list the classes, exceptions and functions (and any other objects) that are exported by the module, 
with a one-line summary of each. (These summaries generally give less detail than the summary line in the object's docstring.)"
However, I will slightly deviate from this convention and include ALL classes, exceptions, functions, globals, and any other objects within the module, not just
those that are exported.

Module docstrings will use the following format:
```Python
"""One-line summary

Classes:
    name -- summary
Exceptions:
    name -- summary
Functions:
    name -- summary
Globals:
    name -- summary
"""
```

#### Class Docstrings
As explained in PEP 257, "the docstring for a class should summarize its behavior and list the public methods and instance variables." Once again, I will slightly deviate from
this convention and include ALL methods and instance variables, not just those that are public.
Additionally, "if a class subclasses another class and its behavior is mostly inherited from that class, its docstring should mention this and summarize the differences. 
Use the verb "override" to indicate that a subclass method replaces a superclass method and does not call the superclass method; 
use the verb "extend" to indicate that a subclass method calls the superclass method (in addition to its own behavior)."

Class docstrings will use the following format:
```Python
"""One-line summary

Methods:
    name -- Overrides/Extends foo. Summary
Attributes:
    name -- Overrides/Extends foo. Summary
"""
```

#### Function/Method Docstrings
As explained in PEP 257, "the docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, 
and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. 
It should be documented whether keyword arguments are part of the interface."

Function/Method docstrings will use the following format:
```Python
"""One-line summary

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
"""
```
