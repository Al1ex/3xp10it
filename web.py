from exp10it import configIniPath
with open(configIniPath, 'r+') as f:
    content = f.read()
#下面用于设置web后台口令及将web后台相关表[session机制,登录数据等属于django功能中要建立的表]存储到数据库
if re.search(r"finish_web_setting", content):
    pass
else:
    os.system("cd pannel")
    os.system("python3 manage.py migrate")
    os.system("python3 manage.py createsupperuser")
    update_config_file_key_value(configIniPath, 'default', 'finish_web_setting', 1)

os.system("python3 manage.py runserver 0.0.0.0:8000")

