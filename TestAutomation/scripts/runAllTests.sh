#!/bin/sh
# This bash script runs all the tests in the testCasesExecutables folder, and
# then outputs to a file in the formal of testResults(counter).txt

COUNTER='1'
REPORTSFILE=$(realpath './reports/testResults'$COUNTER'.txt')
COMPAREFILE=$(realpath './reports/test'$COUNTER'-correct.txt')
TEMPFOLDER=$(realpath temp)
while [ -f $REPORTSFILE ]
do
   COUNTER=$((COUNTER+1))
   REPORTSFILE=$(realpath './reports/testResults'$COUNTER'.txt')
   COMPAREFILE=$(realpath './reports/test'$COUNTER'-correct.txt')
done

cd testCasesExecutables
echo -n "Running all tests in folder: "
pwd
echo "Outputting report to:" $REPORTSFILE

echo $TEMPFOLDER

#iterate through entries
for entry in *;
do
  echo
  echo -n 'Running test with commands stored in file: '
  echo $entry

  TEMPFILE=$TEMPFOLDER'/tempfile'$entry
  echo -n "outputting to tempfile located at "
  echo $TEMPFILE
  python ./../scripts/testInterpreter.py $entry $TEMPFILE
  
  #compares files, routes actual diff output to be deleted, just tests if they're equal
  if diff $TEMPFILE $COMPAREFILE >/dev/null 2>&1
  then
     echo " passed"
     echo -n $entry >> $REPORTSFILE
     echo " passed" >> $REPORTSFILE
  else
     echo " failed"
     echo -n $entry >> $REPORTSFILE
     echo " failed" >> $REPORTSFILE
  fi
  echo
done
cd ..

echo "cleaning temp..."
cd $TEMPFOLDER
rm ./*
