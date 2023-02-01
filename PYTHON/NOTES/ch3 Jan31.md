# Jan 31st: Python Timethon ########################################

## CHAPTER 3: CONTROL ##############################################

**None**
    special value `None` returns Nothing 
        - function that does not specify will do this
        - `None` is Not displayed by the [Interpreter]

**Pure vs. Non-Pure**
    `Pure` - Just return Values        (ex: pow)
    `Non-Pure` - have Side Effects >,@ (ex: print)
    `Functional Programming` - Using only Pure Func.s in a Program

**Multiple Environments**
    *Life of a User-Defined Function*
        `Def Statement`: that whole def-return ordeal in func.s
            ex: name(formal_param):
                body = return return_expr(formal_param)
        `Call Expression`: what happens when body is executed
            ex: operator(operand)
        `Calling/Applying`: defining this all in the stack
            ex: argument -> signature.func() -> return val.
    *Multiple Environments in One Diagram*
        - an `Environment` is a Sequence of Frames
            Global Frame, Local-to-Global Frame

**Names Have No Meaning Without Environments**
    every Expression is evaluated in it's Enviornment's context
        - a `Name` implies a Reference found in it's Environment
    *Names Have Different Meanings in Different Environments*
        `Call Expressions` in the Name vs Body are Unique!!!
            - names can be reused here if absolutely necessary

**Misc. Python Features!**
    *Formal Params Formatting*
        program(n: int, d: string) -> tuple[int, string]
    *Conditional Statements*
        `Statement` - executed by the [Interpereter],
                        to perform an [Action]
        `Compound Statements` - have multiple statements in them!
        example:
            <header>           first header determines statement type
                <statement>    `Suite` -> group of statements
                <statement> ... 
             <header>          `Clause` -> controls if a suite is used
                <statement>
                <statement> ...    
            def statements are compound
        `Conditional Statements`
        example:
            <if>   {suite} 1 of these
            <elif> {suite} Zero or more of these
            <else> {suite} Zero or 1 of these
        `Boolean Contexts`:
            Contexts:
                - < , > , <= , >= , == , 
            False:
                - False, 0, '', None
            True:
                - True, anything else that isn't false
    *Iteration*
        `While Statements`
            <while> {statement}:     Evaluate Header Expression
                <suite>              Do This until Header == True
            
## GIT CRASH COURSE ##############################################

**COMMANDS LIST**
    `git init`       -> create empty repository
    `git status`     -> files committed status
    `git log`        -> shows version history 
        `--decorate` `--oneline`
    `git add <file>` -> self-explanatory `--all`
    `git commit -m "message"` -> self-explanatory  
    `git branch   <name>` -> creates a branch  
    `git checkout <name>` -> switch branch `-b`
    `git switch <name>` -> switch branches 
        `--create` -> self-explanatory (`-c` also)
        `-` -> return to last-visited branch

                