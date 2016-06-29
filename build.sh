#!/bin/bash
base_dir=/tools/swott/rh5/build

# This line is required to enable the newer tools
# on RH5. Otherwise nothing will compile
#scl enable devtoolset-2 bash

# To build webkit we need the latest versions of
# python, ruby and flex. The ones that are packaged with
# redhat5 are too old
#wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
#wget https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.gz
#wget http://sourceforge.net/projects/flex/files/flex-2.5.39.tar.gz/download

# We also need these libraries for webkit
#    yum install gperf
#    yum install bison
#    yum install openssl-devel.x86_64
# Need to include ICU for webkit

#pkg-config --variable pc_path pkg-config
#exit 0

#tar -xzf ../OpenSSL_1_0_1p.tar.gz
#cd openssl-OpenSSL_1_0_1p
#./config --prefix=/home/belliott/usr --openssldir=/home/belliott/usr/openssl --shared
#make
#make install
#cd ..
#exit -1

#tar -xzf ../ruby-2.2.2.tar.gz
#cd ruby-2.2.2
#./configure -prefix=/home/belliott/usr
#make
#make install
#cd ..


#tar -xzf ../Python-2.7.10.tgz
#cd Python-2.7.10
#./configure -prefix=/home/belliott/usr
#make
#make install
#cd ..

# Webkit build will fail without a newer version of flex
#tar -xzf ../flex-2.5.39.tar.gz
#cd flex-2.5.39
#./configure -prefix=/home/belliott/usr
#make
#make install
#cd ..
#exit -1

# ICU - requirement for webkit
#   To get it to build I had to add this line:
#       -L /home/belliott/usr/lib \

#tar -xzf ../icu4c-55_1-src.tgz
#cd icu/source
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..

## xproto
#tar -xjf ../xproto-7.0.23.tar.bz2
#cd xproto-7.0.23
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## pthread stubs
#tar -xzf ../libpthread-stubs-0.3.tar.gz
#cd libpthread-stubs-0.3
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xcb proto
#tar -xzf ../xcb-proto-1.11.tar.gz
#cd xcb-proto-1.11
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xcb util
#tar -xjf ../xcb-util-0.4.0.tar.bz2
#cd xcb-util-0.4.0
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xcb util-image
#tar -xjf ../xcb-util-image-0.4.0.tar.bz2
#cd xcb-util-image-0.4.0
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xcb util-keysyms
#tar -xjf ../xcb-util-keysyms-0.4.0.tar.bz2
#cd xcb-util-keysyms-0.4.0
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xcb util-renderutil
#tar -xjf ../xcb-util-renderutil-0.3.9.tar.bz2
#cd xcb-util-renderutil-0.3.9
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xcb util-wm
#tar -xjf ../xcb-util-wm-0.4.1.tar.bz2
#cd xcb-util-wm-0.4.1
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xcb
#tar -xzf ../libxcb-1.11.tar.gz
#cd libxcb-1.11
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xextproto
#tar -xjf ../xextproto-7.2.1.tar.bz2
#cd xextproto-7.2.1
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## xtrans
#tar -xjf ../xtrans-1.2.7.tar.bz2
#cd xtrans-1.2.7
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## libX11
#tar -xjf ../libX11-1.5.0.tar.bz2
#cd libX11-1.5.0
#./configure -prefix=/home/belliott/usr
#make -j4
#make install
#cd ..
#
## Qt
tar -xzf ../qt-everywhere-opensource-src-5.4.2.tar.gz
cd qt-everywhere-opensource-src-5.4.2

# no perf events => patch that out, won’t compile, at least not for me because of missing syscall/broken kernel header
sed -i "s/#define QTESTLIB_USE_PERF_EVENTS/#undef QTESTLIB_USE_PERF_EVENTS/g" qtbase/src/testlib/qbenchmark_p.h

# configure with some defines to work on centos 5 (fake some defines)
#./configure -R ‘\\\$$ORIGIN’ -D _X_INLINE=inline -D XK_dead_currency=0xfe6f -D XK_ISO_Level5_Lock=0xfe13 -D FC_WEIGHT_EXTRABLACK=215 -D FC_WEIGHT_ULTRABLACK=FC_WEIGHT_EXTRABLACK -v -opensource -confirm-license -sysconfdir /etc/xdg -prefix /tmp/usr/qt -release -shared -qt-zlib -qt-libpng -qt-libjpeg -qt-pcre -qt-xcb -qt-xkbcommon -xkb-config-root /usr/share/X11/xkb -no-xcb-xlib -c++11 -nomake examples -nomake tests -no-dbus -no-icu -no-opengl -skip activeqt -skip androidextras -skip connectivity -skip enginio -skip location -skip macextras -skip multimedia -skip quick1 -skip sensors -skip serialport -skip wayland -skip webchannel -skip webengine -skip webkit -skip webkit-examples -skip websockets -skip winextras -skip x11extras

