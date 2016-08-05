#!/bin/bash

# New PVR add-ons repository for Kodi: https://github.com/kodi-pvr

tag_name=Jarvis

set -x

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
date=$(date +%Y%m%d)
package=kodi-pvr-addons
branch=master
name=kodi-pvr-addons

pushd ${tmp}
mkdir -p ${name}/
# FIXME pvr.vbox
git clone https://github.com/kodi-pvr/pvr.vbox.git kodi-pvr-addons/pvr.vbox
git clone https://github.com/kodi-pvr/pvr.filmon.git kodi-pvr-addons/pvr.filmon
git clone https://github.com/kodi-pvr/pvr.dvblink.git kodi-pvr-addons/pvr.dvblink
git clone https://github.com/kodi-pvr/pvr.demo.git kodi-pvr-addons/pvr.demo
git clone https://github.com/kodi-pvr/pvr.argustv.git kodi-pvr-addons/pvr.argustv
git clone https://github.com/kodi-pvr/pvr.dvbviewer.git kodi-pvr-addons/pvr.dvbviewer
git clone https://github.com/kodi-pvr/pvr.mediaportal.tvserver.git kodi-pvr-addons/pvr.mediaportal
git clone https://github.com/kodi-pvr/pvr.iptvsimple.git kodi-pvr-addons/pvr.iptvsimple
git clone https://github.com/kodi-pvr/pvr.vuplus.git kodi-pvr-addons/pvr.vuplus
git clone https://github.com/kodi-pvr/pvr.stalker.git kodi-pvr-addons/pvr.stalker
git clone https://github.com/kodi-pvr/pvr.pctv.git kodi-pvr-addons/pvr.pctv
git clone https://github.com/kodi-pvr/pvr.njoy.git kodi-pvr-addons/pvr.njoy
git clone https://github.com/kodi-pvr/pvr.nextpvr.git kodi-pvr-addons/pvr.nextpvr
git clone https://github.com/kodi-pvr/pvr.mythtv.git kodi-pvr-addons/pvr.mythtv
git clone https://github.com/kodi-pvr/pvr.vdr.vnsi.git kodi-pvr-addons/pvr.vdr.vnsi
git clone https://github.com/kodi-pvr/pvr.hts.git kodi-pvr-addons/pvr.hts
git clone https://github.com/kodi-pvr/pvr.wmc.git kodi-pvr-addons/pvr.wmc
cd ${package}
#git checkout ${branch}
#tag=$(git rev-list HEAD -n 1 | cut -c 1-7)
#version=`git describe --tags | cut -d '-' -f 1`
version=17.0
cd ${tmp}
tar Jcf "$pwd"/${name}-${version}-${date}.tar.xz ${package}



