%define		module	pyogg
Summary:	A Python module for the Ogg library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki Ogg
Name:		python-%{module}
Version:	1.3
Release:	9
License:	GPL
Group:		Libraries/Python
Source0:	http://ekyo.nerim.net/software/pyogg/%{module}-%{version}.tar.gz
# Source0-md5:	45a4ecc4d0600661199e4040a81ea3fe
URL:		http://ekyo.nerim.net/software/pyogg/
BuildRequires:	libogg-devel
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pyogg

%description
A Python module for the the Ogg library.

%description -l pl.UTF-8
Moduł Pythona do biblioteki Ogg.

%package devel
Summary:	PyOgg development files
Summary(pl.UTF-8):	Pliki nagłówkowe modułu PyOgg
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libogg-devel
%pyrequires_eq	python-devel
Obsoletes:	pyogg-devel

%description devel
PyOgg development files.

%description devel -l pl.UTF-8
Pliki programistyczne modułu PyOgg.

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
chmod a+x test/oggtail.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install test/oggtail.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f test/testogg.py
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%dir %{py_sitedir}/ogg
%attr(755,root,root) %{py_sitedir}/ogg/*.so
%{py_sitedir}/ogg/*.py[co]
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{module}