#./configure -prefix /home/belliott/usr \
#-v \
#-sysconfdir /etc/xdg \
#-I /home/belliott/usr/include \
#-D GLX_GLXEXT_LEGACY \
#-D _X_INLINE=inline \
#-D XK_dead_currency=0xfe6f \
#-D XK_ISO_Level5_Lock=0xfe13 \
#-D FC_WEIGHT_EXTRABLACK=215 \
#-D FC_WEIGHT_ULTRABLACK=FC_WEIGHT_EXTRABLACK \
#-D GLX_CONTEXT_MAJOR_VERSION_ARB=0x2091 \
#-D GLX_CONTEXT_MINOR_VERSION_ARB=0x2092 \
#-D GLX_CONTEXT_DEBUG_BIT_ARB=0x00000001 \
#-D GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB=0x00000002 \
#-D GLX_CONTEXT_FLAGS_ARB=0x2094 \
#-release \
#-opensource \
#-confirm-license \
#-shared \
#-qt-zlib \
#-qt-libpng \
#-qt-libjpeg \
#-qt-pcre \
#-qt-xkbcommon \
#-xcb \
#-xcb-xlib \
#-xkb-config-root /usr/share/X11/xkb \
#-nomake tests \
#-no-dbus \
#-no-icu \
#-no-openssl \
#-skip activeqt \
#-skip androidextras \
#-skip connectivity \
#-skip enginio \
#-skip location \
#-skip macextras \
#-skip multimedia \
#-skip quick1 \
#-skip sensors \
#-skip serialport \
#-skip wayland \
#-skip webchannel \
#-skip webengine \
#-skip webkit \
#-skip webkit-examples \
#-skip websockets \
#-skip winextras \
#-skip x11extras

# You need to setup LD_LIBRARY_PATH manually
# when building or it won't be able to find the shared
# libraries for ICU.
#LD_LIBRARY_PATH=/home/belliott/usr/lib:/usr/local/ssl/lib:${LD_LIBRARY_PATH}
LD_LIBRARY_PATH=/tools/swott/rh5/build/lib:${LD_LIBRARY_PATH}

#-I/usr/local/ssl/include \
#-I/home/belliott/usr/include \
#-L /home/belliott/usr/lib \
#-L /usr/local/ssl/lib \
#-lssl -lcrypto \

./configure -verbose -prefix /tools/swott/rh5/qt \
-v \
-I/tools/swott/rh5/build/include \
-L/tools/swott/rh5/build/lib \
-pkg-config \
-sysconfdir /etc/xdg \
-D GLX_GLXEXT_LEGACY \
-D _X_INLINE=inline \
-D XK_dead_currency=0xfe6f \
-D XK_ISO_Level5_Lock=0xfe13 \
-D FC_WEIGHT_EXTRABLACK=215 \
-D FC_WEIGHT_ULTRABLACK=FC_WEIGHT_EXTRABLACK \
-D GLX_CONTEXT_MAJOR_VERSION_ARB=0x2091 \
-D GLX_CONTEXT_MINOR_VERSION_ARB=0x2092 \
-D GLX_CONTEXT_DEBUG_BIT_ARB=0x00000001 \
-D GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB=0x00000002 \
-D GLX_CONTEXT_FLAGS_ARB=0x2094 \
-D O_CLOEXEC=0 \
-release \
-opensource \
-confirm-license \
-shared \
-openssl \
-qt-zlib \
-qt-libpng \
-qt-libjpeg \
-qt-pcre \
-qt-xcb \
-qt-xkbcommon \
-nomake examples \
-nomake tests \
-no-dbus \
-icu \
-skip activeqt \
-skip androidextras \
-skip connectivity \
-skip enginio \
-skip location \
-skip macextras \
-skip multimedia \
-skip sensors \
-skip serialport \
-skip wayland \
-skip webchannel \
-skip webengine \
-skip webkit-examples \
-skip websockets \
-skip winextras

