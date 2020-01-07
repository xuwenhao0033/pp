import pytest
def test_login():
    print("正在登陆")

if __name__ == '__main__':
    # test_login()
    pytest.main("-s login.py")

# pytest运行方式
# --命令行(在控制台下方打开终端Terminal)
# - pytest -s setup.py
# --代码
# - pytest.main（"-s xxx.py"）