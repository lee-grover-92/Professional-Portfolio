@echo off
REM Step 1: Enable local_infile globally
echo Enabling local_infile...
mysql -u root -p -e "SET GLOBAL local_infile = 1;"

REM Step 2: Launch MySQL client with local_infile enabled
echo Launching MySQL client with --local-infile=1...
start "" "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --local-infile=1 -u root -p

REM Step 3: Restart MySQL service
echo Restarting MySQL service...
net stop MySQL80
net start MySQL80

echo All done. MySQL restarted and local_infile is enabled.
pause