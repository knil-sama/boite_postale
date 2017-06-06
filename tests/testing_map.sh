#! /bin/sh

testSizeMaxMap()
{
  file_size_kb=`du -k "build/index.html" | cut -f1`
  assertTrue "[ $file_size_kb -lt 2800 ]"
}

. shunit2-2.1.6/src/shunit2
