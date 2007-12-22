%define module  HTML-WikiConverter
%define name    perl-%{module}
%define version 0.61
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
summary:        HTML-WikiConverter - An HTML to wiki markup converter
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(URI)
BuildRequires:  perl(HTML::Tree)
BuildRequires:  perl(CSS)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
HTML::WikiConverter is an HTML to wiki converter. It can convert HTML
source into a variety of wiki markups, called wiki "dialects".

%prep
%setup -q -n %{module}-%{version} 

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

