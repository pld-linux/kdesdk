
%define		_state		snapshots
%define		_ver		3.1.94
%define		_snap		040110

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		3
License:	GPL
Group:		X11/Development/Tools
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	593d80099430fad6fe8e75c3d38b6aa0	
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
BuildRequires:	kdebase-devel >= 9:%{version}
BuildRequires:	libltdl-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdesdk-devel

%define		_gimpdir	%(gimptool --gimpdatadir)
%define		_appdefdir	/usr/X11R6/lib/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/21.2
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package cervisia
Summary:	A KDE cvs frontend
Summary(pl):	Frontend CVS pod KDE
Group:		X11/Development/Tools
Requires:	cvs >= 1.10
Obsoletes:	%{name}-devel

%description cervisia
A KDE cvs frontend.

%description cervisia -l pl
Frontend CVS pod KDE.

%package cervisia-devel
Summary:	A KDE cvs frontend - header files
Summary(pl):	Frontend CVS pod KDE - pliki nag³ówkowe
Group:		X11/Development
Obsoletes:	%{name}-devel

%description cervisia-devel
A KDE cvs frontend. This package contains header files.

%description cervisia-devel -l pl
Frontend CVS pod KDE. Ten pakiet zawiera pliki nag³ówkowe.

%package completions-bash
Summary:	Autocomplete definitions for bash
Summary(pl):	Definicje autouzupe³niania dla basha
Group:		Applications/Shells
Requires:	bash-completion
Obsoletes:	%{name}-devel

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl
Definicje autouzupe³niania dla basha.

%package completions-zsh
Summary:	Autocomplete definitions for zsh
Summary(pl):	Definicje autouzupe³niania dla zsh
Group:		Applications/Shells
Requires:	zsh >= 4.0.6-2
Obsoletes:	%{name}-devel

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl
Definicje autouzupe³niania dla zsh.

%package emacs
Summary:	A set of macros for emacs
Summary(pl):	Zestaw makr do emacsa
Group:		X11/Development/Tools
Requires: 	emacs-common
Obsoletes:	%{name}-devel

%description emacs
A set of macros for emacs.

%description emacs -l pl
Zestaw makr do emacsa.

%package kaddressbook-kdeaccounts
Summary:	A kdeaccounts plugin for the KDE adressbook
Summary(pl):	Wtyczka do ksi±¿ki adresowej KDE dodaj±ca obs³ugê kdeaccounts
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8
Obsoletes:	%{name}-devel

%description kaddressbook-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. What is does is adding
the people from KDE's CVS accounts file to the addressbook.

%description kaddressbook-kdeaccounts -l pl
Wtyczka do ksi±¿ki adresowej KDE dodaj±ca obs³ugê kdeaccounts. Dodaje
ona osoby posiadaj±ce konta w CVS KDE do ksi±¿ki adresowej.

%package kapptemplate
Summary:	KDE application framework generator
Summary(pl):	Generator szkieletu dla aplikacji KDE
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kapptemplate
Modular shell script that will automatically create a framework for
either a normal KDE 3.x application, a KPart application, a KPart
plugin, or convert an existing application.

%description kapptemplate -l pl
Modularny skrypt, który potrafi automatycznie wygenerowaæ szkielet
katalogów dla zwyk³ej aplikacji pod KDE 3.x, aplikacji KPart, wtyczki
KPart lub skonwertowaæ istniej±c± aplikacjê.

%package kbabel
Summary:	An advanced and easy to use PO-file editor
Summary(pl):	Rozbudowany i ³atwy w obs³udze edytor plików PO
Group:		X11/Development/Tools
Requires:	gettext-devel
Obsoletes:	%{name}-devel

%description kbabel
KBabel is a tool, that allows easy management, edition and upkeep of
gettext .po files.

%description kbabel -l pl
KBabel jest narzêdziem, które pozwala na ³atwe zarz±dzanie, edycjê i
utrzymanie plików po.

