#!/usr/bin/env python
import os
import subprocess
import shlex
import sys
import shutil

#yum install xz

# These packages are required in order to build QT from sources with most options.
packages = [

#    {"name" : "flex",                "url" : "http://sourceforge.net/projects/flex/files/flex-2.5.39.tar.gz/download", "archive" : "flex-2.5.39.tar.gz"},
#    {"name" : "tar",        "url" : "http://ftp.gnu.org/gnu/tar/tar-1.28.tar.bz2"},
#    {"name" : "libffi",     "url" : "ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz"},
#    {"name" : "glib",       "url" : "http://ftp.gnome.org/pub/GNOME/sources/glib/2.45/glib-2.45.4.tar.xz"},
#    {"name" : "pkg-config", "url" : "http://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz"},
#    {"name" : "cmake", "url" : "http://www.cmake.org/files/v3.3/cmake-3.3.1.tar.gz", "wget" : "--no-check-certificate"},
    
    # First build the latest Python from sources
#    {"name" : "python",              "url" : "https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz"},

    # These libraries are required for OpenGL support
#    {"name" : "macros",               "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/util/util-macros-1.17.tar.gz"},
#    {"name" : "pthreads",            "url" : "http://xcb.freedesktop.org/dist/libpthread-stubs-0.3.tar.bz2"},
#    {"name" : "xcb-proto",           "url" : "http://xcb.freedesktop.org/dist/xcb-proto-1.11.tar.bz2"},
#    {"name" : "xau",                  "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/libXau-1.0.7.tar.bz2"},
#    {"name" : "libxcb",              "url" : "http://xcb.freedesktop.org/dist/libxcb-1.11.tar.gz"},
#    {"name" : "xproto",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/proto/xproto-7.0.23.tar.bz2"},
#    {"name" : "xcb-util",            "url" : "http://xcb.freedesktop.org/dist/xcb-util-0.4.0.tar.bz2"},
#    {"name" : "xcb-util-image",      "url" : "http://xcb.freedesktop.org/dist/xcb-util-image-0.4.0.tar.bz2"},
#    {"name" : "xcb-util-keysyms",    "url" : "http://xcb.freedesktop.org/dist/xcb-util-keysyms-0.4.0.tar.bz2"},
#    {"name" : "xcb-util-renderutil", "url" : "http://xcb.freedesktop.org/dist/xcb-util-renderutil-0.3.9.tar.bz2"},
#    {"name" : "xcb-util-wm",         "url" : "http://xcb.freedesktop.org/dist/xcb-util-wm-0.4.1.tar.bz2"},
#    {"name" : "xextproto",           "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/proto/xextproto-7.2.1.tar.bz2"},
#    {"name" : "inputproto",           "url" : "http://xorg.mirrors.pair.com/X11R7.7/src/proto/inputproto-2.2.tar.bz2"},
#    {"name" : "xtrans",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/lib/xtrans-1.2.7.tar.bz2"},
#    {"name" : "kbproto",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/kbproto-1.0.6.tar.bz2"},
#    {"name" : "fixesproto",           "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/fixesproto-5.0.tar.bz2"},
#    {"name" : "libX11",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/lib/libX11-1.5.0.tar.bz2"},
#    {"name" : "dmcp",                 "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/libXdmcp-1.1.1.tar.bz2"},
#    {"name" : "libXfixes",            "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/libXfixes-5.0.tar.bz2"},
#    {"name" : "renderproto",          "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/renderproto-0.11.1.tar.bz2"},
#    {"name" : "xrender",              "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/libXrender-0.9.7.tar.bz2"},
#    {"name" : "randrproto",            "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/randrproto-1.3.2.tar.bz2"},
#    {"name" : "xext",                  "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/libXext-1.3.1.tar.bz2"},
#    {"name" : "XRander",               "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/libXrandr-1.3.2.tar.bz2"},
#    {"name" : "libXcursor",           "url" : "ftp://xorg.mirrors.pair.com/X11R7.7/src/everything/libXcursor-1.1.13.tar.bz2"},

    # To get https URLs to work with webkit you need OpenSSL
#    {"name" : "openssl",             "url" : "https://github.com/openssl/openssl/archive/OpenSSL_1_0_1p.tar.gz", "wget" : "-O OpenSSL_1_0_1p.tar.gz", "build_dir" : "openssl-OpenSSL_1_0_1p", "configure" : "./config --prefix=/tools/swott/rh5/build --openssldir=/tools/swott/rh5/build/openssl --shared"},
#
    # Newer tools required to build Webkit
#    {"name" : "ruby",                "url" : "https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.gz", "wget" : "--no-check-certificate"},
#    {"name" : "flex",                "url" : "http://sourceforge.net/projects/flex/files/flex-2.5.39.tar.gz/download", "archive" : "flex-2.5.39.tar.gz"},
#
    # Unicode Support
#    {"name" : "icu/unicode",         "url" : "http://download.icu-project.org/files/icu4c/55.1/icu4c-55_1-src.tgz", "build_dir" : "icu/source"},

#    {"name" : "harfbuzz",      "url" : "https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-1.2.7.tar.bz2"},
#     {"name" : "expat",       "url" : "https://sourceforge.net/projects/expat/files/expat/2.2.0/expat-2.2.0.tar.bz2/download", "archive" : "expat-2.2.0.tar.bz2", "wget" : "--no-check-certificate"},
    {"name" : "freetype",    "url" : "https://sourceforge.net/projects/freetype/files/freetype2/2.6.3/freetype-2.6.3.tar.bz2/download", "archive" : "freetype-2.6.3.tar.bz2", "wget" : "--no-check-certificate"},
#     {"name" : "fontconfig",  "url" : "https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.12.0.tar.gz", "wget" : "--no-check-certificate"},
#   {"name" : "libpng",      "url" : "http://prdownloads.sourceforge.net/libpng/libpng-1.6.23.tar.xz?download", "archive" : "libpng-1.6.23.tar.xz", "wget" : "--no-check-certificate"},
#    {"name" : "pixman",      "url" : "https://www.cairographics.org/releases/pixman-0.34.0.tar.gz", "wget" : "--no-check-certificate"},
#     {"name" : "cairo",       "url" : "https://www.cairographics.org/releases/cairo-1.14.6.tar.xz", "wget" : "--no-check-certificate"},
#     {"name" : "pango",       "url" : "http://ftp.gnome.org/pub/GNOME/sources/pango/1.40/pango-1.40.1.tar.xz"},
#    {"name" : "gnuplot",     "url" : "https://sourceforge.net/projects/gnuplot/files/gnuplot/5.0.1/gnuplot-5.0.1.tar.gz/download", "wget" : "--no-check-certificate", "archive" : "gnuplot-5.0.1.tar.gz"},
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
export LDFLAGS=-Wl,-rpath,.
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


