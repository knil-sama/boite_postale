#! /bin/sh

testSizeMaxMap()
{
  file_size_kb=`du -k "index.html" | cut -f1`
  assertTrue "[ $file_size_kb -gt 1800 ]"
}
