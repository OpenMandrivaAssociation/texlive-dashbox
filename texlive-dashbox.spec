# revision 23425
# category Package
# catalog-ctan /macros/latex/contrib/dashbox
# catalog-date 2011-08-05 01:24:20 +0200
# catalog-license lppl
# catalog-version 1.14
Name:		texlive-dashbox
Version:	1.14
Release:	1
Summary:	Draw dashed boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dashbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package can draw boxes that perform like \framebox or
\fbox, but use dashed lines. The package can also draw (an
illusion of) vertical stacks of boxes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dashbox/dashbox.sty
%doc %{_texmfdistdir}/doc/latex/dashbox/dashbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dashbox/dashbox.dtx
%doc %{_texmfdistdir}/source/latex/dashbox/dashbox.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
