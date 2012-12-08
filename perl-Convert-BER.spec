%define upstream_name	 Convert-BER
%define upstream_version 1.3101

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Epoch:		1

Summary:	Convert-BER (module for perl)
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Convert::BER is a perl object class implementation to encode
and decode objects as described by ITU-T standard X.209 (ASN.1)
using Basic Encoding Rules (BER)
	
%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Convert
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.310.100-3mdv2012.0
+ Revision: 765110
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.310.100-2
+ Revision: 763567
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.310.100-1
+ Revision: 676478
- increase epoch
- this version is newer than what's in cooker...
- rebuild
- mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.3101
    - update to new version 1.3101

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.320.0-1mdv2010.1
+ Revision: 460723
- update to 1.32

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.310.100-1mdv2010.0
+ Revision: 406918
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.31.01-7mdv2009.1
+ Revision: 351694
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.31.01-6mdv2009.0
+ Revision: 223577
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.31.01-5mdv2008.1
+ Revision: 136694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.31.01-5mdv2007.0
+ Revision: 108545
- rebuild

* Tue Aug 29 2006 Olivier Thauvin <nanardon@mandriva.org> 1.31.01-4mdv2007.0
+ Revision: 58429
- mkrel
- do make test
- Import perl-Convert-BER

