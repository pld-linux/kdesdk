# TODO:
#   * scripts from scripts/ subdirectory are not installed.
Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	2.2.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdebase-devel = %{version}
BuildRequires:	gettext-devel
BuildRequires:	db2-devel
# kmtrace need /usr/lib/libiberty.a (path hardcoded into configure).
BuildRequires:	binutils-static
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
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
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-nls \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

gzip -9fn README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde2/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
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
