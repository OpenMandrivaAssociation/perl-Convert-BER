%define version	1.31.01
%define realversion	1.3101
%define release	%mkrel 7
%define name 	perl-Convert-BER
%define realname	Convert-BER

Summary:        Convert-BER (module for perl)
Name: 		%{name}
version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source: 	%{realname}-%{realversion}.tar.bz2
BuildArch:	noarch
URL: 		http://www.cpan.org/modules/by-module/Convert/
BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-root/
Requires: 	perl

%description
Convert::BER is a perl object class implementation to encode
and decode objects as described by ITU-T standard X.209 (ASN.1)
using Basic Encoding Rules (BER)
	
%prep
%setup -q -n %{realname}-%{realversion}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Convert
%{_mandir}/*/*


