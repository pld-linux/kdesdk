%bcond_with	cvs	# cvs bcond

%define		_state		snapshots
%define		_ver		3.2.91
%define		_snap		040702
%define		_packager	adgor

%define		_minlibsevr	9:3.2.90.040524
%define		_minbaseevr	9:3.2.90.040524

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		3
License:	GPL
Group:		X11/Development/Tools
%if ! %{with cvs}
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
#Source0:	%{name}-%{_snap}.tar.bz2
##%% Source0-md5:	dcdb8ca2f0855b415138e09bc3965106
%else
Source0:	kdesource.tar.gz
%endif
Patch0:		%{name}-am.patch
URL:		http://www.kde.org/
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
BuildRequires:	kdebase-devel >= %{_minbaseevr}
BuildRequires:	libltdl-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
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
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package kfile
Summary:	Developers' file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach u¿ywanych przez programistów
Group:		X11/Development/Libraries
Requires:	konqueror >= %{_minbaseevr}

%description kfile
This package adds a tab to konqueror "file properties" dialog window
with file enhanced informations for C++ source files, diff files,
gettext and designer translation sourcefiles.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w³a¶ciwo¶ci pliku" konquerora
dodatkow± zak³adkê z rozszerzonymi informacjami o pliku.

%package cervisia
Summary:	A KDE CVS frontend
Summary(pl):	Frontend do CVS dla KDE
Group:		X11/Development/Tools
Requires:	cvs >= 1.10
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-libcvsservice = %{epoch}:%{version}-%{release}

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
Frontend do CVS dla KDE. Ma nastêpuj±ce mo¿liwo¶ci:
- uaktualnianie lub odtwarzanie stanu katalogu lub pojedynczych
  plików; pliki s± wy¶wietlane w ró¿nych kolorach zale¿nie od ich stanu,
  a pokazywane pliki mog± byæ filtrowane wed³ug ich stanu
- podstawowe operacje, takie jak dodawanie, usuwanie i commitowanie
  plików
- zaawansowane operacje, takie jak dodawanie i usuwanie ¶ledzenia,
  w³±czanie i wy³±czanie edycji plików, blokowanie i odblokowywanie
- pobieranie i importowanie modu³ów
- graficzne wy¶wietlanie ró¿nic wzglêdem repozytorium i miêdzy ró¿nymi
  rewizjami
- widok pliku opisany winnymi
- widok loga komentarzy do zmian w postaci drzewa i listy
- rozwi±zywanie konfliktów w pliku
- tagowanie i branchowanie
- uaktualnianie do taga, brancha lub daty
- edytor changelogów po³±czony z oknem dialogowym do commitowania.

%package completions-bash
Summary:	Autocomplete definitions for bash
Summary(pl):	Definicje autouzupe³niania dla basha
Group:		Applications/Shells
Requires:	bash-completion

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl
Definicje autouzupe³niania dla basha.

%package completions-zsh
Summary:	Autocomplete definitions for zsh
Summary(pl):	Definicje autouzupe³niania dla zsh
Group:		Applications/Shells
Requires:	zsh >= 4.0.6-2

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl
Definicje autouzupe³niania dla zsh.

%package emacs
Summary:	A set of macros for emacs
Summary(pl):	Zestaw makr do emacsa
Group:		X11/Development/Tools
Requires:	emacs-common

%description emacs
A set of macros for emacs.

%description emacs -l pl
Zestaw makr do emacsa.

%package kaddressbook-kdeaccounts
Summary:	A kdeaccounts plugin for the KDE adressbook
Summary(pl):	Wtyczka do ksi±¿ki adresowej KDE dodaj±ca obs³ugê kdeaccounts
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8

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
Obsoletes:	kdesdk-kbabel-catalog
Obsoletes:	kdesdk-kbabel-dictionary

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

Also contains KBabel catalog manager. It features:
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

%description kbabel -l pl
KBabel jest narzêdziem, które pozwala na ³atwe zarz±dzanie, edycjê i
utrzymanie plików gettexta .po. Jego mo¿liwo¶ci to:
- obs³uga plików PO GNU gettexta (w³±cznie z formami mnogimi) oraz
  katalogów Qt Linguista
