# Predictive Parser  
By: Amelia Rotondo  
Last Modified: Apr 27, 2023  

## How to Parse:
- `parse(input_string):` parses an input string- returns a Boolean value dictating if the input string is accepted or not. Stack Operations and Parse-Acceptance can be seen from the Terminal.  

## Parsing Examples:
Below Line 117 are examples of various strings and their parsing results. This includes one string for testing functionality, and three strings for demonstration purposes. 

## Parsing Logic:
- `predictive_parse_table` is a dictionary of nonterminals, each with nested dictionaries of terminals, whos values are production rules.  
- `lookup_parse_table(nonterminal, terminal):` is used to find production rules from the `predictive_parse_table` according to their respective nonterminal and terminal input values.  
- `parse(input_string):` is the core method to parse input strings, using both the `predictive_parse_table` and `lookup_parse_table(nonterminal, terminal):` to achieve this parsing. It prints the stack each time the stack changes, as well as a conclusion of whether `input_string` is accepted or not.