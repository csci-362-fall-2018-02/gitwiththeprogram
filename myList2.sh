#!/bin/bash

list()
{
  echo "Current File Path: "${PWD}
  for entry in ./*; 
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
