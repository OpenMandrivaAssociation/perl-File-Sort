%define upstream_name    File-Sort
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Sort a file or merge sort multiple files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


