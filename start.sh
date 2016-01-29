#!/bin/bash
docker build -t middleground . && docker run -p 9998:9998 middleground
