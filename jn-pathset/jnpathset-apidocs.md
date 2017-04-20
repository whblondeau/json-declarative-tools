## The JNPathset API

### Core

----
`map{jnpath:step[]} select_steps( level, jnpathset )`

  `level` is either an integer or a slicing expression. This function returns a map whose keys are jnpaths and whose values are the steps identified by `level`. A jnpath that contains no matching steps will still be included in the return map, with `null` as its value.

  This never throws index out of bounds exceptions.

----
`set(noderep) select_nodes( selectorpath, jsonobject )`

  This function returns all leafpaths in `jsonobject` for which `selects( selectorpath, leafpath )` == `true`.
