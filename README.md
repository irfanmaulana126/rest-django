
## Installation

Buat virtualenv terlebih dahulu (Windows)
```bash
virtualenv {nama_virtual}
```
Masuk kedalam virtual (Windows)
```bash
source {nama_virtual}/Scripts/activate
```
Jika menggunakan linux
```bash
virtualenv -p python3 {nama_virtual} ##untuk python3, ubuntu biasanya menggunakan ini
source {nama_virtual}/bin/activate
```
Install requirements menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
```
tetap pada terminal, jalankan perintah migrasi
```bash
python manage.py makemigrations && python manage.py migrate
```
Jalankan server
```bash
python manage.py runserver
```
## Run Unit Test

Test Function GET all data post
```bash
python manage.py test api.test.test_views.GetAllPostsTest
```

Test Function GET single data post
```bash
python manage.py test api.test.test_views.GetSinglePostsTest
```

Test Function Create data post
```bash
python manage.py test api.test.test_views.CreateNewPostsTest
```

Test Function Update data post
```bash
python manage.py test api.test.test_views.UpdateSinglePostsTest
```

Test Function Delete single data post
```bash
python manage.py test api.test.test_views.DeleteSinglePostsTest
```