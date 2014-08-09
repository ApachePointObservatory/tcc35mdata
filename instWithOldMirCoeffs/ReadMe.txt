instrument data files with collimations coefficients from the old TCC

The current and old TCCs have different physical models for mirrors. As a result, the mirror coefficients must be adjusted to produce the same mirror motion. This is done by putting the old instrument data files (with values such as RotID suitably converted) into this directory and running a converter script mirrorCtrl/bin/35mCoeffConverter.py (a similar script will have to be written for other telescopes).
