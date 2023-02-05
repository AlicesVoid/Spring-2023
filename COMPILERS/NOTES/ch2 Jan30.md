# Jan 30.th Ch2 Notes: Lexical Analysis #

**2.1: Basics**
    *Tasks of the Lexer:*
        -tokenizing source (break up source code)
        -removing comments (overpass)
        -case conversion, if necessary
        -interperetation of compiler directives (ifdef, etc-)
        -deal with [pragmas] (significant comments)
        -saving source locations (file/line/col.) for error msg.s
    *Vocab*
        `token`  - generic type of meaningful unit (keyword,operator)
        `lexeme` - the actual unit instance in the code (if,x,then)
    *Writing a Lexer*
        -each Token can be represented w/ regular expressions
            -represented with a `Finite State Machine (FSM)`
    *FSMs*
        - Allow you to Generate Code within Input Guidelines
        [Deterministic](DFSM)
            - No state has more than one outgoing edge w/ same label
        [Non-Deterministic](NFSM)
            - states may have more than one outgoing edge / same label
            - edges may be labeled with ε (epsilon) (empty string) (λ)
            - automation can make ε transition without consuming input
    **D-FSM**
        `DFSM=(Σ, Q, q0, F, N)` meanings:
            Σ = finite set of input symbols
            q0 ∈ Q is the starting state
            F ⊆ Q is a set of accepting (or final) states
            N: (Q x Σ) -> Q is the State Transition Function
        Notes: 
            - N is a Deterministic Function
            - If N is not fully determined, use a Null State 
    *FSM as a Graph*
        `State`            |[Circle]
        `Start State`      |[Circle] [Pointed-At]
        `Accepting State`  |[Circle] [Bordered]
        `Transition`       |[Circle] [Variable-Line] [Circle-Connect] 
    *Transitions*
        In-State -> (a) -> Out-State
            - if (a), then go to Out-State
            - got stuck? = failed
    *FSM Implementation*
        Table-Driven Approach:
            `Table`
                - 1 row for each Machine State
                - 1 col for each Possible Character
            `Table[j][k]`
                - 3D Table of State `j` on Input Char `k` 
                - Empty Slot = Program got Stuck 
    *DFSM String Acceptance/Rejection*
        DFSM M string recognition if:
            1. entire string has been read
            2. M is in ANY of the accept (final) states
        string ω is accepted by M, if there is a path that spells ω
        [EXAMPLES]: Ch2 pg. 22-25
    *DFSM CODE IMPLEMENTATION*
        `def DFSM(ω : string):`
            `table = array[1..states, 1...alphabets]`  of integer
            `state = 1` the starting state
            `for i in len(ω):`
                `col   = char_to_col(ω[i])` returns col# of table.ch
                `state = table[state, col]` table is TRANSITION-BASED
            `if state ∈ F:`
                `return 1` the state does exist
            `else:`
                `return 0` the state doesn't exist
    **N-FSM**
        `DFSM=(Σ, Q, q0, F, N)` meanings:
             = finite set of input symbols
            q0 ∈ Q is the starting state
            F ⊆ Q is a set of accepting (or final) states
            N: Q x ( Σ U ε) -> P(Q) is the State Transition Function
        Notes: 
            - The symbol ε (epsilon) means no input symbol
            - ε implies just finding a new, working state
            - 1 input can go to multiple states (NOT DFSM)
    *NFSM String Acceptance/Rejection*
        same as DFSM LOL
    *Equivalence of DFSM and NFSM*
        - a `Language` is any set of strings
        - a `Language over an alphabet Σ` string made from char ∈ Σ
        - a `Language accepted by M` L(M) is all strings ∈ Σ ACCEPTED
        [THEOREM:]
            - the Class of Languages accepted by DFSMs and NFSMs is the same. That is, for each NFSM there is an equivalen DFSM, and vice versa. 
        - every `DFSM` can be written as `NDFSM` without `NFSM` tools
        - Every `NFSM` has an equivalent `DFSM` that exists 

**BUILDING A DFSM from a NFSM**
    - For Any NFSM M, we can construct a 'DFSM M'
    - `Given:`
        NFSM M = (Σ, Q, q.0, F, N) -> DFSM M = (Σ', Q', q.0', F', N')
    - `Steps:`
        1. get rid of Epsilon Translations
        2. Solve the Multiple-State Problems
            Σ’ = Σ
            Q’ = POWERSET of States in M (include Null/Empty Set!)
            F’ = all states in Q' that contain One Accepting State ∈ M
          q.0’ = q.0
            N’ : such that ->
                `N’([P1, P2, ...Pn], x ∈ Σ’)` = 
                    `N(P1, x ) U N(P2,x) U...` 
                        `...U ∈ N (Pn,x) in [   ]`
