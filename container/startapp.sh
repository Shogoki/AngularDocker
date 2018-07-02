#!/bin/bash
if [ -d "/app" ]; then
	mkdir /app
fi
cd /app
if [ ! -d "/app/$APPNAME" ]; then
     ng new $APPNAME   
fi
cd $APPNAME
ng serve --host 0.0.0.0