%package kbabel-devel
Summary:	Kbabel headers
Summary(pl):	Pliki nag³ówkowe KBabel
Group:		X11/Development
Requires:	gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Requires:	%{name}-kbabel-catalog = %{epoch}:%{version}-%{release}
Requires:	%{name}-kbabel-dictionary = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-devel

%description kbabel-devel
KBabel headers.

%description kbabel-devel -l pl
Pliki nag³ówkowe KBabel.

%package kbabel-catalog
Summary:	A KBabel catalog manager
Summary(pl):	Zarz±dca zbiorów plików po zintegrowany z KBabel
Group:		X11/Development
Requires:	gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-devel

%description kbabel-catalog
A KBabel catalog manager.

%description kbabel-catalog -l pl
Zarz±dca zbiorów plików po zintegrowany z KBabel.

%package kbabel-dictionary
Summary:	Plugin that supports dictionaries made from po compendia
Summary(pl):	Wtyczka kbabel obs³uguj±ca s³owniki z kompendiów po
Group:		X11/Development
Requires:	gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-devel

%description kbabel-dictionary
Plugin that supports dictionaries made from po compendia.

%description kbabel-dictionary -l pl
Wtyczka kbabel obs³uguj±ca s³owniki z kompendiów po.

%package kbugbuster
Summary:	A tools that allows cooperation with bugs.kde.org
Summary(pl):	Narzêdzie wspó³pracuj±ce z bugs.kde.org
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kbugbuster
KBugBuster allows easy bug management on bugs.kde.org.

%description kbugbuster -l pl
KBugBuster u³atwia wyszukwianie i zarz±dzanie b³êdami na bugs.kde.org.

%package kcachegrind
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kcachegrind
TODO.

%description kcachegrind -l pl
TODO.

%package kmtrace
Summary:	A mtrace to full backtrace conversion tool
Summary(pl):	Narzêdzie do konwersji z mtrace do pe³nego backtrace'a
Group:		X11/Development/Tools
BuildRequires:	binutils-static
Obsoletes:	%{name}-devel

%description kmtrace
Converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl
Konwertuje mtrace glibca do pe³nego backtrace'a.

%package kompare
Summary:	Kompare is a program to view the differences between files
Summary(pl):	Kompare to program s³u¿±cy do porównywania zmian miêdzy plikami
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kompare
Kompare is a program to view the differences between files. Features
include:

  * comparison of files or directories via a graphical interface
  * bezier-based connection widget lets you see both source and destination
    as they really appear
  * graphical viewing of patch files in normal, context, unified and
    diff formats
  * interactive application of differences
  * full network transparency
  * ability to view plain-text diff output in embedded viewer
  * easy navigation of multiple-file diffs with dockable navigation tree
  * graphical interface to commonly used diff command line options
  * switch source and destination with one command
  * diff statistics

%description kompare -l pl
Kompare to program s³u¿±cy do porównywania zmian miêdzy plikami.
Aktualnie dostêpne funkcje:
  * porównanie plików lub katalogów poprzez graficzny interfejs
  * przedstawienie ¼ród³a i celu za pomoc± krzywej Beziera
  * graficzne przegl±danie ³at w formatach diff, unidiff, context i
    zwyk³ym
  * interaktywne wprowadzanie zmian
  * przezroczysto¶æ sieciowa
  * mo¿liwo¶æ ogl±dania wyj¶cia diff w wewnêtrznej przegl±darce
  * ³atwa nawigacja miêdzy wieloplikowymi diffami wraz z dokowalnym drzewem
  * zamiana ¼ród³a i celu za pomoc± pojedynczej komendy
  * statystyki diffów

%package kprofilemethod
Summary:	Kprofilemethod is a set of macros which help profiling using QTime
Summary(pl):	Kprofilemethod to zestaw makr u³atwiaj±cych profilowanie z wykorzystaniem QTime
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kprofilemethod
Kprofilemethod is a set of macros which help profiling using QTime.

