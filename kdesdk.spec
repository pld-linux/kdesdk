#
%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}
#
Summary:	KDESDK - Software Development Kit for KDE
Summary(pl.UTF-8):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	3.5.8
Release:	1
Epoch:		3
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	c809c15eb8c09a7eb2d070395202910b
#Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-kompare-encoding.patch
Patch3:		kde-ac260-lt.patch
URL:		http://www.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
%ifarch %{x8664}
# for kmtrace
BuildRequires:	binutils-devel
%endif
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	emacs-common
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
BuildRequires:	kdebase-devel >= %{_minbaseevr}
BuildRequires:	kdepim-devel >= 3:3.3.1
BuildRequires:	libltdl-devel
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	sed >= 4.0
BuildRequires:	subversion-devel >= 0.37.0
Obsoletes:	kdesdk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gimpdir	%(gimptool --gimpdatadir 2>/dev/null)
%define		_appdefsdir	%{_datadir}/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/%(rpm -q --qf %{V} emacs-common | tr -d '[a-z]')
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
Software Development Kit for KDE.

%description -l pl.UTF-8
Pakiet wspomagający programowanie w środowisku KDE.

%package kfile
Summary:	Developers' file formats enhanced information
Summary(pl.UTF-8):	Rozszerzone informacje o plikach używanych przez programistów
Group:		X11/Development/Libraries
Requires:	konqueror >= %{_minbaseevr}

%description kfile
This package adds a tab to konqueror "file properties" dialog window
with file enhanced informations for C++ source files, diff files,
gettext and designer translation sourcefiles.

%description kfile -l pl.UTF-8
Ten pakiet dodaje do okna dialogowego "właściwości pliku" konquerora
dodatkową zakładkę z rozszerzonymi informacjami o pliku.

%package cervisia
Summary:	A KDE CVS frontend
Summary(pl.UTF-8):	Frontend do CVS dla KDE
Group:		X11/Development/Tools
Requires:	%{name}-libcvsservice = %{epoch}:%{version}-%{release}
Requires:	cvs >= 1.10
Requires:	kdebase-core >= %{_minbaseevr}
Conflicts:	kdesdk-scripts-cvs < 3:3.3.0-1

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

%description cervisia -l pl.UTF-8
Frontend do CVS dla KDE. Ma następujące możliwości:
- uaktualnianie lub odtwarzanie stanu katalogu lub pojedynczych
  plików; pliki są wyświetlane w różnych kolorach zależnie od ich stanu,
  a pokazywane pliki mogą być filtrowane według ich stanu
- podstawowe operacje, takie jak dodawanie, usuwanie i commitowanie
  plików
- zaawansowane operacje, takie jak dodawanie i usuwanie śledzenia,
  włączanie i wyłączanie edycji plików, blokowanie i odblokowywanie
- pobieranie i importowanie modułów
- graficzne wyświetlanie różnic względem repozytorium i między różnymi
  rewizjami
- widok pliku opisany winnymi
- widok loga komentarzy do zmian w postaci drzewa i listy
- rozwiązywanie konfliktów w pliku
- tagowanie i branchowanie
- uaktualnianie do taga, brancha lub daty
- edytor changelogów połączony z oknem dialogowym do commitowania.

%package completions-bash
Summary:	Autocomplete definitions for bash
Summary(pl.UTF-8):	Definicje autouzupełniania dla basha
Group:		Applications/Shells
Requires:	bash-completion

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl.UTF-8
Definicje autouzupełniania dla basha.

%package completions-zsh
Summary:	Autocomplete definitions for zsh
Summary(pl.UTF-8):	Definicje autouzupełniania dla zsh
Group:		Applications/Shells
Requires:	zsh >= 4.0.6-2

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl.UTF-8
Definicje autouzupełniania dla zsh.

%package emacs
Summary:	A set of macros for emacs
Summary(pl.UTF-8):	Zestaw makr do emacsa
Group:		X11/Development/Tools
# due versioned dir
%requires_eq emacs-common

%description emacs
A set of macros for emacs helpful for working on KDE programs.

%description emacs -l pl.UTF-8
Zestaw makr do emacsa pomocnych przy pracy nad programami KDE.

%package kde-resource-kdeaccounts
Summary:	A kdeaccounts plugin for the KDE PIM framework
Summary(pl.UTF-8):	Wtyczka do książki adresowej KDE dodająca obsługę kdeaccounts
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8
Obsoletes:	kaddressbook-kdeaccounts

%description kde-resource-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. It allows adding the
people from KDE's CVS accounts file to the addressbook.

%description kde-resource-kdeaccounts -l pl.UTF-8
Wtyczka do książki adresowej KDE dodająca obsługę kdeaccounts. Dodaje
ona osoby posiadające konta w CVS KDE do książki adresowej.

