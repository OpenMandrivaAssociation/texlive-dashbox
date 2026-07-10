%global tl_name dashbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.14
Release:	%{tl_revision}.1
Summary:	Draw dashed boxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dashbox
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can draw boxes that perform like \framebox or \fbox, but use
dashed lines. The package can also draw (an illusion of) vertical stacks
of boxes.

