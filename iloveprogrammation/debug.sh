#!/bin/bash
path=$(dirname "$0")
path+='/bop.py'
gnome-terminal -- bash -c "python3 $path;$SHELL"
