from .meta import version

__version__ = version


__import__('pkg_resources').declare_namespace(__name__)  # type: ignore