%description kprofilemethod -l pl
Kprofilemethod to zestaw makr u³atwiaj±cych profilowanie z
wykorzystaniem QTime.

%package kspy
Summary:	A utility for egzamining the internal state of a QT/KDE application.
Summary(pl):	Narzêdzie do badania stanu aplikacji QT/KDE
Group:		X11/Development/Tools
Obsoletes:	kdiff
Obsoletes:	kdiff2
Obsoletes:	%{name}-devel

%description kspy
KSpy is a utility intended to help developers examine the internal
state of a Qt/KDE application. KSpy graphically displays all the
QObjects in use, and allows you to browse their properties. Using KSpy
is very simple, include kspy.h and call KSpy::invoke() when you want
to looks inside your app. The KSpy function is inline and the main
part of KSpy is dynamically loaded, so you may even want to leave this
in the release build of an application.

%description kspy -l pl
KSpy to narzêdzie maj±ce u³atwiæ programistom badanie wewnêtrznego
stanu aplikacji QT/KDE. KSpy ilustruje graficznie wszystkie QObjects
jakie s± w u¿yciu i pozwala na ³atwe przegl±danie ich w³a¶ciwo¶ci.
Korzystanie z KSpy jest bardzo proste (wystarczy do³±czyæ plik kspy.h
i wywo³aæ KSpy::invoke() w miejscu, które chcemy obejrzeæ w naszej
aplikacji. Funkcja KSpy jest inline, wiêc mo¿na zostawiæ j± nawet w
wydaniu stabilnym.

%package kstartperf
Summary:	A tool to measure startup time for KDE applications
Summary(pl):	Narzêdzie s³u¿±ce do pomiaru czasu ³adowania aplikacji KDE
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl
Narzêdzie s³u¿±ce do pomiaru czasu ³adowania aplikacji KDE.

%package kuiviewer
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools

%description kuiviewer
TODO.

%description kuiviewer -l pl
TODO.

%package pallette-gimp
Summary:	Adds the KDE Default pallette to GIMP
Summary(pl):	Dodaje domy¶ln± paletê kolorów KDE do GIMP-a
Group:		X11/Applications/Graphics
Requires:	gimp
Obsoletes:	%{name}-devel

%description pallette-gimp
Adds the KDE Default pallette to GIMP.

%description pallette-gimp -l pl
Dodaje domy¶ln± paletê kolorów KDE do GIMP-a.

%package pallette-xpaint
Summary:	Adds the KDE Default pallette to XPaint
Summary(pl):	Dodaje domy¶ln± paletê kolorów KDE do XPainta
Group:		X11/Applications/Graphics
Requires:	xpaint
Obsoletes:	%{name}-devel

%description pallette-xpaint
Adds the KDE Default pallette to XPaint.

%description pallette-xpaint -l pl
Dodaje domy¶ln± paletê kolorów KDE do XPainta.

%package po2xml
Summary:	An xml2po and vice versa converters
Summary(pl):	Konwertery po2xml i vice versa
Group:		X11/Development/Tools
Requires:	/usr/bin/python
Obsoletes:	%{name}-devel

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl
Konwertery po2xml i vice versa.

%package scripts-build
Summary:	An set of scripts useful for building KDE
Summary(pl):	Zestaw skryptów do kompilowania KDE
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-build
A set of scripts useful for building KDE.

%description scripts-build -l pl
Zestaw skryptów do kompilowania KDE.

%package scripts-cxxmetric
Summary:	Statistic meter for c/c++ files
Summary(pl):	Plik do tworzenia statystyki plików c/c++
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-cxxmetric
Counts lines of code, comments and blank space in C and C++ source
files.

%description scripts-cxxmetric -l pl
Zlicza linijki kodu, komentarzy i znaków bia³ych w plikach ¼ród³owych
C i C++.

%package scripts-cvs
Summary:	A set of scripts for maintaining KDE from CVS
Summary(pl):	Zestaw skryptów do zarz±dzania KDE z CVS
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-cvs
A set of scripts for maintaining KDE from CVS.

%description scripts-cvs -l pl
Zestaw skryptów do zarz±dzania KDE z CVS.

%package scripts-doc
Summary:	A set of scripts for quick access to qt/KDE documentation
Summary(pl):	Zestaw skryptów szybkiego dostêpu do dokumentacji qt/KDE
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-doc
A set of scripts for quick access to qt/KDE documentation.

%description scripts-doc -l pl
Zestaw skryptów szybkiego dostêpu do dokumentacji qt/KDE.

%package scripts-extractrc
Summary:	Extracts the strings from .rc files
Summary(pl):	Wyci±ga ³añcuchy z plików .rc
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-extractrc
Obsoletes:	%{name}-devel

%description scripts-extractrc
A Perl script, it extracts the strings in an application's .rc file,
e.g. testappui.rc, and writes into the pot file where the translations
are build with (po-files).

%description scripts-extractrc -l pl
Skrypt napisany w Perlu, który wyci±ga ³añcuchy z plików .rc
aplikacji, np. testappgui.rc i zapisuje je do plików pot, z których
tworzy siê t³umaczenia (pliki po).

%package scripts-findmissingcrystal
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools

%description scripts-findmissingcrystal
TODO.

%description scripts-findmissingcrystal -l pl
TODO.

%package scripts-kdekillall
Summary:	A script for killing KDE apps started with kdeinit
Summary(pl):	Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-kdekillall
A script for killing KDE apps started with kdeinit.

%description scripts-kdekillall -l pl
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scripts-kdelnk2desktop
Summary:	A kdelnk to desktop converter
Summary(pl):	Konwerter plików kdelnk na desktop
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-kdelnk2desktop
A kdelnk to desktop converter.

%description scripts-kdelnk2desktop -l pl
Konwerter plików kdelnk na desktop.

%package scripts-zonetab2pot
Summary:	A zone.tab to .pot converter
Summary(pl):	Konwerter plików zone.tab na .pot
Group:		X11/Development/Tools
Requires:	/usr/bin/python
Requires:	gettext-devel
Obsoletes:	%{name}-devel

%description scripts-zonetab2pot
This script reads timezone list as its first argument or from
/usr/share/zoneinfo/zone.tab, and converts it to a PO file template.

%description scripts-zonetab2pot -l pl
Ten skrypt wczytuje listê stref czasowych z linii poleceñ lub pliku
/usr/share/zoneinfo/zone.tab i konwertuje je na plik POT.

%package scheck
Summary:	KDE Style - Scheck
Summary(pl):	Motyw KDE - Scheck
Group:		X11/Development
Obsoletes:	%{name}-devel

%description scheck
Development style for searching accelerator and style guide conflicts.

%description scheck -l pl
Motyw KDE przeznaczony do szukania konfliktów w oprogramowaniu.

%package umbrello
Summary:	UML Modeler
Summary(pl):	Modeler UML
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description umbrello
UML Modeler.

%description umbrello -l pl
Modeler UML.

%package xemacs
Summary:	A set of macros for xemacs
Summary(pl):	Zestaw makr do xemacsa
Group:		X11/Development/Tools
Requires: 	xemacs-common
Obsoletes:	%{name}-devel

%description xemacs
A set of macros for xemacs.

%description xemacs -l pl
Zestaw makr do xemacsa.

%prep
%setup -q -n %{name}-%{_snap}

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--enable-final

%{__make}

%{__make} -C kstartperf

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%{__make} -C kstartperf install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefdir},%{_emacspkgdir}/kde} \
	$RPM_BUILD_ROOT{%{_xemacspkgdir}/kde,%{_zshfcdir},%{_sysconfdir}/bash_completion.d}

