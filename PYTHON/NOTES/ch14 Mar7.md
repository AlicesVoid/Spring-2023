# Februrary 28.th Python Notes #   
  
## Chapter 14: Trees  
  
### Trees   
 **Basic Tree Components:**  
    `Nodes`  | An Element with a `Label`  
    `Label`  | Some Value/Weight of the `Node`  
    `Root`   | The Shallowest-Depth / Greatest-Height `Node` 
    `Branch` | `2-Node Connection` showing Parent-Child Ownership  
 **Basic Tree Implementation:**  
    *Components:*  
        `Tree`     | Some `Label` and a `List of Branches`  
        `Label`    | Some Value derived from a `Node`  
        `Branches` | Some List of `Nodes`  
        `is_tree`  | Verifies `Tree` has some `Node List`  
        `is_leaf`  | Verifies `Leaf` has no `Node List`
  
### Tree Processing  
 **Recursion**  
    - the Node-Oriented structure of Trees makes them easy to Recurr  
    - ex: `branch_counts = [ count_leaves (b) for b in branches(t)]`  
 **Creating Trees**
    - often includes Recursive Methods 
    - ex: `do something- if not here, then for all of my branches`