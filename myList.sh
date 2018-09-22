#!/bin/bash

cat <<- _EOF_
<HTML>
	<HEAD>
		<TITLE>Directory Listing</TITLE>
	</HEAD>
	<BODY>
		for d in /*; do
			<P>echo $d;</P>
		done
	</BODY>
</HTML>"

_EOF_
