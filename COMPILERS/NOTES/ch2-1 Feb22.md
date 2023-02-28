# Feb 22.nd COMPILER notes #

## Ch 2.1 Pumping Lemma ##

### RECAP: RLs ###############################################
 **RLs:**
    - `Formal Language` that can be defined by an `Reg.Expr.` & `FSA`   
    - VERY useful  
    *How to Prove This?*   
        - Build an FSA that can Accept It  
    *Example:*  
        - B = {(0^𝑛)(1^𝑛)| n ≥ 0}   //this is Not Regular (counting)  
        - L = {1(01)*}              //this is a Regular Language

### PUMPING LEMMA ################################################
 **How to PUMP Lemma?**  
    1. Fulfill the Pumping Reqirements seen below:   
 **PUMPING Requirements:**   
    1. `|y|  >  0`     //  string w ∈ L with |w| ≥ p (= pump strength)  
    2. `|xy| <= p`     //  has substring w = xyz s.t. these req.s:  
    3. `x(y^i)z ∈ L for ∀{i ≥ 0}`  
        a. Note: for any i ≥ 0 string xyiz ∈ L  
    **Proof Conditions:**  
        *Proof By Contradiction:*  
            1. Assume `L is Regular`
            2. `Pump Lemma` to guarantee some Pumping Strength  
            3. Find a `string s ∈ L` that `CANNOT be Pumped`  
                a. NOTE: you cannot choose p (assumed proven)  

### Syntactic Analysis (Parsing) Intro ############################   
 **Parsing:**  
    - example: parse the code `height = (width + 56) * factor(foo)`   
    *Steps:*   
        1. Lexer Output:   
            a. `id:height = (id:width + int:56) * id:factor (id:foo)`  
        2. Next Step?  
            a. determines if the Input Sequence of Tokens is `Valid`  
 **Lexer vs Parser:**  
    *Lexer:*  
        String of `Characters` -> Sequence of `Tokens`
    *Parser:*
        Sequence of `Tokens` -> Syntactic `Parse Tree`

### Grammar ###  
 **Grammar**  
    - A set of rules for proper conversation when writing code  
 **Noam Chomsky**  
    *4 Types of Grammar*  
        `0. `            -> [CFL] -> Turing Machine  
        `1. C-Sensitive` -> [CSL] -> Linear Bounded   
        `2. CFG `        -> [CFL] -> Push Down Automata  
        `3. RG `         -> [RL]  -> FSA  
  
### Context-Free Grammars (CFG) ###  
 **4 Tuples**  
    `V` -> `Set of Variables / Non-Terminals` (uppercase)  
    `T` -> `Set of Terminals` (finite) (lowercase)  
    `S` -> `Start Symbol` (unique)  
    `P` -> `Production Rules` (Bracket Line-Diagram Method)  
 **Derivations**  
    - Transformation of a Variable using an Existing Rule  
        ( i.e: =G> , S =G> aSa =G> abSba =G> abba)  
        ( i.e: S =G> *abba ) //this is the Shortened Form  
    *Theorem 1:*  
        `string β =G> γ` implies there exist a:  
             rule `A =G> w ∈ R` s.t:  
                 β = u A v   
                 γ = u w v  
                 `uAv =G> uvw`  
    - Now, we generate language: `L(G) = {x ∈ T* | S =G> *x}`  
    [NOTE:]  
        - `Language L` is a `CFL` if `∃ a CFG G s.t. L = L(G)`  
    *HOW TO SOLVE!?*  
        - Literally Just Execute the Steps until you Solve or Fail2