- mo¿liwo¶æ otwierania wielu plików (lub wielu widoków tego samego
  pliku)
- pe³na funkcjonalno¶æ edycyjna, dostêpna poprzez graficzny interfejs
  u¿ytkownika, a tak¿e poprzez definiowalne skróty klawiszowe
- potê¿na funkcjonalno¶æ kontroli pisowni
- pe³ne mo¿liwo¶ci nawigacji (takiej jak przechodzenie do nastêpnego
  niepewnego lub nieprzet³umaczonego napisu)
- mo¿liwo¶æ zapisu i odczytu plików kodowanych w unikodzie (utf-8)
- nieograniczona mo¿liwo¶æ cofania zmian
- pod¶wietlanie sk³adni, automatyczne uaktualnianie nag³ówków plików,
  automatyczna zmiana stanu "fuzzy" po przet³umaczeniu komunikatu
- obs³uga ³atwego wstawiania znaczników i URL-i
- sprawdzanie poprawno¶ci i pod¶wietlanie znaczników i elementów XML
- szkielet wtyczek dla s³owników, takich jak pliki kompendiów po, do
  sprawdzania spójno¶ci lub podpowiadania t³umaczeñ
- funkcja "zgrubnego t³umaczenia" do inicjowania nieprzet³umaczonych
  komunikatów podpowiedziami ze s³ownika
- automatyczna kontrola sk³adni przy u¿yciu msgfmt przy zapisie, ³atwe
  przechodzenie do odpowiednich wpisów, je¶li wyst±pi³ b³±d
- ró¿ne metody pokazywania odstêpów na koñcach linii i sprawdzania
  spójno¶ci przet³umaczonych komunikatów, takiej jak porównywanie printf
  i Qt
- obs³uga parametrów w msgid i msgstr
- szybki podgl±d kontekstu w pliku po
- pokazywanie kodu ¼ród³owego po odno¶nikach w komentarzach do
  komunikatów.

Zawiera te¿ zarz±dce katalogów zintegrowany z KBabel. Jego mo¿liwo¶ci
to:
- widok zarz±dcy plików dla katalogów kde-i18n (lub podobnie
  skonstruowanych), pokazuj±cy aktualny stan ka¿dego pliku PO: czy
  wymagaj± przegl±du, jak du¿o niepewnych i nieprzet³umaczonych napisów
  zawieraj± itp.; widok ten jest automatycznie uaktualniany i
  odzwierciedla wszystkie zmiany dokonane w plikach, w³±cznie ze
  zmianami w programach innych ni¿ KBabel
- zintegrowana obs³uga CVS
- ró¿ne mechanizmy otwierania plików do edycji w KBabel: "przeci±gnij
  i upu¶æ", podwójne klikniêcie, menu kontekstowe
- funkcja zaznaczania plików (np. do identyfikowania plików PO, za
  które odpowiadaj± inni t³umacze)
- nawigacja z u¿yciem statystyk plików PO
- automatyczne porównywanie i statystyki plików POT i PO dla szybkiego
  przegl±du, które i jak du¿o plików zosta³o przet³umaczonych, a które
  mog± byæ przestarza³e
- kontrola sk³adni (msgfmt --statistics) dla istniej±cych plików w
  celu sprawdzenia, czy przet³umaczone pliki siê skompiluj± i bêd±
  dzia³aæ po rozpowszechnieniu
- konfigurowalne polecenia, które mo¿na wykonywaæ z menu kontekstowego
  zarz±dcy katalogów
- funkcje szukaj/zast±p w wielu plikach naraz
- kontrola pisowni w wielu plikach naraz
- wykonywanie "zgrubnego t³umaczenia" wielu plików naraz.

%package kbabel-devel
Summary:	KBabel header files
Summary(pl):	Pliki nag³ówkowe KBabel
Group:		X11/Development/Libraries
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}
Requires:	%{name}-kbabel-catalog = %{epoch}:%{version}-%{release}
Requires:	%{name}-kbabel-dictionary = %{epoch}:%{version}-%{release}

