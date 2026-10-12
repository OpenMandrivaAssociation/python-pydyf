Name:		python-pydyf
Version:	0.12.1
Release:	2
Summary:	A low-level PDF generator
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/pydyf/
Source0:	pydyf-0.12.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(flit-core)
BuildArch:	noarch
%description
A low-level PDF generator.

%files
%{py_sitedir}/*
