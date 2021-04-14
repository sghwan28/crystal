txt = "apple, banana, cherry, split, kky"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 3)

print(x)

# note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.