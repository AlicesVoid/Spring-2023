# Feb. 9th, Software Notes #

## Ch.23: Software Review Stuff? ##

**Reviews**      DIFFERENT REVIEW OPTIONS MATRIX (ch.23 pg.21)
    - Meeting Conducted for Technichal People:
        - to assess the technichal quality of the software product
        - good for `quality assurance` and training
    *What Do We Look For?*
        - [Errors]   -> QA problem BEFORE release
        - [Defects]  -> QA problem AFTER  release
        Note:
            [Defects] are WAY WORSE than [Errors], so
                we try to minimize them by eliminating [Errors] early!

**Defect Amplification**
    - Defects can get really bad if Errors are left unfixed
    [NOTE:]
        `EARLIER REVIEW FOR ERRORS BEST IMPROVES DEFECT AMP. ODDS!`
    *Defect Amplification Model:*
        - contains: Defect, Error Output, and %-Detection-Efficiency
    *Defect-Math:*
                E.review = E.p + E.a + E.r 
                Err.tot  = Err.min + Err.maj
        `Defect Density` = Err.tot / WPS    
            [E.p] -> `Preparation Effort` (in-person hours)
            [E.a] -> `Assessment  Effort` (in-person hours)
            [WPS] -> `Work Product Size`  (measurable |db| model)
        [Err.min] -> `Number of Minor Errors`
        [Err.maj] -> `Number of Major Errors`

**Informal Reviews**
    *Methods*
        - simple desk-check with a colleague
        - casual meeting (+2 people) for review purpose
        - `pair-programming` for review-aspects
            - encourages `continuous review`

**Formal Technichal Reviews (FTR)**
    - Class of Reviews that inclues `walkthroughs/inspections`
    - 3 to 5 people (typically), 2 or more hours (expected)
    - Preparation of work in advance
    - Focus on a `work product`
    *Objectives:*
        - uncover Errors in software
        - verify software is meeting requirements
        - ensure software is being represented correctly
        - achieve software that is uniform in development
        - make projects manageable
    *Roles:*
        1. Producer      -> developer
        2. Review Leader -> evaluates overall product
        3. Reviewer(s)   -> reviews work
        4. Recorder      -> recorder

**Sample-Driven Reviews**
    - Inspects a Fraction of software for faults, and expands on that!
    *Method:*
         `f.i = 1 / a.i`
          a.i -> a Fraction of Software i (ex: 1/5th of the code)
          f.i -> Estimate of the number of Faults in the Software

