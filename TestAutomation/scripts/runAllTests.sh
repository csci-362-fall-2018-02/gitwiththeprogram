#!/bin/sh
# cd ..
# cd testCasesExecutables
DIR=$(dirname $0)
echo $DIR
cd testCasesExecutables
#DIR='.'
python testInterpreter.py test1-correct.txt >> testResults.txt
#/testCases/test1.txt


# echo "Running all tests in folder: "$DIR""
#
# for entry in $DIR/*;
# do
#   echo
#   echo $entry
#   python testInterpreter.py $entry >> testResults.txt
# done
