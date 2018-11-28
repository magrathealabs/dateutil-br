# dateutil-br

Implementation to python-dateutil with to Pt-br language. "(>_&lt;)"

```python
print(type(parser().parse('2018 April 10')))
print(parser(BrParserInfo()).parse('8/04/2018'))
print(parser(BrParserInfo()).parse('10 de abril de 2018'))
print(parser(BrParserInfo()).parse('15 horas e 13 min de 10 de abril de 2018'))

```
