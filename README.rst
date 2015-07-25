.. image:: https://travis-ci.org/moagstar/table2dicts.svg?branch=master
:target: https://travis-ci.org/moagstar/table2dicts

table2dicts
=========== 
Python module for converting a html table to a list of dictionaries.

Installation
------------

TODO

Usage
-----

Give it some html with a :code:`table`:

    >>> from table2dicts import table2dicts
    >>> table2dicts('''
    ...    <table>
    ...         <thead>
    ...             <tr><th>a</th><th>b</th><th>c</th></tr>
    ...         </thead>
    ...         <tbody>
    ...             <tr><td>1</td><td>2</td><td>3</td></tr>
    ...             <tr><td>4</td><td>5</td><td>6</td></tr>
    ...         </tbody>
    ...    </table>
    ... ''')
    [{u'a': u'1', u'c': u'3', u'b': u'2'}, {u'a': u'4', u'c': u'6', u'b': u'5'}]

No :code:`thead` or :code:`tbody`, no problem:

    >>> table2dicts('''
    ...    <table>
    ...        <tr><th>a</th><th>b</th><th>c</th></tr>
    ...        <tr><td>1</td><td>2</td><td>3</td></tr>
    ...        <tr><td>4</td><td>5</td><td>6</td></tr>
    ...    </table>
    ... ''')
    [{u'a': u'1', u'c': u'3', u'b': u'2'}, {u'a': u'4', u'c': u'6', u'b': u'5'}]

When no :code:`th` is present, the first row of :code:`td` elements is used as a header:

    >>> table2dicts('''
    ...    <table>
    ...        <tr><td>a</td><td>b</td><td>c</td></tr>
    ...        <tr><td>1</td><td>2</td><td>3</td></tr>
    ...        <tr><td>4</td><td>5</td><td>6</td></tr>
    ...    </table>
    ... ''')
    [{u'a': u'1', u'c': u'3', u'b': u'2'}, {u'a': u'4', u'c': u'6', u'b': u'5'}]