%description kbabel-devel
KBabel header files.

%description kbabel-devel -l pl
Pliki nag³ówkowe KBabel.

%package kbugbuster
Summary:	A tools that allows cooperation with bugs.kde.org
Summary(pl):	Narzêdzie wspó³pracuj±ce z bugs.kde.org
Group:		X11/Development/Tools

%description kbugbuster
KBugBuster allows easy bug management on bugs.kde.org.

%description kbugbuster -l pl
KBugBuster u³atwia wyszukiwanie i zarz±dzanie b³êdami na bugs.kde.org.

%package kcachegrind
Summary:	KCachegrind - visualization of traces generated by profiling
Summary(pl):	KCachegrind - wizualizacja ¶cie¿ek tworzonych przez profilowanie
Group:		X11/Development/Tools

%description kcachegrind
KCachegrind visualizes traces generated by profiling.

%description kcachegrind -l pl
KCachegrind wizualizuje ¶cie¿ki tworzone przez profilowanie.

%package kmtrace
Summary:	A mtrace to full backtrace conversion tool
Summary(pl):	Narzêdzie do konwersji z mtrace do pe³nego backtrace'a
Group:		X11/Development/Tools

%description kmtrace
kmtrace converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl
kmtrace konwertuje mtrace glibca do pe³nego backtrace'a.

%package kompare
Summary:	Kompare - a program to view the differences between files
Summary(pl):	Kompare - program s³u¿±cy do porównywania zmian miêdzy plikami
Group:		X11/Development/Tools
Conflicts:	kdesdk-kbugbuster < 3:3.2.90.040517-3

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
Kompare to program s³u¿±cy do porównywania zmian miêdzy plikami.
Aktualnie dostêpne funkcje:
  - porównanie plików lub katalogów poprzez graficzny interfejs
  - przedstawienie ¼ród³a i celu za pomoc± krzywej Beziera
  - graficzne przegl±danie ³at w formatach diff, unidiff, context i
    zwyk³ym
  - interaktywne wprowadzanie zmian
  - przezroczysto¶æ sieciowa
  - mo¿liwo¶æ ogl±dania wyj¶cia diff w wewnêtrznej przegl±darce
  - ³atwa nawigacja miêdzy wieloplikowymi diffami wraz z dokowalnym
    drzewem
  - zamiana ¼ród³a i celu za pomoc± pojedynczej komendy
  - statystyki diffów

%package kprofilemethod
Summary:	Kprofilemethod - a set of macros which help profiling using QTime
Summary(pl):	Kprofilemethod - zestaw makr u³atwiaj±cych profilowanie z wykorzystaniem QTime
Group:		X11/Development/Tools

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

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl
Narzêdzie s³u¿±ce do pomiaru czasu ³adowania aplikacji KDE.

%package kuiviewer
Summary:	Qt Designer UI file Viewer
Summary(pl):	Przegl±darka plików UI generowanych przez QT designera
Group:		X11/Development/Tools

%description kuiviewer
Qt Designer UI file Viewer.

%description kuiviewer -l pl
Przegl±darka plików UI generowanych przez QT designera.

%package libcvsservice
Summary:	A cvs access library
Summary(pl):	Biblioteka dostêpu do cvs
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Conflicts:	kdesdk-cervisia < 3:3.2.90.040516-2

%description libcvsservice
A library for access to CVS repositories for KDE apps.

%description libcvsservice -l pl
Biblioteka s³u¿±ca do kontroli repozytoriów CVS z poziomu aplikacji
KDE.

%package libcvsservice-devel
Summary:	A cvsservice library - header files
Summary(pl):	Biblioteka cvsservice - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-libcvsservice = %{epoch}:%{version}-%{release}
Obsoletes:	kdesdk-cervisia-devel

%description libcvsservice-devel
A cvsservice library - header files.

%description libcvsservice-devel -l pl
Biblioteka cvsservice - pliki nag³ówkowe.

