"""
Things to Remember
Packages in Python are modules that contain other modules. Packages allow you to organize your code into separate, non-conflicting
namespaces with unique absolute module names.
Simple packages are defined by adding an __init__.py file to a directory that contains other source files. These files become the child
modules of the directory¡¯s package. Package directories may also contain other packages.
You can provide an explicit API for a module by listing its publicly visible names in its __all__ special attribute.
You can hide a package¡¯s internal implementation by only importing public names in the package¡¯s __init__.py file or by naming internal-only
members with a leading underscore.
When collaborating within a single team or on a single codebase, using __all__ for explicit APIs is probably unnecessary.
"""