%package kde-resource-bugzilla
Summary:	A bugzilla plugin for the KDE PIM framework
Summary(pl.UTF-8):	Wtyczka do książki adresowej KDE dodająca obsługę bugzilli
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8

%description kde-resource-bugzilla
A KDE PIM plugin that allows creating bugzilla TODO lists.

%description kde-resource-bugzilla -l pl.UTF-8
Wtyczka KDE PIM umożliwiająca tworzenie list TODO w bugzilli.

%package kapptemplate
Summary:	KDE application framework generator
Summary(pl.UTF-8):	Generator szkieletu dla aplikacji KDE
Group:		X11/Development/Tools

%description kapptemplate
Modular shell script that will automatically create a framework for
either a normal KDE 3.x application, a KPart application, a KPart
plugin, or convert an existing application.

%description kapptemplate -l pl.UTF-8
Modularny skrypt, który potrafi automatycznie wygenerować szkielet
katalogów dla zwykłej aplikacji pod KDE 3.x, aplikacji KPart, wtyczki
KPart lub skonwertować istniejącą aplikację.

%package kbabel
Summary:	An advanced and easy to use PO-file editor
Summary(pl.UTF-8):	Rozbudowany i łatwy w obsłudze edytor plików PO
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

%description kbabel -l pl.UTF-8
KBabel jest narzędziem, które pozwala na łatwe zarządzanie, edycję i
utrzymanie plików gettexta .po. Jego możliwości to:
- obsługa plików PO GNU gettexta (włącznie z formami mnogimi) oraz
  katalogów Qt Linguista
- możliwość otwierania wielu plików (lub wielu widoków tego samego
  pliku)
- pełna funkcjonalność edycyjna, dostępna poprzez graficzny interfejs
  użytkownika, a także poprzez definiowalne skróty klawiszowe
- potężna funkcjonalność kontroli pisowni
- pełne możliwości nawigacji (takiej jak przechodzenie do następnego
  niepewnego lub nieprzetłumaczonego napisu)
- możliwość zapisu i odczytu plików kodowanych w unikodzie (utf-8)
- nieograniczona możliwość cofania zmian
- podświetlanie składni, automatyczne uaktualnianie nagłówków plików,
  automatyczna zmiana stanu "fuzzy" po przetłumaczeniu komunikatu
- obsługa łatwego wstawiania znaczników i URL-i
- sprawdzanie poprawności i podświetlanie znaczników i elementów XML
- szkielet wtyczek dla słowników, takich jak pliki kompendiów po, do
  sprawdzania spójności lub podpowiadania tłumaczeń
- funkcja "zgrubnego tłumaczenia" do inicjowania nieprzetłumaczonych
  komunikatów podpowiedziami ze słownika
- automatyczna kontrola składni przy użyciu msgfmt przy zapisie, łatwe
  przechodzenie do odpowiednich wpisów, jeśli wystąpił błąd
- różne metody pokazywania odstępów na końcach linii i sprawdzania
  spójności przetłumaczonych komunikatów, takiej jak porównywanie printf
  i Qt
- obsługa parametrów w msgid i msgstr
- szybki podgląd kontekstu w pliku po
- pokazywanie kodu źródłowego po odnośnikach w komentarzach do
  komunikatów.

Zawiera też zarządcę katalogów zintegrowany z KBabel. Jego możliwości
to:
- widok zarządcy plików dla katalogów kde-i18n (lub podobnie
  skonstruowanych), pokazujący aktualny stan każdego pliku PO: czy
  wymagają przeglądu, jak dużo niepewnych i nieprzetłumaczonych napisów
  zawierają itp.; widok ten jest automatycznie uaktualniany i
  odzwierciedla wszystkie zmiany dokonane w plikach, włącznie ze
  zmianami w programach innych niż KBabel
- zintegrowana obsługa CVS
- różne mechanizmy otwierania plików do edycji w KBabel: "przeciągnij
  i upuść", podwójne kliknięcie, menu kontekstowe
- funkcja zaznaczania plików (np. do identyfikowania plików PO, za
  które odpowiadają inni tłumacze)
- nawigacja z użyciem statystyk plików PO
- automatyczne porównywanie i statystyki plików POT i PO dla szybkiego
  przeglądu, które i jak dużo plików zostało przetłumaczonych, a które
  mogą być przestarzałe
- kontrola składni (msgfmt --statistics) dla istniejących plików w
  celu sprawdzenia, czy przetłumaczone pliki się skompilują i będą
  działać po rozpowszechnieniu
- konfigurowalne polecenia, które można wykonywać z menu kontekstowego
  zarządcy katalogów
- funkcje szukaj/zastąp w wielu plikach naraz
- kontrola pisowni w wielu plikach naraz
- wykonywanie "zgrubnego tłumaczenia" wielu plików naraz.

