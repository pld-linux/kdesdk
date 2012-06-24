#
%define		_state		stable
%define		_ver		3.2.3

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	%{_ver}
Release:	1
Epoch:		3
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	82808f2780ae970fb38d44512ff9e2f3
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
Patch100:	%{name}-branch.diff
Patch0:		%{name}-kmtrace_glibc23.patch
Patch1:		%{name}-am.patch
URL:		http://www.kde.org/
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
Obsoletes:	kdesdk

%define		_gimpdir	%(gimptool --gimpdatadir)
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/21.2
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj�cy programowanie w �rodowisku KDE.

%package kfile
Summary:	Developers' file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach u�ywanych przez programist�w
Group:		X11/Development/Libraries
Requires:	konqueror >= %{version}
Obsoletes:	kdesdk
Obsoletes:	kdesdk-devel

%description kfile
This package adds a tab to konqueror "file properties" dialog window
with file enhanced informations for C++ source files, diff files,
gettext and designer translation sourcefiles.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w�a�ciwo�ci pliku" konquerora
dodatkow� zak�adk� z rozszerzonymi informacjami o pliku.

%package cervisia
Summary:	A KDE CVS frontend
Summary(pl):	Frontend do CVS dla KDE
Group:		X11/Development/Tools
Requires:	cvs >= 1.10
Obsoletes:	kdesdk-devel

%description cervisia
A KDE CVS frontend. It features:
- updating or retrieving the status of a working directory or single
  files. Files are displayed in different colors depending on their
  status, and the shown files can be filtered according to their status
- common operations like adding, removing and commiting files.
- advanced operations like adding and removing watches, editing and
  unediting files, locking and unlocking.
- checking out and importing modules.
- graphical diff against the repository and between different
  revisions.
- blame-annotated view of a file.
- view of the log messages in tree and list form.
- resolving of conflicts in a file.
- tagging and branching.
- updating to a tag, branch or date.
- a Changelog editor coupled with the commit dialog.

%description cervisia -l pl
Frontend do CVS dla KDE.

%package cervisia-devel
Summary:	Header files for cervisia, a KDE CVS frontend
Summary(pl):	Pliki nag��wkowe cervisii - frontendu do CVS dla KDE
Group:		X11/Development/Libraries
Obsoletes:	kdesdk-devel

%description cervisia-devel
A KDE CVS frontend. This package contains header files.

%description cervisia-devel -l pl
Pliki nag��wkowe cervisii - frontendu do CVS dla KDE.

%package completions-bash
Summary:	Autocomplete definitions for bash
Summary(pl):	Definicje autouzupe�niania dla basha
Group:		Applications/Shells
Requires:	bash-completion
Obsoletes:	kdesdk-devel

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl
Definicje autouzupe�niania dla basha.

%package completions-zsh
Summary:	Autocomplete definitions for zsh
Summary(pl):	Definicje autouzupe�niania dla zsh
Group:		Applications/Shells
Requires:	zsh >= 4.0.6-2
Obsoletes:	kdesdk-devel

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl
Definicje autouzupe�niania dla zsh.

%package emacs
Summary:	A set of macros for emacs
Summary(pl):	Zestaw makr do emacsa
Group:		X11/Development/Tools
Requires:	emacs-common
Obsoletes:	kdesdk-devel

%description emacs
A set of macros for emacs helpful for working on KDE programs.

%description emacs -l pl
Zestaw makr do emacsa.

%package kaddressbook-kdeaccounts
Summary:	A kdeaccounts plugin for the KDE adressbook
Summary(pl):	Wtyczka do ksi��ki adresowej KDE dodaj�ca obs�ug� kdeaccounts
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8
Obsoletes:	kdesdk-devel

%description kaddressbook-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. What is does is adding
the people from KDE's CVS accounts file to the addressbook.

%description kaddressbook-kdeaccounts -l pl
Wtyczka do ksi��ki adresowej KDE dodaj�ca obs�ug� kdeaccounts. Dodaje
ona osoby posiadaj�ce konta w CVS KDE do ksi��ki adresowej.

%package kapptemplate
Summary:	KDE application framework generator
Summary(pl):	Generator szkieletu dla aplikacji KDE
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description kapptemplate
Modular shell script that will automatically create a framework for
either a normal KDE 3.x application, a KPart application, a KPart
plugin, or convert an existing application.

