%include        /usr/lib/rpm/macros.python
%define		module pyogg
Summary:	A Python module for the Ogg library
Summary(pl):	Modu³ pythona do biblioteki Ogg
Name:		python-%{module}
Version:	1.3
Release:	1
License:	GPL
Group:		Libraries/Python
#Source0Download: http://www.andrewchatham.com/pyogg/
Source0:	http://www.andrewchatham.com/pyogg/download/%{module}-%{version}.tar.gz
# Source0-md5:	45a4ecc4d0600661199e4040a81ea3fe
URL:		http://www.andrewchatham.com/pyogg/
BuildRequires:	libogg-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pyogg

%description
A Python module for the the Ogg library.

%description -l pl
Modu³ pythona do biblioteki Ogg.

%package devel
Summary:	PyOgg development files
Summary(pl):	Pliki programistyczne modu³u PyOgg
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Requires:	libogg-devel
Obsoletes:	pyogg-devel

%description devel
PyOgg development files.

%description devel -l pl
Pliki programistyczne modu³u PyOgg.

%prep
%setup -q -n %{module}-%{version}

%build
python config_unix.py \
	--prefix %{_prefix}
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%dir %{py_sitedir}/ogg
%attr(755,root,root) %{py_sitedir}/ogg/*.so
%{py_sitedir}/ogg/*.py[co]

%files devel
%defattr(644,root,root,755)
%doc test/*
%{py_incdir}/%{module}
