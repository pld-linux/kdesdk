
%define         _state          snapshots
%define         _ver		3.1.90
%define		_snap		030726

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		3
License:	GPL
Group:		X11/Development/Tools
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	d4e9ad73d9e3a2a9307f61a35c9d2617
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
BuildRequires:	kdebase-devel >= 9:%{version}
BuildRequires:	libltdl-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdesdk-devel

%define		_htmldir	%{_docdir}/kde/HTML
%define		_icondir	%{_datadir}/icons
%define		_gimpdir	%(gimptool --gimpdatadir)
%define		_appdefdir	/usr/X11R6/lib/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/21.2
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj�cy programowanie w �rodowisku KDE.

%package static
Summary:	Static libraries for kdesdk
Summary(pl):	Statyczne biblioteki dla kdesdk
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description static
Static libraries for kdesdk.

%description static -l pl
Statyczne biblioteki dla kdesdk.

%package cervisia
Summary:        A KDE cvs frontend
Summary(pl):    Frontend CVS pod KDE
Group:		X11/Development/Tools
Requires:	cvs >= 1.10
Obsoletes:	%{name}-devel

%description cervisia
A KDE cvs frontend.

%description cervisia -l pl
Frontend CVS pod KDE.

%package cervisia-devel
Summary:        A KDE cvs frontend - header files
Summary(pl):    Frontend CVS pod KDE - pliki nag��wkowe
Group:		X11/Development
Obsoletes:	%{name}-devel

%description cervisia-devel
A KDE cvs frontend. This package contains header files.

%description cervisia-devel -l pl
Frontend CVS pod KDE. Ten pakiet zawiera pliki nag��wkowe.

%package completions-bash
Summary:        Autocomplete definitions for bash
Summary(pl):    Definicje autouzupe�niania dla basha
Group:		Applications/Shells
Requires:	bash-completion
Obsoletes:	%{name}-devel

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl
Definicje autouzupe�niania dla basha.

%package completions-zsh
Summary:        Autocomplete definitions for zsh
Summary(pl):    Definicje autouzupe�niania dla zsh
Group:          Applications/Shells
Requires:       zsh >= 4.0.6-2
Obsoletes:	%{name}-devel

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl
Definicje autouzupe�niania dla zsh.

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
Summary:        A kdeaccounts plugin for the KDE adressbook
Summary(pl):	Wtyczka do ksi��ki adresowej KDE dodaj�ca obs�ug� kdeaccounts
Group:          X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8
Obsoletes:	%{name}-devel

%description kaddressbook-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. What is does is adding
the people from KDE's CVS accounts file to the addressbook.

%description kaddressbook-kdeaccounts -l pl
Wtyczka do ksi��ki adresowej KDE dodaj�ca obs�ug� kdeaccounts. Dodaje
ona osoby posiadaj�ce konta w CVS KDE do ksi��ki adresowej.

%package kapptemplate
Summary:        KDE application framework generator
Summary(pl):    Generator szkieletu dla aplikacji KDE
Group:          X11/Development/Tools
Obsoletes:	%{name}-devel

%description kapptemplate
Modular shell script that will automatically create a framework for
either a normal KDE 3.x application, a KPart application, a KPart
plugin, or convert an existing application.

%description kapptemplate -l pl
Modularny skrypt, kt�ry potrafi automatycznie wygenerowa� szkielet
katalog�w dla zwyk�ej aplikacji pod KDE 3.x, aplikacji KPart, wtyczki
KPart lub skonwertowa� istniej�c� aplikacj�.

%package kbabel
Summary:        An advanced and easy to use PO-file editor
Summary(pl):    Rozbudowany i �atwy w obs�udze edytor plik�w PO
Group:          X11/Development/Tools
Requires:	gettext-devel
Obsoletes:	%{name}-devel

%description kbabel
KBabel is a tool, that allows easy management, edition and upkeep of
gettext .po files.

%description kbabel -l pl
KBabel jest narz�dziem, kt�re pozwala na �atwe zarz�dzanie, edycj� i
utrzymanie plik�w po.

