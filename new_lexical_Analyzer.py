import re

# Regular expressions for identifying tokens
keyword_regex = r"\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b"
identifier_regex = r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"
constant_regex = r"\b\d+\b"
arithmetic_op_regex = r"[\+\-\*/]"
logical_op_regex = r"(==|!=|>=|<=|>|<)"
parenthesis_regex = r"[()\[\]{}]"
punctuation_regex = r"[;,]"

# Read input from file or keyboard
filename = input("Enter input file name or press Enter to type input:\n")
if filename:
    with open(filename, "r") as f:
        input_str = f.read()
else:
    input_str = input("Enter input:\n")

# Remove redundant spaces, tabs, and newlines
input_str = re.sub(r"\s+", " ", input_str).strip()

# Remove comments
input_str = re.sub(r"//.*|/\*.*?\*/", "", input_str, flags=re.DOTALL)

# Identify tokens
keywords = re.findall(keyword_regex, input_str)
identifiers = re.findall(identifier_regex, input_str)
constants = re.findall(constant_regex, input_str)
arithmetic_ops = re.findall(arithmetic_op_regex, input_str)
logical_ops = re.findall(logical_op_regex, input_str)
parentheses = re.findall(parenthesis_regex, input_str)
punctuation = re.findall(punctuation_regex, input_str)

# Identify duplicate identifiers
duplicates = set()
unique_identifiers = []
for identifier in identifiers:
    if identifier in duplicates:
        continue
    duplicates.add(identifier)
    unique_identifiers.append(identifier)

# Print tokens
print(f"Keyword ({len(keywords)}): {', '.join(keywords)}")
print(f"Identifier ({len(unique_identifiers)}): {', '.join(unique_identifiers)}")
print(f"Constant ({len(constants)}): {', '.join(constants)}")
print(f"Arithmetic Operator ({len(arithmetic_ops)}): {', '.join(arithmetic_ops)}")
print(f"Logical Operator ({len(logical_ops)}): {', '.join(logical_ops)}")
print(f"Parenthesis ({len(parentheses)}): {', '.join(parentheses)}")
print(f"Punctuation ({len(punctuation)}): {', '.join(punctuation)}")