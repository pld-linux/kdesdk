# TODO:
#   * scripts from scripts/ subdirectory are not installed.
#   * separate aplications do subpackages
#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
%define		_with_pixmapsubdirs	1
Summary:	KDESDK - Software Development Kit for KDE
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - ¼ÒÇÁÆ®¿þ¾î °³¹ß µµ±¸ ¸ðÀ½
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	3.0.5a
Release:	0.3
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	%{name}-extra_icons.tar.bz2
Patch0:		%{name}-fix-kbabel-mem-leak.patch
Patch1:		%{name}-fix-kbabel-crash.patch
Patch2:		%{name}-glibc.patch
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
Provides:	kbabel
Provides:	kless
# It's named compare now:
Provides:	kdiff
Provides:	kdiff2
Obsoletes:	kdiff
Obsoletes:	kdiff2
Obsoletes:	kbabel
Obsoletes:	kless
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

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
Requires:	%{name} = %{version}

%description devel
Header files for kdesdk.

%description devel -l pl
Pliki nag³ówkowe dla kdesdk.

%package static
Summary:	Static libraries for kdesdk
Summary(pl):	Statyczne biblioteki dla kdesdk
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{version}

%description static
Static libraries for kdesdk.

%description static -l pl
Statyczne biblioteki dla kdesdk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1	- needs update

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

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

# create in toplevel %%{_pixmapsdir} links to icons
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{catalogmanager,kbabel}.png
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}	
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}

%if %{!?_with_pixmapsubdirs:1}%{?_with_pixmapsubdirs:0}
# moved
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{catalogmanager,kbabel}.png \
# resized
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{cervisia,kbabeldict,kompare}.png
%endif

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

%find_lang cervisia	--with-kde
%find_lang gideon	--with-kde
%find_lang kbabel	--with-kde
%find_lang kbabeldict	--with-kde
%find_lang kbugbuster	--with-kde
%find_lang kdevtipofday	--with-kde
%find_lang kompare	--with-kde
%find_lang kstartperf	--with-kde
%find_lang spy		--with-kde

cat {cervisia,gideon,kbabel,kbabeldict,kdevtipofday,kompare,kstartperf,spy}.lang > kdesdk.lang

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
%{_libdir}/lib*.la
%{_mandir}/man1/[^etk]*
%{_mandir}/man1/extend_dmalloc*
%{_mandir}/man1/transxx*
%{_mandir}/man1/kba*
%{_mandir}/man1/k[^b]*
%{_applnkdir}/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/apps/*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*/*/*/*.png

%files extractrc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extractrc
%{_mandir}/man1/extractrc*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/lib*so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