install ./kdepalettes/KDE_Gimp		$RPM_BUILD_ROOT%{_gimpdir}/palettes/
cp ./kdepalettes/kde_xpaintrc		$RPM_BUILD_ROOT%{_appdefdir}/XPaint.kde
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_emacspkgdir}/kde
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_xemacspkgdir}/kde
cp ./scripts/completions/zsh/_*		$RPM_BUILD_ROOT%{_zshfcdir}
cp ./scripts/completions/bash/dcop	$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

cd $RPM_BUILD_ROOT
rm -rf `find . -name CVS`
cd -

%find_lang	cervisia	--with-kde
%find_lang	kbabel		--with-kde
%find_lang	kcachegrind	--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde
%find_lang	umbrello	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	cervisia		-p /sbin/ldconfig
%postun	cervisia		-p /sbin/ldconfig

%post	kbabel			-p /sbin/ldconfig
%postun	kbabel			-p /sbin/ldconfig

%post	kbabel-dictionary	-p /sbin/ldconfig
%postun	kbabel-dictionary	-p /sbin/ldconfig

%post	kspy			-p /sbin/ldconfig
%postun	kspy			-p /sbin/ldconfig

%post	kstartperf		-p /sbin/ldconfig
%postun	kstartperf		-p /sbin/ldconfig

