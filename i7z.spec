Summary:	i3, i5 and i7 reporting tool for Linux
Name:		i7z
Version:	0.25
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://i7z.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	29376e209ee6e2fb1534d16f0ae83fb4
URL:		http://code.google.com/p/i7z/
BuildRequires:	ncurses-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	QtGui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A better i7 (and now i3, i5) reporting tool for Linux.

%prep
%setup -q

%build
%{__make} \
	INCLUDEFLAGS=-I/usr/include/ncurses
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
