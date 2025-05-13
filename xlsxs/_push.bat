cd ../
set /p commit=请输入提交信息：
python python/push.py %commit%
pause