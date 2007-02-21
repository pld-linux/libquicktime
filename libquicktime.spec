#
# Conditional build:
%bcond_with	mmx	# use MMX in rtjpeg plugin (no runtime detection)
%bcond_without	ffmpeg	# ffmpeg plugin
%bcond_without	gpl	# build LGPL library (disables some plugins)
#
%ifarch athlon pentium3 pentium4 %{x8664}
%define		with_mmx	1
%endif
Summary:	Library for reading and writing quicktime files
Summary(pl):	Biblioteka do odczytu i zapisu plik�w quicktime
Name:		libquicktime
Version:	0.9.10
Release:	2
%if %{with gpl}
License:	GPL
%else
License:	LGPL
%endif
Group:		Libraries
Source0:	http://dl.sourceforge.net/libquicktime/%{name}-%{version}.tar.gz
# Source0-md5:	5ff99f1a7b22f9e1ed85240f736fd14c
Patch0:		%{name}-link.patch
Patch1:		%{name}-x264.patch
URL:		http://libquicktime.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%if %{with gpl}
BuildRequires:	faac-devel >= 1.24
BuildRequires:	faad2-devel >= 2.0
%endif
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.4.9-3.20051020}
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	lame-libs-devel >= 3.93
BuildRequires:	libavc1394-devel >= 0.3.1
BuildRequires:	libdv-devel >= 0.102
BuildRequires:	libjpeg-devel >= 6b
# jpeg-mmx-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libraw1394-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
# pkgconfig: x264 >= 0.45
BuildRequires:	libx264-devel >= 0.1.2-1.20060828_2245
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Obsoletes:	libquicktime-firewire
Obsoletes:	libquicktime-firewire-devel
Obsoletes:	libquicktime-firewire-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libquicktime is a library for reading and writing quicktime files. It
is based on the quicktime4linux library, with the following
extensions:
- Sourcetree upgraded with autoconf/automake/libtool and all the other
  stuff, people like in "standard" Linux libraries.
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

%description -l pl
libquicktime to biblioteka do odczytu i zapisu plik�w quicktime. Jest
oparta na bibliotece quicktime4linux z nast�puj�cymi zmianami:
- drzewo �r�de� zosta�o przerobione na u�ywanie
  autoconfa/automake'a/libtola itp. narz�dzi, tak jak w standardowych
  bibliotekach linuksowych
- wszystkie zewn�trzne biblioteki (jpeg, OggVorbis) zosta�y usuni�te w
  celu zmniejszenia ilo�ci danych do �ci�gania, czasu kompilacji i
  powielonego kodu na dyskach u�ytkownik�w; zamiast tego u�ywane s�
  biblioteki systemowe
- wszystkie kodeki zosta�y przeniesione do dynamicznie �adowanych
  modu��w; pozwala to rozprowadza� kodeki bez �r�de� (lub kodeki z
  niekompatybilnymi licencjami) jako osobne pakiety
- w przeciwie�stwie do innych bibliotek quicktime jest �r�d�owo
  kompatybilna z quicktime4linux; programy takie jak cinelerra czy
  xmovie mog� by� kompilowane z libquicktime
- kodeki tak�e s� �r�d�owo kompatybilne z quicktime4linux, wi�c
  przenoszenie kodek�w pomi�dzy quicktime4linux i libquicktime nie
  wymaga zbyt wiele pracy
- dodano specjalne rozszerzenia API pozwalaj�ce na dost�p do rejestru
  kodek�w; aplikacje mog� pobiera� wa�ne informacje o kodekach, ich
  parametry itp. w czasie dzia�ania aplikacji.

%package devel
Summary:	Header files for libquicktime library
Summary(pl):	Pliki nag��wkowe biblioteki libquicktime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel
Obsoletes:	quicktime4linux-devel

%description devel
Header files for libquicktime library.

%description devel -l pl
Pliki nag��wkowe biblioteki libquicktime.

%package static
Summary:	Static libquicktime library
Summary(pl):	Statyczna biblioteka libquicktime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	quicktime4linux-static

