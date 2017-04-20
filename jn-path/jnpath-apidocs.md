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

##### JSON data types in JNPath

**`array`:** an ordered container whose contents are identified by position (JavaScript `array`, Python `list`)

**`map`:** an unordered container whose contents are identified by `string name` (Javascript `object`, Python `dict`, Perl `hash`, Java `map`; chose "map" because it's short and generic. JSON's official term "object" in particular is far too generic, which is probably a tribute to JavaScript's simple object model.)

**`container`:** the superset of `array` and `map`. Containers may contain child instances. In contrast, the following **`value`** types are incapable of holding additional structural elements in JSON:

  - `string`: always unicode. Typically encoded in UTF-8. Note that, in Python 2, "string" refers to a byte sequence in ASCII encoding. Python 2 uses the `unicode` type to refer to unicode character sequences; conversion between these two string types is awkward and frequently misunderstood. That's why Python 3 switched to "string" meaning a sequence of unicode characters; and that's why the JNPath reference implementation is in Python 3.

  - `number`: a float or integer. Note that many numeric types are typically represented as formatted strings in JSON. Date and Time are good examples of this.

  - `boolean`: in documentation we use capitalized `True` and `False` for the two boolean values, per the Python convention. (This is mainly for salience: `true` and `false` still seem more natural and are the literals in a serialized JSON object. But they are also useful words in natural language.)

  - `null`: any of the various "not a value" usages that various languages support. (Python `None`, Javascript and Java `null`, etc.)


**`leaf value`:** either an **empty** container, or a non-container data element:


**`step`:** a single JNPath element.



**`node`:** a 2-tuple of a `step` and a `value`.

**`stepsequence`:** a sequence of 0 to n `step` elements.

**`path`:** a stepsequence considered in the context of an actual or hypothetical JSON object.

**`leaf`:** 

**`container`:** a JSON value of object or array type; "container type" refers to those two types. The complementary term 
**`non-container`** identifies all other JSON values (string, number, boolean, the various null/None signifiers).

**`wildcard`:** a path step expression of the following types:
  - **`[*]`**, the **general wildcard**, which matches any valid step.
  - **`['*']`** or **`["*"]`**, the **namestep wildcard**, which matches any valid namestep, but no index step.
  - **`[]`**, the **index wildcard**, which matches any valid index step, but no namestep.
  
**`multiselect`:** a path step expression that matches some, but not all, steps of the corresponding type:
  - **`['`globexpr`']`** or **`["`globexpr`"]`**, the **glob step**, where globexpr is an otherwise valid namespace step containing one or more **`*`** characters. It matches any step according to the well-understood behavior of glob matching.
  - **`[`startswith`:]`** or **`[:`endsbefore`]`** or **`[`startswith`:`endsbefore`]`**, the **slicing step**, which matches a range of index numbers according to slicing syntax.

**`instancepath`:** a JNPath expression without any multiselect or node-conditional syntax. In any given JSON object, it identifies zero or one nodes. The last node's unique identifier (property name or array index) is the final step in `instancepath`.

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
----
### Util

`boolean contains( jnpath, jnpath )`

  Compares any two JNPath expressions. Does NOT evaluate selection. Returns `true` if the first argument is equal to the second, or if the first argument begins with the second but is longer. Essentially, this is a descendant/ancestor checker.

  
`boolean is_leafvalue( nodeval )`
 
  Tests whether `nodeval` is childless : either an empty container or a non-container JSON type.

  
`boolean is_instanceform( jnpath )`

  Tests whether `jnpath` is of instancepath form (i. e., free of JN special multiselect or node-conditional syntax).


`step[] select_steps( level, jnpath )`

  `level` is either an integer or a slicing expression: it therefore identifies either a single step or a contiguous sequence of steps. This function returns
  all steps in the path that match the level expression -- with order preserved -- or None if there are no matching paths. 

  This never throws index out of bounds exceptions.
  

  

