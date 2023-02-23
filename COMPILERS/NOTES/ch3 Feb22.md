# Feb 22.nd COMPILER notes #

## Ch 3 Syntactic Analysis 1 ##

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