%package kbabel-devel
Summary:	KBabel header files
Summary(pl.UTF-8):	Pliki nagłówkowe KBabel
Group:		X11/Development/Libraries
Requires:	%{name}-kbabel = %{epoch}:%{version}-%{release}

%description kbabel-devel
KBabel header files.

%description kbabel-devel -l pl.UTF-8
Pliki nagłówkowe KBabel.

%package kbugbuster
Summary:	A tools that allows cooperation with bugs.kde.org
Summary(pl.UTF-8):	Narzędzie współpracujące z bugs.kde.org
Group:		X11/Development/Tools

%description kbugbuster
KBugBuster allows for easy bug management on bugs.kde.org.

%description kbugbuster -l pl.UTF-8
KBugBuster ułatwia wyszukiwanie i zarządzanie błędami na bugs.kde.org.

%package kcachegrind
Summary:	KCachegrind - visualization of traces generated by profiling
Summary(pl.UTF-8):	KCachegrind - wizualizacja ścieżek tworzonych przez profilowanie
Group:		X11/Development/Tools

%description kcachegrind
KCachegrind visualizes traces generated by profiling.

%description kcachegrind -l pl.UTF-8
KCachegrind wizualizuje ścieżki tworzone przez profilowanie.

%package kmtrace
Summary:	A mtrace to full backtrace conversion tool
Summary(pl.UTF-8):	Narzędzie do konwersji z mtrace do pełnego backtrace'a
Group:		X11/Development/Tools

%description kmtrace
kmtrace converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl.UTF-8
kmtrace konwertuje mtrace glibca do pełnego backtrace'a.

%package kompare
Summary:	Kompare - a program to view the differences between files
Summary(pl.UTF-8):	Kompare - program służący do porównywania zmian między plikami
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

%description kompare -l pl.UTF-8
Kompare to program służący do porównywania zmian między plikami.
Aktualnie dostępne funkcje:
  - porównanie plików lub katalogów poprzez graficzny interfejs
  - przedstawienie źródła i celu za pomocą krzywej Beziera
  - graficzne przeglądanie łat w formatach diff, unidiff, context i
    zwykłym
  - interaktywne wprowadzanie zmian
  - przezroczystość sieciowa
  - możliwość oglądania wyjścia diff w wewnętrznej przeglądarce
  - łatwa nawigacja między wieloplikowymi diffami wraz z dokowalnym
    drzewem
  - zamiana źródła i celu za pomocą pojedynczej komendy
  - statystyki diffów

%package kprofilemethod
Summary:	Kprofilemethod - a set of macros which help profiling using QTime
Summary(pl.UTF-8):	Kprofilemethod - zestaw makr ułatwiających profilowanie z wykorzystaniem QTime
Group:		X11/Development/Tools

%description kprofilemethod
Kprofilemethod is a set of macros which help profiling using QTime.

%description kprofilemethod -l pl.UTF-8
Kprofilemethod to zestaw makr ułatwiających profilowanie z
wykorzystaniem QTime.

%package kspy
Summary:	A utility for egzamining the internal state of a Qt/KDE application
Summary(pl.UTF-8):	Narzędzie do badania stanu aplikacji Qt/KDE
Group:		X11/Development/Tools
Obsoletes:	kdiff
Obsoletes:	kdiff2

%description kspy
KSpy is a utility intended to help developers examine the internal
state of a Qt/KDE application. KSpy graphically displays all the
QObjects in use, and allows you to browse their properties. Using KSpy
is very simple, include kspy.h and call KSpy::invoke() when you want
to look inside your app. The KSpy function is inline and the main part
of KSpy is dynamically loaded, so you may even want to leave this in
the release build of an application.

