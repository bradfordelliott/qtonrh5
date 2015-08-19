# qtonrh5
First you'll need to install the development tools. We start by
updating the repositories:

```
wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O /etc/yum.repos.d/devtools-2.repo
```

Now install a minimal set of development packages
```
yum install devtoolset-2 fontconfig-devel libX11-devel libXau-devel libXext-devel libXrender-devel
```

# O_CLOEXEC
This doesn't exist on RH5. Needed to manually define
it to 0. Not sure if it is safe to do this in the ./config
string or not.

# Building QT
../build_qt.sh
make -j4

# Building QTCreator
../build_creator.sh
make -j4
