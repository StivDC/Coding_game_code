import ast
x = "{'a':('1', [1, 2, 3]), 'b': '2'}"
y = ast.literal_eval(x)
print(y)
