%include        /usr/lib/rpm/macros.python
%define		module pyogg
Name:		python-%{module}
Version:	1.2
Release:	1
Summary:	A Python module for the the Ogg library
Summary(pl):	Modu³ pythona do biblioteki Ogg
Group:		Libraries/Python
License:	GPL
URL:		http://www.andrewchatham.com/pyogg/
Source0:	http://www.andrewchatham.com/pyogg/download/%{module}-%{version}.tar.gz
Requires:	python-modules
Requires:	libogg
BuildRequires:	python-devel
BuildRequires:	libogg-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyogg is a wrapper for Ogg library.

%description -l pl
pyogg jest wrapperem dla biblioteki Ogg.

%package devel
Summary:	pyogg header and example programs
Group:		Development/Languages/Python
Requires:	%{name} = %{version}

%description devel
pyogg is a wrapper for Ogg library.

Install python-pyogg-devel if you need the API documentation and example
programs.

%description devel -l pl
pyogg jest wrapperem dla biblioteki Ogg.

Zainstaluj tê paczkê je¶li potrzebujesz dokumentacjê API oraz przyk³adowe
programy.

%prep
%setup -q -n %{module}-%{version}

%build
python config_unix.py --prefix %{_prefix}
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/ogg
%doc AUTHORS ChangeLog README NEWS

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{module}
%doc test/*
