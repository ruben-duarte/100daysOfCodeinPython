Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> tuples
No Python documentation found for 'tuples'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> LIST
No Python documentation found for 'LIST'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> LISTS
Mutable Sequence Types
**********************

The operations in the following table are defined on mutable sequence
types. The "collections.abc.MutableSequence" ABC is provided to make
it easier to correctly implement these operations on custom sequence
types.

In the table *s* is an instance of a mutable sequence type, *t* is any
iterable object and *x* is an arbitrary object that meets any type and
value restrictions imposed by *s* (for example, "bytearray" only
accepts integers that meet the value restriction "0 <= x <= 255").

+--------------------------------+----------------------------------+-----------------------+
| Operation                      | Result                           | Notes                 |
|================================|==================================|=======================|
| "s[i] = x"                     | item *i* of *s* is replaced by   |                       |
|                                | *x*                              |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s[i:j] = t"                   | slice of *s* from *i* to *j* is  |                       |
|                                | replaced by the contents of the  |                       |
|                                | iterable *t*                     |                       |
+--------------------------------+----------------------------------+-----------------------+
| "del s[i:j]"                   | same as "s[i:j] = []"            |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s[i:j:k] = t"                 | the elements of "s[i:j:k]" are   | (1)                   |
|                                | replaced by those of *t*         |                       |
+--------------------------------+----------------------------------+-----------------------+
| "del s[i:j:k]"                 | removes the elements of          |                       |
|                                | "s[i:j:k]" from the list         |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.append(x)"                  | appends *x* to the end of the    |                       |
|                                | sequence (same as                |                       |
|                                | "s[len(s):len(s)] = [x]")        |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.clear()"                    | removes all items from *s* (same | (5)                   |
|                                | as "del s[:]")                   |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.copy()"                     | creates a shallow copy of *s*    | (5)                   |
|                                | (same as "s[:]")                 |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.extend(t)" or "s += t"      | extends *s* with the contents of |                       |
|                                | *t* (for the most part the same  |                       |
|                                | as "s[len(s):len(s)] = t")       |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s *= n"                       | updates *s* with its contents    | (6)                   |
|                                | repeated *n* times               |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.insert(i, x)"               | inserts *x* into *s* at the      |                       |
|                                | index given by *i* (same as      |                       |
|                                | "s[i:i] = [x]")                  |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.pop()" or "s.pop(i)"        | retrieves the item at *i* and    | (2)                   |
|                                | also removes it from *s*         |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.remove(x)"                  | remove the first item from *s*   | (3)                   |
|                                | where "s[i]" is equal to *x*     |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.reverse()"                  | reverses the items of *s* in     | (4)                   |
|                                | place                            |                       |
+--------------------------------+----------------------------------+-----------------------+

Notes:

1. *t* must have the same length as the slice it is replacing.

2. The optional argument *i* defaults to "-1", so that by default the
   last item is removed and returned.

3. "remove()" raises "ValueError" when *x* is not found in *s*.

4. The "reverse()" method modifies the sequence in place for economy
   of space when reversing a large sequence.  To remind users that it
   operates by side effect, it does not return the reversed sequence.

5. "clear()" and "copy()" are included for consistency with the
   interfaces of mutable containers that don’t support slicing
   operations (such as "dict" and "set"). "copy()" is not part of the
   "collections.abc.MutableSequence" ABC, but most concrete mutable
   sequence classes provide it.

   New in version 3.3: "clear()" and "copy()" methods.

6. The value *n* is an integer, or an object implementing
   "__index__()".  Zero and negative values of *n* clear the sequence.
   Items in the sequence are not copied; they are referenced multiple
   times, as explained for "s * n" under Common Sequence Operations.

Related help topics: LISTLITERALS

help> quit()
No Python documentation found for 'quit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
help('ASSERTION')
The "assert" statement
**********************

Assert statements are a convenient way to insert debugging assertions
into a program:

   assert_stmt ::= "assert" expression ["," expression]

The simple form, "assert expression", is equivalent to

   if __debug__:
       if not expression: raise AssertionError

The extended form, "assert expression1, expression2", is equivalent to

   if __debug__:
       if not expression1: raise AssertionError(expression2)

These equivalences assume that "__debug__" and "AssertionError" refer
to the built-in variables with those names.  In the current
implementation, the built-in variable "__debug__" is "True" under
normal circumstances, "False" when optimization is requested (command
line option "-O").  The current code generator emits no code for an
assert statement when optimization is requested at compile time.  Note
that it is unnecessary to include the source code for the expression
that failed in the error message; it will be displayed as part of the
stack trace.

Assignments to "__debug__" are illegal.  The value for the built-in
variable is determined when the interpreter starts.

quit
Use quit() or Ctrl-Z plus Return to exit
num = 5
#variable address
id(num)
2847033131376
name = 'Ruben'
id(name)
2847039788848
a = 10
b = a
a
10
b
10
id(a)
2847033131536
id(b)
2847033131536
id(10)
2847033131536
k = 10
id(k)
2847033131536
a = 9
id(a)
2847033131504
id(b)
2847033131536
k = a
id(k)
2847033131504
b = 8
id(b)
2847033131472
PI = 3.1415
PI
3.1415
PI = 3.14
type(PI)
<class 'float'>
