Task01
```python3 -m doctest -v -o ELLIPSIS task1/test_morse.py >task1/result.txt```

Task02
```python3 -m pip install pytest```
```python3 -m pytest task2/test_morse.py -v >task2/result.txt```

Task03
```python3 -m unittest task3/test_ohe.py -v```

Task04
```python3 -m pip install pytest```
```python3 -m pytest task4/test_ohe.py -v >task4/result.txt```

Task05
```python3 -m pip install pytest```
```python3 -m  pip install pytest-cov```
```python3 -m pytest -v --cov-report=html:task5/htmlcov --cov=task5 task5/ >task5/result.txt```
