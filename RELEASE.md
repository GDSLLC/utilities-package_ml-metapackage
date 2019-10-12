# Releasing utilities-package_ml-metapackage

This documents how to release utilities-package_ml-metapackage. Various steps in this document may
require privileged access to private systems, so this document is only
targetted at utilities-package_ml-metapackage core members who have the ability to cut a release.

1. Update `utilitiespackagemlmetapackage/setup.py` to the version you want to release.

1. Update [CHANGELOG.md](https://github.com/terminal-labs/utilities-package_ml-metapackage/blob/master/CHANGELOG.md) to have a header with the release version and date.

1. Commit those changes and also tag the release with the version:

        $ git tag X.Y.Z
        $ git push --tags

1. Release this version on [GitHub](https://github.com/terminal-labs/utilities-package_ml-metapackage/releases).
