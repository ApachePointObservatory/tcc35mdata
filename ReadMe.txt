Data files for the TCC

The environment variable $TCC_DATA_DIR must point to this directory

Contents:
- axelim.dat: axis limit data in the format of "show block axelim"
- earthpred.dat: Earth orientation predictions as output by earthFilt.py
- iersbulla.dat: IERS Bulletin A. This file is optional, but if present you can run earthFilt.py to generate earthpred.dat.
- posRefCatalog.dat: position reference star catalog; see header for format
- telmod.dat: telescope model in standard TPOINT format
- tune.dat: tuning data in the format of "show block tune"
- inst/: directory of instrument data files, in the form described in the TCC Operator's Manual
