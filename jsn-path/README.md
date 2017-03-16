## JSNPath

This specification tries to strike a helpful balance between the immense utility, power, and  apparently forbidding complexity of XPath on the one hand, and the familiarity of JSON notation on the other.

So, here's how it works:

  - All strings are unicode. Byte sequences must be cast to unicode before using.

  - Every path is a sequence of steps.

  - Every step, syntactically, is enclosed in square brackets `[ ]`

  - Every step is _named_ (as in a JS object or a Python dict), or numbered (as you do with an ordered sequence: a Python List or Tuple, or what JavaScript calls an "Array" LOL.)

  - An **ordered step** that specifies a single index uses the Python indexing: a nonnegative number for zero-based indexing from the start of the sequence; a negative number for one-based indexing from the end of the sequence. (The JavaScript equivalent is sequence.length + negative number.) (You can thank me later.)

  - An **ordered step)) that specifies a _range_ of numbers in the ordered parent ises the Python notation for slicing: [startswith:endsbefore]. For Javascript, this is converted to the `.slice(startswith, endsbefore)` syntax: way less cool, but logically equivalent.

  - An ordered step that does not specify a specific index is represented by the Empty Step `[]`.

  - A **named step** that specifies a 

  - A named step that is does not specify a name is represented by the Star Step `[*]`.

  - There is no syntax for an arbitrary number of Empty or Star steps. (I hope I can hold out on this.)