%package kbabel-devel
Summary:        Kbabel headers
Summary(pl):    Pliki nag��wkowe KBabel
Group:          X11/Development
Requires:       gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Requires:       %{name}-kbabel-catalog = %{epoch}:%{version}-%{release}
Requires:       %{name}-kbabel-dictionary = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-devel

%description kbabel-devel
KBabel headers.

%description kbabel-devel -l pl
Pliki nag��wkowe KBabel.

%package kbabel-dictionary
Summary:        Plugin that supports dictionaries made from po compendia
Summary(pl):    Wtyczka kbabel obs�uguj�ca s�owniki z kompendi�w po
Group:          X11/Development
Requires:       gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-devel

%description kbabel-dictionary
Plugin that supports dictionaries made from po compendia.

%description kbabel-dictionary -l pl
Wtyczka kbabel obs�uguj�ca s�owniki z kompendi�w po.

%package kbabel-catalog
Summary:        A KBabel catalog manager
Summary(pl):    Zarz�dca zbior�w plik�w po zintegrowany z KBabel
Group:          X11/Development
Requires:       gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-devel

%description kbabel-catalog
A KBabel catalog manager.

%description kbabel-catalog -l pl
Zarz�dca zbior�w plik�w po zintegrowany z KBabel.

%package kbugbuster
Summary:        A tools that allows cooperation with bugs.kde.org
Summary(pl):    Narz�dzie wsp�pracuj�ce z bugs.kde.org
Group:          X11/Development/Tools
Obsoletes:	%{name}-devel

%description kbugbuster
KBugBuster allows easy bug management on bugs.kde.org.

%description kbugbuster -l pl
KBugBuster u�atwia wyszukwianie i zarz�dzanie b��dami na bugs.kde.org.

%package kmtrace
Summary:        An mtrace to full backtrace conversion tool
Summary(pl):    Narz�dzie do konwersji z mtrace do pe�nego backtrace'a
Group:          X11/Development/Tools
BuildRequires:  binutils-static
Obsoletes:	%{name}-devel

%description kmtrace
Converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl
Konwertuje mtrace glibca do pe�nego backtrace'a.

%package kompare
Summary:	Kompare is a program to view the differences between files
Summary(pl):	Kompare to program s�u��cy do por�wnywania zmian mi�dzy plikami
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
Kompare to program s�u��cy do por�wnywania zmian mi�dzy plikami.
Aktualnie dost�pne funkcje:
  * por�wnanie plik�w lub katalog�w poprzez graficzny interfejs
  * przedstawienie �r�d�a i celu za pomoc� krzywej Beziera
  * graficzne przegl�danie �at w formatach diff, unidiff, context i
    zwyk�ym
  * interaktywne wprowadzanie zmian
  * przezroczysto�� sieciowa
  * mo�liwo�� ogl�dania wyj�cia diff w wewn�trznej przegl�darce
  * �atwa nawigacja mi�dzy wieloplikowymi diffami wraz z dokowalnym drzewem
  * zamiana �r�d�a i celu za pomoc� pojedynczej komendy
  * statystyki diff�w

%package kprofilemethod
Summary:	Kprofilemethod is a set of macros which help profiling using QTime
Summary(pl):	Kprofilemethod to zestaw makr u�atwiaj�cych profilowanie z wykorzystaniem QTime
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kprofilemethod
Kprofilemethod is a set of macros which help profiling using QTime.

%description kprofilemethod -l pl
Kprofilemethod to zestaw makr u�atwiaj�cych profilowanie z
wykorzystaniem QTime.

