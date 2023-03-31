Name:		texlive-labelschanged
Version:	46040
Release:	2
Summary:	Identify labels which cause endless "may have changed" warnings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/labelschanged
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelschanged.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelschanged.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labelschanged.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Several conditions can cause LaTeX labels to keep changing, no
matter how many times a document is recompiled. This package
helps diagnose the cause of repeated "Label(s) may have
changed" warnings. The names and before/after definitions of
changing labels are printed at the end of each compile.
Multiply-defined labels are printed as well.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/labelschanged
%{_texmfdistdir}/tex/latex/labelschanged
%doc %{_texmfdistdir}/doc/latex/labelschanged

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
