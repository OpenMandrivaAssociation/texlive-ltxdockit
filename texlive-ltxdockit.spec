# revision 21869
# category Package
# catalog-ctan /macros/latex/contrib/ltxdockit
# catalog-date 2010-12-10 17:32:44 +0100
# catalog-license lppl
# catalog-version 1.2c
Name:		texlive-ltxdockit
Version:	1.2d
Release:	2
Summary:	Documentation support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxdockit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxdockit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxdockit.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2c-2
+ Revision: 753573
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2c-1
+ Revision: 718910
- texlive-ltxdockit
- texlive-ltxdockit
- texlive-ltxdockit
- texlive-ltxdockit

