# TODO:
#   * scripts from scripts/ subdirectory are not installed.
%define		_ver		3.0.1
#define		_sub_ver
%define		_rel		1

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	%{_version}
Release:	%{_release}
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	kdebase-devel = %{version}
BuildRequires:	gettext-devel
BuildRequires:	db4-devel
# kmtrace need /usr/lib/libiberty.a (path hardcoded into configure).
BuildRequires:	binutils-static
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_mandir		%{_prefix}/man

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package devel
Summary:	Header files for kdesdk
Summary(pl):	Pliki nag³ówkowe dla kdesdk
Group:		X11/Development/Libraries

%description devel
Header files for kdesdk.

%description devel -l pl
Pliki nag³ówkowe dla kdesdk.

%package static
Summary:	Static libraries for kdesdk
Summary(pl):	Statyczne biblioteki dla kdesdk
Group:		X11/Development/Libraries

%description static
Static libraries for kdesdk.

%description static -l pl
Statyczne biblioteki dla kdesdk.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi

%configure \
	--enable-nls \
	--with-db-name=db3 \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%

gzip -9fn README

%find_lang cervisia --with-kde
%find_lang kbabel --with-kde

cat {cervisia,kbabel}.lang > kdesdk.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdesdk.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/*/*
%{_applnkdir}/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/apps/*
%{_pixmapsdir}/*/*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/lib*so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
