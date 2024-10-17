Name:           ocaml-batteries
Version:        20090903
Release:        %mkrel 4
Summary:        Batteries included: OCaml development platform
License:        LGPL + linking exception, MIT, BSD, public domain
Group:          Development/Other
URL:            https://batteries.forge.ocamlcore.org/
Source0:        http://forge.ocamlcore.org/frs/download.php/256/batteries-%{version}.tgz
Source1:        batteries-beta1-html.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml >= 3.11
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ncurses-devel

BuildRequires:  camlp4
BuildRequires:  ocaml-type-conv
BuildRequires:  ocaml-sexplib-devel >= 3.7.5
BuildRequires:  ocaml-bin-prot-devel
BuildRequires:  ocaml-camomile-devel >= 0.7
BuildRequires:  ocaml-camlzip-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-pcre-devel

Requires:  ocaml-type-conv
Requires:  ocaml-sexplib
Requires:  ocaml-bin-prot
Requires:  ocaml-camomile
Requires:  ocaml-camlzip
Requires:  ocaml-ocamlnet
Requires:  ocaml-pcre

%description
Batteries included is a community-driven effort to standardize on an
uniform, documented, and comprehensive OCaml development platform.

Batteries included serves the following purposes:
 * define a standard set of libraries which may be expected on every
   compliant installation of OCaml
 * organize these libraries into a hierarchy of modules, with one
   source of documentation
 * define a standard set of language extensions which may be expected
   on every compliant installation of OCaml
 * provide a consistent API for otherwise independent libraries.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Development/Other

%description    doc
The %{name}-doc package contains html documentation for %{name}.

%prep
%setup -q -n batteries-%{version}
tar xjf %{SOURCE1}

%build
%configure --prefix=%{buildroot}
make all opt top syntax \
  DESTDIR=%{buildroot}%{_libdir}/ocaml
#make doc

%install
rm -rf %{buildroot}
#make install install-doc \
make install \
  DESTDIR=%{buildroot}%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE ChangeLog README TODO
%dir %{_libdir}/ocaml/batteries
%dir %{_libdir}/ocaml/batteries_threads
%dir %{_libdir}/ocaml/batteries_nothreads
%{_libdir}/ocaml/batteries*/META
%{_libdir}/ocaml/batteries*/*.cma
%{_libdir}/ocaml/batteries*/*.cmi
%{_libdir}/ocaml/batteries*/*.cmo
%{_libdir}/ocaml/batteries/ocaml
%{_libdir}/ocaml/batteries/ocamlbuild
%{_libdir}/ocaml/batteries/ocamlc
%{_libdir}/ocaml/batteries/ocamlcp
%{_libdir}/ocaml/batteries/ocamldep
%{_libdir}/ocaml/batteries/ocamlopt
%{_libdir}/ocaml/batteries/top.ml
%{_libdir}/ocaml/batteries/toplevel.top
%{_libdir}/ocaml/batteries_nothreads/run.byte
%{_libdir}/ocaml/batteries_nothreads/run.native
%{_libdir}/ocaml/batteries_threads/run.byte
%{_libdir}/ocaml/batteries_threads/run.native

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/batteries*/*.a
%{_libdir}/ocaml/batteries*/*.cmxa

%files doc
%defattr(-,root,root)
%doc html

