#! /bin/sh

testSizeMaxMap()
{
  file_size_kb=`du -k "index.html" | cut -f1`
  assertTrue "[ $file_size_kb -lt 1800 ]"
}

. shunit2-2.1.6/src/shunit2
