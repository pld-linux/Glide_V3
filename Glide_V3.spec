Summary:	Glide runtime for 3Dfx Voodoo Banshee and Voodoo3 boards
Summary(pl.UTF-8):	Środowisko Glide dla kart 3Dfx Voodoo Banschee i Voodoo3
Name:		Glide_V3
Version:	2.60
Release:	17
License:	3DFX GLIDE Source Code General Public License
Group:		Libraries
Source0:	GlideV3.tar.gz
# Source0-md5:	9c690dd7b36bbe007806ac62b1366a3b
Patch0:		glide-gcc4.patch
Patch1:		glide-cpp.patch
Patch2:		glide-link.patch
URL:		http://glide.sourceforge.net/
%ifarch %{ix86}
BuildRequires:	/usr/bin/gasp
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package now includes both Glide2x and Glide3x. Glide is a
lowlevel API for accessing 3Dfx Interactive's Voodoo Hardware. This
version of Glide supports Voodoo Banshee and Voodoo3 based 3D
acclerators.

%description -l pl.UTF-8
Ten pakiet zawiera zarówno Glide2x jak i Glide3x. Glide jest
niskopoziomowym API do dostępu do sprzętu Voodoo firmy 3Dfx
Interactive. Ta wersja Glide obsługuje akceleratory 3D oparte na
Voodoo Banshee i Voodoo3.

%package -n Glide_SDK
Summary:	Development libraries for Glide 2.x
Summary(pl.UTF-8):	Część Glide 2.x przeznaczona dla programistów
Version:	2.2
Group:		Development/Libraries

%description -n Glide_SDK
This package includes the header files, documentation, and test files
necessary for developing applications that use any of the 3D
accelerators in the 3Dfx Interactive Voodoo line.

%description -n Glide_SDK -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe, dokumentację i pliki testowe
potrzebne do tworzenia aplikacji korzystających z akceleratorów 3D
serii 3Dfx Interactive Voodoo.

%prep
%setup -q -n GlideV3
%patch0 -p1
%patch1 -p1
%patch2 -p1
chmod +x swlibs/include/make/ostype

ln glide2x/README README.glide2x
ln glide3x/README README.glide3x

%build
%{__make} V3_NODRI \
	CC="%{__cc}" \
	CNODEBUG="%{rpmcflags} %{!?debug:-fomit-frame-pointer}\
		%{!?debug:-funroll-loops -fexpensive-optimizations -ffast-math -DBIG_OPT}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/{glide,glide3}} \
	$RPM_BUILD_ROOT%{_examplesdir}/glide/{tests,tests3x} \
	$RPM_BUILD_ROOT%{_examplesdir}/glide/texus/{lib,cmd,examples}

######################################################################
# Install the Glide2x libraries
######################################################################

# Install the native libraries normally
install glide2x/h3/lib/libglide.so.2.60 $RPM_BUILD_ROOT%{_libdir}

# Create symlinks
ln -sf libglide.so.2 $RPM_BUILD_ROOT%{_libdir}/libglide.so

# Create a compatibility link for the old name
ln -sf libglide.so.2.60 $RPM_BUILD_ROOT%{_libdir}/libglide2x.so.2
ln -sf libglide.so.2 $RPM_BUILD_ROOT%{_libdir}/libglide2x.so

######################################################################
# Install the Glide3X libraries
######################################################################
install glide3x/h3/lib/libglide3.so.3.10 $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/libglide3x.so

# Create symlinks
ln -sf libglide3.so.3 $RPM_BUILD_ROOT%{_libdir}/libglide3.so

# Create a compatibility link for the old name
ln -sf libglide3.so.3.10 $RPM_BUILD_ROOT%{_libdir}/libglide3x.so.3
ln -sf libglide3.so.3 $RPM_BUILD_ROOT%{_libdir}/libglide3x.so

######################################################################
# Install Texus
######################################################################
install swlibs/lib/libtexus.so.1.1 $RPM_BUILD_ROOT%{_libdir}

ln -sf libtexus.so.1.1 $RPM_BUILD_ROOT%{_libdir}/libtexus.so.1
ln -sf libtexus.so.1 $RPM_BUILD_ROOT%{_libdir}/libtexus.so

install swlibs/bin/texus $RPM_BUILD_ROOT%{_bindir}

install glide2x/h3/glide/tests/test00 $RPM_BUILD_ROOT%{_bindir}/test3Dfx
install glide2x/h3/glide/tests/test00 $RPM_BUILD_ROOT%{_bindir}/testGlide2x
install glide3x/h3/glide3/tests/test00 $RPM_BUILD_ROOT%{_bindir}/testGlide3x

######################################################################
# Install the Glide2x SDK material
######################################################################

