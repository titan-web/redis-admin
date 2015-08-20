TARGET=/usr/local/bin/beanstalkd
HOST=10.9.19.90
PORT=11300
START=nohup $TARGET -l $HOST -p $PORT & >/dev/null
DATE=/bin/date
NOTICE=/tmp/beanstalkd-watchdog.txt

BEANSTALKD_PID=`pidof $TARGET`

check_beanstalkd() {
    if [ $BEANSTALKD_PID ];then
        $START
        echo "$TARGET was not running and was started on `$DATE`" >> $NOTICE
    fi
}

check_beanstalkd

exit
