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
    *D-FSM*
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
            2. M is in any of the accept (final) states
        string ω is accepted by M, if there is a path that spells ω
        [EXAMPLES]: Ch2 pg. 22-25
    