### Python HMI (Human machine Interface) for Raspberry 3 ###
#### MF ALfafa ####
#### miftahf77@gmail.com ####
#### 19 August 2018 ####

> Introduction

This is a script made by Python that is used as an HMI (Human Machine Interface) on Raspi 3. This program is very lightweight in size and easy to use. 

> Advantages
1. Program GUI yang cocok (support) digunakan pada Raspi 3 terutama yang menggunakan Sistem Operasi ***Raspbian Jessie*** karena di dalam Sistem Operasi tersebut terdapat aplikasi dan library bawaan yang mendukung pemrograman dengan bahasa Python.
2. Program berbasis GUI yang tergolong sangat ringan jika dijalankan pada Raspi 3 yang menggunakan Sistem Operasi ***Raspbian Jessie*** karena ukuran file-file-nya hanya beberapa kilobyte.
3. Mudah dan cepat dalam proses deploy karena program berbasis GUI tersebut dapat disimulasikan di komputer yang menggunakan berbagai macam Sistem Operasi seperti Windows, Linux ataupun Mac dan juga program berbasis GUI tersebut tidak memerlukan proses compiling dan building yang memakan waktu lama. Hal tersebut dikarenakan Python merupakan jenis Interpreted Language.
4. Terintegrasi dengan SQL Database seperti MySQL dan PostgreSQL
5. Mudah dalam pembuatan GUI-nya dengan menggunakan bantuan software Qt5 designer (drag & drop object)

> Disadvantages
1. Widget terbatas. Jika ingin custom widget maka diperlukan coding yang cukup rumit.


> Installation

sudo apt-get install python-psycopg2

> Note!

To enable remote connection in PosgreSQL server IP, change the following files:
1. pg_hba.conf		#192.168.10.151 = PostgreSQL Server IP

Add this script :
```
host all all 192.168.10.151/24
```
2. postgresql.conf
```
listen_addresses = '*'
```

```
install python 3.5

pip install --upgrade pip
pip install psycopg2-binary
pip install pyqt5
pip install pyserial

or

sudo apt-get update
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools

```