%description kspy -l pl.UTF-8
KSpy to narzędzie mające ułatwić programistom badanie wewnętrznego
stanu aplikacji Qt/KDE. KSpy ilustruje graficznie wszystkie QObjects
jakie są w użyciu i pozwala na łatwe przeglądanie ich właściwości.
Korzystanie z KSpy jest bardzo proste (wystarczy dołączyć plik kspy.h
i wywołać KSpy::invoke() w miejscu, które chcemy obejrzeć w naszej
aplikacji. Funkcja KSpy jest inline, więc można zostawić ją nawet w
wydaniu stabilnym.

%package kstartperf
Summary:	A tool to measure startup time for KDE applications
Summary(pl.UTF-8):	Narzędzie służące do pomiaru czasu ładowania aplikacji KDE
Group:		X11/Development/Tools

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl.UTF-8
Narzędzie służące do pomiaru czasu ładowania aplikacji KDE.

%package kuiviewer
Summary:	Qt Designer UI file Viewer
Summary(pl.UTF-8):	Przeglądarka plików UI generowanych przez Qt designera
Group:		X11/Development/Tools

%description kuiviewer
Qt Designer UI file Viewer.

%description kuiviewer -l pl.UTF-8
Przeglądarka plików UI generowanych przez Qt designera.

%package kunittest
Summary:	KUnit Test
Summary(pl.UTF-8):	Narzędzie testujące KUnit
Group:		X11/Development/Tools

%description kunittest
KUnit Test.

%description kunittest -l pl.UTF-8
Narzędzie testujące KUnit.

%package libcvsservice
Summary:	A cvs access library
Summary(pl.UTF-8):	Biblioteka dostępu do cvs
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Conflicts:	kdesdk-cervisia < 3:3.2.90.040516-2

%description libcvsservice
A library for access to CVS repositories for KDE apps.

%description libcvsservice -l pl.UTF-8
Biblioteka służąca do kontroli repozytoriów CVS z poziomu aplikacji
KDE.

%package libcvsservice-devel
Summary:	A cvsservice library - header files
Summary(pl.UTF-8):	Biblioteka cvsservice - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-libcvsservice = %{epoch}:%{version}-%{release}
Obsoletes:	kdesdk-cervisia-devel

%description libcvsservice-devel
A cvsservice library - header files.

%description libcvsservice-devel -l pl.UTF-8
Biblioteka cvsservice - pliki nagłówkowe.

%package palette-gimp
Summary:	Package which adds the KDE Default palette to GIMP
Summary(pl.UTF-8):	Pakiet dodający domyślną paletę kolorów KDE do GIMP-a
Group:		X11/Applications/Graphics
Requires:	gimp
Obsoletes:	kdesdk-pallette-gimp

%description palette-gimp
This package adds the KDE Default palette to GIMP.

%description palette-gimp -l pl.UTF-8
Pakiet dodający domyślną paletę kolorów KDE do GIMP-a.

%package palette-xpaint
Summary:	Package which adds the KDE Default palette to XPaint
Summary(pl.UTF-8):	Pakiet dodający domyślną paletę kolorów KDE do XPainta
Group:		X11/Applications/Graphics
Requires:	xpaint
Requires:	xorg-lib-libXt >= 1.0
Obsoletes:	kdesdk-pallette-xpaint

%description palette-xpaint
This package adds the KDE Default palette to XPaint.

%description palette-xpaint -l pl.UTF-8
Pakiet dodający domyślną paletę kolorów KDE do XPainta.

%package po2xml
Summary:	An xml2po and vice versa converters
Summary(pl.UTF-8):	Konwertery po2xml i vice versa
Group:		X11/Development/Tools
Requires:	/usr/bin/python

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl.UTF-8
Konwertery po2xml i vice versa.

%package scripts-developer
Summary:	An set of scripts useful for building and maintaining KDE
Summary(pl.UTF-8):	Zestaw skryptów do kompilowania i utrzymywania KDE
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	kdesdk-extractrc
Obsoletes:	kdesdk-scripts-build
Obsoletes:	kdesdk-scripts-cxxmetric
Obsoletes:	kdesdk-scripts-extractrc
Obsoletes:	kdesdk-scripts-findmissingcrystal
Obsoletes:	kdesdk-scripts-kdelnk2desktop
Obsoletes:	kdesdk-scripts-misc
Obsoletes:	kdesdk-scripts-zonetab2pot

%description scripts-developer
This package contains:
- script that extracts strings in an application's .rc file, e.g.
  testappui.rc, and writes into the pot file
- script that counts lines of code, comments and blank space in C and
  C++ source files
- script for finding missing and packaging crystal icons.
- kdelnk to desktop and zonetab2pot converter
- set of kde-build scripts
- set of scripts that allow more comfortable profiling of KDE apps
- set of scripts to fix licence header/KDE includes directives and
  strip irrelevant tags from .ui files
- KDE man pages generator
- multi-frame PNG to MNG converter

%description scripts-developer -l pl.UTF-8
Ten pakiet zawiera:
- skrypt, który wyciąga łańcuchy z plików .rc aplikacji, np.
  testappgui.rc i zapisuje je do plików pot, z których tworzy się
  tłumaczenia (pliki po)
- skrypt zliczający linijki kodu, komentarzy i znaków białych w
  plikach źródłowych C i C++
- skrypt do wyszukiwania brakujących i pakietowania ikon z motywu
  crystal.
- konwerter plików kdelnk na desktop i zonetab na pot
- zestaw skryptów kde-build
- zestaw skryptów umożliwiających wygodne profilowanie aplikacji KDE
- zestaw skryptów do poprawiania nagłówków informujących o licencji i
  dyrektyw w plikach nagłówkowych KDE oraz usuwania nieistotnych
  znaczników z plików .ui
- generator stron man dla KDE
- konwerter wieloramkowych PNG na MNG

%package scripts-cvs
Summary:	A set of scripts for maintaining KDE from CVS
Summary(pl.UTF-8):	Zestaw skryptów do zarządzania KDE z CVS
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-cvs
A set of scripts for maintaining KDE from CVS.

%description scripts-cvs -l pl.UTF-8
Zestaw skryptów do zarządzania KDE z CVS.

%package scripts-doc
Summary:	A set of scripts for quick access to Qt/KDE documentation
Summary(pl.UTF-8):	Zestaw skryptów szybkiego dostępu do dokumentacji Qt/KDE
Group:		X11/Development/Tools

%description scripts-doc
A set of scripts for quick access to Qt/KDE documentation.

%description scripts-doc -l pl.UTF-8
Zestaw skryptów szybkiego dostępu do dokumentacji Qt/KDE.

%package scripts-kdekillall
Summary:	A script for killing KDE apps started with kdeinit
Summary(pl.UTF-8):	Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit
Group:		X11/Development/Tools

%description scripts-kdekillall
A script for killing KDE apps started with kdeinit.

%description scripts-kdekillall -l pl.UTF-8
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scheck
Summary:	KDE Style - Scheck
Summary(pl.UTF-8):	Motyw KDE - Scheck
Group:		X11/Development/Tools

%description scheck
Development style for searching accelerator and style guide conflicts.

%description scheck -l pl.UTF-8
Motyw KDE przeznaczony do szukania konfliktów w akceleratorach oraz
sprawdzania zgodności z wytycznymi dot. wyglądu graficznego aplikacji
KDE.

%package umbrello
Summary:	UML Modeler
Summary(pl.UTF-8):	Modeler UML
Group:		X11/Development/Tools
Obsoletes:	umbrello

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

%description umbrello -l pl.UTF-8
Modeler UML Umbrello to narzędzie do diagramów UML pomagające w
procesie tworzenia oprogramowania. Szczególnie podczas etapów analizy
i projektowania, modeler UML Umbrello może pomóc w uzyskaniu wysokiej
jakości produktu. UML może być używany do dokumentowania projektu
programu, aby pomóc programiście i jego współpracownikom.

UML to język diagramów używany do opisu takich modeli. Można
przedstawiać idee w UML-u przy użyciu różnych rodzajów diagramów.
Modeler UML Umbrello 1.2 obsługuje następujące rodzaje:
 - diagram klas
 - diagram sekwencji
 - diagram współpracy
 - diagram przypadków użycia
 - diagram stanów
 - diagram aktywności
 - diagram składników.

%package xemacs
Summary:	A set of macros for xemacs
Summary(pl.UTF-8):	Zestaw makr do xemacsa
Group:		X11/Development/Tools
Requires:	xemacs-common

%description xemacs
A set of macros for xemacs useful for developing KDE applications.

%description xemacs -l pl.UTF-8
Zestaw makr do xemacsa przydatnych przy tworzeniu aplikacji KDE.

%package -n kde-kio-svn
Summary:	SVN protocol service
Summary(pl.UTF-8):	Obsługa protokołu SVN
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description -n kde-kio-svn
SVN protocol service.

%description -n kde-kio-svn -l pl.UTF-8
Obsługa protokołu SVN.

%prep
%setup -q
#%patch100 -p0
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

#echo "KDE_OPTIONS = nofinal" >> cervisia/Makefile.am
#echo "KDE_OPTIONS = nofinal" >> umbrello/umbrello/classparser/Makefile.am

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;GUIDesigner;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kuiviewer/kuiviewer.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;RevisionControl;/' \
	-e 's/Terminal=0/Terminal=false/' \
	cervisia/cervisia.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Profiling;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kcachegrind/kcachegrind/kcachegrind.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;ProjectManagement;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kbugbuster/kbugbuster.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Translation;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kbabel/catalogmanager/catalogmanager.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Translation;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kbabel/kbabeldict/kbabeldict.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;Translation;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kbabel/kbabel/kbabel.desktop
%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	kompare/kompare.desktop
%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	umbrello/umbrello/umbrello.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '^Categories=.*[^;]$' $f; then
		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
	fi
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%if "%{_lib}" != "lib"
%{__sed} -i -e "s,/usr/lib,%{_libdir},g" kmtrace/configure.in.in
%{__sed} -i -e "s,/usr/lib,%{_libdir},g" kmtrace/Makefile.am
%endif

%build
#export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

# Used in cervisia Makefile
#export kde_htmldir=%{_kdedocdir}

%configure \
	--disable-rpath \
	--disable-final \
	--with-apr-config=%{_bindir}/apr-1-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-svn-include=%{_includedir} \
	--with-svn-lib=%{_libdir} \
	--with-extra-includes=%{py_incdir} \
	--with-pythondir=%{py_libdir} \
	--with-qt-libraries=%{_libdir}

%{__make}

%{__make} -C kstartperf

%ifarch %{x8664}
%{__make} -C kmtrace
%endif

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

%ifarch %{x8664}
%{__make} -C kmtrace install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}
%endif

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
rm -f ./scripts/completions/zsh/_dcop
cp ./scripts/completions/zsh/_*		$RPM_BUILD_ROOT%{_zshfcdir}

