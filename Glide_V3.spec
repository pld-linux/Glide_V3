Summary:	Glide runtime for 3Dfx Voodoo Banshee and Voodoo3 boards
Name:		Glide_V3
Version:	2.60
Release:	16
Group:		Libraries
Copyright:	3DFX GLIDE Source Code General Public License
URL:		http://www.3dfx.com	
Source:		GlideV3.tar.gz
Vendor:		3Dfx Interactive Inc.
Icon:		3dfx.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This package now includes both Glide2x and Glide3x. Glide is a
lowlevel API for accessing 3dfx Interactive's Voodoo Hardware. This
version of Glide supports Voodoo Banshee and Voodoo3 based 3D
acclerators.

%package -n Glide_SDK
Summary:	Development libraries for Glide 2.x
Version:	2.2
Group:		Development/Libraries

%description -n Glide_SDK
This package includes the header files, documentation, and test files
necessary for developing applications that use any of the 3D
acceleratos in the 3Dfx Interactive Voodoo line.

%prep
%setup -q -n GlideV3
chmod +x swlibs/include/make/ostype

%build
%{__make} V3_NODRI CNODEBUG="$RPM_OPT_FLAGS -fomit-frame-pointer \
	-funroll-loops -fexpensive-optimizations -ffast-math -DBIG_OPT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/{glide,glide3}}
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/{tests,tests3x}
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/{lib,cmd,examples}

######################################################################
# Install the Glide2x libraries
######################################################################

# Install the native libraries normally
install -s glide2x/h3/lib/libglide.so.2.60 $RPM_BUILD_ROOT%{_libdir}

# Create symlinks
ln -s libglide.so.2 $RPM_BUILD_ROOT%{_libdir}/libglide.so

# Create a compatibility link for the old name
ln -s libglide.so.2.60 $RPM_BUILD_ROOT%{_libdir}/libglide2x.so
ln -s libglide2x.so $RPM_BUILD_ROOT%{_libdir}/libglide2x.so.2

######################################################################
# Install the Glide3X libraries
######################################################################
install -s glide3x/h3/lib/libglide3.so.3.10 $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/libglide3x.so

# Create symlinks
ln -s libglide3.so.3 $RPM_BUILD_ROOT%{_libdir}/libglide3.so

# Create a compatibility link for the old name
ln -s libglide3.so.3 $RPM_BUILD_ROOT%{_libdir}/libglide3x.so
ln -s libglide3x.so $RPM_BUILD_ROOT%{_libdir}/libglide3x.so.3

######################################################################
# Install Texus
######################################################################
install -s swlibs/lib/libtexus.so.1.1 $RPM_BUILD_ROOT%{_libdir}

ln -s libtexus.so.1.1 $RPM_BUILD_ROOT%{_libdir}/libtexus.so.1
ln -s libtexus.so.1 $RPM_BUILD_ROOT%{_libdir}/libtexus.so

install -s swlibs/bin/texus $RPM_BUILD_ROOT%{_bindir}

install -s glide2x/h3/glide/tests/test00 $RPM_BUILD_ROOT%{_bindir}/test3Dfx
install -s glide2x/h3/glide/tests/test00 $RPM_BUILD_ROOT%{_bindir}/testGlide2x
install -s glide3x/h3/glide3/tests/test00 $RPM_BUILD_ROOT%{_bindir}/testGlide3x

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
install glide2x/h3/glide/tests/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests/makefile
install glide2x/h3/glide/tests/*.3df $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests
install glide2x/h3/glide/tests/test??.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests
install glide2x/h3/glide/tests/tldata.inc $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests
install glide2x/h3/glide/tests/tlib.[ch] $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests

# Install the Texus source
install swlibs/texus/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/makefile
install swlibs/texus/lib/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/lib/makefile
install swlibs/texus/cmd/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/cmd/makefile
install swlibs/texus/examples/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/examples/makefile
install swlibs/texus/lib/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/lib
install swlibs/texus/lib/texusint.h $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/lib
install swlibs/texus/cmd/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/cmd
install swlibs/texus/examples/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/examples

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
install glide3x/h3/glide3/tests/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests3x/makefile
install glide3x/h3/glide3/tests/*.3df $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests3x
install glide3x/h3/glide3/tests/test??.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests3x
install glide3x/h3/glide3/tests/tldata.inc $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests3x
install glide3x/h3/glide3/tests/tlib.[ch] $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests3x

gzip -9nf glide_license.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc glide_license.txt.gz
%attr(755,root,root) %{_bindir}/texus
%attr(755,root,root) %{_bindir}/test3Dfx
%attr(755,root,root) %{_bindir}/testGlide3x
%attr(755,root,root) %{_bindir}/testGlide2x
%attr(755,root,root) %{_libdir}/libglide.so.2.60
%attr(755,root,root) %{_libdir}/libglide.so
%attr(755,root,root) %{_libdir}/libglide2x.so
%attr(755,root,root) %{_libdir}/libglide2x.so.2
%attr(755,root,root) %{_libdir}/libglide3.so.3.10
%attr(755,root,root) %{_libdir}/libglide3.so
%attr(755,root,root) %{_libdir}/libglide3x.so
%attr(755,root,root) %{_libdir}/libglide3x.so.3
%attr(755,root,root) %{_libdir}/libtexus.so.1.1
%attr(755,root,root) %{_libdir}/libtexus.so

%files -n Glide_SDK
%defattr(644,root,root,755)
%doc docs2x/*.pdf docs3x/*.pdf
%{_prefix}/src/examples/glide
%{_includedir}/glide
%{_includedir}/glide3
