# TODO
# - libavcodec: Missing
Summary:	Library for reading and writing quicktime files
Summary(pl):	Biblioteka do odczytu i zapisu plików quicktime
Name:		libquicktime
Version:	0.9.7
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libquicktime/%{name}-%{version}.tar.gz
# Source0-md5:	e5c977567df59c876c50ac191bb1caf6
URL:		http://libquicktime.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	automake
# avcodec-acl = 0.4.8acl ???
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	lame-libs-devel
BuildRequires:	libavc1394-devel >= 0.3.1
BuildRequires:	libdv-devel
BuildRequires:	libjpeg-devel
# jpeg-mmx-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw1394-devel >= 0.9
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libquicktime is a library for reading and writing quicktime files. It
is based on the quicktime4linux library, with the following
extensions:
- Sourcetree upgraded with autoconf/automake/libtool and all the other
  stuff, people like in "standard" linux libraries.
- All 3rd party libraries (jpeg, OggVorbis) were removed to reduce
  download size, compilation time and code duplication on users
  harddisks. Instead, the sytemwide installed libraries are used.
- All codecs have been moved into dynamically loadable modules. This
  makes it possible to distribute closed source codecs (or codecs with
  an incompatible license) as separate packages.
- Unlike other quicktime libraries, it's source compatible with
  quicktime4linux. Programs like cinelerra or xmovie can be compiled
  with libquicktime.
- The codecs themselves are also source compatible with
  quicktime4linux, so porting codecs between quicktime4linux and
  libquicktime requires only little brain load.
- Special API extensions allow access to the codec registry.
  Applications can get important information about the codecs, their
  settable parameters etc. at runtime.

%package devel
Summary:	Header files for libquicktime library
Summary(pl):	Pliki nag³ówkowe biblioteki libquicktime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libquicktime library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libquicktime.

%package static
Summary:	Static libquicktime library
Summary(pl):	Statyczna biblioteka libquicktime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libquicktime library.

%description static -l pl
Statyczna biblioteka libquicktime.

%package utils
Summary:	libquicktime utilities
Summary(pl):	Narzêdzia do libquicktime
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description utils
libquicktime utilities.

%description utils -l pl
Narzêdzia do libquicktime.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libquicktime/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/lqtvrplay
# R: glib, zlib
%attr(755,root,root) %{_libdir}/libquicktime.so.*.*.*
# R: libdv, libraw1394, libavc1394
%attr(755,root,root) %{_libdir}/libquicktime1394.so.*.*.*
%dir %{_libdir}/libquicktime
%attr(755,root,root) %{_libdir}/libquicktime/lqt_audiocodec.so
# R: libdv
%attr(755,root,root) %{_libdir}/libquicktime/lqt_dv.so
# R: avcodec-acl
#%attr(755,root,root) %{_libdir}/libquicktime/lqt_ffmpeg.so
# R: lame-libs
%attr(755,root,root) %{_libdir}/libquicktime/lqt_lame.so
# R: libjpeg
%attr(755,root,root) %{_libdir}/libquicktime/lqt_mjpeg.so
%attr(755,root,root) %{_libdir}/libquicktime/lqt_opendivx.so
# R: libpng
%attr(755,root,root) %{_libdir}/libquicktime/lqt_png.so
%attr(755,root,root) %{_libdir}/libquicktime/lqt_rtjpeg.so
%attr(755,root,root) %{_libdir}/libquicktime/lqt_videocodec.so
# R: libogg, libvorbis
%attr(755,root,root) %{_libdir}/libquicktime/lqt_vorbis.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lqt-config
%attr(755,root,root) %{_libdir}/libquicktime.so
%attr(755,root,root) %{_libdir}/libquicktime1394.so
%{_libdir}/libquicktime.la
%{_libdir}/libquicktime1394.la
%{_includedir}/lqt
%{_aclocaldir}/lqt.m4
%{_libdir}/pkgconfig/libquicktime.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libquicktime.a
%{_libdir}/libquicktime1394.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libquicktime_config
%attr(755,root,root) %{_bindir}/lqtplay
%attr(755,root,root) %{_bindir}/lqt_transcode
%attr(755,root,root) %{_bindir}/qt*
%{_mandir}/man1/lqtplay.1*
