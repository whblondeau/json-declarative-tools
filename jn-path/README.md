## JNPath

This specification tries to strike a helpful balance between the immense utility, power, and  apparently forbidding complexity of XPath on the one hand, and the familiarity of JSON notation on the other. The end result, of course, is neither as powerful as XPath nor as immediately familiar as Javascript's Object and Array syntax, or Python's corresponding Dictionary and List.

----
### JNPath is different from XPath

There is no way JNPath is ever going to have the same analytical or expressive power as XPath. That's a feature, not a bug: as good as XPath is, it became pretty heavyweight. Capabilities, features, and syntax of JNPath will be chosen based on the following criteria:

  - Is this feature genuinely useful in real-world cases?
  
  - Is the syntax for its implementation cognitively clear? Nonconfusing? Salient? Idiomatic-ish?
  
  - Is it possible to implement without `[**]['Hell']`?

So no, your favoritest XPath thing ever isn't gonna get implemented. If JNPath is a 70% or even 60% solution, and usable, it'll be a thumping success.

Hopefully, it's at least big and dumb and obvious.

----

### JNPath Examples

`['stores']['*parrot'][*]`                  get all child nodes of any child of the  
                                            "stores" top-level node, whose name ends
                                            in "parrot"

`['stores'][**]['inventory'][*]`            get any child nodes of any "inventory"   
                                            descendants of the "stores" top-level node

`['student'](['first_name'] == 'Ann')[*]`   get the enture contents of every "student"
                                            record where the record's "first_name"
                                            property has a value of "Ann"

`[0]`                                       get the first top-level element of a JSON
                                            array object

`[-2]`                                      get the next to last top-level element
                                            of a JSON array object

`[**](['herp'] == 'derp')`                  get all nodes in the JSON object for
                                            which the "herp" property has a value
                                            of "derp"

`['books'][](no ['donor'])`                 get any nodes from the "books" top-level
                                            array that have no "donor" property

`['books'][](yes ['donor'])`                get any nodes from the "books" top-level
                                            array that do have a "donor" property
                                            (irrespective of "donor"'s value or
                                            lack of value)

`['books'][](falsy ['donor'])`              get any nodes from the "books" top-level
                                            array that have a "donor" property whose
                                            value is falsy `(null`, empty string,
                                            boolean `false`, etc)

`['books'][](empty ['donor'])`              get any nodes from the "books" top-level
                                            array that have a "donor" property whose
                                            value is an empty object or array

`['album']['tracks'][3][*]`                 get the fourth node from the "tracks" array 
                                            in the "album" top-level object

`['album']['tracks'][-1][*]`                get the last node from the "tracks" array
                                            in the "album" top-level object

`['album']['tracks'][2:7][*]`               get the third through seventh node from the  
                                            "tracks" array in the "album" top-level object

`['album']['tracks'][3, 5, 8][*]`           get the fourth, sixth, and ninth nodes from the  
                                            "tracks" array in the "album" top-level object

`['album']['tracks'][1:-1][*]`              get all nodes _except_ the first and last from
                                            the "tracks" array in the "album" top-level
                                            object

`[*]`                                       get all top-level nodes of a JSON object



#### Things the examples show

JNPaths are composed of square-bracketed **steps**. Each step represents traversal down into the JSON object. Typically, this is a direct traversal to a child node. (The special descent shortcut expression `[**]` is the only exception to this.)

**`namexpr` name expressions:**

When the square brackets contain a string, that's the name of a node. The name can be exact, or it can be a glob expression.

**`indexpr` index expressions:**

When the square brackets contain a number, that's the index of the node in its parent array.

`[nonnegative index]` is a zero-based index for a node's position in its parent array.

`[negative index]` is a one-based index counting backwards from the last item in the parent array. This is a very elegant and powerful syntax taken directly from Python. Its Javascript equivalent would be `parent.length + negativeindex`.

`[startwith:endbefore]` is slicing syntax, cribbed directly from Python but consistent with Javascript's `.slice(startwith, endbefore)`.

