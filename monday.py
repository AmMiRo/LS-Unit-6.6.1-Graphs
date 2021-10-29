problem = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

# initialize total at 0
total = 0
# iterate through dict
for item in problem:
    # if value number add to total
    if isinstance(problem[item], int):
        total += problem[item]
# return total
print(total)