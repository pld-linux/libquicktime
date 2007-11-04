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
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu plików quicktime
Name:		libquicktime
Version:	1.0.1
Release:	1
%if %{with gpl}
License:	GPL v2+
%else
License:	LGPL v2.1+
%endif
Group:		Libraries
Source0:	http://dl.sourceforge.net/libquicktime/%{name}-%{version}.tar.gz
# Source0-md5:	3146ef9f88ea6a887658ceadac317997
URL:		http://libquicktime.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
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
# pkgconfig: x264 >= 0.48
BuildRequires:	libx264-devel >= 0.1.2-1.20060828_2245
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXv-devel
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

%description -l pl.UTF-8
libquicktime to biblioteka do odczytu i zapisu plików quicktime. Jest
oparta na bibliotece quicktime4linux z następującymi zmianami:
- drzewo źródeł zostało przerobione na używanie
  autoconfa/automake'a/libtola itp. narzędzi, tak jak w standardowych
  bibliotekach linuksowych
- wszystkie zewnętrzne biblioteki (jpeg, OggVorbis) zostały usunięte w
  celu zmniejszenia ilości danych do ściągania, czasu kompilacji i
  powielonego kodu na dyskach użytkowników; zamiast tego używane są
  biblioteki systemowe
- wszystkie kodeki zostały przeniesione do dynamicznie ładowanych
  modułów; pozwala to rozprowadzać kodeki bez źródeł (lub kodeki z
  niekompatybilnymi licencjami) jako osobne pakiety
- w przeciwieństwie do innych bibliotek quicktime jest źródłowo
  kompatybilna z quicktime4linux; programy takie jak cinelerra czy
  xmovie mogą być kompilowane z libquicktime
- kodeki także są źródłowo kompatybilne z quicktime4linux, więc
  przenoszenie kodeków pomiędzy quicktime4linux i libquicktime nie
  wymaga zbyt wiele pracy
- dodano specjalne rozszerzenia API pozwalające na dostęp do rejestru
  kodeków; aplikacje mogą pobierać ważne informacje o kodekach, ich
  parametry itp. w czasie działania aplikacji.

%package devel
Summary:	Header files for libquicktime library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libquicktime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel
Obsoletes:	quicktime4linux-devel

%description devel
Header files for libquicktime library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libquicktime.

%package static
Summary:	Static libquicktime library
Summary(pl.UTF-8):	Statyczna biblioteka libquicktime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	quicktime4linux-static

%description static
Static libquicktime library.

%description static -l pl.UTF-8
Statyczna biblioteka libquicktime.

%package utils
Summary:	libquicktime utilities
Summary(pl.UTF-8):	Narzędzia do libquicktime
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description utils
libquicktime utilities.

%description utils -l pl.UTF-8
Narzędzia do libquicktime.

%package dv
Summary:	DV plugin for libquicktime
Summary(pl.UTF-8):	Wtyczka DV dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description dv
DV plugin for libquicktime.

%description dv -l pl.UTF-8
Wtyczka DV dla libquicktime.

%package faac
Summary:	faac plugin for libquicktime
Summary(pl.UTF-8):	Wtyczka faac dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description faac
faac plugin for libquicktime.

%description faac -l pl.UTF-8
Wtyczka faac dla libquicktime.

%package faad2
Summary:	faad2 plugin for libquicktime
Summary(pl.UTF-8):	Wtyczka faad2 dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description faad2
faad2 plugin for libquicktime.

%description faad2 -l pl.UTF-8
Wtyczka faad2 dla libquicktime.

%package ffmpeg
Summary:	ffmpeg plugin for libquicktime
Summary(pl.UTF-8):	Wtyczka ffmpeg dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ffmpeg
ffmpeg plugin for libquicktime.

%description ffmpeg -l pl.UTF-8
Wtyczka ffmpeg dla libquicktime.

%package lame
Summary:	lame plugin for libquicktime
Summary(pl.UTF-8):	Wtyczka lame dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description lame
lame plugin for libquicktime.

%description lame -l pl.UTF-8
Wtyczka lame dla libquicktime.

%package vorbis
Summary:	Ogg Vorbis plugin for libquicktime
Summary(pl.UTF-8):	Wtyczka Ogg Vorbis dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description vorbis
Ogg Vorbis plugin for libquicktime.

%description vorbis -l pl.UTF-8
Wtyczka Ogg Vorbis dla libquicktime.

%package x264
Summary:	X264 plugin for libquicktime
Summary(pl.UTF-8):	Wtyczka X264 dla libquicktime
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libx264 >= 0.1.2-1.20060430_2245

%description x264
X264 plugin for libquicktime.

%description x264 -l pl.UTF-8
Wtyczka X264 dla libquicktime.

%prep
%setup -q

# evil, sets CFLAGS basing on /proc/cpuinfo, overrides our optflags
# (--with-cpuflags=none disables using /proc/cpuinfo, but not overriding)
sed -i -e '19,$d;18aAC_DEFUN([LQT_OPT_CFLAGS],[OPT_CFLAGS="$CFLAGS"])' m4/lqt_opt_cflags.m4

%build
touch config.rpath
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
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
