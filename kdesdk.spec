# TODO:
#   * scripts from scripts/ subdirectory are not installed.
#   * separate aplications do subpackages
Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	3.0.3
Release:	2
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-fix-kbabel-mem-leak.patch
BuildRequires:	binutils-static
BuildRequires:	bison
BuildRequires:	db3-devel
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel = %{version}
# required by kbabel:
Requires:	gettext-devel
# kmtrace need /usr/lib/libiberty.a (path hardcoded into configure).
Requires:	kdelibs = %{version}
Requires:	%{name}-extractrc = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kbabel
Obsoletes:	kless

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_mandir		%{_prefix}/man

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package extractrc
Summary:	extracts the strings from .rc files
Summary(pl):	odnajduje stringi w plikach .rc
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description extractrc
A Perl script, it extracts the strings in an application´s .rc file,
e.g. testappui.rc, and writes into the pot file where the translations
are build with (po-files)

%description extractrc -l pl
Skrypt napisany w Perlu, który odnajduje stringi w plikach .rc aplikacji,
np. testappgui.rc i zapisuje je do plików pot

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
Group:		X11/Development/Tools

%description static
Static libraries for kdesdk.

%description static -l pl
Statyczne biblioteki dla kdesdk.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-nls \
	--with-db-name=db3 \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang cervisia	--with-kde
%find_lang gideon	--with-kde
%find_lang kbabel	--with-kde
%find_lang kbabeldict	--with-kde
%find_lang kbugbuster	--with-kde
%find_lang kdevtipofday	--with-kde
%find_lang kompare	--with-kde
%find_lang kstartperf	--with-kde
%find_lang spy		--with-kde

cat {cervisia,gideon,kbabel,kbabeldict,kbugbuster,kdevtipofday,kompare,kstartperf,spy}.lang > kdesdk.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kdesdk.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/[!e]*
%attr(755,root,root) %{_bindir}/extend_dmalloc
%attr(755,root,root) %{_libdir}/kde3/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/*/*
%{_applnkdir}/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/apps/*
%{_pixmapsdir}/*/*/*

%files extractrc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extractrc

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/lib*so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
