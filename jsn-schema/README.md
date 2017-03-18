# JSNSchema

JSNSchema is a very simple toolset, far less capable and powerful than XML Schema. On the other hand, it's hopefully much easier to understand and use.

An instance of a JSNSchema is a collection of **constraints** on the structure and content of a JSON instance. A constraint is a 2-tuple: ( JSNPath expression, set( value-assertiont )). Any constraint may be compared to any JSON instance. There are two logically distinct forms of evaluation:

  - **require** evaluation of the JSON results in `false` if the JSNPath expression is not found in the JSON object. This form of evaluation is used to establish **minimal** compliance with a JSNSchema,
  
  - **permit** evaluation returns `true` if the JSNPath expression is not found in the JSON object. This form of evaluation is used to establish a **superset** of valid JSON content, over and above what the evaluation of required cpnstraints defines.
  
In either case, if **all** values obtained by selecting nodes with the constraint's JSNPath expression are compliant with **all** value-assertions in the constraint, the result evaluates as `true`. Otherwise the evaluation is `false`: the JSON object is not compliant with the constraint.

A JSNSchema **schema** is a collection of constraints. The JSNPath expressions of the constraints must all be unique within the scope of the schema. Accordingly, the JSNSchema in-memory implementation type is an object (Javascript) or dictionary (Python) whose name keys are JSNPath expressions.

JSNSchema serialization is intended for reasonable sight-reading.

There are two general categories of assertion: **required** for the JSON object to be schema-valid, and **permitted** in order to remain schema-valid.