%package kspy
Summary:        A utility for egzamining the internal state of a QT/KDE application.
Summary(pl):    Narz�dzie do badania stanu aplikacji QT/KDE
Group:          X11/Development/Tools
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
KSpy to narz�dzie maj�ce u�atwi� programistom badanie wewn�trznego
stanu aplikacji QT/KDE. KSpy ilustruje graficznie wszystkie QObjects
jakie s� w u�yciu i pozwala na �atwe przegl�danie ich w�a�ciwo�ci.
Korzystanie z KSpy jest bardzo proste (wystarczy do��czy� plik kspy.h
i wywo�a� KSpy::invoke() w miejscu, kt�re chcemy obejrze� w naszej
aplikacji. Funkcja KSpy jest inline, wi�c mo�na zostawi� j� nawet w
wydaniu stabilnym.

%package kstartperf
Summary:	A tool to measure startup time for KDE applications
Summary(pl):	Narz�dzie s�u��ce do pomiaru czasu �adowania aplikacji KDE
Group:          X11/Development/Tools
Obsoletes:	%{name}-devel

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl
Narz�dzie s�u��ce do pomiaru czasu �adowania aplikacji KDE.

%package pallette-gimp
Summary:        Adds the KDE Default pallette to GIMP
Summary(pl):    Dodaje domy�ln� palet� kolor�w KDE do GIMP-a
Group:          X11/Applications/Graphics
Requires:	gimp
Obsoletes:	%{name}-devel

%description pallette-gimp
Adds the KDE Default pallette to GIMP.

%description pallette-gimp -l pl
Dodaje domy�ln� palet� kolor�w KDE do GIMP-a.

%package pallette-xpaint
Summary:        Adds the KDE Default pallette to XPaint
Summary(pl):    Dodaje domy�ln� palet� kolor�w KDE do XPainta
Group:          X11/Applications/Graphics
Requires:       xpaint
Obsoletes:	%{name}-devel

%description pallette-xpaint
Adds the KDE Default pallette to XPaint.

%description pallette-xpaint -l pl
Dodaje domy�ln� palet� kolor�w KDE do XPainta.

%package po2xml
Summary:	An xml2po and vice versa converters
Summary(pl):	Konwertery po2xml i vice versa
Group:          X11/Development/Tools
Requires:	/usr/bin/python
Obsoletes:	%{name}-devel

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl
Konwertery po2xml i vice versa.

%package scripts-build
Summary:        An set of scripts useful for building KDE
Summary(pl):    Zestaw skrypt�w do kompilowania KDE
Group:          X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-build
A set of scripts useful for building KDE.

%description scripts-build -l pl
Zestaw skrypt�w do kompilowania KDE.

%package scripts-cxxmetric
Summary:	Statistic meter for c/c++ files
Summary(pl):	Plik do tworzenia statystyki plik�w c/c++
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-cxxmetric
Counts lines of code, comments and blank space in C and C++ source
files.

%description scripts-cxxmetric -l pl
Zlicza linijki kodu, komentarzy i znak�w bia�ych w plikach �r�d�owych
C i C++.

%package scripts-cvs
Summary:        A set of scripts for maintaining KDE from CVS
Summary(pl):    Zestaw skrypt�w do zarz�dzania KDE z CVS
Group:          X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-cvs
A set of scripts for maintaining KDE from CVS.

%description scripts-cvs -l pl
Zestaw skrypt�w do zarz�dzania KDE z CVS.

%package scripts-doc
Summary:        A set of scripts for quick access to qt/KDE documentation
Summary(pl):    Zestaw skrypt�w szybkiego dost�pu do dokumentacji qt/KDE
Group:          X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-doc
A set of scripts for quick access to qt/KDE documentation.

%description scripts-doc -l pl
Zestaw skrypt�w szybkiego dost�pu do dokumentacji qt/KDE.

%package scripts-extractrc
Summary:	Extracts the strings from .rc files
Summary(pl):	Wyci�ga �a�cuchy z plik�w .rc
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-extractrc
Obsoletes:	%{name}-devel

%description scripts-extractrc
A Perl script, it extracts the strings in an application's .rc file,
e.g. testappui.rc, and writes into the pot file where the translations
are build with (po-files).

%description scripts-extractrc -l pl
Skrypt napisany w Perlu, kt�ry wyci�ga �a�cuchy z plik�w .rc
aplikacji, np. testappgui.rc i zapisuje je do plik�w pot, z kt�rych
tworzy si� t�umaczenia (pliki po).

%package scripts-kdekillall
Summary:	A script for killing KDE apps started with kdeinit
Summary(pl):	Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit
Group:          X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-kdekillall
A script for killing KDE apps started with kdeinit.

%description scripts-kdekillall -l pl
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scripts-kdelnk2desktop
Summary:	A kdelnk to desktop converter
Summary(pl):	Konwerter plik�w kdelnk na desktop
Group:          X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-kdelnk2desktop
A kdelnk to desktop converter.

%description scripts-kdelnk2desktop -l pl
Konwerter plik�w kdelnk na desktop.

%package scripts-zonetab2pot
Summary:	A zone.tab to .pot converter
Summary(pl):	Konwerter plik�w zone.tab na .pot
Group:          X11/Development/Tools
Requires:	/usr/bin/python
Requires:	gettext-devel
Obsoletes:	%{name}-devel

%description scripts-zonetab2pot
This script reads timezone list as its first argument or from
/usr/share/zoneinfo/zone.tab, and converts it to a PO file template.

%description scripts-zonetab2pot -l pl
Ten skrypt wczytuje list� stref czasowych z linii polece� lub pliku
/usr/share/zoneinfo/zone.tab i konwertuje je na plik POT.

%package scheck
Summary:	KDE Style - Scheck
Summary(pl):	Motyw KDE - Scheck
Group:		X11/Development
Obsoletes:	%{name}-devel

%description scheck
Development style for searching accelerator and style guide conflicts.

%description scheck -l pl
Motyw KDE przeznaczony do szukania konflikt�w w oprogramowaniu.

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

for plik in `find ./ -name *.desktop` ; do
	if [ -d $plik ]; then
	echo $plik
	sed -ie 's/\[nb\]/\[no\]/g' $plik
	fi
done

%configure

%{__make}

%{__make} -C kstartperf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefdir},%{_emacspkgdir}/kde} \
	$RPM_BUILD_ROOT{%{_xemacspkgdir}/kde,%{_zshfcdir},%{_sysconfdir}/bash_completion.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_htmldir}

