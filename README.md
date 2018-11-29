# Dateutil-br

Implementation to python-dateutil with to Pt-br language. "(>_&lt;)"

This implementation rewrites the constants used in the [dateutil](https://github.com/dateutil/dateutil) library's date parse.

You can see the repository `pypi` on: https://pypi.org/project/dateutil-br/

## Install

```sh
pip install dateutil-br
```

## Usage Exemples

```python
>>> from dateutil_br import BrParserInfo
>>> from dateutil.parser import parserinfo, parser

>>> print(parser(BrParserInfo()).parse('8/04/2018'))
"2018-04-08 00:00:00"

>>> print(parser(BrParserInfo()).parse('10 de abril de 2018'))
"2018-04-10 00:00:00"

>>> print(parser(BrParserInfo()).parse('15 horas e 13 min de 10 de abril de 2018'))
"2018-04-10 15:13:00"
```

## Maintainer

This code is sustained by Magrathea Labs, in the repository https://github.com/magrathealabs/dateutil-br

## License

The package is available as open source under the terms of the MIT License.
