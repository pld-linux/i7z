Summary:	i3, i5 and i7 reporting tool for Linux
Summary(pl.UTF-8):	Narzędzie informacyjne dla procesorów i3, i5 i i7 pod Linuksem
Name:		i7z
Version:	0.27.2
Release:	2
License:	GPL v2
Group:		Applications/System
#Source0Download: http://code.google.com/p/i7z/downloads/list
Source0:	http://i7z.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	7f2c4928146b722d67ecdd0d905a4353
URL:		http://code.google.com/p/i7z/
BuildRequires:	ncurses-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	QtGui-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
A better i7 (and now i3, i5) reporting tool for Linux.

%description -l pl.UTF-8
Lepsze narzędzie informacyjne dla procesorów i7 (teraz także i3, i5)
działające pod Linuksem.

%package gui
Summary:	Qt-based graphical i3/i5/i7 CPU reporting tool
Summary(pl.UTF-8):	Oparte na Qt graficzne narzędzie informacyjne dla procesorów i3/i5/i7
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gui
Qt-based graphical i3/i5/i7 CPU reporting tool.

%description gui -l pl.UTF-8
Oparte na Qt graficzne narzędzie informacyjne dla procesorów i3/i5/i7.

%prep
%setup -q

%build
%{__make} clean
CFLAGS="%{rpmcflags} %{rpmcppflags} -I/usr/include/ncurses" \
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	LIBS="-lncurses -ltinfo -lpthread -lrt -lm"

cd GUI
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install GUI/i7z_GUI $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_sbindir}/i7z

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/i7z_GUI
