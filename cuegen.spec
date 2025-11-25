# No debug package produced by build
%global		debug_package %{nil}

Summary:	FLAC-compatible cuesheet generator for Linux
Name:	cuegen
Version:	1.2.2
Release:	1
License:	GPLv3+
Group:	Sound
Url:		https://sourceforge.net/projects/cuegen/
Source0:	https://sourceforge.net/projects/cuegen/files/%{name}.src.tar.gz
BuildRequires:	lazarus >= 2.0.4

%description
CUEgen is a FLAC-compatible cuesheet generator for Linux. The FLAC format
allows cuesheets to be embedded in .flac files by storing their data in the
CUESHEET metadata block. The cuesheet itself is simply a description of the
contents of an audio CD. The cuesheet can be used in conjunction with a .flac
file to store a complete album in a single FLAC file and then retrieve
individual tracks from that file. The cuesheet may also be used by CD burning
applications to recreate an identical copy of an original audio CD from its
FLAC representation and an associated cuesheet. As such, cuesheets are of
great use in archiving, transporting and burning FLAC-encoded audio files.

%files
%doc COPYING.txt readme.txt
%{_bindir}/%{name}

#-----------------------------------------------------------------------------

%prep
%setup -qn %{version}

# Fix wrong perms
chmod -x *.txt


%build
# See buildlinux.sh in the sources
lazbuild --bm="release generic" cuegenerator.lpi


%install
# No install script
install -D -m 755 bin/release/cuegenerator %{buildroot}%{_bindir}/%{name}
