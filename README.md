# Pengenalan-Bahasa-Pemograman-Python-01
Pengenalan Bahasa Pemograman Python bagian 1

# 1 Variabel dan Operasi

## 1.1 Variabel
Variabel adalah suatu nilai yang kita simpan di memori dan bisa kita panggil saat akan digunakan. Contoh kasus variabel adalah seperti saat kita menyimpan memori di otak kita bahwa nilai $\pi$ (variabel) adalah 3,14. Saat mengingat atau memanggil $\pi$ di memori otak kita maka akan muncul angka 3,14. Cara kerja komputer juga demikian sehingga Python sebagai salah satu bahasa pemrograman juga bertindak seperti itu. Dalam implementasinya cara 'menyimpan ingatan' ini dilakukan dengan cara yang mudah:
```Python
pi=3.14
```
Variabel dalam Python sendiri dibedakan menjadi beberapa jenis seperti:

-   `Integer`: bilangan bulat
-   `Float`: *floating point*, bilangan dengan desimal
-   `String`: teks
-   `Complex numbers`: bilangan kompleks
-   `Boolean`: benar (`True`) atau salah (`False`)

Python akan menginterpretasikan jenis variabel dari **cara kita
menulis** variabel tersebut:
``` {.python}
angka=1 #integer
Angka=1.0 #float
ANGKA="1" #string
ANGKA2='1' #string
bil_kompleks=5-1j #complex
bools=True #boolean True atau False
```
``` {.python}
angka
```
1

Sama seperti ingatan manusia, jika suatu menyimpan ke memori dengan kata
kunci yang sama maka nilai sebelumnya akan dilupakan, contoh:
``` {.python}
angka=2
```
``` {.python}
angka
```
2

Saat kita panggil `angka` maka `2` yang akan muncul, bagaimana kalau
nilai `angka` kita ganti:

``` {.python}
angka=3
print(angka)
```
3

## 1.2 Operasi

Jika kita sudah bisa menyimpan suatu nilai ke dalam ingatan komputer dengan mendefinisikan suatu `variable`, selanjutnya kita akan mengoperasikan variabel-variabel tersebut. Beberapa operasi standar yang dapat kita lakukan adalah:

|Simbol Operasi|	Kegunaan	|
|----|-----|
|**+**	|penjumlahan |
|**-** | pengurangan |
|**\***|  perkalian|
| **/** | pembagian |
|  **%** | mengembalikan sisa pembagian (_modulo_).|
| **\*\*** |pangkat|
|**+=** | menambah dan mengganti |
| **-=** | mengurangkan dan mengganti |
| ==  | mengetes kesamaan |
| != | mengetes ketidaksamaan |

Contoh implementasi operasi-operasi di atas:

```Python
angka1=3
angka2=5
angka3=angka1+angka2
print(angka3)
```
8

``` Python
angka4=angka1-angka3
print(angka4)
```
-5

```Python
angka5=angka1**angka2
print(angka5)
```

243

``` {.python}
angka5 = 5
```

``` {.python}
angka5
```

5

``` {.python}
angka5 += 1
```

``` {.python}
angka5
```

 6

# Jenis variabel yang dioperasikan akan berpengaruh terhadap hasil operasinya, misalkan operasi perkalian antar `integer`:

``` {.python}
10*10
```

100

``` {.python}
type(10*10)
```

int

Hasil operasi di atas berupa `integer` karena variabel yang dikalikan
sama-sama

------------------------------------------------------------------------

`integer`. Jika salah satu atau kedua data merupakan `float` maka hasil
dari operasi akan berjenis `float`:

``` {.python}
10*10.0
```
100.0

``` {.python}
type(10*10.0)
```

float
Bagaimana dengan operasi `string`?
``` {.python}
"1"+"3"
```

``` {.json}
{"type":"string"}
```

``` {.python}
"13"-"3"
```
----> 1 "13"-"3"

TypeError: unsupported operand type(s) for -: 'str' and 'str'


Operasi penjumlahan pada `string` akan \'menumpuk\' string tersebut
sedangkan operasi pengurangan tidak bisa dijalankan. Operasi perkalian antar `string` juga akan menghasilkan error:

```Python
"1"*"3"
```
TypeError: can't multiply sequence by non-int of type 'str'

`string` bisa dikalikan dengan `integer`,  hasil perkalian ini berupa penumpukan string sebanyak angka yang dikalikan:
``` {.python}
"1"*10
```

``` {.json}
{"type":"string"}
```
operasi dengan `float` akan menghasilkan error:
```Python
"1"*3.
```
Error:----> 1 "1"*3.

```Python
"1"*int(3.)
```

```
string
```
Apa yang terjadi apabila kita merubah 3.4 menjadi integer int(3.4) \--\>
3 atau 4? int(3.6) \--\> 3 atau 4?

# 2 Struktur Data {#2-struktur-data}

Data dalam geofisika biasanya merupakan kumpulan nilai atau angka yang
erat kaitannya dengan pengukuran. Kita akan menggunakan studi kasus
pengukuran suhu suatu ruangan setiap 4 jam dalam satu hari, dengan kata
lain kita akan memiliki 6 angka hasil pengukuran. Bagaimana mewakili 6
angka tersebut dalam Python?

Python menyediakan beberapa jenis struktur data yang bisa digunakan
untuk menyimpan data kita yang masing-masing memiliki fungsinya sendiri.
Beberapa jenis struktur data yang umum di dalam Python adalah:

-   `List`
-   `Tuple`
-   `Dictionary`
-   `Sets`
:::

::: {.cell .markdown id="5dd9cfd1"}
## 2.1 List {#21-list}

`List` ditulis dalam Python dengan `[]` yang bisa diisi berbagai macam
variable yang sama ataupun berbeda dan masing-masing variabel tersebut
dipisahkan dengan tanda koma (`,`):

``` {.python}
suhu_24h=[34.0, 35.0, 34.3, 32.0, 31.1, 29.0]
print(suhu_24h)
```


``` {.python}
type(suhu_24h)
```


``` {.python}
suhu_x=[10, 35.0, "ini komponen list", 32.0, False, 29.0]
```

``` {.python}
print(suhu_x)
```

``` {.python}
suhu_24h*suhu_24h
```

TypeError: can't multiply sequence by non-int of type 'list'

dalam kasus pengukuran suhu ruangan tersebut kita mendapatkan 6 angka
pengukuran yang kemudian dituangkan dalam `list` di Python seperti di
atas. Setiap element `list` berasosiasi dengan `index` yang dimulai
dengan angka 0 pada element pertama dan seterusnya. Contoh apabila kita
ingin mengambil pengukuran ketiga maka `index`nya adalah 2:

``` {.python}
pengukuran_3=suhu_24h[2]
print(pengukuran_3)
```

34.3

Kita juga dapat memanggil dari belakang dengan `index` -1 untuk element
terakhir, -2 untuk element kedua dari akhir, dan seterusnya, seperti
contoh:

``` {.python}
pengukuran_terakhir=suhu_24h[-1]
print(pengukuran_terakhir)
```

29.0


``` {.python}
print(suhu_24h[2]==suhu_24h[-4])
```

True
Dengan `index` kita juga bisa mengambil lebih dari 1 elemen dengan
tambahan simbol `:`:


``` {.python}
pengukuran_1dan2=suhu_24h[0:2]
print(pengukuran_1dan2)
```

[34.0, 35.0]

Element dalam `list` dapat diganti/*mutable* seperti pada contoh dibawah
ini:

``` {.python}
print(suhu_24h[0])
```

34.0

``` {.python}
suhu_24h[0]=37.0
print(suhu_24h)
```

[37.0, 35.0, 34.3, 32.0, 31.1, 29.0]

`list` memiliki banyak sekali `method` yang digunakan untuk mengolah
`list` tersebut, opsi-opsi atau `method` tersebut dapat kita lihat
dengan mengetikkan `help`:

``` {.python}
help(suhu_24h)
```

Help on list object:

    class list(object)
     |  list(iterable=(), /)
     |  
     |  Built-in mutable sequence.
     |  
     |  If no argument is given, the constructor creates a new empty list.
     |  The argument must be an iterable if specified.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(self, /)
     |      Return a reverse iterator over the list.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Return the size of the list in memory, in bytes.
     |  
     |  append(self, object, /)
     |      Append object to the end of the list.
     |  
     |  clear(self, /)
     |      Remove all items from list.
     |  
     |  copy(self, /)
     |      Return a shallow copy of the list.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  extend(self, iterable, /)
     |      Extend list by appending elements from the iterable.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  insert(self, index, object, /)
     |      Insert object before index.
     |  
     |  pop(self, index=-1, /)
     |      Remove and return item at index (default last).
     |      
     |      Raises IndexError if list is empty or index is out of range.
     |  
     |  remove(self, value, /)
     |      Remove first occurrence of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  reverse(self, /)
     |      Reverse *IN PLACE*.
     |  
     |  sort(self, /, *, key=None, reverse=False)
     |      Stable sort *IN PLACE*.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None

``` {.python}
print(suhu_24h)
```

[37.0, 35.0, 34.3, 32.0, 31.1, 29.0]

``` {.python}
suhu_24h.count(35.0)
```


    1



``` {.python}
suhu_24h[5] = 35.0
print(suhu_24h)
```


[37.0, 35.0, 34.3, 32.0, 31.1, 35.0]

``` {.python}
suhu_24h.count(35.0)
```

2

Berdasarkan petunjuk di atas kita akan mencoba 1 `method` yaitu `pop`
yang petunjuknya adalah:

    pop(self, index=-1, /)
     |      Remove and return item at index (default last).

berdasarkan petunjuk tersebut maka `pop` akan mengambil elemen list
sekaligus menghapusnya dari `list` kita:
``` {.python}
print("list sebelum pop", suhu_24h)
elemen_terhapus=suhu_24h.pop()
print("elemen yang dihapus",elemen_terhapus)
print("list setelah pop", suhu_24h)
```

list sebelum pop [37.0, 35.0, 34.3, 32.0, 31.1, 29.0]
elemen yang dihapus 29.0
list setelah pop [37.0, 35.0, 34.3, 32.0, 31.1]

## 2.2 Tuple {#22-tuple}

`Tuple` sangat mirip dengan `List` hanya saja `Tuple` merupakan
*sequence* yang elemennya tidak bisa diganti (*immutable*). Penulisan
`Tuple` dalam Python menggunakan tanda `()`:

``` {.python}
suhu_24h_lock=(37.0, 35.0, 34.3, 32.0, 31.1, 29.0)
```
Pemanggilan element sama dengan `list` yaitu menggunakan `index`:

``` {.python}
pengukuran_1=suhu_24h_lock[0]
print(pengukuran_1)
```

37.0

Jika kita coba mengedit element dalam `tuple` maka akan muncul error:

``` {.python}
suhu_24h_lock[0]=29.0
```

----> 1 suhu_24h_lock[0]=29.0

TypeError: 'tuple' object does not support item assignment

## 2.3 Sets {#23-sets}

`Sets` adalah data dalam bentuk koleksi unik yang tak berurutan dan
sifatnya *immutable* seperti `tuple`. Secara sederhana `sets` bisa kita
artikan sebagai himpunan dalam bahasa Indonesia. Kegunaannya juga mirip
seperti himpunan:

``` {.python}
Sayur={"seledri", "tomat", "bayam"}
Sayur
```

{'bayam', 'seledri', 'tomat'}

elemen `sets` harus unik dan tidak ada yang duplikat:

``` {.python}
Sayur={"seledri", "tomat", "bayam", "tomat"}
Sayur
```

{'bayam', 'seledri', 'tomat'}

Walaupun bersifat *immutable* tapi `sets` dapat ditambah elemennya:

``` {.python}
Sayur.add("kol")
Sayur
```

{'bayam', 'kol', 'seledri', 'tomat'}

`sets` juga dapat dioperasikan dengan `sets` yang lain:

``` {.python}
Buah={"tomat","apel","jeruk"}
Buah
```

{'apel', 'jeruk', 'tomat'}

dalam contoh pertama kita akan melihat elemen dari dua `sets` yang sama
dengan method `intersection`:

``` {.python}
Sayur.intersection(Buah)
```

{'tomat'}

Dari contoh di atas kita seperti mencari irisan dari dua buah himpunan
yaitu Sayur dan Buah, karena tomat masuk keduanya maka tomat adalah
irisannya. Contoh selanjutnya adalah dengan metode `difference` dan
`union`kira-kira apa yang terjadi?

``` {.python}
Sayur.difference(Buah)
```

{'bayam', 'seledri'}
``` {.python}
Sayur.union(Buah)
```

{'apel', 'bayam', 'jeruk', 'seledri', 'tomat'}

## 2.4 Dictionary {#24-dictionary}

`Dictionary` menyimpan data di dalam `keys` bersifat alfanumerik, `keys`
bisa dianalogikan sebagai sebuah judul kolom yang masing-masing kolom
tersebut terdapat data. Penulisan `dictionary` mirip dengan `sets` yaitu
menggunakan `{}`. Dalam contoh di bawah ini masih menggunakan studi
kasus pengukuran suhu, dengan `dictionary` kita dapat mendefinisikan
data lain yaitu waktu pengukuran dalam menit:

``` {.python}
pengukuran_suhu={"waktu_menit":[10,20,30], "suhu":[29,30,27], "operator":"Kaka"}
print(pengukuran_suhu)
```

{'waktu_menit': [10, 20, 30], 'suhu': [29, 30, 27], 'operator': 'Kaka'}
Jika dalam `list` dan dalam `tuple` kita bisa mengambil elemen dengan
menggunakan indeks, dalam `dictionary` kita menggunakan `keys` dari data
yang akan kita ambil. Apabila kita ingin mengambil data waktu pengukuran
maka kita menggunakan `keys` `waktu_menit`:

``` {.python}
waktu_pengukuran=pengukuran_suhu['waktu_menit']
waktu_pengukuran
```

[10, 20, 30]

Dengan memanggil `waktu_pengukuran` kita mendapatkan isi dari `key`
tersebut yang berupa `list`, seperti yang kita definisikan di atas.

# 3 Conditional (Pembuatan Keputusan) {#3-conditional-pembuatan-keputusan}

Pada pembuatan suatu aplikasi pasti akan sampai dalam sebuah titik
dimana kita harus mengambil keputusan dan harus memilih satu dari
beberapa pilihan tergantung kondisi. Dalam implementasinya kita akan
mengenal `if`, `elif`, dan `else`:
``` {.python}
waktu_menit=20

if waktu_menit > 60:
    print("pengukuran lebih dari 1 jam")
    print("operator: Kaka")
elif waktu_menit > 30:
    print("pengukuran lebih dari 0.5 jam")
# else:
#     print("pengukuran kurang dari 0.5 jam")

print("test")
```


Pada contoh di atas kita membuat variabel `waktu_menit`, apabila nilai
dalam variabel tersebut melebihi 60 menit (`if waktu_menit > 60`) maka
akan dicetak tulisan: `pengukuran lebih dari 1 jam`. Jika waktu kurang
dari 60 maka tidak akan terjadi apa-apa:

``` {.python}
waktu_menit=10

if waktu_menit > 60:
    print("pengukuran lebih dari 1 jam")
```

Kita bisa menambah percabangan lagi dengan `else` apabila `waktu_menit`
tidak lebih besar dari 60:

``` {.python}
waktu_menit=10

if waktu_menit > 60:
    print("pengukuran lebih dari 1 jam")
else:
    print("pengukuran kurang dari 1 jam")
```

pengukuran kurang dari 1 jam

Untuk percabangan yang lebih dari 2 maka kita perlu menggunakan `elif`
atau else-if:

``` {.python}
waktu_menit=60

if waktu_menit > 60:
    print("pengukuran lebih dari 1 jam")
elif waktu_menit == 60:
    print("pengukuran tepat 1 jam")
else:
    print("pengukuran kurang dari 1 jam")
```

pengukuran tepat 1 jam

`Conditional` ini dapat bertingkat (`nested`), contoh apabila pengukuran
selesai setelah 120 menit atau 2 jam:

``` {.python}
waktu_menit=130
timer_off=120

if waktu_menit > 60:
    if waktu_menit < timer_off:
        print("pengukuran lebih dari 1 jam")
    else:
        print("pengukuran selesai karena sudah 2 jam")
elif waktu_menit == 60:
    print("pengukuran tepat 1 jam")
else:
    print("pengukuran kurang dari 1 jam")
```

pengukuran selesai karena sudah 2 jam

# Penugasan

1.  Buatlah 3 rumus fisika dasar dan operasikan rumus tersebut
    berdasarkan input yang kalian tentukan sendiri

``` {.python}
a=float(input('masukan alas:'))
t=float(input('masukan tinggi:'))
b=0.5*a*t
print('luas=',b)
```

    masukan alas:12
    masukan tinggi:10
    luas= 60.0

``` {.python}
a=float(input('angka:'))
if a % 2==0:
  print('genap')
else:
  print('gempi') 
```

    angka:12
    genap

## Lisensi

Material ini di bawah lisensi [Creative Commons Attribution 4.0
International License](http://creativecommons.org/licenses/by/4.0/).

## Referensi

Lisa Tauxe, <ltauxe@ucsd.edu>, Hanna Asefaw, <hasefaw@ucs.dedu>, &
Brendan Cych, <bcych@ucsd.edu>, Python Programming for Earth Science
Students, Repository:

