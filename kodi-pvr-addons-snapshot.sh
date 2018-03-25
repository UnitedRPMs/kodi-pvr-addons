#!/bin/bash

# New PVR add-ons repository for Kodi: https://github.com/kodi-pvr

tag_name=master

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
# FIXME pvr.stalker
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.vbox.git kodi-pvr-addons/pvr.vbox
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.filmon.git kodi-pvr-addons/pvr.filmon
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.dvblink.git kodi-pvr-addons/pvr.dvblink
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.demo.git kodi-pvr-addons/pvr.demo
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.argustv.git kodi-pvr-addons/pvr.argustv
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.dvbviewer.git kodi-pvr-addons/pvr.dvbviewer
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.mediaportal.tvserver.git kodi-pvr-addons/pvr.mediaportal
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.iptvsimple.git kodi-pvr-addons/pvr.iptvsimple
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.vuplus.git kodi-pvr-addons/pvr.vuplus
git clone -b ${tag_name} --depth=1 https://github.com/Rechi/pvr.stalker.git kodi-pvr-addons/pvr.stalker
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.pctv.git kodi-pvr-addons/pvr.pctv
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.njoy.git kodi-pvr-addons/pvr.njoy
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.nextpvr.git kodi-pvr-addons/pvr.nextpvr
git clone -b ${tag_name} --depth=1 https://github.com/FernetMenta/pvr.vdr.vnsi.git kodi-pvr-addons/pvr.vdr.vnsi
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.hts.git kodi-pvr-addons/pvr.hts
git clone -b ${tag_name} https://github.com/kodi-pvr/pvr.wmc.git kodi-pvr-addons/pvr.wmc
git clone -b ${tag_name} --depth=1 https://github.com/janbar/pvr.mythtv.git kodi-pvr-addons/pvr.mythtv
cd ${package}
#git checkout ${branch}
#tag=$(git rev-list HEAD -n 1 | cut -c 1-7)
#version=`git describe --tags | cut -d '-' -f 1`
version=18
cd ${tmp}
tar Jcf "$pwd"/${name}-${version}-${date}.tar.xz ${package}

popd
#upload_source=$( curl --upload-file ${name}-${version}-${date}.tar.xz https://transfer.sh/${name}-${version}-${date}.tar.xz )
#if [ -n "$upload_source" ]; then
#GCOM=$( sed -n '/Source0:/=' ${name}.spec)
#sed -i "${GCOM}s#.*#Source0:	${upload_source}#" ${name}.spec
#fi


