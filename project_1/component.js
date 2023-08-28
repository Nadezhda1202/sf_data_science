import React from 'react';
import RegularGraph from '@bit/eden-gal-code.home_task.regular-graph';
 const Data = [
    { X: "jan", john: 90, doe: 92, jin: 74 },
    { X: "feb", john: 100, doe: 76, jin: 32 },
    { X: "mar", john: 72, doe: 88, jin: 56 },
  ];
  const keys = ["john", "doe", "jin"];
export default (
	<div style={{width:300}}>
	<RegularGraph label="Grades" data={Data} keys={keys}/>
	</div>
)