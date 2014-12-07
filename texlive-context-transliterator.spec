# revision 29801
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-transliterator
# catalog-date 2013-04-09 13:56:04 +0200
# catalog-license bsd
# catalog-version undef
Name:		texlive-context-transliterator
Version:	20130409
Release:	8
Summary:	Transliterate text from 'other' alphabets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-transliterator
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-transliterator.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-transliterator.doc.tar.xz
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
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.ctl
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.log
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.mkii
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.mkiv
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.mkiv.prep
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.pdf
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.run
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.tex
%{_texmfdistdir}/tex/context/third/transliterator/t-transliterator.tuc
%{_texmfdistdir}/tex/context/third/transliterator/trans_tables_bg.lua
%{_texmfdistdir}/tex/context/third/transliterator/trans_tables_glag.lua
%{_texmfdistdir}/tex/context/third/transliterator/trans_tables_gr.lua
%{_texmfdistdir}/tex/context/third/transliterator/trans_tables_iso9.lua
%{_texmfdistdir}/tex/context/third/transliterator/trans_tables_scntfc.lua
%{_texmfdistdir}/tex/context/third/transliterator/trans_tables_sr.lua
%{_texmfdistdir}/tex/context/third/transliterator/trans_tables_trsc.lua
%{_texmfdistdir}/tex/context/third/transliterator/transliterator.ctl
%{_texmfdistdir}/tex/context/third/transliterator/transliterator.log
%{_texmfdistdir}/tex/context/third/transliterator/transliterator.lua
%{_texmfdistdir}/tex/context/third/transliterator/transliterator.run
%{_texmfdistdir}/tex/context/third/transliterator/transliterator.tuc
%doc %{_texmfdistdir}/doc/context/third/transliterator/COPYING
%doc %{_texmfdistdir}/doc/context/third/transliterator/transliterator.pdf
%doc %{_texmfdistdir}/doc/context/third/transliterator/transliterator.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
