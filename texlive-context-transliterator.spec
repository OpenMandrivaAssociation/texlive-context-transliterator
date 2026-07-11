%global tl_name context-transliterator
%global tl_revision 61127

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Transliterate text from other alphabets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-transliterator
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-transliterator.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-transliterator.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package will read text in one alphabet, and provide a transliterated
version in another; this is useful for readers who cannot read the
original alphabet. The package can make allowance for hyphenation.

