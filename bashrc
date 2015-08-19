# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
#export PATH=/home/belliott/usr/bin:${PATH}
export LD_LIBRARY_PATH=/tools/swott/rh5/build/lib/:${LD_LIBRARY_PATH}
export PKG_CONFIG_PATH=/tools/swott/rh5/build/lib/pkgconfig:/tools/swott/rh5/build/share/pkgconfig:/usr/lib/pkgconfig
export PKG_CONFIG_PREFIX=/tools/swott/rh5/build/lib/pkgconfig
export PATH=/tools/swott/rh5/build/bin:/tools/swott/rh5/qt/bin:${PATH}
