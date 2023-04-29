# Amelia Rotondo
# Last Modified: 4/26/2023

#The Actual Parse Tables:
predictive_parse_table = {
    "E": {
        "a": "TQ",
        "+": "error",
        "-": "error",
        "*": "error",
        "/": "error",
        "(": "TQ",
        ")": "error",
        "$": "error"
    },
    "Q": {
        "a": "error",
        "+": "+TQ",
        "-": "-TQ",
        "*": "error",
        "/": "error",
        "(": "error",
        ")": "e",
        "$": "e"
    },
    "T": {
        "a": "FR",
        "+": "error",
        "-": "error",
        "*": "error",
        "/": "error",
        "(": "FR",
        ")": "error",
        "$": "error"
    },
    "R": {
        "a": "error",
        "+": "e",
        "-": "e",
        "*": "*FR",
        "/": "/FR",
        "(": "error",
        ")": "e",
        "$": "e"
    },
    "F": {
        "a": "a",
        "+": "error",
        "-": "error",
        "*": "error",
        "/": "error",
        "(": "(E)",
        ")": "error",
        "$": "error"
    }
}

#Method to Lookup the Parse Table
def lookup_parse_table(nonterminal, terminal):
    # Check if the nonterminal is in the parse table
    if nonterminal not in predictive_parse_table:
        return "error"
    
    # Check if the terminal is in the parse table for the current nonterminal
    if terminal not in predictive_parse_table[nonterminal]:
        return "error"
    
    # Return the production rule associated with the nonterminal and terminal
    return predictive_parse_table[nonterminal][terminal]
    
#Method to Parse an Input String using Above Functions
def parse(input_string):
    # Initialize the parser stack and pointer to the first input symbol
    stack = ["$", "E"]
    input_pointer = 0
    
    # Loop until the parser stack is empty or an error is encountered
    while len(stack) > 0:
        # Get the current stack symbol and input symbol
        current_symbol = stack[-1]
        input_symbol = input_string[input_pointer]
        
        # If the current symbol and input symbol match, advance the input pointer and pop the stack symbol
        if current_symbol == input_symbol:
            input_pointer += 1
            stack.pop()
        else:
            # Look up the production rule in the parsing table
            production_rule = lookup_parse_table(current_symbol, input_symbol)
            
            if production_rule == "error":
                # Terminate Parser
                print("Input string is not in the grammar")
                return False
            elif production_rule == "e":
                # Pop the top symbol from the stack
                stack.pop()
            else:
                # Apply the production rule by popping the corresponding number of symbols from the stack
                # and pushing the left-hand side of the rule onto the stack
                stack.pop()
                for symbol in reversed(production_rule):
                    stack.append(symbol)
        
        # Print the current stack
        print("Stack:", stack)
    
    # If the input pointer has reached the end of the input string and the stack contains only the start symbol, the input is valid
    if input_pointer == len(input_string) and len(stack) == 0:
        print("Input string is in the grammar")
        return True
    else:
        # Otherwise, the input is invalid
        print("Input string is not in the grammar")
        return False

############################### PARSING EXAMPLES: ###########################
#input_string_test = "(a+a)$"
input_string_1 = "(a+a)*a$"
input_string_2 = "a*(a/a)$"
input_string_3 = "a(a+a)$"

#accepted_test = parse(input_string_test)
accepted_1 = parse(input_string_1)
accepted_2 = parse(input_string_2)
accepted_3 = parse(input_string_3)
    

