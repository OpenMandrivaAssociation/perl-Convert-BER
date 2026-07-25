%define upstream_name	 Convert-BER
%define upstream_version 1.32

Summary:	Convert-BER (module for perl)
Name:		perl-%{upstream_name}
Epoch:		1
Version:	%{upstream_version}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Convert-BER
Source0:	https://cpan.metacpan.org/authors/id/G/GB/GBARR/Convert-BER-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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