%description kapptemplate -l pl
Modularny skrypt, kt�ry potrafi automatycznie wygenerowa� szkielet
katalog�w dla zwyk�ej aplikacji pod KDE 3.x, aplikacji KPart, wtyczki
KPart lub skonwertowa� istniej�c� aplikacj�.

%package kbabel
Summary:	An advanced and easy to use PO-file editor
Summary(pl):	Rozbudowany i �atwy w obs�udze edytor plik�w PO
Group:		X11/Development/Tools
Requires:	gettext-devel
Obsoletes:	kdesdk-devel

%description kbabel
KBabel is a tool, that allows easy management, edition and upkeep of
gettext .po files. It features:
- support for GNU gettext PO files (including plural forms) and Qt
  Linguist catalogs
- capability to open multiple files (or multiple views of the same
  file)
- full editing functionality, accessible through the graphic user
  interface as well as through user definable keyboard shortcuts
- powerful spell checking functionality
- capability to show diffs to older messages
- full navigation capabilities (such as go to next fuzzy or
  untranslated string)
- capability to save and read files in unicode encoding (utf-8)
- unlimited undo capability
- syntax highlighting, automatic file header updates, automatic change
  of "fuzzy" status of translated messages
- support for easy insertion of tags and URLs
- validation and highlighting of tags and XML entities
- a plugin framework for dictionaries, such as po compendium files,
  for consistency checks or translation suggestions
- a "rough translation" function to initialize untranslated messages
  with suggestion from a dictionary
- automatic syntax check with msgfmt when saving and if an error
  occured easy navigation to messages, which contain errors
- various methods to "see" whitespaces at end of lines or check
  consistency of translated messages, like comparing printf and Qt
- arguments in msgid and msgstr
- quick overview over context in the po file
- showing source code by references in message comments

%description kbabel -l pl
KBabel jest narz�dziem, kt�re pozwala na �atwe zarz�dzanie, edycj� i
utrzymanie plik�w po.

%package kbabel-devel
Summary:	KBabel header files
Summary(pl):	Pliki nag��wkowe KBabel
Group:		X11/Development/Libraries
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Requires:	%{name}-kbabel-catalog = %{epoch}:%{version}-%{release}
Requires:	%{name}-kbabel-dictionary = %{epoch}:%{version}-%{release}
Obsoletes:	kdesdk-devel

%description kbabel-devel
KBabel header files.

%description kbabel-devel -l pl
Pliki nag��wkowe KBabel.

%package kbabel-catalog
Summary:	A KBabel catalog manager
Summary(pl):	Mened�er plik�w po zintegrowany z KBabel
Group:		X11/Development/Tools
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Obsoletes:	kdesdk-devel

%description kbabel-catalog
A KBabel catalog manager. It features:
- file manager view for kde-i18n (or similarly structured)
  directories, which shows the present status of all PO files: if they
  are in need of a revision or not, how many fuzzies and untranslated
  strings are included etc. This view is always automatically updated
  and reflects all changes done to the files, including changes by
  programs other than KBabel.
- integrated CVS support
- various file open mechanisms for editing in KBabel: use Drag & Drop,
  double click, keyboard or context menu
- "Mark files" function (e.g. to identify POs that are in the
  responsibility of other translators)
- powerful navigation using PO file statistics
- automatic comparisons and statistics of POT and PO files for a quick
  overview which and how many files are translated (or not) and which
  files may be obsolete
- syntax check (msgfmt --statistics) for existing files to control if
  the translated files will compile and, accordingly, work when
  distributed
- configurable commands, that can be executed from the Catalog
  Manager's context menu.
- search/replace functions in multiple files at once.
- spellchecking of multiple files at once.
- doing "rough translation" for multiple files at once.

%description kbabel-catalog -l pl
Mened�er plik�w po zintegrowany z KBabel.

%package kbabel-dictionary
Summary:	Plugin that supports dictionaries made from po compendia
Summary(pl):	Wtyczka KBabel obs�uguj�ca s�owniki z kompendi�w po
Group:		X11/Development/Tools
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Obsoletes:	kdesdk-devel

%description kbabel-dictionary
KBabel plugin that supports dictionaries made from po compendia or TMX
1.4-based dicionaries

%description kbabel-dictionary -l pl
Wtyczka KBabel obs�uguj�ca s�owniki z kompendi�w po.

