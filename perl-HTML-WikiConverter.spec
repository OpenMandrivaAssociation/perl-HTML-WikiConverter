%define upstream_name    HTML-WikiConverter
%define upstream_version 0.68

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	HTML-WikiConverter - An HTML to wiki markup converter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(URI)
BuildRequires:	perl(HTML::Tree)
BuildRequires:	perl(CSS)
BuildRequires:	perl(Params::Validate)
BuildArch:	noarch

%description
HTML::WikiConverter is an HTML to wiki converter. It can convert HTML
source into a variety of wiki markups, called wiki "dialects".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Test is broken ATM because of test server being down
# make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{_bindir}/*
%{perl_vendorlib}/HTML


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.680.0-1mdv2010.0
+ Revision: 403265
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdv2010.0
+ Revision: 370130
- update to new version 0.68

* Wed Mar 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.67-1mdv2009.1
+ Revision: 357203
- update to new version 0.67

* Tue Mar 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdv2009.1
+ Revision: 353417
- update to new version 0.66

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2009.1
+ Revision: 302826
- update to new version 0.63

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.62-2mdv2009.0
+ Revision: 268524
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.62-1mdv2009.0
+ Revision: 208353
- update to new version 0.62

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-2mdv2008.1
+ Revision: 137162
- fix build dependencies
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdv2007.0
- New version 0.61
- buildrequires

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2007.0
- New version 0.55

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdv2007.0
- New release 0.53
- better source URL

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-1mdk
- New release 0.52

* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.51-1mdk
- New release 0.51

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdk
- New release 0.50
- spec cleanup
- fix directory ownership

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.30-4mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.30-3mdk
- Buildrequires fix

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.30-2mdk
- Fix buildrequires

* Tue Aug 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> -
- new version
- fix sources url for rpmbuildupdate
- drop empty directories

* Thu Apr 28 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.22-1mdk
- initial release