%post	umbrello		-p /sbin/ldconfig
%postun	umbrello		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/kde3/kfile_[!dp]*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_[!dp]*.so
%{_datadir}/services/kfile_cpp.desktop
%{_datadir}/services/kfile_h.desktop
%{_datadir}/services/kfile_ts.desktop

%files cervisia -f cervisia.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cervisia
%attr(755,root,root) %{_bindir}/cvsaskpass
%attr(755,root,root) %{_bindir}/cvsservice
%{_libdir}/libcvsservice.la
%attr(755,root,root) %{_libdir}/libcvsservice.so.*.*.*
%{_libdir}/kde3/libcervisiapart.la
%attr(755,root,root) %{_libdir}/kde3/libcervisiapart.so
%{_datadir}/apps/cervisia*
%{_datadir}/apps/kconf_update/change_colors.pl
%{_datadir}/apps/kconf_update/cervisia.upd
%{_datadir}/apps/kconf_update/move_repositories.pl
%{_datadir}/services/cvsservice.desktop
%{_desktopdir}/kde/cervisia.desktop
%{_iconsdir}/*/*/*/cervisia.png
%{_mandir}/man1/cervisia*

%files cervisia-devel
%{_includedir}/cvsjob_stub.h
%{_includedir}/cvsservice_stub.h
%{_includedir}/repository_stub.h
%{_libdir}/libcvsservice.so

%files completions-bash
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d

%files completions-zsh
%defattr(644,root,root,755)
%{_zshfcdir}/*

%files emacs
%defattr(644,root,root,755)
%{_emacspkgdir}/kde

%files kapptemplate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapptemplate
%dir %{_datadir}/apps/kapptemplate
%{_datadir}/apps/kapptemplate/[!b]*
%dir %{_datadir}/apps/kapptemplate/bin
%attr(755,root,root) %{_datadir}/apps/kapptemplate/bin/*

%files kaddressbook-kdeaccounts
%defattr(644,root,root,755)
%{_libdir}/kde3/kabcformat_kdeaccounts.la
%attr(755,root,root) %{_libdir}/kde3/kabcformat_kdeaccounts.so
%{_datadir}/apps/kabc/formats/*

%files kbabel -f kbabel.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbabel
%{_libdir}/libkbabelcommon.la
%attr(755,root,root) %{_libdir}/libkbabelcommon.so.*.*.*
%{_libdir}/libkbabeldictplugin.la
%attr(755,root,root) %{_libdir}/libkbabeldictplugin.so.*.*.*
%{_libdir}/kde3/kbabel_*.la
%attr(755,root,root) %{_libdir}/kde3/kbabel_*.so
%{_datadir}/apps/kbabel
# Already in kdelibs
#%{_datadir}/mimelnk/application/x-gettext.desktop
%{_datadir}/services/kbabel_accelstool.desktop
%{_datadir}/services/kbabel_argstool.desktop
%{_datadir}/services/kbabel_contexttool.desktop
%{_datadir}/services/kbabel_equationstool.desktop
%{_datadir}/services/kbabel_gettext_export.desktop
%{_datadir}/services/kbabel_gettext_import.desktop
%{_datadir}/services/kbabel_lengthtool.desktop
%{_datadir}/services/kbabel_linguist_export.desktop
%{_datadir}/services/kbabel_linguist_import.desktop
%{_datadir}/services/kbabel_nottranslatedtool.desktop
%{_datadir}/services/kbabel_pluralformstool.desktop
%{_datadir}/services/kbabel_punctuationtool.desktop
%{_datadir}/services/kbabel_setfuzzytool.desktop
%{_datadir}/services/kbabel_whitespacetool.desktop
%{_datadir}/services/kbabel_xmltool.desktop
%{_datadir}/servicetypes/kbabel_*.desktop
%{_datadir}/servicetypes/kbabelfilter.desktop
%{_desktopdir}/kde/kbabel.desktop
%{_iconsdir}/[!l]*/*/*/kbabel.png
# Already in kdelibs
#%{_iconsdir}/[!l]*/*/mimetypes/gettext.png

