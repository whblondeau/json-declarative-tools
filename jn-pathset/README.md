## JNPathset

JNPathset defines data structures and functions that operate on sets of leaf JNPaths.

The use of "set" in the name is deliberate and meaningful. If a JSON object is resolved into leafpaths, no two paths can be identical. When working to put disparate paths -- constructed, derived from multiple JSON objects, or whatever -- into a single resulting JSON object, the result must be deterministic and unsurprising. The use of mathematical sets is the core concept in this.

### Basic pathset resolution logic

Given an arbitrary set of leafpaths, resolution to a set is performed as follows:

    1. Add the paths to a set. Duplicates will be eliminated.

    2. Step names or indexes are resolved by a breadth logic: 

        `for index in longest path:
            step = set of all paths[index]

    2. If the first steps in all of the paths are named, they will be considered to be children of an anonymous `{}` root node.

    3. If the first steps in all of the paths are indexed, they will be considered to be children of an anonymous `[]` root node. They will be reindexed as necessary