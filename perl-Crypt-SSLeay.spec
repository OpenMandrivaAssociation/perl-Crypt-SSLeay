%define	modname	Crypt-SSLeay
%define modver	0.58

Summary:	Support for the https protocol under LWP
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/Crypt-SSLeay-%{modver}.tar.gz
Patch0:		perl-Crypt-SSLeay-cryptdef.patch
# https://rt.cpan.org/Ticket/Display.html?id=61883
Patch1:		0001-Add-SNI-support-to-Crypt-SSLeay.patch
BuildRequires:	pkgconfig(openssl)
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-URI
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3

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
%patch0 -p1 -b .cryptdef
%patch1 -p1 -b .sni

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/Net
%{_mandir}/man3/*

