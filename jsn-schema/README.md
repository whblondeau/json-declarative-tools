# JSNSchema

JSNSchema is a very simple toolset, far less capable and powerful than XML Schema.

An instance of a JSNSchema is an object (Javascript) or dictionary (Python) whose name keys are JSNPath expressions and whose values are boolean assertions about the nodes found by evaluating the JSNPath. Taken together, these things are called JSNSchema _assertions_.

There are two general categories of assertion: **required** for the JSON object to be schema-valid, and **permitted** in order to remain schema-valid.

In general, one node in violation of schema=validity is a thumbs down for the entire JSON object.

There are some specific keywords and functions established for making assertions about the values of node objects.
