%define		pdir	Language
%define		pnam	Functional
Summary:	Language::Functional - makes Perl slightly more functional
Summary(pl.UTF-8):	Language::Functional - uczynienie Perla nieco bardziej funkcyjnym
Name:		perl-Language-Functional
Version:	0.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	59c81abfd14c940f47115f19dc6288c2
URL:		http://search.cpan.org/dist/Language-Functional/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl already contains some functional-like functions, such as `map'
and `grep'. The purpose of this module is to add other functional-like
functions to Perl, such as foldl and foldr, as well as the use of
infinite lists.

%description -l pl.UTF-8
Perl ma zawiera trochę funkcji w stylu funkcyjnym, takich jak map czy
grep. Celem tego modułu jest dodanie większej liczby takich funkcji,
jak na przykład foldl i foldr, a także użycia nieskończonych list.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Language/Functional.pm
%{_mandir}/man3/*
