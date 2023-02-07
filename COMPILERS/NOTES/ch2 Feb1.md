# Feb 1.st Chapter #? Notes: (Probably Making These Up Too Lawl) #

**2.5 Regular Expressions (REs)**
    - Means to describe languages
    - Class of Expressions that coincides with Class:Regular Languages
    - REs -> more compact way to define a language / acceptance case
    - ex: 
        (O U 1)01* -> the set of all binary strings that:
            start with either 0 or 1         (0 U 1)
            the second symbol is 0           (01)
            the ending is some amount of 1's (1)
    *Definition:*
        `let Σ be a non-empty alphabet:`
            1. [ε]  is a Regular Expression
            2. [∅] is a Regular Expression
            3. For each alphabet symbol `a ∈ Σ`, 
               [a]  is a Regular Expression  
        `if...:`
            1. R1 and R2 ∈ REs, then R1 U R2 ∈ REs -> [R1|R2] ∈ REs
            1. R1 and R2 ∈ REs, then [R1R2] ∈ REs (concatenation)   
            2. R ∈ RE         , then `Kleene star` [R*] ∈ REs  
                a. Kleene Star -> Concatenation of Strings from R
                b. R+ = R*R
        `also these...`
            1. L1 and L2 ∈ Languages, R1 U R2 -> L1 U L2 
            2. L1 and L2 ∈ Languages, R1R2 -> L1L2
            3. Yes, even R* -> L* 
    *Example 1*
        Given: Σ = {0,1}: 
            (0, 1, 01, 10, 0|1, 1*, 1+,0*1, etc...) ∈ REs

**2.6 FSMs and REs**
    [GOAL:]
        develop a procedure for generating state tables for Lex Anal.
    *Note:*
        - FSM is a good "visual" aid, but not concise enough for use
            - use REs instea silly goose!
        - REs are like if FSMs were more readable 
            - define "tokens" and etc. stuff 
    *FSM and RE Similarities*
        [Theorem:]
            There exists a FSM for each RE, and vice-versa
        [Application:]
            `Thomson Construction Method`
                - Build an FSM from smaller, inductive FSMs 
                - For each RE, define a NFSM (ch.2 pg.56)
                - Edges are NOT marked ε
                - Next, convert each NFSM to a DFSM
    *RE Operands:*
        Operands are the same as Edge Labels for FSMs
            - single characters / special character ε
            - letters and digits 
            - sometimes we use quotes (ex: | * ( ) needs parentheses)
        [Precedence:]
            RE operator  | Analogous Arithmetic op. | Precedence
                |           plus                        lowest
                ()          times                       middle
                *           exponentiation              highest