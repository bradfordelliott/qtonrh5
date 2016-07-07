# qtonrh5

First you'll need to install the development tools. We start by
updating the repositories. We need the development tools and EPEL (for git)

```
wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O /etc/yum.repos.d/devtools-2.repo
wget http://ftp.tu-chemnitz.de/pub/linux/fedora-epel/5/x86_64/epel-release-5-4.noarch.rpm
rpm -i epel-release-5.4.noarch.rpm
```

Now using sudo or root you'll need to install the development toolset and install Git:
```
yum install devtoolset-2
yum install git
yum install xz
yum install glib
yum install zlib-devel
```

Enable the newer devepment tools:
```
scl enable devtoolset-2 bash
```

and then clone the git repository

```
git clone https://github.com/bradfordelliott/qtonrh5.git
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