%package kbugbuster
Summary:	A tools that allows cooperation with bugs.kde.org
Summary(pl):	Narz�dzie wsp�pracuj�ce z bugs.kde.org
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description kbugbuster
KBugBuster allows for easy bug management on bugs.kde.org.

%description kbugbuster -l pl
KBugBuster u�atwia wyszukiwanie i zarz�dzanie b��dami na bugs.kde.org.

%package kcachegrind
Summary:	KCachegrind - visualization of traces generated by profiling
Summary(pl):	KCachegrind - wizualizacja �cie�ek tworzonych przez profilowanie
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description kcachegrind
KCachegrind visualizes traces generated by profiling.

%description kcachegrind -l pl
KCachegrind wizualizuje �cie�ki tworzone przez profilowanie.

%package kmtrace
Summary:	A mtrace to full backtrace conversion tool
Summary(pl):	Narz�dzie do konwersji z mtrace do pe�nego backtrace'a
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description kmtrace
kmtrace converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl
kmtrace konwertuje mtrace glibca do pe�nego backtrace'a.

%package kompare
Summary:	Kompare - a program to view the differences between files
Summary(pl):	Kompare - program s�u��cy do por�wnywania zmian mi�dzy plikami
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description kompare
Kompare is a program to view the differences between files. Features
include:

  - comparison of files or directories via a graphical interface
  - bezier-based connection widget lets you see both source and
    destination as they really appear
  - graphical viewing of patch files in normal, context, unified and
    diff formats
  - interactive application of differences
  - full network transparency
  - ability to view plain-text diff output in embedded viewer
  - easy navigation of multiple-file diffs with dockable navigation tree
  - graphical interface to commonly used diff command line options
  - switch source and destination with one command
  - diff statistics

%description kompare -l pl
Kompare to program s�u��cy do por�wnywania zmian mi�dzy plikami.
Aktualnie dost�pne funkcje:
  - por�wnanie plik�w lub katalog�w poprzez graficzny interfejs
  - przedstawienie �r�d�a i celu za pomoc� krzywej Beziera
  - graficzne przegl�danie �at w formatach diff, unidiff, context i
    zwyk�ym
  - interaktywne wprowadzanie zmian
  - przezroczysto�� sieciowa
  - mo�liwo�� ogl�dania wyj�cia diff w wewn�trznej przegl�darce
  - �atwa nawigacja mi�dzy wieloplikowymi diffami wraz z dokowalnym
    drzewem
  - zamiana �r�d�a i celu za pomoc� pojedynczej komendy
  - statystyki diff�w

%package kprofilemethod
Summary:	Kprofilemethod - a set of macros which help profiling using QTime
Summary(pl):	Kprofilemethod - zestaw makr u�atwiaj�cych profilowanie z wykorzystaniem QTime
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description kprofilemethod
Kprofilemethod is a set of macros which help profiling using QTime.

%description kprofilemethod -l pl
Kprofilemethod to zestaw makr u�atwiaj�cych profilowanie z
wykorzystaniem QTime.

%package kspy
Summary:	A utility for egzamining the internal state of a QT/KDE application.
Summary(pl):	Narz�dzie do badania stanu aplikacji QT/KDE
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel
Obsoletes:	kdiff
Obsoletes:	kdiff2

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
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl
Narz�dzie s�u��ce do pomiaru czasu �adowania aplikacji KDE.

%package kuiviewer
Summary:	Qt Designer UI file Viewer
Summary(pl):	Przegl�darka plik�w UI generowanych przez QT designera
Group:		X11/Development/Tools

%description kuiviewer
Qt Designer UI file Viewer.

%description kuiviewer -l pl
Przegl�darka plik�w UI generowanych przez QT designera.

%package pallette-gimp
Summary:	Package which adds the KDE Default pallette to GIMP
Summary(pl):	Pakiet dodaj�cy domy�ln� palet� kolor�w KDE do GIMP-a
Group:		X11/Applications/Graphics
Requires:	gimp
Obsoletes:	kdesdk-devel

%description pallette-gimp
This package adds the KDE Default pallette to GIMP.

%description pallette-gimp -l pl
Pakiet dodaj�cy domy�ln� palet� kolor�w KDE do GIMP-a.

