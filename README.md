# Visitor Pattern
Sample problem featuring the visitor pattern.

## Task 1 - Reduce prices
Welcome to Pizza<sup>2</sup>! There has been a surcharge on pizza ingredients (sauce, cheese & dough) this past month. See for yourself by running the following command:

```
python visitor
```

Now we are finally seeing the prices drop. Implement the visitor design pattern to show a 50% drop in ingredient prices from original prices.

### Previous output

```
Sauce item: Price with Surcharge
2.36
Cheese item: Price with Surcharge
3.9000000000000004
Dough item: Price with Surcharge
5.8
```

### Desired output

```
Sauce item: Price with Price-drop
1.00
Cheese item: Price with Price-drop
1.50
Dough item: Price with Price-drop
2.0
```

## Task 2 - Testing

Our test coverage is pretty terrible. See for yourself by running the following commands:

```
coverage run --source visitor -m unittest discover tests
coverage report -m
```

Increase this to 100%.
