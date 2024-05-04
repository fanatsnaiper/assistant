@ECHO OFF
set count=0
echo Fatal Error.
set /p input= Check files?(y/n) 
set list="design" "memory" "modules"
IF %input%==y ( 
   :: обработка ответа yes
   for %%a in (%list%) do ( 
   IF EXIST %%a (
   ECHO folder %%a exists) ELSE (
   ECHO folder %%a does not exist
))
   pause
) ELSE IF %input%==n (
   :: обработка ответа no
   echo It's up too you
   pause
) ELSE (
   :: обработка неверной команды
    echo Wrong command
    pause
)