%package pallette-xpaint
Summary:	Package which adds the KDE Default pallette to XPaint
Summary(pl):	Pakiet dodaj�cy domy�ln� palet� kolor�w KDE do XPainta
Group:		X11/Applications/Graphics
Requires:	xpaint
Obsoletes:	kdesdk-devel

%description pallette-xpaint
This package adds the KDE Default pallette to XPaint.

%description pallette-xpaint -l pl
Pakiet dodaj�cy domy�ln� palet� kolor�w KDE do XPainta.

%package po2xml
Summary:	An xml2po and vice versa converters
Summary(pl):	Konwertery po2xml i vice versa
Group:		X11/Development/Tools
Requires:	/usr/bin/python
Obsoletes:	kdesdk-devel

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl
Konwertery po2xml i vice versa.

%package scripts-build
Summary:	An set of scripts useful for building KDE
Summary(pl):	Zestaw skrypt�w do kompilowania KDE
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	kdesdk-devel

%description scripts-build
A set of scripts useful for building KDE.

%description scripts-build -l pl
Zestaw skrypt�w do kompilowania KDE.

%package scripts-cxxmetric
Summary:	Statistic meter for c/c++ files
Summary(pl):	Program do tworzenia statystyki plik�w c/c++
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	kdesdk-devel

%description scripts-cxxmetric
This program counts lines of code, comments and blank space in C and
C++ source files.

%description scripts-cxxmetric -l pl
Ten program zlicza linijki kodu, komentarzy i znak�w bia�ych w plikach
�r�d�owych C i C++.

%package scripts-cvs
Summary:	A set of scripts for maintaining KDE from CVS
Summary(pl):	Zestaw skrypt�w do zarz�dzania KDE z CVS
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	kdesdk-devel

%description scripts-cvs
A set of scripts for maintaining KDE from CVS.

%description scripts-cvs -l pl
Zestaw skrypt�w do zarz�dzania KDE z CVS.

%package scripts-doc
Summary:	A set of scripts for quick access to Qt/KDE documentation
Summary(pl):	Zestaw skrypt�w szybkiego dost�pu do dokumentacji Qt/KDE
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description scripts-doc
A set of scripts for quick access to Qt/KDE documentation.

%description scripts-doc -l pl
Zestaw skrypt�w szybkiego dost�pu do dokumentacji Qt/KDE.

%package scripts-extractrc
Summary:	Extracting the strings from .rc files
Summary(pl):	Wyci�ganie �a�cuch�w z plik�w .rc
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	kdesdk-devel
Obsoletes:	kdesdk-extractrc

%description scripts-extractrc
A Perl script, it extracts the strings in an application's .rc file,
e.g. testappui.rc, and writes into the pot file where the translations
are build with (po-files).

%description scripts-extractrc -l pl
Skrypt napisany w Perlu, kt�ry wyci�ga �a�cuchy z plik�w .rc
aplikacji, np. testappgui.rc i zapisuje je do plik�w pot, z kt�rych
tworzy si� t�umaczenia (pliki po).

%package scripts-findmissingcrystal
Summary:	A script for finding missing crystal icons
Summary(pl):	Skrypt do wyszukiwania brakuj�cych ikon z tematu crystal
Group:		X11/Development/Tools

%description scripts-findmissingcrystal
A script for finding missing crystal icons.

%description scripts-findmissingcrystal -l pl
Skrypt do wyszukiwania brakuj�cych ikon z tematu crystal.

%package scripts-kdekillall
Summary:	A script for killing KDE apps started with kdeinit
Summary(pl):	Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description scripts-kdekillall
A script for killing KDE apps started with kdeinit.

%description scripts-kdekillall -l pl
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scripts-kdelnk2desktop
Summary:	A kdelnk to desktop converter
Summary(pl):	Konwerter plik�w kdelnk na desktop
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description scripts-kdelnk2desktop
A kdelnk to desktop converter.

%description scripts-kdelnk2desktop -l pl
Konwerter plik�w kdelnk na desktop.

%package scripts-zonetab2pot
Summary:	A zone.tab to .pot converter
Summary(pl):	Konwerter plik�w zone.tab na .pot
Group:		X11/Development/Tools
Requires:	/usr/bin/python
Requires:	gettext-devel
Obsoletes:	kdesdk-devel

%description scripts-zonetab2pot
This script reads timezone list as its first argument or from
/usr/share/zoneinfo/zone.tab, and converts it to a PO file template.