%package pallette-gimp
Summary:	Package which adds the KDE Default pallette to GIMP
Summary(pl):	Pakiet dodaj±cy domy¶ln± paletê kolorów KDE do GIMP-a
Group:		X11/Applications/Graphics
Requires:	gimp

%description pallette-gimp
This package adds the KDE Default pallette to GIMP.

%description pallette-gimp -l pl
Pakiet dodaj±cy domy¶ln± paletê kolorów KDE do GIMP-a.

%package pallette-xpaint
Summary:	Package which adds the KDE Default pallette to XPaint
Summary(pl):	Pakiet dodaj±cy domy¶ln± paletê kolorów KDE do XPainta
Group:		X11/Applications/Graphics
Requires:	xpaint

%description pallette-xpaint
This package adds the KDE Default pallette to XPaint.

%description pallette-xpaint -l pl
Pakiet dodaj±cy domy¶ln± paletê kolorów KDE do XPainta.

%package po2xml
Summary:	An xml2po and vice versa converters
Summary(pl):	Konwertery po2xml i vice versa
Group:		X11/Development/Tools
Requires:	/usr/bin/python

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl
Konwertery po2xml i vice versa.

%package scripts-build
Summary:	An set of scripts useful for building KDE
Summary(pl):	Zestaw skryptów do kompilowania KDE
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-build
A set of scripts useful for building KDE.

%description scripts-build -l pl
Zestaw skryptów do kompilowania KDE.

%package scripts-cvs
Summary:	A set of scripts for maintaining KDE from CVS
Summary(pl):	Zestaw skryptów do zarz±dzania KDE z CVS
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-cvs
A set of scripts for maintaining KDE from CVS.

%description scripts-cvs -l pl
Zestaw skryptów do zarz±dzania KDE z CVS.

%package scripts-doc
Summary:	A set of scripts for quick access to Qt/KDE documentation
Summary(pl):	Zestaw skryptów szybkiego dostêpu do dokumentacji Qt/KDE
Group:		X11/Development/Tools

%description scripts-doc
A set of scripts for quick access to Qt/KDE documentation.

%description scripts-doc -l pl
Zestaw skryptów szybkiego dostêpu do dokumentacji Qt/KDE.

%package scripts-kdekillall
Summary:	A script for killing KDE apps started with kdeinit
Summary(pl):	Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit
Group:		X11/Development/Tools

%description scripts-kdekillall
A script for killing KDE apps started with kdeinit.

%description scripts-kdekillall -l pl
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scripts-misc
Summary:	Miscellaneous scripts for maintaining KDE
Summary(pl):	Ró¿ne skrypty do utrzymywania KDE
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	kdesdk-extractrc
Obsoletes:	kdesdk-scripts-cxxmetric
Obsoletes:	kdesdk-scripts-extractrc
Obsoletes:	kdesdk-scripts-findmissingcrystal
Obsoletes:	kdesdk-scripts-kdelnk2desktop
Obsoletes:	kdesdk-scripts-zonetab2pot

%description scripts-misc
This package contains:
- A Perl script, it extracts the strings in an application's .rc file,
  e.g. testappui.rc, and writes into the pot file where the translations
  are build with (po-files).

- A script that counts lines of code, comments and blank space in C
  and C++ source files.

- A script for finding missing crystal icons.

- A kdelnk to desktop and zonetab2pot converter.

%description scripts-misc -l pl
Ten pakiet zawiera:
- Skrypt napisany w Perlu, który wyci±ga ³añcuchy z plików .rc
  aplikacji, np. testappgui.rc i zapisuje je do plików pot, z których
  tworzy siê t³umaczenia (pliki po).

- Skrypt zliczaj±cy linijki kodu, komentarzy i znaków bia³ych w
  plikach ¼ród³owych C i C++.

- Skrypt do wyszukiwania brakuj±cych ikon z tematu crystal.

- Konwerter plików kdelnk na desktop i zonetab na pot.

%package scheck
Summary:	KDE Style - Scheck
Summary(pl):	Motyw KDE - Scheck
Group:		X11/Development/Tools

