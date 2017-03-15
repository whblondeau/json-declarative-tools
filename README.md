# json-declarative-tools
_tl;dr: a lightweight, ad-hoc toolkit that **unambitiously** provides minimal XPATH/XSLT-like declarative capability for JSON._

## Rationale and Rant
The immense benefits of declarative programming style are well understood by anyone who has ever worked with a well-designed declarative language. Some of the best of those are the XPath technologies, XSLT and XQuery. Since the JSON datamodel is a much-simplified but still valid subset of the XML datamodel, it would seem to be an obvious move to create, e.g., "JSONPath", "JSONSLT", "JSONQuery" to translate the benefits to the JavaScript world. Unfortunately, worthy efforts to get something going seem to have foundered. 

Why this happened has probably more to do with the fundamentally unserious nature of what's called "modern full-stack programming" than anything. Today's web programming discipline (if such it can be called) seems predominantly myopic and unsystematic, and plagued with faddishness. The benefits of declarative integrity seem to hold little purchase in the minds of javascript developers. Partly this is because JavaScript itself is a poorly designed and implemented language, and partly it's inherent in the Web's business priorities: short-term imperatives and the neverending quest for customer lock-in.

Currently, the best one can do is to translate JSON to a cleanly defined XML dialect and use the XML tools. However, the XML tools are not well understood in the JavaScript community, and XQuery in particular is not well understood most anywhere.

Furthermore, even if there were well-implemented JSONPath, JSONSLT etc, they'd probably not be much used.

Which brings us to `json-declarative-tools`.

## Design Overview

Since attempts to imitate the XML technologies have failed for reasons probably impossible to overcome, `json-declarative-tools` will be built from the ground up. Unusually, it will provide two parallel implementations: a **Python reference implementation** (for rigor and clarity) and a **JavaScript working implementation** for clientside and NodeJS programming.

### Principles
`json-declarative-tools` will not attempt to closely mimic the implementation of the XML toolsets.

`json-declarative-tools` will attempt to reproduce a modest subset of the _benefits_ of the XML toolsets, in a way that is accessible to JavaScript developers.

To that end, **`json-declarative-tools` consists of the following parts:**

  - **JSNPath**, a node selection notation;
 
  - **JSNSchema**, a simple means of validating a JSON instance against a set of JSNPath expression/requirement pairs;
 
  - **JSNTemplate**, an extremely simple templating language that defines an **output composed of:**
    - **nodes** drawn from an input JSON instance
    - simple **declarative expressions** that can access those nodes
    - **string literals** (HTML, Markdown, CSS plain text etc)
    - **parameters** passed at runtime
    JSNTemplate will be as simple and user-friendly as possible, providing affordances for aliasing JSNPath expressions using a simple notation.


