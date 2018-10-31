%define upstream_name	 Convert-BER
%define upstream_version 1.3101

Summary:	Convert-BER (module for perl)
Name:		perl-%{upstream_name}
Epoch:		1
Version:	%perl_convert_version %{upstream_version}
Release:	15
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Convert::BER is a perl object class implementation to encode
and decode objects as described by ITU-T standard X.209 (ASN.1)
using Basic Encoding Rules (BER)
	
%prep
%setup -qn %{upstream_name}-%{upstream_version}

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
%{_mandir}/man3/*

