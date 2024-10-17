Name:		texlive-ltxdockit
Version:	21869
Release:	2
Summary:	Documentation support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ltxdockit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxdockit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxdockit.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle, consisting of a simple wrapper class and some
packages, forms a small LaTeX/BibTeX documentation kit; the
author uses it for some of his own packages. The package is not
supported: users should not attempt its use unless they are
capable of dealing with problems unaided. (The actual purpose
of releasing the package is to make it possible for third
parties to compile the documentation of other packages, should
that be necessary.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltxdockit/btxdockit.sty
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.cfg
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.cls
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.def
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.sty
%doc %{_texmfdistdir}/doc/latex/ltxdockit/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
