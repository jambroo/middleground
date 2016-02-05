#!/bin/bash
docker stop -t 0 $(docker ps | grep middleground | cut -c1-12)
