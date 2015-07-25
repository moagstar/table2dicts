#!/usr/bin/env python
"""Python module for converting a html table to a list of dictionaries."""
try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict
from bs4 import BeautifulSoup


def table2dicts(html):
    """
    Converts a html table to a list of dictionaries, for example:

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
    [OrderedDict([('a', '1'), ('b', '2'), ('c', '3')]), OrderedDict([('a', '4'), ('b', '5'), ('c', '6')])]

    It is also possibly to convert a html table with no thead / tbody,
    in which case the first row is used as headers:

    >>> table2dicts('''
    ...    <table>
    ...        <tr><th>a</th><th>b</th><th>c</th></tr>
    ...        <tr><td>1</td><td>2</td><td>3</td></tr>
    ...        <tr><td>4</td><td>5</td><td>6</td></tr>
    ...    </table>
    ... ''')
    [OrderedDict([('a', '1'), ('b', '2'), ('c', '3')]), OrderedDict([('a', '4'), ('b', '5'), ('c', '6')])]

    Similarly, when no th is present, the first row of td is used as
    headers:

    >>> table2dicts('''
    ...    <table>
    ...        <tr><td>a</td><td>b</td><td>c</td></tr>
    ...        <tr><td>1</td><td>2</td><td>3</td></tr>
    ...        <tr><td>4</td><td>5</td><td>6</td></tr>
    ...    </table>
    ... ''')
    [OrderedDict([('a', '1'), ('b', '2'), ('c', '3')]), OrderedDict([('a', '4'), ('b', '5'), ('c', '6')])]

    :param html: The html table to convert to a list of dictionaries.
    :return: list of dictionaries with data from the html.
    """
    
    def _get_headers_and_values(soup):
        headers = [x.string or '' for x in soup.select('table tr th')]
        if len(headers) == 0:
            # maybe no th specified? just use the first row of td's
            headers = [x.string or '' for x in soup.select('table tr')[0].select('td')]
        values = [x or '' for x in soup.select('table tr')][1:]
        return headers, values
        
    soup = BeautifulSoup(html)
    headers, values = _get_headers_and_values(soup)
    result = [
        OrderedDict([
            (str(headers[i]), str(y.decode_contents()))
            for i, y in enumerate(x.select('td'))
        ])
        for x in values
    ]
    
    return result
