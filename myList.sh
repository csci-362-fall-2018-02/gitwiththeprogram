#!/bin/bash

DIR=$(dirname $0)

list()
{
  echo "Listing directory contents of: "$DIR""
  for entry in $DIR/*; 
  do
    echo "<P>"
      echo $entry
      echo "</P>"
  done
}

cat <<- EOF
 <html>
    <head>
        <title>
        Directory Listing
        </title>
    </head>
    <body>
    $(list)
    </body>
    </html>
EOF
