import getpass
import subprocess

USERNAME = input("Nhập tài khoản: ")
PASSWORD = getpass.getpass("Nhập mật khẩu: ")

p1 = subprocess.Popen(["python", "createAns.py", USERNAME])
p1.wait()
if p1.returncode != 0:
    print("Tạo đáp án lỗi!!")
else:
    p2 = subprocess.Popen(["python", "submit.py", USERNAME, PASSWORD])
    p2.wait()
    if p2.returncode != 0:
        print("Submit lỗi!!")
