%define upstream_name    File-Sort
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Sort a file or merge sort multiple files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module sorts text files by lines (or records). Comparisons are based
on one or more sort keys extracted from each line of input, and are
performed lexicographically. By default, if keys are not given, sort
regards each input line as a single field. The sort is a merge sort. If you
don't like that, feel free to change it.

Options
    The following options are available, and are passed in the hash
    reference passed to the function in the format:

      OPTION => VALUE

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Sep 23 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.10.0-1mdv2012.0
+ Revision: 701121
- import perl-File-Sort

