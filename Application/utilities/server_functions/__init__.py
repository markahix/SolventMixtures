from flask import Flask, flash, request, redirect, render_template, session
import os
import sys
import subprocess as S

parent = os.path.dirname
MAIN_DIR = parent(parent(__file__))
BIN_DIR = os.path.join(parent(MAIN_DIR),"bin/")
sys.path.append(BIN_DIR)
UPLOAD_FOLDER = MAIN_DIR+'/uploads/'
STATIC_DIR = MAIN_DIR+'/static/'
DATABASE_DIR = MAIN_DIR+'/database/'
TEMPLATES_DIR = MAIN_DIR+'/templates/'
LOGFILES_DIR = TEMPLATES_DIR+'logfiles/'
os.makedirs(DATABASE_DIR,exist_ok=True)
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
os.makedirs(LOGFILES_DIR,exist_ok=True)