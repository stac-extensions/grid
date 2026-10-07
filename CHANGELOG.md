# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0]

### Added

- EEA Reference Grid
- Major TOM Grid

### Changed

- Clarified that numeric components of grid codes are zero-padded to a fixed width,
  with the widths for MGRS, MSIN, WRS-1, WRS-2 and CDEM
- Clarified that CDEM codes refer to the south-west corner of 1° × 1° tiles
- Aligned the allowed characters for grid square codes with the JSON schema

## [1.1.0]

### Fixed

- Text describes code prefix as alphanumeric and WGS1 and WGS2 are specified for Landsat, but
  schema only allows A-Z in the prefix.  This has been fixed to allow \[A-Z0-9]

## 1.0.0

### Added

- Initial release

[1.2.0]: <https://github.com/stac-extensions/grid/compare/v1.1.0...v1.2.0>
[1.1.0]: <https://github.com/stac-extensions/grid/compare/v1.0.0...v1.1.0>
