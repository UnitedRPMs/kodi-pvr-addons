%global gitdate 20180627
%global debug_package %{nil}

Name:           kodi-pvr-addons
Version:        18.0
Release:        5%{?dist}
Summary:        Kodi PVR add-ons

Group:          Applications/Multimedia
License:        GPLv3 and GPLv2+ and LGPLv2+ and MIT
URL:            https://github.com/kodi-pvr
Source0:	https://github.com/UnitedRPMs/%{name}/releases/download/18.0/%{name}-18-%{gitdate}.tar.xz
Source1:        kodi-pvr-addons-snapshot.sh
Source2:        kodi-pvr-addons.txt

BuildRequires:  cmake
BuildRequires:  kodi-devel >= 18
BuildRequires:  platform-devel 
BuildRequires:  kodi-platform-devel >= 18
BuildRequires:  jsoncpp-devel 
BuildRequires:  tinyxml2-devel
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
#BuildRequires:  git
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mariadb-devel
BuildRequires:  libcurl-devel
#BuildRequires:  libtool
BuildRequires:  cppmyth-devel
BuildRequires:  cryptopp-devel
BuildRequires:  rapidxml-devel
BuildRequires:	libxml2-devel
#-------------------------------------
Provides:       xbmc-pvr-addons-common = %{version}-%{release}
Provides:       kodi-pvr-addons-common = %{version}-%{release}
Provides:       xbmc-pvr-addons = %{version}
Obsoletes:      xbmc-pvr-addons-common < 14.0
Obsoletes:      xbmc-pvr-addons <= %{version}
#-------------------------------------
Requires:       kodi >= 17.0
Requires:       kodi-pvr-argustv 
Requires:       kodi-pvr-demo 
Requires:       kodi-pvr-dvblink 
Requires:       kodi-pvr-dvbviewer 
Requires:       kodi-pvr-hts 
Requires:       kodi-pvr-iptvsimple 
Requires:       kodi-pvr-mediaportal-tvserver 
Requires:       kodi-pvr-mythtv 
Requires:       kodi-pvr-nextpvr 
Requires:       kodi-pvr-njoy 
Requires:       kodi-pvr-vdr-vnsi 
Requires:       kodi-pvr-vuplus 
Requires:       kodi-pvr-wmc 
Requires:       kodi-pvr-filmon 
Requires:       kodi-pvr-pctv 
Recommends:	kodi-pvr-stalker 
Requires: 	kodi-pvr-vbox


%description    
This package install all Kodi PVR addons.

#----------

%package -n     kodi-pvr-argustv
Summary:        Kodi frontend for the ARGUS TV PVR
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-argustv = %{version}-%{release}
Obsoletes:      xbmc-pvr-argustv < 14.0

%description -n kodi-pvr-argustv
ARGUS TV PVR frontend for Kodi. Supports streaming of Live TV & recordings,
listening to radio channels, EPG and schedules.

#----------

%package -n     kodi-pvr-demo
Summary:        Demo PVR Client for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-demo = %{version}-%{release}
Obsoletes:      xbmc-pvr-demo < 14.0

%description -n kodi-pvr-demo
%{summary}.

#----------

%package -n     kodi-pvr-dvblink
Summary:        Kodi PVR Plugin for DVBLink
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-dvblink = %{version}-%{release}
Obsoletes:      xbmc-pvr-dvblink < 14.0

%description -n kodi-pvr-dvblink
PVR Plugin for DVBLink from DvbLogic.com for Kodi; supporting streaming of Live
TV & recordings, EPG, timers.

#----------

%package -n     kodi-pvr-dvbviewer
Summary:        Kodi's frontend for DVBViewer
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-dvbviewer = %{version}-%{release}
Obsoletes:      xbmc-pvr-dvbviewer < 14.0

%description -n kodi-pvr-dvbviewer
DVBViewer Recording Service frontend; supporting streaming of LiveTV, timers,
recordings & EPG.

#----------

%package -n     kodi-pvr-hts
Summary:        Kodi's frontend for Tvheadend
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-hts = %{version}-%{release}
Obsoletes:      xbmc-pvr-hts < 14.0

%description -n kodi-pvr-hts
Tvheadend frontend; supporting streaming of Live TV & recordings, EPG, timers.

#----------

%package -n     kodi-pvr-iptvsimple
Summary:        Kodi PVR addon for IPTV support
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-iptvsimple = %{version}-%{release}
Obsoletes:      xbmc-pvr-iptvsimple < 14.0

%description -n kodi-pvr-iptvsimple
IPTV Simple PVR Client support m3u playlists, streaming of Live TV for
multicast/unicast sources, listening to radio channels and EPG.

#----------

%package -n     kodi-pvr-mediaportal-tvserver
Summary:        Kodi frontend for the MediaPortal TV Server (ffmpeg + tsreader version)
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-mediaportal-tvserver = %{version}-%{release}
Obsoletes:      xbmc-pvr-mediaportal-tvserver < 14.0

