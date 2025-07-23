# Changelog

## [2.0.0](https://github.com/lippoliv/paperlessngx-to-sevdesk/compare/v1.0.2...v2.0.0) (2025-07-23)


### ⚠ BREAKING CHANGES

* **deps:** require python 3.13 (after #47)

### Features

* add success boot log output incl. info about starting document id ([#49](https://github.com/lippoliv/paperlessngx-to-sevdesk/issues/49)) ([7cb482d](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/7cb482d3f5c61d80c15955b1ad29ce7f2320d3b8))
* add webhook endpoint ([#51](https://github.com/lippoliv/paperlessngx-to-sevdesk/issues/51)) ([d94cc32](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/d94cc32d97f46fe65b23843860836f2c68042675))


### Miscellaneous Chores

* **deps:** require python 3.13 (after [#47](https://github.com/lippoliv/paperlessngx-to-sevdesk/issues/47)) ([68e3ada](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/68e3ada3369fb483137426fccc8c4226bf7ca554))

## [1.0.2](https://github.com/lippoliv/paperlessngx-to-sevdesk/compare/v1.0.1...v1.0.2) (2024-07-23)


### Bug Fixes

* index out of range error ([#36](https://github.com/lippoliv/paperlessngx-to-sevdesk/issues/36)) ([f237d90](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/f237d90aa80bbb48d2163dc8980ed0d39a8d885c))

## [1.0.1](https://github.com/lippoliv/paperlessngx-to-sevdesk/compare/v1.0.0...v1.0.1) (2023-12-18)


### Bug Fixes

* run actions on release please tags ([ecb620c](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/ecb620c7c885bbd2b7d842c6e7e3aadd13c46017))

## 1.0.0 (2023-12-18)


### Features

* make tag id and document type id optional ([921431a](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/921431a71e6d9d56d0a0135ab20ffd175bc6eaef))


### Bug Fixes

* show error message if important env var is not set ([d2c9af1](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/d2c9af1035e79f0ee7579b5a003ee8cd05027c3b))


### Performance Improvements

* use smaller docker image (python:3.11.7-slim) ([a2fd387](https://github.com/lippoliv/paperlessngx-to-sevdesk/commit/a2fd3878259e29f38c0ed5e5dddbd802af8be692))