%description static
Static libquicktime library.

%description static -l pl
Statyczna biblioteka libquicktime.

%package utils
Summary:	libquicktime utilities
Summary(pl):	Narz�dzia do libquicktime
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description utils
libquicktime utilities.

%description utils -l pl
Narz�dzia do libquicktime.

%package dv
Summary:	DV plugin for libquicktime
Summary(pl):	Wtyczka DV dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description dv
DV plugin for libquicktime.

%description dv -l pl
Wtyczka DV dla libquicktime.

%package faac
Summary:	faac plugin for libquicktime
Summary(pl):	Wtyczka faac dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description faac
faac plugin for libquicktime.

%description faac -l pl
Wtyczka faac dla libquicktime.

%package faad2
Summary:	faad2 plugin for libquicktime
Summary(pl):	Wtyczka faad2 dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description faad2
faad2 plugin for libquicktime.

%description faad2 -l pl
Wtyczka faad2 dla libquicktime.

%package ffmpeg
Summary:	ffmpeg plugin for libquicktime
Summary(pl):	Wtyczka ffmpeg dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ffmpeg
ffmpeg plugin for libquicktime.

%description ffmpeg -l pl
Wtyczka ffmpeg dla libquicktime.

%package lame
Summary:	lame plugin for libquicktime
Summary(pl):	Wtyczka lame dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description lame
lame plugin for libquicktime.

%description lame -l pl
Wtyczka lame dla libquicktime.

%package vorbis
Summary:	Ogg Vorbis plugin for libquicktime
Summary(pl):	Wtyczka Ogg Vorbis dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description vorbis
Ogg Vorbis plugin for libquicktime.

%description vorbis -l pl
Wtyczka Ogg Vorbis dla libquicktime.

%package x264
Summary:	X264 plugin for libquicktime
Summary(pl):	Wtyczka X264 dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libx264 >= 0.1.2-1.20060430_2245

%description x264
X264 plugin for libquicktime.

%description x264 -l pl
Wtyczka X264 dla libquicktime.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# evil, sets CFLAGS basing on /proc/cpuinfo, overrides our optflags
# (--with-cpuflags=none disables using /proc/cpuinfo, but not overriding)
echo 'AC_DEFUN([LQT_OPT_CFLAGS],[OPT_CFLAGS="$CFLAGS"])' > m4/lqt_opt_cflags.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_gpl:--enable-gpl} \
	%{!?with_mmx:--disable-mmx} \
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
# R: zlib
%attr(755,root,root) %{_libdir}/libquicktime.so.*.*.*
%dir %{_libdir}/libquicktime
%attr(755,root,root) %{_libdir}/libquicktime/lqt_audiocodec.so
# R: libjpeg
%attr(755,root,root) %{_libdir}/libquicktime/lqt_mjpeg.so
# R: libpng
%attr(755,root,root) %{_libdir}/libquicktime/lqt_png.so
%attr(755,root,root) %{_libdir}/libquicktime/lqt_rtjpeg.so
%attr(755,root,root) %{_libdir}/libquicktime/lqt_videocodec.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lqt-config
%attr(755,root,root) %{_libdir}/libquicktime.so
%{_libdir}/libquicktime.la
%{_includedir}/lqt
%{_aclocaldir}/lqt.m4
%{_pkgconfigdir}/libquicktime.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libquicktime.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libquicktime_config
%attr(755,root,root) %{_bindir}/lqtplay
%attr(755,root,root) %{_bindir}/lqt_transcode
%attr(755,root,root) %{_bindir}/qt*
%{_mandir}/man1/lqtplay.1*

%files dv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquicktime/lqt_dv.so

%if %{with gpl}
%files faac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquicktime/lqt_faac.so

%files faad2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquicktime/lqt_faad2.so
%endif

%if %{with ffmpeg}
%files ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquicktime/lqt_ffmpeg.so
%endif

%files lame
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquicktime/lqt_lame.so

%files vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquicktime/lqt_vorbis.so

%files x264
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquicktime/lqt_x264.so
