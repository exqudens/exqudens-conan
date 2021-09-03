# Install On Linux

--------------------------------------------------

##### (optional) bash command line run:
```
python -m pip install --user virtualenv
```

##### bash command line run:
```
python -m virtualenv conan-1.39
```

##### bash command line run:
```
./conan-1.39/bin/pip install conan==1.39.0
```

##### bash command line run:
```
ln -s ./conan-1.39/bin/conan conan
```

--------------------------------------------------

# Install On Windows

--------------------------------------------------

##### (optional) git-bash command line run:
```
py [-3.9] -m pip install --user virtualenv
```

##### git-bash command line run:
```
py -m virtualenv conan-1.39
```

##### git-bash command line run:
```
./conan-1.39/Scripts/pip install conan==1.39.0
```

##### windows admin command line run:
```
mklink conan.exe conan-1.39/Scripts/conan.exe
```

--------------------------------------------------

