%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	Functional
Summary:	Language::Functional perl module - makes Perl slightly more functional
Summary(pl):	Modu³ perla Language::Functinal - czyni±cy Perla nieco bardziej funkcyjnym
Name:		perl-Language-Functional
Version:	0.03
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl already contains some functional-like functions, such as `map'
and `grep'. The purpose of this module is to add other functional-like
functions to Perl, such as foldl and foldr, as well as the use of
infinite lists.

%description -l pl
Perl ma zawiera trochê funkcji w stylu funkcyjnym, takich jak map czy
grep. Celem tego modu³u jest dodanie wiêkszej liczby takich funkcji,
jak na przyk³ad foldl i foldr, a tak¿e u¿ycia nieskoñczonych list.

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
%doc Changes README
%{perl_vendorlib}/Language/Functional.pm
%{_mandir}/man3/*
