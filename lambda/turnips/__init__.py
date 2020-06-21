import pkg_resources
import setuptools_scm

PKGNAME = 'turnips'


def install_version() -> str:
    return pkg_resources.get_distribution(PKGNAME).version


def live_version() -> str:
    version = setuptools_scm.get_version(root='..', relative_to=__file__)
    return version


def get_version() -> str:
    try:
        version = live_version()
    except LookupError:
        version = install_version()
    return version
