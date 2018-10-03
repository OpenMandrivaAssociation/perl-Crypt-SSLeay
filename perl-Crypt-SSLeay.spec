%define	modname	Crypt-SSLeay
%define modver	0.72

Summary:	Support for the https protocol under LWP
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/Crypt-SSLeay-%{modver}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-URI
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3
BuildRequires:	perl-Path-Class

%description 
This perl module provides support for the https protocol under LWP, so
that a LWP::UserAgent can make https GET & HEAD requests.

The Crypt::SSLeay package contains Net::SSL, which is automatically
loaded by LWP::Protocol::https on https requests, and provides the
necessary SSL glue for that module to work via these deprecated modules:

This product includes cryptographic software written by 
Eric Young (eay@cryptsoft.com)

%prep
%setup -qn %{modname}-%{modver}
%apply_patches

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README.md META.yml
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/Net
%{_mandir}/man3/*