%{__make} -C kstartperf install DESTDIR=$RPM_BUILD_ROOT

install ./kdepalettes/KDE_Gimp		$RPM_BUILD_ROOT%{_gimpdir}/palettes/
cp ./kdepalettes/kde_xpaintrc		$RPM_BUILD_ROOT%{_appdefdir}/XPaint.kde
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_emacspkgdir}/kde
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_xemacspkgdir}/kde
cp ./scripts/completions/zsh/_*		$RPM_BUILD_ROOT%{_zshfcdir}
cp ./scripts/completions/bash/dcop	$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Development/*.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}

cd $RPM_BUILD_ROOT
rm -rf `find . -name CVS`
cd -

%find_lang	cervisia	--with-kde
%find_lang	kbabel		--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde
%find_lang	umbrello	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	cervisia
/sbin/ldconfig

%postun	cervisia
/sbin/ldconfig

%post	kbabel
/sbin/ldconfig

%postun	kbabel
/sbin/ldconfig

%post	kbabel-dictionary
/sbin/ldconfig

%postun	kbabel-dictionary
/sbin/ldconfig

%post	kspy
/sbin/ldconfig

%postun	kspy
/sbin/ldconfig

%post	kstartperf
/sbin/ldconfig

%postun	kstartperf
/sbin/ldconfig

%post	umbrello
/sbin/ldconfig

%postun	umbrello
/sbin/ldconfig

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
%{_libdir}/libcvsservice.la
%attr(755,root,root) %{_libdir}/libcvsservice.so.*.*.*
%{_libdir}/kde3/libcervisiapart.la
%attr(755,root,root) %{_libdir}/kde3/libcervisiapart.so
%{_datadir}/apps/cervisia*
%{_datadir}/apps/kconf_update/cervisia.upd
%{_datadir}/apps/kconf_update/move_repositories.pl
%{_datadir}/services/cvsservice.desktop
%{_desktopdir}/cervisia.desktop
%{_icondir}/*/*/*/cervisia.png
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
%{_libdir}/kde3/kbabel_*.la
%attr(755,root,root) %{_libdir}/kde3/kbabel_*.so
%{_datadir}/apps/kbabel
# Already in kdelibs
#%{_datadir}/mimelnk/application/x-gettext.desktop
%{_datadir}/services/accelstool.desktop
%{_datadir}/services/argstool.desktop
%{_datadir}/services/contexttool.desktop
%{_datadir}/services/equationstool.desktop
%{_datadir}/services/kbabel_gettext_*.desktop
%{_datadir}/services/kbabel_linguist_*.desktop
%{_datadir}/services/lengthtool.desktop
%{_datadir}/services/nottranslatedtool.desktop
%{_datadir}/services/pluralformstool.desktop
%{_datadir}/services/setfuzzytool.desktop
%{_datadir}/services/whitespacetool.desktop
%{_datadir}/services/xmltool.desktop
%{_datadir}/servicetypes/kbabel_*.desktop
%{_datadir}/servicetypes/kbabelfilter.desktop
%{_desktopdir}/kbabel.desktop
%{_icondir}/[!l]*/*/*/kbabel.png
%{_icondir}/*/*/*/gettext.png

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
%{_desktopdir}/catalogmanager.desktop
%{_icondir}/[!l]*/*/*/catalogmanager.png

%files kbabel-dictionary
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbabeldict
%{_libdir}/libkbabeldictplugin.la
%attr(755,root,root) %{_libdir}/libkbabeldictplugin.so.*.*.*
%{_libdir}/kde3/kbabeldict_*.la
%attr(755,root,root) %{_libdir}/kde3/kbabeldict_*.so
%{_datadir}/services/dbsearchengine.desktop
%{_datadir}/services/tmxcompendium.desktop
%{_datadir}/services/poauxiliary.desktop
%{_datadir}/services/pocompendium.desktop
%{_datadir}/servicetypes/kbabeldict_module.desktop
%{_desktopdir}/kbabeldict.desktop
%{_icondir}/[!l]*/*/*/kbabeldict.png

%files kbabel-devel
%defattr(644,root,root,755)
%{_includedir}/kbabel
%{_libdir}/libkbabelcommon.so
%{_libdir}/libkbabeldictplugin.so

%files kbugbuster -f kbugbuster.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_datadir}/apps/kbugbuster
%{_desktopdir}/kbugbuster.desktop
%{_icondir}/[!l]*/*/*/kbugbuster.png

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
%{_libdir}/kde3/kfile_diff.la
%attr(755,root,root) %{_libdir}/kde3/kfile_diff.so
%{_libdir}/kde3/libkompare*.la
%attr(755,root,root) %{_libdir}/kde3/libkompare*.so
%{_datadir}/apps/kompare*
%{_datadir}/services/kfile_diff.desktop
%{_datadir}/services/kompare*.desktop
%{_datadir}/servicetypes/kompare*.desktop
%{_desktopdir}/kompare.desktop
%{_icondir}/[!l]*/*/*/kompare.png

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

%files pallette-gimp
%defattr(644,root,root,755)
%{_gimpdir}/palettes

%files pallette-xpaint
%defattr(644,root,root,755)
%{_appdefdir}

%files po2xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fixsgml
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/transxx
%attr(755,root,root) %{_bindir}/xml2pot

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

%files scripts-doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtdoc
%attr(755,root,root) %{_bindir}/kdedoc

%files scripts-extractrc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extractrc

%files scripts-cxxmetric
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxxmetric

%files scripts-kdekillall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdekillall

%files scripts-kdelnk2desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py

%files scripts-zonetab2pot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zonetab2pot.py

%files scheck
%{_libdir}/kde3/plugins/styles/scheck.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/scheck.so
%{_datadir}/apps/kstyle/themes/scheck.themerc

%files umbrello -f umbrello.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/umbrello
%{_libdir}/libcodegenerator.la
%{_libdir}/libcodegenerator.so
%attr(755,root,root) %{_libdir}/libcodegenerator.so.*.*.*
%{_libdir}/kde3/libumlwidgets.la
%attr(755,root,root) %{_libdir}/kde3/libumlwidgets.so*
%{_datadir}/apps/umbrello
%{_datadir}/mimelnk/application/x-umbrello.desktop
%{_desktopdir}/umbrello.desktop
%{_icondir}/hicolor/*/apps/umbrello.png

%files xemacs
%defattr(644,root,root,755)
%{_xemacspkgdir}/kde
