"""Provides classes that are algebraic structures and classes that can be acted on by the algebraic structures.

The classes that are algebraic structures are 'Perm', 'PermGroup',
and 'PermCoset'.

Other classes in the package can be acted on
by the algebraic structures and use methods to find subalgebras
that stabilize the action. These classes are 'Grid', 'Code', and 'Graph'.
The 'Code' class is found within the 'PermCoset' module due to
its interdependence of the 'PermCoset' class.

These algebras behave similarly to categories by being able to take
direct products and coproducts among other categorical transformations.
Thus, these classes extend from the abstract class 'CAT'.

Classes that behave as factories for the classes described above are
'Cycle', 'RandomPerm', and 'SymGroup'. The class 'Combinatorics' has
common functions for enumerating subsets of a set of integers.

"""