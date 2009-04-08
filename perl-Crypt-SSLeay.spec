%define	module	Crypt-SSLeay
%define	name	perl-%{module}
%define	version	0.57
%define	release	%mkrel 4

Summary:	Support for the https protocol under LWP
Name:		%{name}
Version:	%version
Release:	%release
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/Crypt-SSLeay-%{version}.tar.bz2
Patch0:		perl-Crypt-SSLeay-cryptdef.patch
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	perl-URI
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	perl

%description 
This perl module provides support for the https protocol under LWP, so
that a LWP::UserAgent can make https GET & HEAD requests.

The Crypt::SSLeay package contains Net::SSL, which is automatically
loaded by LWP::Protocol::https on https requests, and provides the
necessary SSL glue for that module to work via these deprecated modules:

This product includes cryptographic software written by 
Eric Young (eay@cryptsoft.com)

%prep

%setup -q -n %{module}-%{version}
%patch0 -p1 -b .cryptdef

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/Net
%{_mandir}/*/*


