#!/bin/bash


function cancel()
{
    sub=`ps -ef|grep "serve_daemon.sh"|grep -v grep|awk '{print $2}'`
    if [[ "x$sub" != "x" ]]; then
        `ps -ef|grep "serve_daemon.sh"|grep -v grep|awk '{print $2}'|xargs kill -9`
    fi
    rm -rf serve.tmp
    exit 0
}

trap cancel SIGINT SIGTERM SIGQUIT


echo "" > serve.tmp
./serve_daemon.sh &
gitbook serve | tee serve.tmp

