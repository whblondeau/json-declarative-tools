#!/usr/bin/python3

# This is the jsn_path object.

def match_tupl(pattern, path):
    '''both arguments are tuples'''
    if len(path) < len(pattern):
        # when the pattern has more steps than 
        # the path, no way it works.
        return False
    subpath = path[:len(pattern)]

    return (subpath == pattern)

# --------------------------------------- FUNCTIONS

def match_tupl(pattern, path):
    '''both arguments are tuples'''
    if len(path) < len(pattern):
        # when the pattern has more steps than 
        # the path, no way it works.
        return False
    subpath = path[:len(pattern)]

    return (subpath == pattern)


def enumerate_leafpaths(current_node, current_pathstring='', current_steplist=[]):
    '''This function accepts a parsed JSON object and 
    returns a generator that, when iterated, provides 
    3-tuples of all leaf paths in the instance. 
    The 3-tuple is of the form (pathstring, steplist, leafnode).
    Note that pathstring and steplist are logically equivalent. This method
    provides both because they afford different conveniences for
    the various JSNPath evaluation techniques that will operate on these
    leafpaths.'''

    # children to iterate through?
    if isinstance(current_node, list):
        if not current_node:
            # empty list. This is a leaf. Give it up.
            yield (current_node, current_pathstring, current_steplist)
        else:
            for indx, val in enumerate(current_node):
                childpath = current_pathstring + '[' + str(indx) + ']'
                # make a separate copy!
                childsteplist = copy.copy(current_steplist)
                childsteplist.append(str(indx))
                result = enumerate_leafpaths(val, childpath, childsteplist)
                for item in result:
                    # result best be nested iterators of tuples!
                    yield item

    elif isinstance(current_node, dict):
        if not current_node:
            # empty dict. This too is a leaf. Give it up.
            yield (current_node, current_pathstring, current_steplist)
        else:
            for attrname in current_node:
                val = current_node[attrname]
                childpath = current_pathstring + '[' + attrname + ']'
                # make a separate copy!
                childsteplist = copy.copy(current_steplist)
                childsteplist.append(attrname)
                result = enumerate_leafpaths(val, childpath, childsteplist)
                for item in result:
                    # result best be nested iterators of tuples!
                    yield item
    else:
        leafpath = (current_node, current_pathstring, current_steplist)
        yield leafpath


def build_analysis_dicts(jsonobj):
    '''accepts a compiled json object and 
    returns two logically equivalent dictionaries:
    one with string keys in JSNPath format, and
    one with tuple(string) keys representing the 
    same path information. Values are the leaf
    node values.
    The return value is a tuple: (path dict, tuple dict).
    '''

    # get a generator of 3-tuple path info
    leafpaths = enumerate_leafpaths(jsonobj)

    pathdict = {}
    tupldict = {}
    for noderep in leafpaths:

        pathstring = noderep[1]
        pathdict[pathstring] = noderep[0]

        stepstuple = ()
        if noderep[2]:
            stepstuple = tuple(noderep[2])
        tupldict[stepstuple] = noderep[0]

    return pathdict, tupldict




# INTERNAL
# def recurse_json(id, value, path):
#     '''JSON nodes can be container types (`dict`, `list`) or value types
#     (`string`, `boolean`, `number` the various undefined types.)'''
#     if isinstance(value, list):
#         return [recurse_json(child) for child in 


# def capitalize(x):
#    if isinstance(x, list):
#      return [capitalize(v) for v in x]
#    elif isinstance(x, dict):
#      return {k[0].upper() + k[1:]: capitalize(v) for k, v in x.items()}
#    else:
# return x

# def enumerate(self, path=None):
#     """Iterate through the PelicanJson object yielding 1) the full path to
#     each value and 2) the value itself at that path.
#     """
#     if path is None:
#         path = []
#     for k, v in self.store.items():
#         current_path = path[:]
#         current_path.append(k)

#         if isinstance(v, PelicanJson):
#             yield from v.enumerate(path=current_path)
#         elif isinstance(v, list):
#             for idx, list_item in enumerate(v):
#                 list_path = current_path[:]
#                 list_path.append(idx)
#                 if isinstance(list_item, PelicanJson):
#                     yield from list_item.enumerate(path=list_path)
#                 else:
#                     yield list_path, list_item
#         else:
#             yield current_path, v

# --------------------------------------- CONSTANTS

# --------------------------------------- EXECUTE


