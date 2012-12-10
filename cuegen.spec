%define	version	1.2.0
%define release	%mkrel 5

Summary:	FLAC-compatible cuesheet generator for Linux
Name:		cuegen
Version:	%{version}
Release:	%{release}
License:	GPL+
Group:		Sound
URL:		http://www.cs.man.ac.uk/~slavinp/cuegen.html
Source:		http://www.cs.man.ac.uk/~slavinp/files/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CUEgen is a FLAC-compatible cuesheet generator for Linux. The
FLAC format allows cuesheets to be embedded in .flac files by
storing their data in the CUESHEET metadata block. The cuesheet
itself is simply a description of the contents of an audio CD. The
cuesheet can be used in conjunction with a .flac file to store a
complete album in a single FLAC file and then retrieve individual
tracks fro m that file. The cuesheet may also be used by CD burning
applications to recreate an identical copy of an original audio CD
from its FLAC representation and an associated cuesheet. As such,
cuesheets are of great use in archiving, transporting and burning
FLAC-enc oded audio files.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
install -D -m 755 cuegen %{buildroot}%{_bindir}/cuegen

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdv2011.0
+ Revision: 617442
- the mass rebuild of 2010.0 packages

* Sun Jul 05 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.0-4mdv2010.0
+ Revision: 392407
- fix license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-3mdv2009.0
+ Revision: 243802
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2008.1
+ Revision: 123537
- kill re-definition of %%buildroot on Pixel's request
- import cuegen


* Thu Oct 27 2005 Abel Cheung <deaddog@mandriva.org> 1.2.0-1mdk
- First Mandriva package
