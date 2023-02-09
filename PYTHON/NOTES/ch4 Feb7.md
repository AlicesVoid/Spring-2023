# Feb 7.th Python Notes # 

## Ch.4: Higher Order Func.s ##

**Describing Functions**
    `Domain` -> all the possible inputs  taken as arg.s
    `Range`  -> all the possible outputs given as val.s
    `Behavior` -> Relationshup between Domain and Range
    *A Guide to Function Design:*
        - give each function, 1 job, but make it multi-applicable
        - DRY (don't repeat yourself)

**Generalization**
    *Patterns with Algorithms*
        Generalizing Geometry: separate like-minded functions
        [EXAMPLE:]
            2D Shape Area ~~ radial-factor and constant-shape-factor:
                circle  = pi            * (r^2)
                square  =  1            * (r^2)
                hexagon = (3*sqrt(3))/2 * (r^2)

**Higher-Order Functions**
    *Summation Notation*
        summation Σ ~ from i=1 to n : process(i)
            ex:
                i=1 Σ 5: i^3 -> 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 255
        [NOTE:]
            when coding, pass ONE NUM and ONE FUNC for Transparency

**Functions as Return Values**
    *Locally-Defined Functions*
        Func.s defined in Func. Bodies are bound to Local Frames
    *Call Expressions as Operator Expressions*
        `Operator(Init.) ( Operand )` //this format works too!!

**Lambda Expressions**
    [METHOD:]
        lambda input : output(x)
    *Why not use Def statements?*
        Def statements have `intrinsic names`
        Lambda statements have a preset placeholder name (dumb haha)
