# TODO: optflags in GUI
Summary:	i3, i5 and i7 reporting tool for Linux
Summary(pl.UTF-8):	Narzędzie informacyjne dla procesorów i3, i5 i i7 pod Linuksem
Name:		i7z
Version:	0.26
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: http://code.google.com/p/i7z/downloads/list
Source0:	http://i7z.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	4f16f8ba2096e6156caab300e9e034e3
Patch0:		%{name}-c++.patch
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
działajace pod Linuksem.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGSANY="%{rpmcflags} %{rpmcppflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -DBUILD_MAIN -Wall" \
	INCLUDEFLAGS=-I/usr/include/ncurses \
	LDFLAGS="%{rpmldflags} -lncurses -ltinfo -lpthread"
%{__make} -C GUI \
#	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install GUI/GUI $RPM_BUILD_ROOT%{_sbindir}/%{name}_GUI

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_sbindir}/%{name}*
