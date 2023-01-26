# Jan 25: Programming Languages and Compilers (Intro/Ch.1) #

**Coding Language Purposes**
    *Scientific Computing*
        - Good float points, good arrays, parallelism, etc-
            - ex1: Fortran
    *Business Computing*
        - persistence, good report facilities, data analysis, etc-
            - ex1: SQL
    *System Programming*
        - control of resources, real time constraints, etc-
            - ex1: C/C++

**Basic Terminology**
    [Compiler]
        - software to convert Source Code to Target-Machine's Code
    [Source_Language]
        - Programming High-Level Language used in Compiler Input
    [Object_Language]
        - Particular Machine Language used in Compiler Output
    [Object_File]   
        - An External File storing Object Code (ex: myProj.obj) 
    [Target_Machine]
        - Computer designated to run the Object Code 

**Compiler History**
    *A-0 System (1951)* 
        - Written by Grace Hopper
        - Functioned as a Linker/Loader
    *Fortran 1 (1950s)*
        - 1st Successful HL Programming Language 
        - 1st Commercially Available Compiler 
        - Outline is Preserved in Modern Compilers

**Compiler Structure**
    1. Lexical Analysis 
    2. Syntax Analysis (Parsing)
    3. Semantic Analysis 
    4. Intermediate Code Generation
    5. Code Optimization
    6. Target Code Generation
    *Lexical Analyzer*
        - [Lexemes] and [Tokens]
            - a [Lexeme] is a string of char.s
                - Lowest-Level Syntactic Unit in the Language
                - Nearly-Inifnite Amount of These
            - a [Token] is a category->class of [Lexemes]
                - For Instance, "Keywords" or "Operators"
                - Small Amount of These
        - Does Other Things Too
            - Removes White-Space, Ignores Comments, Case-Conversion
    *Syntax Analyzer*
        - Uses Boolean Math to check if Input Code is Logically Sound
        - [Parser]
            - Determines the Tokens Recognized in a Lexical Analyzer
        - [Parse_Tree]
            - Boolean-Math Tree that displays logical argument of code
            