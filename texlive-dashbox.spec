Name:		texlive-dashbox
Version:	23425
Release:	2
Summary:	Draw dashed boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dashbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
