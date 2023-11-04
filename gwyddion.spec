%define major 0
%define api 2

%define libname			%mklibname %{name} %{api} %{major}
%define devname			%mklibname %{name} %{api} -d
%define libgwyapp		%mklibname gwyapp %{api} %{major}
%define libgwydgets		%mklibname gwydgets %{api} %{major}
%define libgwydraw		%mklibname gwydraw %{api} %{major}
%define libgwymodule	%mklibname gwymodule %{api} %{major}
%define libgwyprocess	%mklibname gwyprocess %{api} %{major}

%bcond_without	doc
%bcond_without	doc_pdf
%bcond_without	python
%bcond_with		thumbnailer_gconf
%bcond_with		thumbnailer_kde45

Summary:	A SPM (scanning probe microscopy) data visualization and analysis tool
Name:		gwyddion
Version:	2.64
Release:	1
License:	GPLv2+
Group:		Sciences/Physics
URL:		http://gwyddion.net/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.sig
# (upstream) http://gwyddion.net/download/2.53/gwyddion-2.53-gcc9-openmp-shared-const.patch
#Patch0:		gwyddion-2.53-gcc9-openmp-shared-const.patch

BuildRequires:	ruby
BuildRequires:	intltool
BuildRequires:	hdf5-devel
BuildRequires:	inkscape
BuildRequires:	pngcrush
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(jansson)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(zlib)
%if %{with python}
BuildRequires:	epydoc
BuildRequires:	python2dist(numpy)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(pygtk-2.0)
%endif
%if %{with doc}
BuildRequires:	gtk-doc
%endif
%if %{with doc_pdf}
BuildRequires:	gtk-doc-mkpdf
%endif
%if %{with thumbnailer_kde45}
BuildRequires:	pkgconfig(Qt5Core)
#kdelibs-devel > 4
%endif

%description
Gwyddion is a modular program for SPM (scanning probe microscopy) data
visualization and analysis. Primarily it is intended for analysis of height
fields obtained by scanning probe microscopy techniques (AFM, MFM, STM,
SNOM/NSOM) and it supports many SPM data formats. However, it can also be
used for general height field and image processing, for instance for analysis
of profilometry data.

Gwyddion aims to provide a modular program for 2D data processing and analysis
that can be easily extended by third-party modules and scripts. Moreover, the
status of free software enables to provide the source code to developers and
users, which makes the further program improvement easier.

Its graphical user interface is based on Gtk+.

%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-thumbnailer.1*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_libdir}/%{name}/modules/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_metainfodir}/net.gwyddion.Gwyddion.appdata.xml
%{_datadir}/thumbnailers/gwyddion.thumbnailer
%if %{with python}
%{python2_sitearch}/gwy.so
%endif

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for Gwyddion
Group:		System/Libraries

%description -n %{libname}
Shared library for Gwyddion and its modules.

%files -n %{libname}
%{_libdir}/lib%{name}%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwyapp}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwyapp}
Shared library for Gwyddion and its modules.

%files -n %{libgwyapp}
%{_libdir}/libgwyapp%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwydgets}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwydgets}
Shared library for Gwyddion and its modules.

%files -n %{libgwydgets}
%{_libdir}/libgwydgets%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwydraw}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwydraw}
Shared library for Gwyddion and its modules.

%files -n %{libgwydraw}
%{_libdir}/libgwydraw%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwymodule}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwymodule}
Shared library for Gwyddion and its modules.

%files -n %{libgwymodule}
%{_libdir}/libgwymodule%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwyprocess}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwyprocess}
Shared library for Gwyddion and its modules.

%files -n %{libgwyprocess}
%{_libdir}/libgwyprocess%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers, libraries and tools for Gwyddion module development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libgwyapp} = %{EVRD}
Requires:	%{libgwydgets} = %{EVRD}
Requires:	%{libgwydraw} = %{EVRD}
Requires:	%{libgwymodule} = %{EVRD}
Requires:	%{libgwyprocess} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < %{version}
Conflicts:	%{name}-devel < %{version}

%description -n %{devname}
Header files, libraries and tools for Gwyddion module and plug-in development.
This package also contains the API docmentation and sample plug-ins in various
programming languages.

%files -n %{devname}
%doc devel-docs/CODING-STANDARDS
%doc data/%{name}.vim
%{_includedir}/%{name}/
%if %{with doc}
%{_datadir}/gtk-doc/html/*
%endif
%{_libdir}/*.so
%{_libdir}/pkgconfig/gwyddion.pc
%{_libdir}/%{name}/include/gwyconfig.h
# Plug-ins and plug-in devel stuff
%{_docdir}/%{name}/plugins/
%{_libdir}/%{name}/perl/
%{_libdir}/%{name}/ruby/
%{_libexecdir}/%{name}/plugins/
%if %{with python}
%{_libdir}/%{name}/python/
%{_datadir}/gtksourceview-2.0/language-specs/pygwy.lang
%endif

#----------------------------------------------------------------------------

%if %{with thumbnailer_gconf}
%package thumbnailer_gconf
Summary:	GConf schemas for gwyddion-thumbnailer integration
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{EVRD}

%description thumbnailer_gconf
GConf schemas that register gwyddion-thumbnailer as thumbnailer for SPM files
in GNOME and XFce.

%files thumbnailer_gconf
%config(noreplace) %{_sysconfdir}/gconf/schemas/gwyddion-thumbnailer.schemas
%endif

#----------------------------------------------------------------------------

%if %{with thumbnailer_kde45}
%package thumbnailer_kde45
Summary:	kde45 gwyddion thumbnailer module
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description thumbnailer_kde45
Gwyddion-thumbnailer based KDE thumbnail creator extension module for SPM
files.

%files thumbnailer_kde45
%{_libdir}/kde45/gwythumbcreator.so
%endif

#----------------------------------------------------------------------------

%prep
%autosetup

%build
%if %{with python}
export PYTHON=%{__python3}
%endif

autoreconf -fiv
%configure \
	--enable-library-bloat \
	--%{?with_doc:en}%{!?with_doc:dis}able-gtk-doc-html \
	--%{?with_doc_pdf:en}%{!?with_doc_pdf:dis}able-gtk-doc-pdf \
	--%{?with_python:en}%{!?with_python:dis}able-pygwy \
	--with%{!?with_thumbnailer_kde45:out}-kde45-thumbnailer \
	--with%{!?with_python:out}-python \
	%{nil}
%make_build

%install
%make_install

# add plugins path
install -dm 0755 %{buildroot}%{_libexecdir}/%{name}/plugins/

# fix .desktop
desktop-file-edit \
	--remove-category="GTK" \
	--add-category="GTK" \
 	--add-category="Education" \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Perl, Python, and Ruby modules are private, remove the Perl man page.
rm -f %{buildroot}%{_mandir}/man3/Gwyddion::dump.*

# locales
%find_lang %{name}