%description scheck
Development style for searching accelerator and style guide conflicts.

%description scheck -l pl
Motyw KDE przeznaczony do szukania konfliktów w akceleratorach oraz
sprawdzania zgodno¶ci z wytycznymi dot. wygl±du graficznego aplikacji
KDE.

%package umbrello
Summary:	UML Modeler
Summary(pl):	Modeler UML
Group:		X11/Development/Tools

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
Modeler UML Umbrello to narzêdzie do diagramów UML pomagaj±ce w
procesie tworzenia oprogramowania. Szczególnie podczas etapów analizy
i projektowania, modeler UML Umbrello mo¿e pomóc w uzyskaniu wysokiej
jako¶ci produktu. UML mo¿e byæ u¿ywany do dokumentowania projektu
programu, aby pomóc programi¶cie i jego wspó³pracownikom.

UML to jêzyk diagramów u¿ywany do opisu takich modeli. Mo¿na
przedstawiaæ idee w UML-u przy u¿yciu ró¿nych rodzajów diagramów.
Modeler UML Umbrello 1.2 obs³uguje nastêpuj±ce rodzaje:
 - diagram klas
 - diagram sekwencji
 - diagram wspó³pracy
 - diagram przypadków u¿ycia
 - diagram stanów
 - diagram aktywno¶ci
 - diagram sk³adników.

%package xemacs
Summary:	A set of macros for xemacs
Summary(pl):	Zestaw makr do xemacsa
Group:		X11/Development/Tools
Requires:	xemacs-common

%description xemacs
A set of macros for xemacs.

%description xemacs -l pl
Zestaw makr do xemacsa.

%prep
%if ! %{with cvs}
%setup -q -n %{name}-%{_snap}
%else
%setup -q -n %{name} -D
%endif
%patch0 -p1

echo "KDE_OPTIONS = nofinal" >> cervisia/Makefile.am
echo "KDE_OPTIONS = nofinal" >> umbrello/umbrello/classparser/Makefile.am
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;GUIDesigner;/' \
	kuiviewer/kuiviewer.desktop

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;RevisionControl;/' \
	cervisia/cervisia.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Profiling;/' \
	kcachegrind/kcachegrind/kcachegrind.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;ProjectManagement;/' \
	kbugbuster/kbugbuster.desktop

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Translation;/' \
	kbabel/catalogmanager/catalogmanager.desktop

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Translation;/' \
	kbabel/kbabeldict/kbabeldict.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Translation;/' \
	kbabel/kbabel/kbabel.desktop

%build
cp %{_datadir}/automake/config.sub admin

export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

# Used in cervisia Makefile
export kde_htmldir=%{_kdedocdir}

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

# Undefined references
%{__make} -C kstartperf

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%{__make} -C kstartperf install \
	DESTDIR=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d \
	$RPM_BUILD_ROOT%{_appdefsdir} \
	$RPM_BUILD_ROOT%{_gimpdir}/palettes \
	$RPM_BUILD_ROOT%{_emacspkgdir}/kde \
	$RPM_BUILD_ROOT%{_xemacspkgdir}/kde \
	$RPM_BUILD_ROOT%{_zshfcdir} \
	$RPM_BUILD_ROOT%{_mandir}/man1