rm -rf `find $RPM_BUILD_ROOT -name CVS`

# Debian manpages
# overwrites cvscheck.1 - it's OK (original manual is much shorter)
#install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

# unsupported
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/locolor

rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*/*/*.la

%find_lang	cervisia	--with-kde
%find_lang	kbabel		--with-kde
%find_lang	kcachegrind	--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde
%find_lang	umbrello	--with-kde
%find_lang	kdesvn-build --with-kde

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
%attr(755,root,root) %{_libdir}/kde3/kfile_[!dp]*.so
%{_datadir}/services/kfile_cpp.desktop
%{_datadir}/services/kfile_h.desktop
%{_datadir}/services/kfile_ts.desktop

%files cervisia -f cervisia.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cervisia
%attr(755,root,root) %{_bindir}/cvsaskpass
%attr(755,root,root) %{_bindir}/cvsservice
%attr(755,root,root) %{_libdir}/kde3/*cervisia*.so
%attr(755,root,root) %{_libdir}/libkdeinit_cervisia.so
%{_libdir}/libkdeinit_cervisia.la


%{_datadir}/apps/cervisia*
%{_datadir}/config.kcfg/cervisiapart.kcfg
%{_datadir}/apps/kconf_update/change_colors.pl
%{_datadir}/apps/kconf_update/cervisia.upd
%{_datadir}/apps/kconf_update/cervisia-change_repos_list.pl
%{_datadir}/apps/kconf_update/cervisia-normalize_cvsroot.pl
%{_datadir}/apps/kconf_update/move_repositories.pl
%{_datadir}/services/cvsservice.desktop
%{_desktopdir}/kde/cervisia.desktop
%{_iconsdir}/[!l]*/*/*/vcs*
%{_iconsdir}/[!l]*/*/*/cervisia*
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
#%{_mandir}/man1/kapptemplate.1*

%files kde-resource-kdeaccounts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kabcformat_kdeaccounts.so
%{_datadir}/apps/kabc/formats/*

%files kde-resource-bugzilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kcal_bugzilla.so
%{_datadir}/services/kresources/kcal/bugzilla.desktop

%files kbabel -f kbabel.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/catalogmanager
%attr(755,root,root) %{_bindir}/kbabel
%attr(755,root,root) %{_bindir}/kbabeldict
%{_libdir}/libkbabelcommon.la
%attr(755,root,root) %{_libdir}/libkbabelcommon.so.*.*.*
%{_libdir}/libkbabeldictplugin.la
%attr(755,root,root) %{_libdir}/libkbabeldictplugin.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/kbabel_*.so
%attr(755,root,root) %{_libdir}/kde3/kbabeldict_*.so
%attr(755,root,root) %{_libdir}/kde3/kfile_po.so
%attr(755,root,root) %{_libdir}/kde3/pothumbnail.so
%{_datadir}/apps/catalogmanager
%{_datadir}/apps/kbabel
%{_datadir}/config.kcfg/kbabel.kcfg
%{_datadir}/config.kcfg/kbprojectsettings.kcfg
%{_datadir}/apps/kconf_update/kbabel-project.upd
%{_datadir}/apps/kconf_update/kbabel-projectrename.upd
%{_datadir}/apps/kconf_update/kbabel-difftoproject.upd
%{_datadir}/services/dbsearchengine.desktop
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
%{_datadir}/services/kbabel_regexptool.desktop
%{_datadir}/services/kbabel_setfuzzytool.desktop
%{_datadir}/services/kbabel_whitespacetool.desktop
%{_datadir}/services/kbabel_xliff_export.desktop
%{_datadir}/services/kbabel_xliff_import.desktop
%{_datadir}/services/kbabel_xmltool.desktop
%{_datadir}/services/kfile_po.desktop
%{_datadir}/services/poauxiliary.desktop
%{_datadir}/services/pocompendium.desktop
%{_datadir}/services/pothumbnail.desktop
%{_datadir}/services/tmxcompendium.desktop
%{_datadir}/servicetypes/kbabel_*.desktop
%{_datadir}/servicetypes/kbabeldict_module.desktop
%{_datadir}/servicetypes/kbabelfilter.desktop
%{_desktopdir}/kde/catalogmanager.desktop
%{_desktopdir}/kde/kbabel.desktop
%{_desktopdir}/kde/kbabeldict.desktop
%{_iconsdir}/[!l]*/*/*/catalogmanager.png
%{_iconsdir}/[!l]*/*/*/kbabel.png
%{_iconsdir}/[!l]*/*/*/kbabeldict.png
#%{_mandir}/man1/catalogmanager.1*
#%{_mandir}/man1/kbabel.1*
#%{_mandir}/man1/kbabeldict.1*

%files kbabel-devel
%defattr(644,root,root,755)
%{_includedir}/kbabel
%attr(755,root,root) %{_libdir}/libkbabelcommon.so
%attr(755,root,root) %{_libdir}/libkbabeldictplugin.so

%files kbugbuster -f kbugbuster.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_datadir}/apps/kbugbuster
%{_desktopdir}/kde/kbugbuster.desktop
%{_iconsdir}/[!l]*/*/*/kbugbuster.png
#%{_mandir}/man1/kbugbuster.1*

%files kcachegrind -f kcachegrind.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcachegrind
%{_datadir}/apps/kcachegrind
%{_datadir}/mimelnk/application/x-kcachegrind.desktop
%{_desktopdir}/kde/kcachegrind.desktop
%{_iconsdir}/hicolor/*/apps/kcachegrind.png
#%{_mandir}/man1/kcachegrind.1*

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
%attr(755,root,root) %{_libdir}/kde3/kfile_diff.so
%attr(755,root,root) %{_libdir}/kde3/libkomparenavtreepart.so
%attr(755,root,root) %{_libdir}/kde3/libkomparepart.so
%{_datadir}/apps/kompare*
%{_datadir}/services/kfile_diff.desktop
%{_datadir}/services/kompare*.desktop
%{_datadir}/servicetypes/kompare*.desktop
%{_desktopdir}/kde/kompare.desktop
%{_iconsdir}/[!l]*/*/*/kompare.*
#%{_mandir}/man1/kompare.1*