**Commas inside square brackets are boolean OR expressions:**

`[indexpr, indexpr,...]` is syntactic sugar allowing multiple numeric index expressions so you don't have to write a lot of separate JNPaths.

`[namexpr, namexpr,...]` is syntactic sugar allowing multiple name expressions so you don't have to write a lot of separate JNPaths.

**Wildcard node expressions**

`[]` means "any number" for an array index.

`['*']` means "any named node" -- really just a special case of glob.

`[*]` means "any node" irrespective of whether its parent is an object or an array.

`[**]` means "any descendant sequence" of nodes.

**where**

`(boolean expression)` is a WHERE clause applied to the immediately preceding step. (For those who know XPath, the irony will not be lost: in XPath the notation is "[boolean expression]".)

**Special boolean operators**

`yes` is syntactic sugar for "does the following expression find at least one existing node?"

`no` is syntactic sugar for "does the following expression find no existing nodes?"

`falsy` is syntactic sugar for "does the following expression find no nodes at all whose value is truthy?" Sense of this is equivalent to JavaScript's `truthy`/`falsy` semantics (NOT the same as Python's! Sorry, Pythonistas.)

`empty` is syntactic sugar for "does the following expression find at leaast one node whose value is an empty collection (i.e., JSON lists the value as `[]` or `{}`)?"

`not` is the boolean negative, same as Javascript's `!` or Python's `not`.

#### Return value "retexpr"

JNPath returns a very specific data structure for each node it finds. This is an array representing a 2-tuple:

`[<explicit path>, <node value>]`

where the explicit path includes the node's name (if the parent is an object) or index (if the parent is an array.)


----

So, here's how it works.

### JSON is a simple structure

A JSON object is a collection of nodes, whose structural relationships are hierarchical and acyclic. In other words, this means that nodes have the following possible _immediate relationships_:

  - parent

  - child

and **there are no sideways relationships.** (That's )

and the possible _transitive relationships_:

  - ancestor: a node that can be reached by following a sequence of one or more linked parent relationships; the immediate parent is the simplest possible case of this.

  - descendant: a node that can be reached by following a sequence of one or more linked child relationships; the immediate child is the simplest possible case of this.

A _path_, using these definitions, is an ordered sequence of descendance: one child node after the other. (If you evaluate it backwards, which is legit, it's a sequence of ascending parent nodes; but the convention in hierarchies is to descend.) 

A path represents a traversal of 




JNPath defines structural constraints on a JSON object. These constraints operates in two senses:

  - They can be evaluated with respect to a JSON instance to yield a boolean result of _conformance_, which is the basis of JNSchema.

  - They can 




### The Path Model

A **path** represents a JSON structure

A Path is a sequence of steps. Each step represents a set of possible JSON nodes. 

Some steps define exactly one node, and are called _exact_ steps.


  - All strings are unicode. Byte sequences must be cast to unicode before evaluation.

  - Every path is a sequence of **steps**. A step 


### Step Notation



  - Every step, syntactically, is enclosed in square brackets `[ ]`

  - Every step is _named_ (as in a JS object or a Python dict), or numbered (as you do with an ordered sequence: a Python List or Tuple, or a JavaScript Array.)

  - An **ordered step** that specifies a single index uses the Python indexing: a nonnegative number for zero-based indexing from the start of the sequence; a negative number for one-based indexing from the end of the sequence. (The JavaScript equivalent is sequence.length + negative number.) (You can thank me later.)

  - An **ordered step)) that specifies a _range_ of numbers in the ordered parent ises the Python notation for slicing: [startswith:endsbefore]. For Javascript, this is converted to the `.slice(startswith, endsbefore)` syntax: way less cool, but logically equivalent.

  - An ordered step that does not specify a specific index is represented by the Empty Step `[]`.

  - A **named step** that specifies a 

  - A named step that is does not specify a name is represented by the Star Step `[*]`.

  - There is a special syntax for an arbitrary number of Empty or Star steps: the `[**]`