%description -n kodi-pvr-mediaportal-tvserver
MediaPortal TV Server frontend for Kodi. Supports streaming of Live TV &
recordings, listening to radio channels, EPG and timers. This addon combines the
former ffmpeg and tsreader addons.

#----------

%package -n     kodi-pvr-mythtv
Summary:        Kodi frontend for MythTV (using libcmyth)
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-mythtv-cmyth = %{version}-%{release}
Obsoletes:      xbmc-pvr-mythtv-cmyth < 14.0

%description -n kodi-pvr-mythtv
MythTV frontend (up to MythTV 0.26). Supports streaming of Live TV & recordings,
listening to radio channels, EPG and timers.

#----------

%package -n     kodi-pvr-nextpvr
Summary:        Kodi frontend for the NextPVR
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-nextpvr = %{version}-%{release}
Obsoletes:      xbmc-pvr-nextpvr < 14.0

%description -n kodi-pvr-nextpvr
NextPVR frontend for Kodi. Supports streaming of Live TV & recordings, listening
to radio channels and EPG.

#----------

%package -n     kodi-pvr-njoy
Summary:        Njoy N7 PVR Client for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-njoy = %{version}-%{release}
Obsoletes:      xbmc-pvr-njoy < 14.0

%description -n kodi-pvr-njoy
Njoy N7 PVR Client for Kodi.

#----------

%package -n     kodi-pvr-vdr-vnsi
Summary:        PVR client to connect VDR to Kodi over the VNSI interface
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-vdr-vnsi = %{version}-%{release}
Obsoletes:      xbmc-pvr-vdr-vnsi < 14.0

%description -n kodi-pvr-vdr-vnsi
VDR frontend for KODI; supporting streaming of Live TV & recordings, EPG, timers
over the VNSI plugin.

NOTE: this package requires the VNSI plugin (package vdr-vnsiserver on Fedora)
to be installed on the VDR backend.

#----------

%package -n     kodi-pvr-vuplus
Summary:        Kodi's frontend for VU+ / Enigma2 based settop boxes
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-vuplus = %{version}-%{release}
Obsoletes:      xbmc-pvr-vuplus < 14.0

%description -n kodi-pvr-vuplus
VU+ frontend; supporting streaming of Live TV & recordings, EPG, timers.

#----------

%package -n     kodi-pvr-wmc
Summary:        Windows Media Center client for Kodi
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0
Provides:       xbmc-pvr-wmc = %{version}-%{release}
Obsoletes:      xbmc-pvr-wmc < 14.0

%description -n kodi-pvr-wmc
An Kodi client to interface to Windows Media Center's record and EPG service.

#----------

%package -n     kodi-pvr-filmon
Summary:        Kodi's Filmon client addon 
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-pvr-filmon
Kodi's Filmon client addon.

#----------

%package -n     kodi-pvr-pctv
Summary:        Kodi's PCTV client addon  
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-pvr-pctv
Kodi's PCTV client addon.

#----------
%package -n     kodi-pvr-stalker
Summary:        Stalker Middleware PVR client addon for Kodi  
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-pvr-stalker
A PVR Client that connects Kodi to Stalker Middleware.

#----------
%package -n     kodi-pvr-vbox
Summary:        Kodi's PCTV client addon  
Group:          Applications/Multimedia
Requires:       kodi  >= 17.0

%description -n kodi-pvr-vbox
Kodi PVR addon for interfacing with the VBox Communications XTi TV Gateway devices.



%prep
%setup -qn kodi-pvr-addons 

#https://github.com/kodi-pvr/pvr.argustv/issues/57
find -name "FindJsonCpp.cmake" -exec sed -i 's/JSONCPP jsoncpp/JSONCPP json/g' {} ';'

%build

ls -d */ | sed 's:/::g' | tee addons.txt

file=addons.txt
while IFS= read -r line; do
        # display $line or do something with $line
    mkdir -p $line/build/ 
pushd %{_builddir}/kodi-pvr-addons/$line/build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi -DBUILD_SHARED_LIBS=1 ..
make 
popd  
done <"$file"


%install
file=addons.txt
while IFS= read -r line; do
        # display $line or do something with $line
pushd %{_builddir}/kodi-pvr-addons/$line/build
export PKG_CONFIG_PATH=%{_sourcedir}:%{_libdir}/pkgconfig
make install DESTDIR=%{buildroot}
popd  
done <"$file"


install -dm 755 %{buildroot}/%{_datadir}/licenses/
install -m644 %{SOURCE2} %{buildroot}/%{_datadir}/licenses/

%files 
%{_datadir}/licenses/%{name}.txt


%files -n kodi-pvr-argustv
%{_libdir}/kodi/addons/pvr.argustv/
%{_datadir}/kodi/addons/pvr.argustv/


%files -n kodi-pvr-demo
%{_libdir}/kodi/addons/pvr.demo/
%{_datadir}/kodi/addons/pvr.demo/


%files -n kodi-pvr-dvblink
%{_libdir}/kodi/addons/pvr.dvblink/
%{_datadir}/kodi/addons/pvr.dvblink/


