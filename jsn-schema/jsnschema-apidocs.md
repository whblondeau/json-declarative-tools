## The JSNSchema API

### Notation and conventions


#### Terminology

**`value-assert`:** a statement that can be compared to a JSON value object. If the assertion is `true` about the value object, the object is said to be **value-compliant**.

**`constraint`:** The basic unit of schema-compliance testing. Consists of a 2-tuple: `(jsnpathexpr, set(value-assert))`
if **all** nodes found by selecting from a JSON object with `jsnpathexpr` are value-compliant with **all** `value-assert`s in the `constraint`, the JSON object is said to be **constraint-valid**.

**`schema`:** A collection of costraints. If a JSON object is found to be constraint-valid for *all** of the constraints in the schema, then the JSON object is said to be **schema-valid**.

When evaluating schema-validity for a JSON object, it's important to consider a couple of logical questions:

  - what if a constraint's JSNPath expression finds no nodes?
  
  - what if the object contains paths that are not evaluated for constraint-validity?
  
The answer lies in the difference between **required** and **permitted** evaluation.

A schema may contain constraints that require the presence of certain nodes: if they are missing from a JSON object, the object is not schema-valid. A schema may also contain constraints that are permitted but not required. The absence of a permitted node **will not break** schema-compliance.

However, the presence of any permitted constraint is _potentially_ a logical game-changer. It is possible, but not necessary, that a "permitted" constraint is intented simply to ensure the correct content of any node to which it applies, _if found_. However, it is also possible that a set of "permitted" constraints is intended to define the entire possible path/value space for a JSON object. In the latter case, for a JSON object to exhibit leafpaths that exceed the union of the "required" and "permitted" constraints' JSNPath expressions.

Accordingly another, analytical, capability of JSNSchema is to report **unconstrained paths**: Leaf paths in the JSON object that are not explicitly constrained by the schema. 

For a JSON object to be schema-valid with respect to a schema, all constraints must evaluate as `true` for the schema. In form, a schema's constraints must all have a unique `jsnpathexpr`, with all `valueassert`s about nodes identified by that path being contained in the single constraint. (This isn't a logical necessity: it's just a means of forcing users to keep all of their per-`jsnpathexpr`-applicable constraints in one place.)



----
----

### Core

----
`boolean **report_nonvalid(** schema, jsonobject **)**`

  if `jsonobject` evaluates as valid for all constraints in `schema`, returns a falsy value, indicating no complaints. If `jsonobject` is NOT valid, list complaints.
  
  This core schema-validation function is defined in terms of negative logic because all invalidations (including raised exceptions as well as genuinely invalid characteristics of `jsonobject`) merit an explanation; validity does not. Non-empty strings will evaluate as truthy.

----
`boolean **report_noncompliant(** constraint, jsonobject **)**`

 if `jsonobject` evaluates as `false` for any of the 

----


----
----
### Util

