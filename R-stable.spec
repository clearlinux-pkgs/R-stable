#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-stable
Version  : 1.1.4
Release  : 13
URL      : https://cran.r-project.org/src/contrib/stable_1.1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/stable_1.1.4.tar.gz
Summary  : Probability Functions and Generalized Regression Models for
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-stable-lib = %{version}-%{release}
Requires: R-rmutil
Requires: R-stabledist
BuildRequires : R-rmutil
BuildRequires : R-stabledist
BuildRequires : buildreq-R

%description
stable variate; generalized regression models for the parameters
    of a stable distribution. See the README for how to make equivalent calls
    to those of 'stabledist'. See github for Journal article.

%package lib
Summary: lib components for the R-stable package.
Group: Libraries

%description lib
lib components for the R-stable package.


%prep
%setup -q -c -n stable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569375144

%install
export SOURCE_DATE_EPOCH=1569375144
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stable
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc stable || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/stable/DESCRIPTION
/usr/lib64/R/library/stable/INDEX
/usr/lib64/R/library/stable/Meta/Rd.rds
/usr/lib64/R/library/stable/Meta/features.rds
/usr/lib64/R/library/stable/Meta/hsearch.rds
/usr/lib64/R/library/stable/Meta/links.rds
/usr/lib64/R/library/stable/Meta/nsInfo.rds
/usr/lib64/R/library/stable/Meta/package.rds
/usr/lib64/R/library/stable/NAMESPACE
/usr/lib64/R/library/stable/NEWS.md
/usr/lib64/R/library/stable/R/stable
/usr/lib64/R/library/stable/R/stable.rdb
/usr/lib64/R/library/stable/R/stable.rdx
/usr/lib64/R/library/stable/help/AnIndex
/usr/lib64/R/library/stable/help/aliases.rds
/usr/lib64/R/library/stable/help/paths.rds
/usr/lib64/R/library/stable/help/stable.rdb
/usr/lib64/R/library/stable/help/stable.rdx
/usr/lib64/R/library/stable/html/00Index.html
/usr/lib64/R/library/stable/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/stable/libs/stable.so
/usr/lib64/R/library/stable/libs/stable.so.avx2
/usr/lib64/R/library/stable/libs/stable.so.avx512
