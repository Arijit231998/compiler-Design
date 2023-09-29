def eliminate_left_recursion(grammar):
    new_grammar = {}
    epsilon = "EPSILON"

    for non_terminal, productions in grammar.items():
        alpha = []
        beta = []

        for production in productions:
            if production[0] == non_terminal:
                alpha.append(production[1:])
            else:
                beta.append(production)

        if len(alpha) > 0:
            new_non_terminal = non_terminal + "'"
            new_grammar[non_terminal] = [b + new_non_terminal for b in beta]
            new_grammar[new_non_terminal] = [a + new_non_terminal if a != epsilon else epsilon for a in alpha] + [epsilon]
        else:
            new_grammar[non_terminal] = productions

    return new_grammar

# Example usage:
input_grammar = {
    "S": ["S + S", "S * S", "a"]
}

result_grammar = eliminate_left_recursion(input_grammar)

for non_terminal, productions in result_grammar.items():
    print(non_terminal, "->", " | ".join(productions))