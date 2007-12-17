%define	version	1.2.0
%define release	%mkrel 1

Summary:	FLAC-compatible cuesheet generator for Linux
Name:		cuegen
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://www.cs.man.ac.uk/~slavinp/cuegen.html
Source:		http://www.cs.man.ac.uk/~slavinp/files/%{name}-%{version}.tar.bz2

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

