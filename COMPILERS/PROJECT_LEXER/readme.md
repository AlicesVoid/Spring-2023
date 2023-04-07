# CPSC 323 PROJECT 1: The Lexer #   
> Author: Amelia Rotondo   
> Last Modified: April 6th, 2023    

# File Reading/Writing:  
1. The Lexer reads a single text file named `input_scode.txt`
2. The Lexer writes a single text file named `output.txt`
  
# Input Format:  
This lexer is abridged, and does not include all C++ Methods for concision purposes. The methods supported by this lexer are:   
- All Real Numbers 
- All Integers  
- All Identifiers  
- All Arithmatic Operators  
- The Following Separators: 
    - `()` and `;`  
- The Following Keywords: 
    - `while`  
  
# Output Format: 
The lexer outputs a two-column list that shows the token type and lexeme. This two-column list takes the following format:  
1. The first row shows the format of the output: `TokenType | Lexeme`  
2. The second row is blank 
3. The remaining rows represent the input code in the format of the first row.  
    - (ex: `KEYWORD | while`)  