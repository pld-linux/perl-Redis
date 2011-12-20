#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Redis
%include	/usr/lib/rpm/macros.perl
Summary:	Redis - Perl binding for Redis database
Name:		perl-Redis
Version:	1.904
Release:	2
# note if it is "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Redis/%{pdir}-%{version}.tar.gz
# Source0-md5:	1c023390a5de0187a208ead7ade3d0a6
URL:		http://search.cpan.org/dist/Redis/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-String
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Tie::StdHash is present in Tie/Hash.pm package
%define		_noautoreq	perl(Tie::StdHash)

%description
Pure Perl bindings for <http://redis.io/>

This version supports protocol 2.x (multi-bulk) or later of Redis
available at <https://github.com/antirez/redis/>.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Redis.pm
%{perl_vendorlib}/Redis
%{_mandir}/man3/*