# Install the headers
install swlibs/include/3dfx.h $RPM_BUILD_ROOT%{_includedir}/glide
install glide2x/h3/include/glide.h $RPM_BUILD_ROOT%{_includedir}/glide
install glide2x/h3/include/glidesys.h $RPM_BUILD_ROOT%{_includedir}/glide
install glide2x/h3/include/glideutl.h $RPM_BUILD_ROOT%{_includedir}/glide
install glide2x/h3/include/sst1vid.h $RPM_BUILD_ROOT%{_includedir}/glide
install glide2x/h3/include/gump.h $RPM_BUILD_ROOT%{_includedir}/glide
install swlibs/include/linutil.h $RPM_BUILD_ROOT%{_includedir}/glide
install swlibs/include/texus.h $RPM_BUILD_ROOT%{_includedir}/glide

# Install the examples and their source
install glide2x/h3/glide/tests/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/tests/makefile
install glide2x/h3/glide/tests/*.3df $RPM_BUILD_ROOT%{_examplesdir}/glide/tests
install glide2x/h3/glide/tests/test??.c $RPM_BUILD_ROOT%{_examplesdir}/glide/tests
install glide2x/h3/glide/tests/tldata.inc $RPM_BUILD_ROOT%{_examplesdir}/glide/tests
install glide2x/h3/glide/tests/tlib.[ch] $RPM_BUILD_ROOT%{_examplesdir}/glide/tests

# Install the Texus source
install swlibs/texus/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/makefile
install swlibs/texus/lib/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/lib/makefile
install swlibs/texus/cmd/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/cmd/makefile
install swlibs/texus/examples/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/examples/makefile
install swlibs/texus/lib/*.c $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/lib
install swlibs/texus/lib/texusint.h $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/lib
install swlibs/texus/cmd/*.c $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/cmd
install swlibs/texus/examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/examples

######################################################################
# Install the Glide3x SDK material
######################################################################
# Install the headers
install swlibs/include/3dfx.h $RPM_BUILD_ROOT%{_includedir}/glide3
install glide3x/h3/include/glide.h $RPM_BUILD_ROOT%{_includedir}/glide3
install glide3x/h3/include/glidesys.h $RPM_BUILD_ROOT%{_includedir}/glide3
install glide3x/h3/include/glideutl.h $RPM_BUILD_ROOT%{_includedir}/glide3
install glide3x/h3/include/sst1vid.h $RPM_BUILD_ROOT%{_includedir}/glide3
install swlibs/include/linutil.h $RPM_BUILD_ROOT%{_includedir}/glide3
install swlibs/include/texus.h $RPM_BUILD_ROOT%{_includedir}/glide3

# Install the examples and their source
install glide3x/h3/glide3/tests/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/tests3x/makefile
install glide3x/h3/glide3/tests/*.3df $RPM_BUILD_ROOT%{_examplesdir}/glide/tests3x
install glide3x/h3/glide3/tests/test??.c $RPM_BUILD_ROOT%{_examplesdir}/glide/tests3x
install glide3x/h3/glide3/tests/tldata.inc $RPM_BUILD_ROOT%{_examplesdir}/glide/tests3x
install glide3x/h3/glide3/tests/tlib.[ch] $RPM_BUILD_ROOT%{_examplesdir}/glide/tests3x

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc glide_license.txt
%attr(755,root,root) %{_bindir}/texus
%attr(755,root,root) %{_bindir}/test3Dfx
%attr(755,root,root) %{_bindir}/testGlide3x
%attr(755,root,root) %{_bindir}/testGlide2x
%attr(755,root,root) %{_libdir}/libglide.so.2.60
%attr(755,root,root) %ghost %{_libdir}/libglide.so.2
%attr(755,root,root) %{_libdir}/libglide.so
%attr(755,root,root) %{_libdir}/libglide2x.so
%attr(755,root,root) %{_libdir}/libglide2x.so.2
%attr(755,root,root) %{_libdir}/libglide3.so.3.10
%attr(755,root,root) %ghost %{_libdir}/libglide3.so.3
%attr(755,root,root) %{_libdir}/libglide3.so
%attr(755,root,root) %{_libdir}/libglide3x.so
%attr(755,root,root) %{_libdir}/libglide3x.so.3
%attr(755,root,root) %{_libdir}/libtexus.so.1.1
%attr(755,root,root) %ghost %{_libdir}/libtexus.so.1
%attr(755,root,root) %{_libdir}/libtexus.so

%files -n Glide_SDK
%defattr(644,root,root,755)
%doc docs2x/*.pdf docs3x/*.pdf
%{_examplesdir}/glide
%{_includedir}/glide
%{_includedir}/glide3
