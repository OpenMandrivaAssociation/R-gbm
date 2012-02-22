%global packname  gbm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.6_3.1
Release:          1
Summary:          Generalized Boosted Regression Models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-3.1.tar.gz
Requires:         R-survival R-lattice R-splines
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-survival
BuildRequires:    R-lattice R-splines

%description
This package implements extensions to Freund and Schapire's AdaBoost
algorithm and Friedman's gradient boosting machine. Includes regression
methods for least squares, absolute loss, quantile regression, logistic,
Poisson, Cox proportional hazards partial likelihood, and AdaBoost
exponential loss.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
