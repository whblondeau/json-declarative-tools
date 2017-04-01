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

def step_empty(stepcontent):
    return step == ''



def match_tupl(pattern, path):
    '''both arguments are tuples'''
    if len(path) < len(pattern):
        # when the pattern has more steps than 
        # the path, no way it works.
        return False
    subpath = path[:len(pattern)]

    return (subpath == pattern)


def enumerate_leafpaths(current_node, current_pathstring='', current_steplist=[]):
    '''INTERNAL: This function accepts a parsed JSON object and 
    returns a generator that, when iterated, provides 
    3-tuples of all leaf paths in the instance. 
    The 3-tuple is of the form (pathstring, steplist, leafnode).
    Note that pathstring and steplist are logically equivalent. This method
    provides both because they afford different conveniences for
    the various JSNPath evaluation techniques that will operate on these
    leafpaths.
    Note that this is '''

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




# --------------------------------------- CONSTANTS

# BUILDING BLOCKS: regexes or regex fragments that are useful
# in their own right but mostly serve to populate `jsnpath_regexes`

wildcard_index_pattern = '(' + '\[\]' + ')'

num_pattern = '-?[0-9]+'

single_index_pattern = '(' + num_pattern + ')'

slice_startwith_pattern = '((' + num_pattern + ')[:])'
slice_stopbefore_pattern = '([:](' + num_pattern + '))'
slice_startwith_stopbefore_pattern = '((' + num_pattern + ')[:](' + num_pattern + '))'

slice_pattern =  slice_startwith_pattern
slice_pattern += '|'
slice_pattern += slice_stopbefore_pattern
slice_pattern += '|'
slice_pattern += slice_startwith_stopbefore_pattern

index_pattern =  wildcard_index_pattern
index_pattern += '|'
index_pattern += '(' + '\[(' + single_index_pattern
index_pattern += '|'
index_pattern += slice_pattern + ')\]' + ')'

# more API-oriented exposure of specific regexes
jsnpath_regex = {
    'name_literal_content': '([A-Za-z0-9]{1,2})|([A-Za-z0-9][A-Za-z0-9_]*[A-Za-z0-9])',

    'name_globbed_content': '([A-Za-z0-9*+]{1,2})|([A-Za-z0-9][A-Za-z0-9*+_]*[A-Za-z0-9*+])',

    'index_literal_content':            single_index_pattern,
    'index_slicing_content':            slice_pattern,
    'name_wildcard_content':            '(("*")|(\'*\'))',
    'identifier_step_wildcard':         '*',
    'identifier_multistep_wildcard':    '**',

}

# The distinguished names for types of step in
# a JSNPath expression
step_types = {
    'name_literal':
    {
        'description':  '''The step has quoted content, and contains
                            nothing but alphanumeric characters
                            (upper or lower case) and non-leading,
                            non-trailing underscore `_` characters.
                            Repeated `_` characters are prohibited.''',

        'content_regex':    '(("' + jsnpath_regex['name_literal_content'] + '")'
                            + '|'
                            + "('" + jsnpath_regex['name_literal_content'] + "'))",

        'examples':     {
                            'good': (
                                'a', 'ab_cd', 'A12knf', '3', 'altitude_max', '4567', 'AbleBaker',
                            ),
                            'bad': {
                                'a__b'      : 'two consecutive `_` characters prohibited',
                                '_svg_Elem' : 'leading `_` forbidden',
                                'a_'        : 'trailing `_` forbidden',
                                'abc*12rtf' : '`*` (glob wildcard) invalid in literal',
                                '45:67'     : '`:` (slice operator for indexes) not valid in name',
                            }
                        }
    },

    'name_globbed':
    {
        'description':  '''The node name is expressed with at least one `*`
                            glob symbol, which is a subsitition notiation
                            for 0-n characters.''',

        'content_regex':    '(("' + jsnpath_regex['name_globbed_content'] + '")'
                            + '|'
                            + "('" + jsnpath_regex['name_globbed_content'] + "'))",

        'examples':     {
                            'good': (
                                'a*', '*a', '*a*', 'ab*_cd', 'A12k*nf', '3*', 
                                'alt*_max', '4*567', 'Able*Baker',
                                'abc*12rtf', '*_*'

                            ),
                            'bad': {
                                'abc_678'    : 'not a valid glob because no `*` present',
                                'sh**art'    : 'two consecutive `*` characters prohibited',
                                '_svg_Elem*' : 'leading `_` forbidden',
                                'a*_'        : 'trailing `_` forbidden',
                                '45:67*'     : '`:` (slice operator for indexes) not valid in name',
                            }
                        }
    },

    'name_wildcard':
    {
        'description':  '''A quoted single glob character `*` that is
                            a match for ANY name, and therefore a
                            selector for ALL children of the context
                            JSON parent object.''',

        'regex'

        'examples':     {
                            'good': (
                                '"*"', "'*'",
                            ),
                            'bad': {
                                '*'     : 'UNQUOTED `*` is a DIFFERENT KIND OF WILDCARD',
                                '**'    : 'UNQUOTED `**` is a DIFFERENT KIND OF WILDCARD',
                                '"**"'  : 'Not valid as anything at all',
                            }
                        }
    },

    'index_literal':
    {
        'description':  '''The step has UNQUOTED content, and contains
                            nothing but numbers with optional leading 
                            minus sign `-`.
                            Note that negative indexing is done from the
                            end of the array, and is 1-based counting: 
                            `array[-1]` is the last item in the array.
                            
                            Example of positive and negative indexing:
                            `['a', 'b', 'c', 'd', 'e', 'f', 'g']
                               0    1    2    3    4    5    6
                              -7   -6   -5   -4   -3   -2   -1
                            ''',

        'content-regex':    jsnpath_regex['index_literal_content'],

        'examples':     {
                            'good': (
                                '0', '1450', '-3',
                            ),
                            'bad': {
                                '-0':   'semantically meaningless',
                                '3.5':  ''
                            }
                        }
    },

    'index_slice': 
    {
        'description':  '''The step has UNQUOTED content, containing exactly
                            one slice operator `:`. The slice operator is
                            either preceded by a "startswith" number, followed
                            by an "endsbefore" number, or both. The numbers
                            may be positive or negative; a zero in the slice
                            is without meaning but will not be considered an
                            error.
                            (Note that an attempt to apply slicing numbers that
                            do not exist in the array of context will either
                            terminate with an array out of bounds error, OR
                            will fail silenly, depending on the `strict`
                            parameter: `strict == True` will cause the error,
                            and `strict == False` will cause the silent fail.)''',

    },

    'index_wildcard':
    {  
        'description':  '''The step represents ANY index (numeric) literal, and is
                            therefore a selector for ALL children of the 
                            parent array. The step is an empty pair of
                            brackets, `[]`, and the content is therefore
                            the empty string. (Note that the content_regex
                            does not work when using multiline mode; but
                            this is a degenerate case anyway. Step content
                            can be tested against the empty string in many
                            efficient ways wihout recourse to regex!''',

        'content_regex':    '^$',

        'content_eval': step_empty,
    },

    'index':
    {

    }

}




# This dictionary maps non-literal steps in a JSNPath
# expression to the corresponding
# stepwise matching logic.
# Each key is a generic step type
match_dict = {
    
}

# --------------------------------------- EXECUTE

print('NO GROSS SYNTAX ERROS.')