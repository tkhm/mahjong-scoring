#!/bin/bash

# @see Creating and invoking OpenWhisk actions https://console.ng.bluemix.net/docs/openwhisk/openwhisk_actions.html#openwhisk_actions
CMD="wsk action update"

args=($@)

for ((i=0; i < $#; ++i ))
do
  file_path=${args[${i}]}

  # remove file dir path
  file_name=${file_path##*/}

  # remove file extension
  action_name=${file_name%.*}

  # deploy to openwhisk on Bluemix
  $CMD $action_name $file_path
done

