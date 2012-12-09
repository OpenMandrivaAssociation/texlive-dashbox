# revision 23425
# category Package
# catalog-ctan /macros/latex/contrib/dashbox
# catalog-date 2011-08-05 01:24:20 +0200
# catalog-license lppl
# catalog-version 1.14
Name:		texlive-dashbox
Version:	1.14
Release:	2
Summary:	Draw dashed boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dashbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can draw boxes that perform like \framebox or
\fbox, but use dashed lines. The package can also draw (an
illusion of) vertical stacks of boxes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dashbox/dashbox.sty
%doc %{_texmfdistdir}/doc/latex/dashbox/dashbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dashbox/dashbox.dtx
%doc %{_texmfdistdir}/source/latex/dashbox/dashbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.14-2
+ Revision: 750763
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.14-1
+ Revision: 718200
- texlive-dashbox
- texlive-dashbox
- texlive-dashbox
- texlive-dashbox

