#
# Conditional build:
%bcond_with	mmx	# use MMX in rtjpeg plugin
#
%ifarch athlon pentium3 pentium4 %{x8664}
%define	with_mmx	1
%endif
# TODO
# - libavcodec: Missing (ffmpeg?)
Summary:	Library for reading and writing quicktime files
Summary(pl):	Biblioteka do odczytu i zapisu plików quicktime
Name:		libquicktime
Version:	0.9.7
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libquicktime/%{name}-%{version}.tar.gz
# Source0-md5:	e5c977567df59c876c50ac191bb1caf6
Patch0:		%{name}-link.patch
URL:		http://libquicktime.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
# avcodec-acl = 0.4.8acl ???
BuildRequires:	ffmpeg-devel
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
BuildRequires:	zlib-devel
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
libquicktime to biblioteka do odczytu i zapisu plików quicktime. Jest
oparta na bibliotece quicktime4linux z nastêpuj±cymi zmianami:
- drzewo ¼róde³ zosta³o przerobione na u¿ywanie
  autoconfa/automake'a/libtola itp. narzêdzi, tak jak w standardowych
  bibliotekach linuksowych
- wszystkie zewnêtrzne biblioteki (jpeg, OggVorbis) zosta³y usuniête w
  celu zmniejszenia ilo¶ci danych do ¶ci±gania, czasu kompilacji i
  powielonego kodu na dyskach u¿ytkowników; zamiast tego u¿ywane s±
  biblioteki systemowe
- wszystkie kodeki zosta³y przeniesione do dynamicznie ³adowanych
  modu³ów; pozwala to rozprowadzaæ kodeki bez ¼róde³ (lub kodeki z
  niekompatybilnymi licencjami) jako osobne pakiety
- w przeciwieñstwie do innych bibliotek quicktime jest ¼ród³owo
  kompatybilna z quicktime4linux; programy takie jak cinelerra czy
  xmovie mog± byæ kompilowane z libquicktime
- kodeki tak¿e s± ¼ród³owo kompatybilne z quicktime4linux, wiêc
  przenoszenie kodeków pomiêdzy quicktime4linux i libquicktime nie
  wymaga zbyt wiele pracy
- dodano specjalne rozszerzenia API pozwalaj±ce na dostêp do rejestru
  kodeków; aplikacje mog± pobieraæ wa¿ne informacje o kodekach, ich
  parametry itp. w czasie dzia³ania aplikacji.

%package devel
Summary:	Header files for libquicktime library
Summary(pl):	Pliki nag³ówkowe biblioteki libquicktime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel

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
%patch0 -p1

# evil, sets CFLAGS basing on /proc/cpuinfo
echo 'AC_DEFUN([LQT_OPT_CFLAGS],[OPT_CFLAGS="$CFLAGS"])' > m4/lqt_opt_cflags.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
%attr(755,root,root) %{_bindir}/lqtvrplay
# R: glib, zlib
%attr(755,root,root) %{_libdir}/libquicktime.so.*.*.*
# R: libdv, libraw1394, libavc1394
%attr(755,root,root) %{_libdir}/libquicktime1394.so.*.*.*
%dir %{_libdir}/libquicktime
%attr(755,root,root) %{_libdir}/libquicktime/lqt_audiocodec.so
# R: libdv
%attr(755,root,root) %{_libdir}/libquicktime/lqt_dv.so
# R: avcodec-acl (ffmpeg?)
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
%{_pkgconfigdir}/libquicktime.pc

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
