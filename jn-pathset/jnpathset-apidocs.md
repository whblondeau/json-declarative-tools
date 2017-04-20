## The JNPathset API

### Core

----
`set(step) breadth_steps( level, pathset )`

  `level` is either an integer or a slicing expression. This function returns
  all steps in the pathset that 

----
`set(noderep) select_nodes( selectorpath, jsonobject )`

  This function returns all leafpaths in `jsonobject` for which `selects( selectorpath, leafpath )` == `true`.
