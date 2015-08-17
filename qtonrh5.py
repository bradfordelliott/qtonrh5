#!/usr/bin/env python
import os
import subprocess
import shlex
import sys
import shutil

#yum install xz

# These packages are required in order to build QT from sources with most options.
packages = [

    {"name" : "tar",        "url" : "http://ftp.gnu.org/gnu/tar/tar-1.28.tar.bz2"},
    {"name" : "libffi",     "url" : "ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz"},
    {"name" : "glib",       "url" : "http://ftp.gnome.org/pub/GNOME/sources/glib/2.45/glib-2.45.4.tar.xz"},
    {"name" : "pkg-config", "url" : "http://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz"},
    {"name" : "cmake", "url" : "http://www.cmake.org/files/v3.3/cmake-3.3.1.tar.gz"},
    
    # First build the latest Python from sources
    {"name" : "python",              "url" : "https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz"},

    # These libraries are required for OpenGL support
    {"name" : "macros",               "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/util/util-macros-1.17.tar.gz"},
    {"name" : "pthreads",            "url" : "http://xcb.freedesktop.org/dist/libpthread-stubs-0.3.tar.bz2"},
    {"name" : "xcb-proto",           "url" : "http://xcb.freedesktop.org/dist/xcb-proto-1.11.tar.bz2"},
    {"name" : "libxcb",              "url" : "http://xcb.freedesktop.org/dist/libxcb-1.11.tar.gz"},
    {"name" : "xproto",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/proto/xproto-7.0.23.tar.bz2"},
    {"name" : "xcb-util",            "url" : "http://xcb.freedesktop.org/dist/xcb-util-0.4.0.tar.bz2"},
    {"name" : "xcb-util-image",      "url" : "http://xcb.freedesktop.org/dist/xcb-util-image-0.4.0.tar.bz2"},
    {"name" : "xcb-util-keysyms",    "url" : "http://xcb.freedesktop.org/dist/xcb-util-keysyms-0.4.0.tar.bz2"},
    {"name" : "xcb-util-renderutil", "url" : "http://xcb.freedesktop.org/dist/xcb-util-renderutil-0.3.9.tar.bz2"},
    {"name" : "xcb-util-wm",         "url" : "http://xcb.freedesktop.org/dist/xcb-util-wm-0.4.1.tar.bz2"},
    {"name" : "xextproto",           "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/proto/xextproto-7.2.1.tar.bz2"},
    {"name" : "xtrans",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/lib/xtrans-1.2.7.tar.bz2"},
    {"name" : "libX11",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/lib/libX11-1.5.0.tar.bz2"},

    # To get https URLs to work with webkit you need OpenSSL
    {"name" : "openssl",             "url" : "https://github.com/openssl/openssl/archive/OpenSSL_1_0_1p.tar.gz", "wget" : "-O OpenSSL_1_0_1p.tar.gz", "build_dir" : "openssl-OpenSSL_1_0_1p", "configure" : "./config --prefix=/tools/swott/rh5/build --openssldir=/tools/swott/rh5/build/openssl --shared"},

    # Newer tools required to build Webkit
    {"name" : "ruby",                "url" : "https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.gz", "wget" : "--no-check-certificate"},
    {"name" : "flex",                "url" : "http://sourceforge.net/projects/flex/files/flex-2.5.39.tar.gz/download", "archive" : "flex-2.5.39.tar.gz"},

    # Unicode Support
    {"name" : "icu/unicode",         "url" : "http://download.icu-project.org/files/icu4c/55.1/icu4c-55_1-src.tgz", "build_dir" : "icu/source"},
]

output = []

for package in packages:
    print package["name"]
    # Figure out what the archive is
    if(package.has_key("archive")):
        archive = package["archive"]
    else:
        archive = os.path.basename(package["url"])

    # First download the package
    if(not os.path.exists(archive)):
        print "Downloading %s" % archive
        wget_args = ""
        if(package.has_key("wget")):
            wget_args = package["wget"]
        cmd_download = shlex.split("wget %s %s" % (wget_args, package["url"]))
        phandle = subprocess.Popen(cmd_download, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print phandle.stdout.read()
        print phandle.stderr.read()
        phandle.wait()
        rc = phandle.returncode

        if(rc != 0):
            print "Aborting Download Process"
            sys.exit(-1)
    
    # Now determine the build directory
    if(package.has_key("build_dir")):
        build_dir = package["build_dir"]
    else:
        build_dir = archive.replace(".tar.gz", "")
        build_dir = build_dir.replace(".tar.xz", "")
        build_dir = build_dir.replace(".tar.bz2", "")
        build_dir = build_dir.replace(".tgz", "")
        build_dir = build_dir.replace(".gz", "")

    if(os.path.exists(build_dir)):
        shutil.rmtree(build_dir)

    print "Extracting %s" % package["name"]
    tar = "/tools/swott/rh5/build/bin/tar"
    if(not os.path.exists("/tools/swott/rh5/build/bin/tar")):
        tar = "tar"
    cmd_extract = shlex.split("%s -xf %s" % (tar,archive))
    phandle = subprocess.Popen(cmd_extract, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print phandle.stdout.read()
    print phandle.stderr.read()
    phandle.wait()
    rc = phandle.returncode

    if(rc != 0):
        print "Failed extracting %s" % package["name"]
        sys.exit(-1)

    print "Building %s in %s" % (package["name"], build_dir)
    handle = open("run.sh", "wt")

    config = "./configure --prefix=/tools/swott/rh5/build"
    if(package.has_key("configure")):
        config = package["configure"]
    handle.write('''
#!/bin/bash -ex
. /opt/rh/devtoolset-2/enable
# package config
export PKG_CONFIG_PATH=/tools/swott/rh5/build/lib/pkgconfig:/tools/swott/rh5/build/share/pkgconfig
cd "%s"
%s
make
make install
''' % (build_dir, config))
    handle.close()
    os.chmod("run.sh", 0777)
    
    cmd_build = shlex.split("/bin/bash ./run.sh")
    phandle = subprocess.Popen(cmd_build, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print phandle.stdout.read()
    print phandle.stderr.read()
    phandle.wait()
    rc = phandle.returncode

    if(rc != 0):
        print "Failed build %s" % package["name"]
        print " ".join(cmd_build)


