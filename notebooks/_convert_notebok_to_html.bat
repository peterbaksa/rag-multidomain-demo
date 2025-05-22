@echo off
title Convert Notebook to HTML

REM Initialize conda
call "%USERPROFILE%\anaconda3\Scripts\activate.bat" >nul 2>&1
REM Activate conda
call conda activate rag-multidomain-env
REM Convert
jupyter nbconvert --to html rag_demo.ipynb