Summary:	Library for reading and writing quicktime files
Summary(pl):	Biblioteka do odczytu i zapisu plików quicktime
Name:		libquicktime
Version:	0.9.2
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libquicktime/%{name}-%{version}.tar.gz
# Source0-md5:	1b42ca12966526647fa9a1b14fb947a1
Patch0:		%{name}-what.patch
URL:		http://libquicktime.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	libavc1394-devel
BuildRequires:	libdv-devel
BuildRequires:	libjpeg-devel
#jpeg-mmx-devel
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
 
#%description -l pl

%package devel
Summary:	Header files for libquicktime library
Summary(pl):	Pliki nag³ówkowe biblioteki libquicktime
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libquicktime library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libquicktime.

%package static
Summary:	Static libquicktime library
Summary(pl):	Statyczna biblioteka libquicktime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libquicktime library.

%description static -l pl
Statyczna biblioteka libquicktime.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/foo
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
