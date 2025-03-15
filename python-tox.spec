# TODO:
# - packaging of
#        /usr/bin/tox
#        /usr/bin/tox-quickstart
# - fix tests on builders

# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	tox
Summary:	Virtualenv-based automation of test activities
Summary(pl.UTF-8):	Oparta na Virtualenv automatyka testów
Name:		python-%{module}
Version:	3.23.0
Release:	7
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/t/tox/tox-%{version}.tar.gz
# Source0-md5:	bd96f55bb0b50be9aec5bab6094a3eb1
Patch0:		virtualenv.patch
URL:		http://tox.testrun.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-filelock
BuildRequires:	python-flaky
BuildRequires:	python-modules
BuildRequires:	python-pip
BuildRequires:	python-pluggy
BuildRequires:	python-virtualenv
BuildRequires:	python-pytest >= 2.3.5
BuildRequires:	python-pytest-timeout
BuildRequires:	python-py
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tox is a generic virtualenv management and test command line tool you
can use for:
- checking your package installs correctly with different Python
  versions and interpreters
- running your tests in each of the environments, configuring your
  test tool of choice
- acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%description -l pl.UTF-8
Tox jest ogólnym, operatym na virtualenv narzędziem linii poleceń
które może być użyte do:
- testowania czy pakiet instaluje się poprawnie z róznymi wersjami
  Pythona
- uruchamionia testów dla każdego ze środowisk, konfigurując narzędzia
  testowe
- jako frontend dla serwerów Continuous Integration,

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}
%patch -P 0 -p1

%build
%py_build %{?with_tests:test}

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
