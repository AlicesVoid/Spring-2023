# Feb. 15th. Compiler Notes #

**Regular Expressions (RE.s)**
    [See](/COMPILERS/NOTES/ch2%20Feb1.md)

**Regular Represent Set**
        (REs)       |     (Value of REs)
         ∅         |      { }             empty
         `ε`        |      {ε}
         a*         |      {ε,a,aa,aaa,...}
         `a+b`      |      {a,b}
         a*b        |      {ab}
         `a*+ba`    |      {ε,aaa...,ba}
                    |