#!/usr/bin/env bash
nohup java -Xms128m -Xmx512m -XX:+HeapDumpOnOutOfMemoryError -jar ai-monitor-service-0.0.1-SNAPSHOT.jar &
