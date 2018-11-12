#!/bin/sh
# cd ..
# cd testCasesExecutables
# DIR=$(dirname $0)

cd testCasesExecutables
DIR='.'

echo "Running all tests in folder: "$DIR""
for entry in $DIR/*;
do
  echo
  echo $entry
  python $entry >> testResults.txt
done
