#!/bin/bash

rm -rf out/ && python3 ./main.py && npm run build && npm run minify
