import numpy as np
import sys
from scipy.linalg import solve
import matplotlib.pyplot as plt
from math import cos, exp, pi
from scipy.integrate import quad
from scipy.linalg import solve
import matplotlib.pyplot as plt
from math import cos, exp, pi
import sympy as sy
def trapesium1pias():
    print("Metode ini untuk persamaan polinomial orde 3, sehingga jika ingin mengubah menjadi orde lainya, silahkan edit pada bagian code")
    print("Default persamaan adalah: ax^3 + bx^2 + cx + d")
    a = float(input("Masukan nilai untuk a: "))
    b = float(input("Masukan nilai untuk b: "))
    c = float(input("Masukan nilai untuk c: "))
    d = float(input("Masukan nilai untuk d: "))
    X1 = int(input("Masukan nilai untuk X1 (Batas bawah): "))
    X2 = int(input("Masukan nilai untuk X2 (Batas atas): "))
    print(f"""Persamaan yang akan di proses adalah: ({a}x^3) + ({b}x^2) + ({c}x) + {d}""") 
    judul = str(input("Masukan nama file yang akan di save: "))
    print("========== Proses ==========")
    curve = np.array([a,b,c,d])
    xax = np.linspace(X1-5,X2+5,100)
    yax = [np.polyval(curve, i) for i in xax]    
    n = (X2-X1)/2
    fx1 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
    fx2 = (a*(X2)**3)+(b*(X2)**2)+(c*X2)+d
    z = n*(fx2+fx1)
    x = sy.Symbol("x")
    yy = ((a*(x)**3)+(b*(x)**2)+(c*x)+d)
    integrasi = sy.integrate(yy, (x, X1, X2))
    xx = np.array(range(X1-1,X2+1)) 
    y = ((a*(xx)**3)+(b*(xx)**2)+(c*xx)+d)
    error = ((integrasi-z)/integrasi)*100
    sby = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
    label = (f"""Daerah Arsir \nToleransi Error: {error}%""")
    save = (f"""image\{judul}.png""")
    plt.plot(xax,yax, color="red", label=sby)
    plt.fill_between([X1,X2], [fx1,fx2], label=label)
    plt.title('Grafik Metode Trapesium Satu Pias')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.axhline(color="black", label="Garis Nol")
    plt.legend()
    plt.savefig(save)
    print("=== Gambar grafik sudah di Save ===")
    print("Luas dengan metode trapesium 1 pias:", z)
    print("Luas dengan metode trapesium 1 pias eksak:", integrasi)
def tra_banyak_pias():        
    print("Metode ini untuk persamaan polinomial orde 3, sehingga jika ingin mengubah menjadi orde lainya, silahkan edit pada bagian code")
    print("Default persamaan adalah: ax^3 + bx^2 + cx + d")
    a = float(input("Masukan nilai untuk a: "))
    b = float(input("Masukan nilai untuk b: "))
    c = float(input("Masukan nilai untuk c: "))
    d = float(input("Masukan nilai untuk d: "))
    X1 = int(input("Masukan nilai untuk X1 (Nilai penguji pertama): "))
    X2 = int(input("Masukan nilai untuk X2 (Nilai penguji kedua): "))
    delta = int(input("Masukan nilai n (Jumlah pias): "))
    print(f"""Persamaan yang akan di proses adalah: ({a}x^3) + ({b}x^2) + ({c}x) + {d}""") 
    judul = str(input("Masukan nama file yang akan di save: "))
    print("========== Proses ==========") 
    curve = np.array([a,b,c,d])
    xax = np.linspace(X1-5,X2+5,100)
    yax = [np.polyval(curve, i) for i in xax]
    n = (X2-X1)/delta
    n = int(n)
    Z = 0
    integrasi = 0
    fx11 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
    fx22 = (a*(X2)**3)+(b*(X2)**2)+(c*X2)+d
    for i in range(X1,X2,n):
        fx1 = (a*(X1)**3)+(b*(X1)**2)+(c*X1)+d
        Xn = X1+n
        fx2 = (a*(Xn)**3)+(b*(Xn)**2)+(c*Xn)+d
        sym = sy.Symbol("x")
        y = ((a*(sym)**3)+(b*(sym)**2)+(c*sym)+d)
        integrasi = integrasi + (sy.integrate(y, (sym, X1, Xn)))
        x = np.array(range(delta+1)) 
        y = ((a*(x)**3)+(b*(x)**2)+(c*x)+d)
        FXi = 0
        for j in range(X1+1, X2-1, 1):
            FXi = (a*(j)**3)+(b*(j)**2)+(c*j)+d
        Z = Z + (n/delta)*(fx11+fx22+(2*FXi))
        error = ((integrasi-Z)/Z)*100
        plt.plot(xax,yax, color="red")
        plt.fill_between([X1,Xn], [fx1,fx2])
        plt.xlabel('Sumbu X')
        plt.ylabel('Sumbu Y')
        plt.axhline(color="black")
        if (Xn == delta and (error <= -10 or error >= 10)):
            sby2 = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
            label2 = (f"""Daerah Arsir \nToleransi Error: {error}""")
            save2 = (f"""image\{judul}.png""")
            title2 = (f"""Grafik Metode Trapesium Banyak Pias""")
            plt.plot(xax,yax, color="red", label=sby2)
            plt.fill_between([X1,Xn], [fx1,fx2], label=label2)
            plt.title(title2)
            plt.xlabel('Sumbu X')
            plt.ylabel('Sumbu Y')
            plt.axhline(color="black", label="Garis Nol")
            plt.legend()
            plt.savefig(save2)
        if (error >= -10 and error <= 10):
            sby = (f"""$Y = ({a}x^3) + ({b}x^2) + ({c}x) + ({d})$""")
            label = (f"""Daerah Arsir \nToleransi Error: {error}""")
            save = (f"""image\{judul}_BEST_MODEL.png""")
            plt.plot(xax,yax, color="red", label=sby)
            plt.fill_between([X1,Xn], [fx1,fx2], label=label)
            plt.title('Grafik Metode Trapesium Banyak Pias (Best Model)')
            plt.xlabel('Sumbu X')
            plt.ylabel('Sumbu Y')
            plt.axhline(color="black", label="Garis Nol")
            plt.legend()
            plt.savefig(save)
        if (Xn == X1+n):
            X1=X1+n
    print("=== Gambar grafik sudah di Save ===")
    print("Nilai error yang didapat: ", error)
    print("Luas dengan metode trapesium banyak pias:", Z)
    print("Luas dengan metode trapesium banyak pias eksak:", integrasi)
print("Kode penggunaan program integrasi numerik: \n",
    "1. Metode Trapesium Satu Pias \n",
    "2. Metode Trapesium Banyak Pias \n")
setting = int(input("Masukkan kode penggunaan program integrasi numerik: "))
if (setting == 1):
    X = trapesium1pias()
elif(setting == 2):
    X = tra_banyak_pias()
elif(setting == 3):
    X = gaussseidel()
else:
    X = jacobi()