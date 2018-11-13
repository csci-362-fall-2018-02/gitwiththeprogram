#!/bin/sh
# This bash script runs all the tests in the testCasesExecutables folder, and
# then outputs to a file in the formal of testResults(counter).txt

COUNTER='1'
REPORTSFILE='./reports/testResults'$COUNTER'.txt'
COMPAREFILE='./reports/test'$COUNTER'-correct.txt'
echo "here"
while [ -f $REPORTSFILE ]
do
   COUNTER=$((COUNTER+1))
   REPORTSFILE='./reports/testResults'$COUNTER'.txt'
   COMPAREFILE='./reports/test'$COUNTER'-correct.txt'
   TEMPFILE='./temp/tempfile'$COUNTER'.txt'
done

cd testCasesExecutables
echo -n "Running all tests in folder: "
pwd
echo "Outputting report to:" $REPORTSFILE

for entry in *;
do
  echo
  echo -n $entry
  TEMPFILE='./temp/tempfile'$entry
  python ./../scripts/testInterpreter.py $entry > ./../$TEMPFILE
  if diff ./../$TEMPFILE ./../$COMPAREFILE >/dev/null 2>&1
  then
     echo " passed"
     echo -n $entry >> ./../$REPORTSFILE
     echo " passed" >> ./../$REPORTSFILE
  else
     echo " failed"
     echo -n $entry >> ./../$REPORTSFILE
     echo " failed" >> ./../$REPORTSFILE
  fi
done
cd ..

#echo "cleaning temp"
#cd ./temp/
#rm ./*
