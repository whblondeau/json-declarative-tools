## The JNPath API

### Notation and conventions

The API is written in a functional style. 

**Functions have no side effects.** 

  - A function does not modify its operands.
  
  - A function does not update any kind of state data anywhere. Data manipulations within functions are scoped to the function's execution. That which is not returned is discarded.

**Functions are referentially transparent.** A function's return value depends solely upon its operands. Functions do not consult application state in order to modify their return.

**Function names** are either 

  - **verbs,** when a resultset of some sort is returned, or 
  
  - **assertions,** when a boolean result is returned.

**When there is a single argument,** the argument is operated upon by the function.

**When there are multiple arguments,** the first argument is the context, and subsequent arguments are evaluated in terms of the context. In grammatical terms, the first argument is the subject; the function name is the verb; and the rest of the arguments are objects.

So, for example,

  `selects( selectorpath, instancepath )`
  
which returns a `boolean`, is equivalent to the natural language assertion "`selectorpath` selects `instancepath`"; and in object-oriented syntax it would be something like:

  `selectorpath.selects(instancepath)`

#### Terminology

**`container`:** a JSON value of object or array type; "container type" refers to those two types. The complementary term 
**`non-container`** identifies all other JSON values (string, number, boolean, the various null/None signifiers).

**`instancepath`:** a JNPath expression without any multiselect syntax. In any given JSON object, it identifies zero or one nodes. The last node's unique identifier (property name or array index) is the final step in `instancepath`.

**`leafnode`:** a JSON node whose value is either:

  - of a non-container type, or 
  
  - an empty container.

**`leafpath`:** an `instancepath` terminating in a leaf node. 

**`selectorpath`:** a JNPath against which instancepaths can be evaluated.

**`noderep`:** a two-tuple `(instancepath, value)` representation of an extant node. `value` is the value of the node.

**`jsonobject`:** either a JSON datastructure or a serialization of a JSON datastructure. If the latter, a function will attempt to parse `jsonobject`, raising an exception if `jsonobject` is unparseable.

----
----

### Core

----
`boolean selects( selectorpath, instancepath )`

  `selectorpath` is a JNPath expression against which `instancepath` is compared. If `selectorpath` describes `instancepath`, returns `true`, else `false`

----
`set(noderep) read_leafpaths( jsonobject )`

  This function computes and returns all extant leafpaths in `jsonobject`, returning them and their values.

----
`set(noderep) select_nodes( selectorpath, jsonobject )`

  This function returns all leafpaths in `jsonobject` for which `selects( selectorpath, leafpath )` == `true`.


----
----
### Util

`boolean contains( jnpath, jnpath )`

  Compares any two JNPath expressions. Does NOT evaluate selection. Returns `true` if the first argument is equal to the second, or if the first argument begins with the second but is longer. Essentially, this is a descendant/ancestor checker.
  
`boolean is_leafnode( nodeval )`
 
  Tests whether `nodeval` is a childless .
  
`boolean is_instanceform( jnpath )`

  Tests whether `jnpath` is of instancepath form (i. e., free of JN special multiselect or node-conditional syntax).
  

  

