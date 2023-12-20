def simplify_path(path):
    parts = path.split("/")
    stack = []

    for part in parts:
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != ".":
            stack.append(part)

    return "/" + "/".join(stack)

# Test the function with the provided examples
example1 = "/home/"
example2 = "/../"
example3 = "/home//foo/"

output1 = simplify_path(example1)
output2 = simplify_path(example2)
output3 = simplify_path(example3)

output1, output2, output3
