table2dicts
===========
Python module for converting a html table to a list of dictionaries

Installation
------------

TODO

Usage
-----

.. code-block:: python

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

    It is also possibly to convert a html table with no thead / tbody,
    in which case the first row is used as headers:

    >>> table2dicts('''
    ...    <table>
    ...        <tr><th>a</th><th>b</th><th>c</th></tr>
    ...        <tr><td>1</td><td>2</td><td>3</td></tr>
    ...        <tr><td>4</td><td>5</td><td>6</td></tr>
    ...    </table>
    ... ''')
    [{u'a': u'1', u'c': u'3', u'b': u'2'}, {u'a': u'4', u'c': u'6', u'b': u'5'}]

    Similarly, when no th is present, the first row of td is used as
    headers:

    >>> table2dicts('''
    ...    <table>
    ...        <tr><td>a</td><td>b</td><td>c</td></tr>
    ...        <tr><td>1</td><td>2</td><td>3</td></tr>
    ...        <tr><td>4</td><td>5</td><td>6</td></tr>
    ...    </table>
    ... ''')
    [{u'a': u'1', u'c': u'3', u'b': u'2'}, {u'a': u'4', u'c': u'6', u'b': u'5'}]
