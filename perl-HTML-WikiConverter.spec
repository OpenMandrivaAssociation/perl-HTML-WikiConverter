%define upstream_name    HTML-WikiConverter
%define upstream_version 0.68

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

summary:    HTML-WikiConverter - An HTML to wiki markup converter
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(URI)
BuildRequires:  perl(HTML::Tree)
BuildRequires:  perl(CSS)
BuildRequires:  perl(Params::Validate)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
HTML::WikiConverter is an HTML to wiki converter. It can convert HTML
source into a variety of wiki markups, called wiki "dialects".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{_bindir}/*
%{perl_vendorlib}/HTML