%files kbabel-devel
%defattr(644,root,root,755)
%{_includedir}/kbabel
%{_libdir}/libkbabelcommon.so
%{_libdir}/libkbabeldictplugin.so

%files kbabel-catalog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/catalogmanager
%{_libdir}/kde3/kfile_po.la
%attr(755,root,root) %{_libdir}/kde3/kfile_po.so
%{_libdir}/kde3/pothumbnail.la
%attr(755,root,root) %{_libdir}/kde3/pothumbnail.so
%{_datadir}/apps/catalogmanager
%{_datadir}/services/kfile_po.desktop
%{_datadir}/services/pothumbnail.desktop
%{_desktopdir}/kde/catalogmanager.desktop
%{_iconsdir}/[!l]*/*/*/catalogmanager.png

%files kbabel-dictionary
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbabeldict
%{_libdir}/kde3/kbabeldict_*.la
%attr(755,root,root) %{_libdir}/kde3/kbabeldict_*.so
%{_datadir}/services/dbsearchengine.desktop
%{_datadir}/services/tmxcompendium.desktop
%{_datadir}/services/poauxiliary.desktop
%{_datadir}/services/pocompendium.desktop
%{_datadir}/servicetypes/kbabeldict_module.desktop
%{_desktopdir}/kde/kbabeldict.desktop
%{_iconsdir}/[!l]*/*/*/kbabeldict.png

%files kbugbuster -f kbugbuster.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_datadir}/apps/kbugbuster
%{_desktopdir}/kde/kbugbuster.desktop
%{_iconsdir}/[!l]*/*/*/kbugbuster.png

