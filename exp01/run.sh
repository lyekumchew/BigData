#!/bin/bash

STREAM_JAR_PATH="/home/hduser/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar"

if [ $# != 1 ]; then
  echo "USAGE: bash $0 DATA_NAME"
  echo "e.g.: bash $0 small.txt"
  exit 1
fi

file_name=${1%.*}

INPUT_FILE_PATH="/exp01/${1}"
OUTPUT_PATH="/exp01/${file_name}_result"
OUTPUT_PATH_2="/exp01/${file_name}_result_2"
OUTPUT_PATH_3="/exp01/${file_name}_result_3"

hadoop dfs -rmr "$OUTPUT_PATH"

hadoop jar $STREAM_JAR_PATH \
  -input "$INPUT_FILE_PATH" \
  -output "$OUTPUT_PATH" \
  -mapper "python3 map.py" \
  -reducer "python3 reduce.py" \
  -file ./map.py \
  -file ./reduce.py

hadoop dfs -rmr "$OUTPUT_PATH_2"

hadoop jar $STREAM_JAR_PATH \
  -input "$OUTPUT_PATH" \
  -output "$OUTPUT_PATH_2" \
  -mapper "python3 map_2.py" \
  -reducer "python3 reduce_2.py" \
  -file ./map_2.py \
  -file ./reduce_2.py

hadoop dfs -rmr "$OUTPUT_PATH_3"

hadoop jar $STREAM_JAR_PATH \
  -input "$OUTPUT_PATH" \
  -output "$OUTPUT_PATH_3" \
  -mapper "python3 map_3.py" \
  -reducer "python3 reduce_3.py" \
  -file ./map_3.py \
  -file ./reduce_3.py