cp ./scripts/completions/bash/dcop	$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
cp ./kdepalettes/kde_xpaintrc		$RPM_BUILD_ROOT%{_appdefsdir}/XPaint.kde
install ./kdepalettes/KDE_Gimp		$RPM_BUILD_ROOT%{_gimpdir}/palettes
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_emacspkgdir}/kde
cp ./scripts/kde-emacs/*.*		$RPM_BUILD_ROOT%{_xemacspkgdir}/kde
cp ./scripts/completions/zsh/_*		$RPM_BUILD_ROOT%{_zshfcdir}

rm -rf `find $RPM_BUILD_ROOT -name CVS`

# Debian manpages
# overwrites cvscheck.1 - it's OK (original manual is much shorter)
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang	cervisia	--with-kde
%find_lang	kbabel		--with-kde
%find_lang	kcachegrind	--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde
%find_lang	umbrello	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	kbabel			-p /sbin/ldconfig
%postun	kbabel			-p /sbin/ldconfig

%post	kompare			-p /sbin/ldconfig
%postun	kompare			-p /sbin/ldconfig

%post	kspy			-p /sbin/ldconfig
%postun	kspy			-p /sbin/ldconfig

%post	kstartperf		-p /sbin/ldconfig
%postun	kstartperf		-p /sbin/ldconfig

%post	libcvsservice		-p /sbin/ldconfig
%postun	libcvsservice		-p /sbin/ldconfig

%files kfile
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
%{_libdir}/kde3/libcervisiapart.la
%attr(755,root,root) %{_libdir}/kde3/libcervisiapart.so
%{_datadir}/apps/cervisia*
%{_datadir}/config.kcfg/cervisiapart.kcfg
%{_datadir}/apps/kconf_update/change_colors.pl
%{_datadir}/apps/kconf_update/cervisia.upd
%{_datadir}/apps/kconf_update/move_repositories.pl
%{_datadir}/services/cvsservice.desktop
%{_desktopdir}/kde/cervisia.desktop
%{_iconsdir}/*/*/*/cervisia.png
%{_mandir}/man1/cervisia.1*

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
%{_datadir}/config.kcfg/kbabel.kcfg
%{_datadir}/apps/kconf_update/kbabel-project.upd
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
# catalog part
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
# dictionary part
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

%files kbabel-devel
%defattr(644,root,root,755)
%{_includedir}/kbabel
%attr(755,root,root) %{_libdir}/libkbabelcommon.so
%attr(755,root,root) %{_libdir}/libkbabeldictplugin.so

%files kbugbuster -f kbugbuster.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_libdir}/kde3/kcal_bugzilla.la
%attr(755,root,root) %{_libdir}/kde3/kcal_bugzilla.so
%{_datadir}/apps/kbugbuster
# this dir belongs to kdepim
%{_datadir}/services/kresources/kcal/bugzilla.desktop
%{_desktopdir}/kde/kbugbuster.desktop
%{_iconsdir}/[!l]*/*/*/kbugbuster.png
%{_mandir}/man1/kbugbuster.1*

%files kcachegrind -f kcachegrind.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcachegrind
%{_datadir}/apps/kcachegrind
%{_datadir}/mimelnk/application/x-kcachegrind.desktop
%{_desktopdir}/kde/kcachegrind.desktop
%{_iconsdir}/hicolor/*/apps/kcachegrind.png
%{_mandir}/man1/kcachegrind.1*

# -- doesn't build with glibc >= 2.3
%files kmtrace
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/demangle
%attr(755,root,root) %{_bindir}/kminspector
%attr(755,root,root) %{_bindir}/kmmatch
%attr(755,root,root) %{_bindir}/kmtrace
%{_libdir}/libktrace*.la
%attr(755,root,root) %{_libdir}/libktrace*.so*
%{_libdir}/libktrace*.a
%{_includedir}/ktrace.h
%{_datadir}/apps/kmtrace
#%{_mandir}/man1/demangle.1*
#%{_mandir}/man1/kminspector.1*
#%{_mandir}/man1/kmmatch.1*
#%{_mandir}/man1/kmtrace.1*

%files kompare -f kompare.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%{_libdir}/libkompareinterface.la
%attr(755,root,root) %{_libdir}/libkompareinterface.so
%attr(755,root,root) %{_libdir}/libkompareinterface.so.*.*.*
%{_libdir}/kde3/kfile_diff.la
%attr(755,root,root) %{_libdir}/kde3/kfile_diff.so
# TODO: this is shared lib - why in kde3 dir?
%{_libdir}/kde3/libdialogpages.la
%attr(755,root,root) %{_libdir}/kde3/libdialogpages.so*
%{_libdir}/kde3/libkomparenavtreepart.la
%attr(755,root,root) %{_libdir}/kde3/libkomparenavtreepart.so
%{_libdir}/kde3/libkomparepart.la
%attr(755,root,root) %{_libdir}/kde3/libkomparepart.so
%{_datadir}/apps/kompare*
%{_datadir}/services/kfile_diff.desktop
%{_datadir}/services/kompare*.desktop
%{_datadir}/servicetypes/kompare*.desktop
%{_desktopdir}/kde/kompare.desktop
%{_iconsdir}/[!l]*/*/*/kompare.*
%{_mandir}/man1/kompare.1*

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