%description scripts-zonetab2pot -l pl
Ten skrypt wczytuje list� stref czasowych z linii polece� lub pliku
/usr/share/zoneinfo/zone.tab i konwertuje je na plik POT.

%package scheck
Summary:	KDE Style - Scheck
Summary(pl):	Motyw KDE - Scheck
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description scheck
Development style for searching accelerator and style guide conflicts.

%description scheck -l pl
Motyw KDE przeznaczony do szukania konflikt�w w akceleratorach oraz
sprawdzania zgodno�ci z wytycznymi dot. wygl�du graficznego aplikacji
KDE.

%package umbrello
Summary:	UML Modeler
Summary(pl):	Modeler UML
Group:		X11/Development/Tools
Obsoletes:	kdesdk-devel

%description umbrello
Umbrello UML Modeller is a UML diagram tool that can support you in
the software development process. Especially during the analysis and
design phases of this process, Umbrello UML Modeller will help you to
get a high quality product. UML can also be used to document your
software designs to help you and your fellow developers.

UML is the diagramming language used to describing such models. You
can represent your ideas in UML using different types of diagrams.
Umbrello UML Modeller 1.2 supports the following types:
- class Diagram
- sequence Diagram
- collaboration Diagram
- use Case Diagram
- state Diagram
- activity Diagram
- component Diagram

%description umbrello -l pl
Modeler UML.

%package xemacs
Summary:	A set of macros for xemacs
Summary(pl):	Zestaw makr do xemacsa
Group:		X11/Development/Tools
Requires:	xemacs-common
Obsoletes:	kdesdk-devel

%description xemacs
A set of macros for xemacs useful for developing KDE applications.

%description xemacs -l pl
Zestaw makr do xemacsa.

%prep
%setup -q
%patch100 -p1
%patch0 -p1
%patch1 -p1 

echo "KDE_OPTIONS=nofinal" >> umbrello/umbrello/dialogs/Makefile.am
echo "KDE_OPTIONS=nofinal" >> umbrello/umbrello/classparser/Makefile.am

%build
cp -f %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
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
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%{__make} -C kstartperf install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir},%{_emacspkgdir}/kde} \
	$RPM_BUILD_ROOT{%{_xemacspkgdir}/kde,%{_zshfcdir},%{_sysconfdir}/bash_completion.d}

install ./kdepalettes/KDE_Gimp		$RPM_BUILD_ROOT%{_gimpdir}/palettes
cp ./kdepalettes/kde_xpaintrc		$RPM_BUILD_ROOT%{_appdefsdir}/XPaint.kde
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_emacspkgdir}/kde
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_xemacspkgdir}/kde
cp ./scripts/completions/zsh/_*		$RPM_BUILD_ROOT%{_zshfcdir}
cp ./scripts/completions/bash/dcop	$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

cd $RPM_BUILD_ROOT
rm -rf `find . -name CVS`
cd -

# Debian manpages
# overwrites cvscheck.1 - it's OK (original manual is much shorter)
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

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

%files kfile
%defattr(644,root,root,755)
%doc README
%{_libdir}/kde3/kfile_[!dp]*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_[!dp]*.so
%{_datadir}/services/kfile_cpp.desktop
%{_datadir}/services/kfile_h.desktop
%{_datadir}/services/kfile_ts.desktop

%files cervisia
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
%{_mandir}/man1/cervisia.1*
%{_kdedocdir}/en/cervisia

%files cervisia-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcvsservice.so
%{_includedir}/cvsjob_stub.h
%{_includedir}/cvsservice_stub.h
%{_includedir}/repository_stub.h

%files completions-bash
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*

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
%{_mandir}/man1/kapptemplate.1*

%files kaddressbook-kdeaccounts
%defattr(644,root,root,755)
%{_libdir}/kde3/kabcformat_kdeaccounts.la
%attr(755,root,root) %{_libdir}/kde3/kabcformat_kdeaccounts.so
%{_datadir}/apps/kabc/formats/*

%files kbabel
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
%{_mandir}/man1/kbabel.1*
%{_kdedocdir}/en/kbabel

%files kbabel-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbabelcommon.so
%attr(755,root,root) %{_libdir}/libkbabeldictplugin.so
%{_includedir}/kbabel

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
%{_mandir}/man1/catalogmanager.1*

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
%{_mandir}/man1/kbabeldict.1*

%files kbugbuster
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_datadir}/apps/kbugbuster
%{_desktopdir}/kde/kbugbuster.desktop
%{_iconsdir}/[!l]*/*/*/kbugbuster.png
%{_mandir}/man1/kbugbuster.1*
%{_kdedocdir}/en/kbugbuster

%files kcachegrind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcachegrind
%{_datadir}/apps/kcachegrind
%{_datadir}/mimelnk/application/x-kcachegrind.desktop
%{_desktopdir}/kde/kcachegrind.desktop
%{_iconsdir}/hicolor/*/apps/kcachegrind.png
%{_mandir}/man1/kcachegrind.1*
%{_kdedocdir}/en/kcachegrind