%files -n kodi-pvr-dvbviewer
%{_libdir}/kodi/addons/pvr.dvbviewer/
%{_datadir}/kodi/addons/pvr.dvbviewer/


%files -n kodi-pvr-hts
%{_libdir}/kodi/addons/pvr.hts/
%{_datadir}/kodi/addons/pvr.hts/


%files -n kodi-pvr-iptvsimple
%{_libdir}/kodi/addons/pvr.iptvsimple/
%{_datadir}/kodi/addons/pvr.iptvsimple/


%files -n kodi-pvr-mediaportal-tvserver
%{_libdir}/kodi/addons/pvr.mediaportal.tvserver/
%{_datadir}/kodi/addons/pvr.mediaportal.tvserver/


%files -n kodi-pvr-mythtv
%{_libdir}/kodi/addons/pvr.mythtv/
%{_datadir}/kodi/addons/pvr.mythtv/


%files -n kodi-pvr-nextpvr
%{_libdir}/kodi/addons/pvr.nextpvr/
%{_datadir}/kodi/addons/pvr.nextpvr/


%files -n kodi-pvr-njoy
%{_libdir}/kodi/addons/pvr.njoy/
%{_datadir}/kodi/addons/pvr.njoy/


%files -n kodi-pvr-vdr-vnsi
%{_libdir}/kodi/addons/pvr.vdr.vnsi/
%{_datadir}/kodi/addons/pvr.vdr.vnsi/


%files -n kodi-pvr-vuplus
%{_libdir}/kodi/addons/pvr.vuplus/
%{_datadir}/kodi/addons/pvr.vuplus/


%files -n kodi-pvr-wmc
%{_libdir}/kodi/addons/pvr.wmc/
%{_datadir}/kodi/addons/pvr.wmc/

#----
%files -n kodi-pvr-filmon
%{_libdir}/kodi/addons/pvr.filmon/
%{_datadir}/kodi/addons/pvr.filmon/

%files -n kodi-pvr-pctv
%{_libdir}/kodi/addons/pvr.pctv/
%{_datadir}/kodi/addons/pvr.pctv/

%files -n kodi-pvr-stalker
%{_libdir}/kodi/addons/pvr.stalker/
%{_datadir}/kodi/addons/pvr.stalker/

%files -n kodi-pvr-vbox
%{_libdir}/kodi/addons/pvr.vbox/
%{_datadir}/kodi/addons/pvr.vbox/


%changelog

* Wed Jun 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 18.0-5
- Updated to current commit

* Thu Apr 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 18.0-4
- Updated to current commit

* Wed Mar 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 18.0-2
- Rebuilt for tinyxml2

* Wed Mar 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 18.0-1
- Updated to 18.0

* Sun Oct 22 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 17.5-1
- Updated to 17.5

* Wed Oct 11 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 17.4-3
- Rebuilt for jsoncpp

* Fri Sep 01 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.4-2
- Rebuilt for Kodi cmake
- Xlocale patch

* Wed Jun 14 2017 Martin Janser <martin AT duss-janser DOT ch> - 17.2-2
- Removed USE_LTO flag to fix build

* Wed May 24 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.2-1
- Updated to 17.2-1

* Fri May 19 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.0-7
- Rebuilt

* Fri Mar 17 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.0-5
- Massive rebuild

* Mon Jan 16 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.0-4
- Kripton compatibility

* Tue Jan 10 2017 Pavlo Rudyi <paulcarroty at riseup.net> - 17.0-3
- Updated to the latest snapshot

* Sun Oct 16 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.0-2
- Massive rebuild

* Fri Aug 05 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.0-1
- Updated for compatibility with Krypton

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 16.1-5
- Massive rebuild

* Mon Jun 06 2016 David Vasquez <davidjeremias82 at gmail dot com> - 16.1-4
- Rebuilt thanks to tinyxml2-devel

* Sun May 15 2016 Sérgio Basto <sergio@serjux.com> - 16.1-3
- Build with a fix in all FindJsonCpp.cmake to compile against
  jsoncpp-1.7.2-1.fc24 from Fedore proper
  https://github.com/kodi-pvr/pvr.argustv/issues/57
  and remove the previous hack on jsoncpp.
- clean and retab spec file.

* Wed May 11 2016 David Vasquez <davidjeremias82 at gmail dot com> - 16.1-2
- Rebuilt with p8-platform from Fedora proper need backport some patches from upstream.

* Mon May 02 2016 David Vasquez <davidjeremias82 at gmail dot com> - 16.1-20160502-1
- Updated to 16.1-20160502

* Sat Mar 05 2016 David Vasquez <davidjeremias82 at gmail dot com> - 16.0-20160305-1
- Updated to 16.0-20160305

* Tue Oct 20 2015 David Vasquez <davidjeremias82 at gmail dot com> - 15.2-20151020-1
- Updated to 15.2-20151020

* Thu Sep 10 2015 David Vasquez <davidjeremias82 at gmail dot com> - 15.1-20150910-1
- Updated to 15.1-20150910

* Thu May 21 2015 David Vasquez <davidjeremias82 at gmail dot com> - 15.0-20150521-1
- Initial build rpm