%files kprofilemethod
%defattr(644,root,root,755)
%{_includedir}/kprofilemethod.h

%files kspy
%defattr(644,root,root,755)
%{_libdir}/libkspy.la
%{_libdir}/libkspy.so
%attr(755,root,root) %{_libdir}/libkspy.so.*.*.*
%{_includedir}/kspy.h
#%{_mandir}/man1/testkspy.1*

%files kstartperf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstartperf
%{_libdir}/libkstartperf.la
%{_libdir}/libkstartperf.so
%attr(755,root,root) %{_libdir}/libkstartperf.so.*.*.*

%files kuiviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuiviewer
%attr(755,root,root) %{_libdir}/kde3/libkuiviewerpart.so
%attr(755,root,root) %{_libdir}/kde3/quithumbnail.so
%dir %{_datadir}/apps/kuiviewer
%{_datadir}/apps/kuiviewer/kuiviewerui.rc
%dir %{_datadir}/apps/kuiviewerpart
%{_datadir}/apps/kuiviewerpart/kuiviewer_part.rc
%{_datadir}/services/designerthumbnail.desktop
%{_datadir}/services/kuiviewer_part.desktop
%{_desktopdir}/kde/kuiviewer.desktop
%{_iconsdir}/[!l]*/*/apps/kuiviewer.png

%files kunittest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kunit*
%{_libdir}/libkunit*.la
%attr(755,root,root) %{_libdir}/libkunit*.so.*.*.*
%{_includedir}/kunittest

%files libcvsservice
%defattr(644,root,root,755)
%{_libdir}/libcvsservice.la
%attr(755,root,root) %{_libdir}/libcvsservice.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdeinit_cvsservice.so
%attr(755,root,root) %{_libdir}/libkdeinit_cvsaskpass.so
%attr(755,root,root) %{_libdir}/kde3/cvs*.so

%files libcvsservice-devel
%defattr(644,root,root,755)
%{_includedir}/cvsjob_stub.h
%{_includedir}/cvsservice_stub.h
%{_includedir}/repository_stub.h
%attr(755,root,root) %{_libdir}/libcvsservice.so
%{_libdir}/libkdeinit_cvsservice.la
%{_libdir}/libkdeinit_cvsaskpass.la

%files palette-gimp
%defattr(644,root,root,755)
%{_gimpdir}/palettes

%files palette-xpaint
%defattr(644,root,root,755)
%{_appdefsdir}/*

%files po2xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/transxx
%attr(755,root,root) %{_bindir}/xml2pot
#%{_mandir}/man1/po2xml.1*
#%{_mandir}/man1/split2po.1*
#%{_mandir}/man1/swappo.1*
#%{_mandir}/man1/transxx.1*
#%{_mandir}/man1/xml2pot.1*

%files scheck
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/scheck.so
%{_datadir}/apps/kstyle/themes/scheck.themerc

%files scripts-developer -f kdesvn-build.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adddebug
%attr(755,root,root) %{_bindir}/build-progress.sh
%attr(755,root,root) %{_bindir}/create*
%attr(755,root,root) %{_bindir}/cheatmake
%attr(755,root,root) %{_bindir}/extend*
%attr(755,root,root) %{_bindir}/extractattr
%attr(755,root,root) %{_bindir}/fixkdeincludes
%attr(755,root,root) %{_bindir}/fixuifiles
%attr(755,root,root) %{_bindir}/includemocs
%attr(755,root,root) %{_bindir}/kde-build
%attr(755,root,root) %{_bindir}/kdemangen.pl
%attr(755,root,root) %{_bindir}/licensecheck
%attr(755,root,root) %{_bindir}/makeobj
%attr(755,root,root) %{_bindir}/dprof2calltree
%attr(755,root,root) %{_bindir}/hotshot2calltree
%attr(755,root,root) %{_bindir}/memprof2calltree
%attr(755,root,root) %{_bindir}/op2calltree
%attr(755,root,root) %{_bindir}/png2mng.pl
%attr(755,root,root) %{_bindir}/pprof2calltree
%attr(755,root,root) %{_bindir}/cxxmetric
%attr(755,root,root) %{_bindir}/extractrc
%attr(755,root,root) %{_bindir}/findmissingcrystal
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py
%attr(755,root,root) %{_bindir}/package_crystalsvg
%attr(755,root,root) %{_bindir}/zonetab2pot.py
%{_datadir}/apps/katepart/syntax/kdesvn-buildrc.xml
#%{_mandir}/man1/cxxmetric.1*
#%{_mandir}/man1/extractrc.1*
#%{_mandir}/man1/findmissingcrystal.1*
#%{_mandir}/man1/kdelnk2desktop.py.1*
#%{_mandir}/man1/zonetab2pot.py.1*
#%{_mandir}/man1/adddebug.1*
#%{_mandir}/man1/build-progress*.1*
#%{_mandir}/man1/cheatmake.1*
#%{_mandir}/man1/create*.1*
#%{_mandir}/man1/extend_dmalloc.1*
#%{_mandir}/man1/fixkdeincludes.1*
%{_mandir}/man1/includemocs.1*
%{_mandir}/man1/kde-build.1*
%{_mandir}/man1/kdesvn-build.1*
#%{_mandir}/man1/licensecheck.1*
#%{_mandir}/man1/makeobj.1*
#%{_mandir}/man1/dprof2calltree.1*
#%{_mandir}/man1/extractattr.1*
#%{_mandir}/man1/fixuifiles.1*
#%{_mandir}/man1/hotshot2calltree.1*
#%{_mandir}/man1/kdemangen.pl.1*
#%{_mandir}/man1/memprof2calltree.1*
#%{_mandir}/man1/op2calltree.1*
#%{_mandir}/man1/package_crystalsvg.1*
#%{_mandir}/man1/png2mng.pl.1*
#%{_mandir}/man1/pprof2calltree.1*


%files scripts-cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs*
%exclude %{_bindir}/cvsaskpass
%exclude %{_bindir}/cvsservice
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/pruneemptydirs
%{_mandir}/man1/cvs*.1*
%{_mandir}/man1/noncvslist.1*
#%{_mandir}/man1/pruneemptydirs.1*

%files scripts-doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdedoc
%attr(755,root,root) %{_bindir}/qtdoc
#%{_mandir}/man1/kdedoc.1*
#%{_mandir}/man1/qtdoc.1*

%files scripts-kdekillall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdekillall
#%{_mandir}/man1/kdekillall.1*

%files umbrello -f umbrello.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/umbrello
%attr(755,root,root) %{_bindir}/umbodoc
%{_datadir}/apps/umbrello
%{_datadir}/mimelnk/application/x-umbrello.desktop
%{_desktopdir}/kde/umbrello.desktop
%{_iconsdir}/hicolor/*/apps/umbrello.png
%{_iconsdir}/hicolor/*/mimetypes/umbrellofile.png
%{_iconsdir}/hicolor/scalable/apps/umbrello.svgz
%{_iconsdir}/crystalsvg/*/*/umbrello*.*

%files xemacs
%defattr(644,root,root,755)
%{_xemacspkgdir}/kde

%files -n kde-kio-svn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*svn*
%attr(755,root,root) %{_libdir}/kde3/kio_svn.so
%attr(755,root,root) %{_libdir}/kde3/kded_ksvnd.so
%{_datadir}/services/kded/*svn*.desktop
%{_datadir}/services/svn*.protocol
%{_datadir}/apps/konqueror/servicemenus/subversion*
%{_iconsdir}/crystalsvg/*/*/*svn*.*