%files libcvsservice
%defattr(644,root,root,755)
%{_libdir}/libcvsservice.la
%attr(755,root,root) %{_libdir}/libcvsservice.so.*.*.*

%files libcvsservice-devel
%defattr(644,root,root,755)
%{_includedir}/cvsjob_stub.h
%{_includedir}/cvsservice_stub.h
%{_includedir}/repository_stub.h
%attr(755,root,root) %{_libdir}/libcvsservice.so

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
%attr(755,root,root) %{_bindir}/cheatmake
%attr(755,root,root) %{_bindir}/extend*
%attr(755,root,root) %{_bindir}/fixkdeincludes
%attr(755,root,root) %{_bindir}/fixuifiles
%attr(755,root,root) %{_bindir}/includemocs
%attr(755,root,root) %{_bindir}/kde-build
%attr(755,root,root) %{_bindir}/kdemangen.pl
%attr(755,root,root) %{_bindir}/licensecheck
%attr(755,root,root) %{_bindir}/makeobj
%{_mandir}/man1/adddebug.1*
%{_mandir}/man1/cheatmake.1*
%{_mandir}/man1/create*.1*
%{_mandir}/man1/extend_dmalloc.1*
%{_mandir}/man1/fixkdeincludes.1*
%{_mandir}/man1/includemocs.1*
%{_mandir}/man1/kde-build.1*
%{_mandir}/man1/licensecheck.1*
%{_mandir}/man1/makeobj.1*
# TODO
# Merge all scripts into one subpkg?
%attr(755,root,root) %{_bindir}/dprof2calltree
%attr(755,root,root) %{_bindir}/hotshot2calltree
%attr(755,root,root) %{_bindir}/memprof2calltree
%attr(755,root,root) %{_bindir}/op2calltree
%attr(755,root,root) %{_bindir}/png2mng.pl
%attr(755,root,root) %{_bindir}/pprof2calltree

%files scripts-cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs*
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/pruneemptydirs
%{_mandir}/man1/cvs*.1*
%{_mandir}/man1/noncvslist.1*
%{_mandir}/man1/pruneemptydirs.1*

%files scripts-doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdedoc
%attr(755,root,root) %{_bindir}/qtdoc
%{_mandir}/man1/kdedoc.1*
%{_mandir}/man1/qtdoc.1*

%files scripts-kdekillall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdekillall
%{_mandir}/man1/kdekillall.1*

%files scripts-misc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxxmetric
%attr(755,root,root) %{_bindir}/extractrc
%attr(755,root,root) %{_bindir}/findmissingcrystal
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py
%attr(755,root,root) %{_bindir}/package_crystalsvg
%attr(755,root,root) %{_bindir}/zonetab2pot.py
%{_mandir}/man1/cxxmetric.1*
%{_mandir}/man1/extractrc.1*
%{_mandir}/man1/findmissingcrystal.1*
%{_mandir}/man1/kdelnk2desktop.py.1*
%{_mandir}/man1/zonetab2pot.py.1*

%files umbrello -f umbrello.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/umbrello
%{_datadir}/apps/umbrello
%{_datadir}/mimelnk/application/x-umbrello.desktop
%{_desktopdir}/kde/umbrello.desktop
%{_iconsdir}/hicolor/*/apps/umbrello.png
%{_iconsdir}/hicolor/*/mimetypes/umbrellofile.png
%{_iconsdir}/crystalsvg/*/*/umbrello*.*
%{_mandir}/man1/umbrello.1*

%files xemacs
%defattr(644,root,root,755)
%{_xemacspkgdir}/kde
