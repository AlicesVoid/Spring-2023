import re
import os

class LexerCPP:

    # Constructor
    def __init__(self, file_path):
        self.token_types = []
        self.lexemes = []
        self.cpp_code = self.read_cpp_code_from_file(file_path)
        self.tokenize()

    # CPP Text-File Reading Method
    def read_cpp_code_from_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    # Tokenizes CPP Code
    def tokenize(self):
        # Regular expressions for integers, identifiers, operators, and separators
        integer_regex = r'\b\d+\b'
        real_regex = r'-?\d+(\.\d+)?([eE][-+]?\d+)?'
        identifier_regex = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
        operator_regex = r'[<>=+\-*/%]'
        separator_regex = r'[();]'

        # Other tokens in the code, such as keywords
        other_tokens = {
            'while': 'KEYWORD',
        }

        # Iterate over each token in the input code
        find_token_regex = r'\d+\.\d+|\w+|[()<>;=]|[-+*/]|(?:\|\||&&)'
        for token in re.findall(find_token_regex, self.cpp_code):
            if re.match(real_regex, token):
                self.token_types.append('REAL')
                self.lexemes.append(token)
            elif re.match(integer_regex, token):
                self.token_types.append('INTEGER')
                self.lexemes.append(token)
            elif re.match(identifier_regex, token):
                token_type = other_tokens.get(token, 'IDENTIFIER')
                self.token_types.append(token_type)
                self.lexemes.append(token)
            else:
                for char in token:
                    if char in other_tokens:
                        self.token_types.append(other_tokens[char])
                        self.lexemes.append(char)
                    elif re.match(operator_regex, char):
                        self.token_types.append('OPERATOR')
                        self.lexemes.append(char)
                    elif re.match(separator_regex, char):
                        self.token_types.append('SEPARATOR')
                        self.lexemes.append(char)

    # Prints the Types and Lexemes
    def write_tokens_to_file(self, output_file='output.txt'):
        with open(output_file, 'w') as file:
            file.write("TokenType | Lexeme\n\n")
            for token_type, lexeme in zip(self.token_types, self.lexemes):
                file.write(f"{token_type} | {lexeme}\n")


# Get the directory of the script and join it with the input file name
script_directory = os.path.dirname(os.path.abspath(__file__))

# Collects the Input File 
cpp_path = os.path.join(script_directory, 'input_scode.txt')

# Instantiate the LexerCPP class and tokenize the C++ code
lexer = LexerCPP(cpp_path)

# Print the token-types and lexemes lists
lexer.write_tokens_to_file()
