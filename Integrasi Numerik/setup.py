import os
os.system('color a')
print(" ====================================================================================== \n",
     "================================PROGRAM METODE NUMERIK================================ \n",
     "===================================INTEGRASI NUMERIK================================== \n",)
setting = int(input("Apakah library untuk program ini sudah anda install? 1: Ya (Butuh koneksi internet), 2: Tidak>>"))
if setting == 1:
    os.system('python -m pip install --upgrade pip')
    os.system('pip install numpy')
    os.system('pip install matplotlib')
    os.system('pip install ipython')
    os.system('pip install scipy')
    os.system('pip install sympy')
    os.system('pip install sys')
else:
    print("Baik kita lanjutkan!") 
os.system('python code/integrasinumerik.py')
k=input("Tekan ENTER untuk exit") 