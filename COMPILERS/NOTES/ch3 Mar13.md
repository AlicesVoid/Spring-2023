# March 6.th Compiler Notes #   
  
## Chapter 3: Syntactic Parsing 1 (Top-Down Parsing) ##  
  
### SIDENOTE:    
 `* IMPLIES 0 OR MORE, + IMPLIES 1 OR MORE`  
  
### 3.3: Chomsky Heirarchy of Grammars  
 **Notation Conventions:**  
    - nontermials | `A,B,C,...`  
    - terminals   | `a,b,c,...`  
    - greek chars | `α, β, δ, γ  ... strings of N and T`  
 **Hierarchy:**  
    *Type 0: Unrestricted Grammar*  
        - Form α → β , where α and β are Any string of N and T  
    *Type 1: Context-Sensitive Grammar*  
        - Form α → β ,  |β| ≥ |α| , changes n.t's 1 at a time  
    *Type 2: Context-Free Grammar*  
        - Form A → β , A is a Single Nonterminal (n.t)  
    *Type 3: Regular Grammar*  
        - Form A → β , A is Single n.t, β is all terminals or 1 n.t   
  
### Parsers (Trees)  
 **CFL to Parser:**  
    *Top-Down Parser:*  
        - Start at the Root, end at a Leaf  
        `Eliminating Left Recursion` :  
            [METHOD:]  
                - Introduce a new nonterminal   
                - Modify the new Nonterminal to take an ε (empty)  
            [EXAMPLE:]  
                - A  → δA'  
                - A' → aA' | ε (without ε , A' doesn't terminate)  
    *Bottom-Up Parser:*  
        - Starts at a Leaf, ends at the Root`  
  