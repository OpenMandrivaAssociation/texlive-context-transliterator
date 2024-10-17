Name:		texlive-context-transliterator
Version:	61127
Release:	2
Summary:	Transliterate text from 'other' alphabets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-transliterator
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-transliterator.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-transliterator.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The package will read text in one alphabet, and provide a
transliterated version in another; this is useful for readers
who cannot read the original alphabet. The package can make
allowance for hyphenation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-transliterator.xml
%{_texmfdistdir}/tex/context/third/transliterator
%doc %{_texmfdistdir}/doc/context/third/transliterator

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
