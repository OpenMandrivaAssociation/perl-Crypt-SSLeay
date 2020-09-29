%define	modname	Crypt-SSLeay
%define modver	0.72

Summary:	Support for the https protocol under LWP
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/Crypt-SSLeay-%{modver}.tar.gz
Patch1:		Crypt-SSLeay-0.72-Do-not-use-SSLv2_client_method-with-OpenSSL-1.1.0.patch
Patch2:		Crypt-SSLeay-0.72-Fix-building-on-Perl-without-dot-in-INC.patch
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-URI
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3
BuildRequires:	perl-Path-Class
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(Test::More)

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
%autopatch -p1

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make_build CFLAGS="%{optflags}"

%check
%make test

%install
%make_install

%files
%doc README.md META.yml
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/Net
%{_mandir}/man3/*

