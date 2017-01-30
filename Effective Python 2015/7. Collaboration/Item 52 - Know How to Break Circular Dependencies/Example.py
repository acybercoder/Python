"""
Things to Remember
Circular dependencies happen when two modules must call into each other at import time. They can cause your program to crash at startup.
The best way to break a circular dependency is refactoring mutual dependencies into a separate module at the bottom of the dependency tree.
Dynamic imports are the simplest solution for breaking a circular dependency between modules while minimizing refactoring and complexity.
"""