%files kcachegrind -f kcachegrind.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcachegrind
%{_datadir}/apps/kcachegrind
%{_datadir}/mimelnk/application/x-kcachegrind.desktop
%{_desktopdir}/kde/kcachegrind.desktop
%{_iconsdir}/hicolor/*/apps/kcachegrind.png

#%files kmtrace
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kmtrace
#%attr(755,root,root) %{_bindir}/kminspector
#%attr(755,root,root) %{_bindir}/demangle
#%attr(755,root,root) %{_bindir}/match
#%{_libdir}/libktrace*.la
#%attr(755,root,root) %{_libdir}/libktrace*.so*
#%{_includedir}/ktrace.h
#%{_datadir}/apps/kmtrace

%files kompare -f kompare.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%{_libdir}/libkompareinterface.la
%attr(755,root,root) %{_libdir}/libkompareinterface.so
%attr(755,root,root) %{_libdir}/libkompareinterface.so.*.*.*
%{_libdir}/kde3/kfile_diff.la
%attr(755,root,root) %{_libdir}/kde3/kfile_diff.so
%{_libdir}/kde3/libkompare*.la
%attr(755,root,root) %{_libdir}/kde3/libkompare*.so
%{_datadir}/apps/kompare*
%{_datadir}/services/kfile_diff.desktop
%{_datadir}/services/kompare*.desktop
%{_datadir}/servicetypes/kompare*.desktop
%{_desktopdir}/kde/kompare.desktop
%{_iconsdir}/[!l]*/*/*/kompare.png

%files kprofilemethod
%defattr(644,root,root,755)
%{_includedir}/kprofilemethod.h

%files kspy
%defattr(644,root,root,755)
%{_libdir}/libkspy.la
%{_libdir}/libkspy.so
%attr(755,root,root) %{_libdir}/libkspy.so.*.*.*
%{_includedir}/kspy.h

%files kstartperf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstartperf
%{_libdir}/libkstartperf.la
%{_libdir}/libkstartperf.so
%attr(755,root,root) %{_libdir}/libkstartperf.so.*.*.*

%files kuiviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuiviewer
%{_libdir}/kde3/libkuiviewerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkuiviewerpart.so
%{_libdir}/kde3/quithumbnail.la
%attr(755,root,root) %{_libdir}/kde3/quithumbnail.so
%{_datadir}/apps/kuiviewer/kuiviewer.rc
%{_datadir}/apps/kuiviewerpart/kuiviewer_part.rc
%{_datadir}/services/designerthumbnail.desktop
%{_datadir}/services/kuiviewer_part.desktop
%{_desktopdir}/kde/kuiviewer.desktop
%{_iconsdir}/*/*/apps/kuiviewer.png

%files pallette-gimp
%defattr(644,root,root,755)
%{_gimpdir}/palettes

%files pallette-xpaint
%defattr(644,root,root,755)
%{_appdefdir}

%files po2xml
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/fixsgml
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/transxx
%attr(755,root,root) %{_bindir}/xml2pot

%files scheck
%{_libdir}/kde3/plugins/styles/scheck.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/scheck.so
%{_datadir}/apps/kstyle/themes/scheck.themerc

%files scripts-build
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adddebug
%attr(755,root,root) %{_bindir}/build-progress.sh
%attr(755,root,root) %{_bindir}/create*
%attr(755,root,root) %{_bindir}/extend*
%attr(755,root,root) %{_bindir}/makeobj
%attr(755,root,root) %{_bindir}/licensecheck
%attr(755,root,root) %{_bindir}/includemocs
%attr(755,root,root) %{_bindir}/fixkdeincludes
%attr(755,root,root) %{_bindir}/kde-build
%attr(755,root,root) %{_bindir}/cheatmake
%{_mandir}/man1/kde-build.1*
%{_mandir}/man1/includemocs.1*

%files scripts-cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs*
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/pruneemptydirs
%{_mandir}/man1/*cvs*

%files scripts-cxxmetric
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxxmetric

%files scripts-doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtdoc
%attr(755,root,root) %{_bindir}/kdedoc

%files scripts-extractrc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extractrc

%files scripts-findmissingcrystal
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/findmissingcrystal

%files scripts-kdekillall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdekillall

%files scripts-kdelnk2desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py

%files scripts-zonetab2pot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zonetab2pot.py

%files umbrello -f umbrello.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/umbrello
#%{_libdir}/libcodegenerator.la
#%{_libdir}/libcodegenerator.so
#%attr(755,root,root) %{_libdir}/libcodegenerator.so.*.*.*
#%{_libdir}/kde3/libumlwidgets.la
#%attr(755,root,root) %{_libdir}/kde3/libumlwidgets.so*
%{_datadir}/apps/umbrello
%{_datadir}/mimelnk/application/x-umbrello.desktop
%{_desktopdir}/kde/umbrello.desktop
%{_iconsdir}/hicolor/*/apps/umbrello.png
%{_iconsdir}/hicolor/*/mimetypes/umbrellofile.png

%files xemacs
%defattr(644,root,root,755)
%{_xemacspkgdir}/kde
