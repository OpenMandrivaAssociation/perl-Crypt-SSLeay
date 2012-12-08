%define	upstream_name	 Crypt-SSLeay
%define upstream_version 0.58

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    11
Summary:	Support for the https protocol under LWP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/Crypt-SSLeay-%{upstream_version}.tar.gz
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
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .cryptdef
%patch1 -p1 -b .sni

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make CFLAGS="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc README META.yml
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/Net
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.580.0-10
+ Revision: 765138
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.580.0-9
+ Revision: 763652
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.580.0-8
+ Revision: 763020
- Build for perl 5.14.x

* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.580.0-7
+ Revision: 687085
- SNI support (RT patch #61883)

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.580.0-6
+ Revision: 667062
- mass rebuild

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.580.0-5mdv2011.0
+ Revision: 573805
- update to 0.58

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.570.0-5mdv2011.0
+ Revision: 564392
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.570.0-4mdv2011.0
+ Revision: 555311
- rebuild

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 0.570.0-3mdv2010.1
+ Revision: 532507
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.570.0-2mdv2010.1
+ Revision: 511614
- rebuilt against openssl-0.9.8m

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.570.0-1mdv2010.0
+ Revision: 406961
- rebuild using %%perl_convert_version

* Thu Apr 09 2009 Thierry Vignaud <tv@mandriva.org> 0.57-4mdv2009.1
+ Revision: 365380
- rediff patch 0
- rebuild to be newer than 2009.0 updates

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.57-3mdv2009.0
+ Revision: 223585
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.57-2mdv2008.1
+ Revision: 151352
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.57-1mdv2008.1
+ Revision: 97435
- update to new version 0.57

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-2mdv2008.0
+ Revision: 90052
- rebuild

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-1mdv2008.0
+ Revision: 52487
- update to new version 0.56

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2008.0
+ Revision: 46617
- update to new version 0.55

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 0.54-1mdv2008.0
+ Revision: 19316
- 0.54


* Mon Jan 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.53-1mdv2007.0
+ Revision: 106109
- 0.53

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Crypt-SSLeay

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.51-6mdk
- added P0,P1,P2 from fedora

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.51-5mdk
- Rebuild for new perl

* Fri Jun 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.51-4mdk
- Remove unneeded virtual package SSLeay.pm

* Thu Feb 26 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.51-3mdk
- rebuild
- Own dir

