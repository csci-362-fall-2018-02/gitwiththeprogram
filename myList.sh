#!/bin/bash

echo "<HTML>
	<HEAD>
		<TITLE>Directory Listing</TITLE>
	</HEAD>
	<BODY>"
		for d in ./*; do
			echo "<P>"; echo $d; echo "</P>"
		done
echo	"</BODY>
</HTML>"
