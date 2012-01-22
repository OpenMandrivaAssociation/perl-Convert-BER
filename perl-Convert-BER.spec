%define upstream_name	 Convert-BER
%define upstream_version 1.3101

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Convert-BER (module for perl)
License: 	GPL
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz
Epoch: 1
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Convert::BER is a perl object class implementation to encode
and decode objects as described by ITU-T standard X.209 (ASN.1)
using Basic Encoding Rules (BER)
	
%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Convert
%{_mandir}/*/*