%files kmtrace
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/demangle
%attr(755,root,root) %{_bindir}/kminspector
%attr(755,root,root) %{_bindir}/kmmatch
%attr(755,root,root) %{_bindir}/kmtrace
%{_libdir}/libktrace*.la
%attr(755,root,root) %{_libdir}/libktrace*.so*
%{_includedir}/ktrace.h
%{_datadir}/apps/kmtrace
##%{_mandir}/man1/demangle.1*
##%{_mandir}/man1/kminspector.1*
##%{_mandir}/man1/kmmatch.1*
##%{_mandir}/man1/kmtrace.1*

%files kompare
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
%{_mandir}/man1/kompare.1*
%{_kdedocdir}/en/kompare

%files kprofilemethod
%defattr(644,root,root,755)
%{_includedir}/kprofilemethod.h

%files kspy
%defattr(644,root,root,755)
%{_libdir}/libkspy.la
%{_libdir}/libkspy.so
%attr(755,root,root) %{_libdir}/libkspy.so.*.*.*
%{_includedir}/kspy.h
%{_mandir}/man1/testkspy.1*

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
%{_iconsdir}/[!l]*/*/apps/kuiviewer.png
%{_mandir}/man1/kuiviewer.1*

%files pallette-gimp
%defattr(644,root,root,755)
%{_gimpdir}/palettes

%files pallette-xpaint
%defattr(644,root,root,755)
%{_appdefsdir}/*

%files po2xml
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/fixsgml
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/transxx
%attr(755,root,root) %{_bindir}/xml2pot
#%{_mandir}/man1/fixsgml.1*
%{_mandir}/man1/po2xml.1*
%{_mandir}/man1/split2po.1*
%{_mandir}/man1/swappo.1*
%{_mandir}/man1/transxx.1*
%{_mandir}/man1/xml2pot.1*

%files scheck
%defattr(644,root,root,755)
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
%{_mandir}/man1/adddebug.1*
%{_mandir}/man1/cheatmake.1*
%{_mandir}/man1/create*.1*
%{_mandir}/man1/extend_dmalloc.1*
%{_mandir}/man1/fixkdeincludes.1*
%{_mandir}/man1/includemocs.1*
%{_mandir}/man1/kde-build.1*
%{_mandir}/man1/licensecheck.1*
%{_mandir}/man1/makeobj.1*

%files scripts-cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs*
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/pruneemptydirs
%{_mandir}/man1/cvs*.1*
%{_mandir}/man1/noncvslist.1*
%{_mandir}/man1/pruneemptydirs.1*

%files scripts-cxxmetric
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxxmetric
%{_mandir}/man1/cxxmetric.1*

%files scripts-doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdedoc
%attr(755,root,root) %{_bindir}/qtdoc
%{_mandir}/man1/kdedoc.1*
%{_mandir}/man1/qtdoc.1*

%files scripts-extractrc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extractrc
%{_mandir}/man1/extractrc.1*

%files scripts-findmissingcrystal
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/findmissingcrystal
%{_mandir}/man1/findmissingcrystal.1*

%files scripts-kdekillall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdekillall
%{_mandir}/man1/kdekillall.1*

%files scripts-kdelnk2desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py
%{_mandir}/man1/kdelnk2desktop.py.1*

%files scripts-zonetab2pot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zonetab2pot.py
%{_mandir}/man1/zonetab2pot.py.1*

%files umbrello
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
%{_iconsdir}/crystalsvg/*/*/umbrello*.*
%{_mandir}/man1/umbrello.1*
%{_kdedocdir}/en/umbrello

%files xemacs
%defattr(644,root,root,755)
%{_xemacspkgdir}/kde
