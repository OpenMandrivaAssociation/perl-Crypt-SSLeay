%define	upstream_name	 Crypt-SSLeay
%define	upstream_version 0.57

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	Support for the https protocol under LWP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/Crypt-SSLeay-%{upstream_version}.tar.bz2
Patch0:		perl-Crypt-SSLeay-cryptdef.patch

BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	perl-URI
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
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
%setup -q -n %{upstream_name}-%{upstream_version}
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
