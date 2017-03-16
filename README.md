# json-declarative-tools
_tl;dr: a lightweight, ad-hoc toolkit that **unambitiously** provides minimal XPATH/XSLT-like declarative capability for JSON._

## Rationale and Rant
The immense benefits of declarative programming style are well understood by anyone who has ever worked with a well-designed declarative language. Some of the best of those are the XPath technologies, XSLT and XQuery. Since the JSON datamodel is a much-simplified but still valid subset of the XML datamodel, it would seem to be an obvious move to create, e.g., "JSONPath", "JSONSLT", "JSONQuery" to translate the benefits to the JavaScript world. Unfortunately, worthy efforts to get something going seem to have foundered. 

Why this happened has probably more to do with the fundamentally unserious nature of what's called "modern full-stack programming" than anything. Today's web programming discipline (if such it can be called) seems predominantly myopic and unsystematic, and plagued with faddishness. The benefits of declarative integrity seem to hold little purchase in the minds of javascript developers. Partly this is because JavaScript itself is a poorly designed and implemented language, and partly it's inherent in the Web's business priorities: short-term imperatives and the neverending quest for customer lock-in.

Currently, the best one can do is to translate JSON to a cleanly defined XML dialect and use the XML tools. However, the XML tools are not well understood in the JavaScript community, and XQuery in particular is not well understood most anywhere.

Furthermore, even if there were well-implemented JSONPath, JSONSLT etc, they'd probably not be much used.

Which brings us to `json-declarative-tools`.

## Design Overview

Since attempts to imitate the XML technologies have failed for reasons probably impossible to overcome, `json-declarative-tools` will be built from the ground up. Unusually, it will provide two parallel implementations: a **Python reference implementation** (for rigor and clarity) which is usable in CLI scripting and serverside Flask/DJango development; and a **JavaScript working implementation** for clientside and NodeJS programming.

Besides their obvious merits for the task, Javascript and Python share a peculiar distinction:

    _JSON syntax is valid Javascript. It is also valid Python._

In other words, a JSON string is an `expression`, which can be directly evaluated, in both languages. Most languages need to parse a JSON string in order to obtain the corresponding datastructure.

Yes, direct evaluation, as opposed to parsing, of unknown strings can be dangerous. But `json-declarative-tools` will not concern itself with the problems of sanitizing input. That, Dear Reader, is on you.

### Principles
`json-declarative-tools` will **not attempt to closely mimic** the implementation of the XML toolsets.

`json-declarative-tools` will attempt to **reproduce a modest subset of the _benefits_** of the XML toolsets, in a way that is accessible to JavaScript developers.

`json-declarative-tools` will provide **no affordances for incorporated imperative programming.** 

`json-declarative-tools` will define **minimal, language-independent notation** as necessary. 

To that end, **`json-declarative-tools` consists of the following parts:**

  - **JSNPath**, a node selection notation;
 
  - **JSNSchema**, a simple means of validating a JSON instance against a set of JSNPath expression/requirement pairs;
 
  - **JSNTemplate**, an extremely simple templating language that defines an **output composed of:**
    - **nodes** drawn from an input JSON instance
    - simple **declarative expressions** that can access those nodes
    - **string literals** (HTML, Markdown, CSS, plain text etc)
    - **parameters** passed at runtime
    
    JSNTemplate will be as simple and user-friendly as possible, providing affordances for aliasing JSNPath expressions using a simple notation.

### How does `json-declarative-tools` differ from the XML toolsets?

  - **No Namespaces.** This is pretty obvious, since JSON doesn't support namespaces in the first place. But it's a hopeful sign. About 94% of the time, when somebody can't work out why their XPath expression isn't getting the correct results, or their XSLT isn't bringing the right information across, when _It's right there, goddammit_, the blame for the confusion goes to namespaces. Not going to re-litigate the considerable merits of namespaces right now, but as a practitioner and would-be evangelist, it's probably the biggest obstacle to XML tools' adoption I've seen.

  - **Restricted Capabilities.** Almost all of the XML tools suffered grievously from the academic compulsion to provide a sound and logically complete solution. Unfortunately, _the cost of getting to 100% is never linear._ That last 20% takes twice as long, and generates twice as many problems, as the first 80%.

  So, JSNPath will not offer the stunning array of selectors and facets that XPath does. JSNSchema and JSNTemplate will restrict themselves to a modest and immediately useful set of goals.

  - **Syntactic Clarity at all times.** To me, XML and the XML tools were quite reasonable. But I was one of those people who could sight-read XML Schema, so my view of the technologies was warped going in. I eventually found out that I was a useful but really rather unwelcome weirdo in a world full of people who got all kinds of strident butt-hurt when someone needed them to close a tag. So, the design constraint here is that `json-declarative-tools` is going to put a lot of work into being:

    - visually simple,

    - cognitively accessible,

    - resistant to casual error;

  As much as JSON's origins will permit.


### "Declarative". WTF?

Not giving this up. It works too damn well.

The secret about declarative programming is: it takes about as long as imperative programming, but there's no real bug list. Just some reminders about things you forgot to specify.

This is some kind of astonishing difference. Leave the bugs for the poor C programmers who wrote your interpreters and/or compilers to tussle with. Seriously: they like to.

`json-declarative-tools` is immensely easier to use than, say, `json-whateverdude-tools` could be. All of the affordances in this toolkit will be declarative. Pure functional or whatever. (This, btw, comes from XSLT, which was a heavily disguised dialect of Lisp.)

You're welcome.

