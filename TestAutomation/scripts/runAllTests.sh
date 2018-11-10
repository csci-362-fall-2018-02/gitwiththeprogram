# import sys
# sys.path.insert(0, 'testCasesExecutables')
# import os
# import glob
#
#
# numberOfFiles = len(glob.glob1('testCases', '*.txt'))+1
# for i in range(1, numberOfFiles):
#     currentTestCase = 'testCases/testCase' + str(i)
#     testCase = open((currentTestCase + '.py'), 'r')

#!/bin/sh
cd ..
cd testCasesExecutables
DIR=$(dirname $0)

#list()

echo "Listing directory contents of: "$DIR""
for entry in $DIR/*;
do
  echo "<P>"
  echo $entry
  echo "</P>"
done

# cat <<- EOF
#  <html>
#     <head>
#         <title>
#         Directory Listing
#         </title>
#     </head>
#     <body>
#     $(list)
#     </body>
#     </html>
# EOF
