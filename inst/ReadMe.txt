instrument data files

Each instrument has one or more data files associated with it, to tell the TCC how the instrument is configured (is a rotator available, etc.) and where the instrument is located in the focal plane. Even the names of the files supply important information, so please be careful when making changes!

For information on creating and modifying these files, please read the Operator's Manual. 

A description of the instrument position names (e.g. CA1, NA1) is contained in include/tcc/basics.h

The data files themselves contain extensive comments. Further information on individual entries in the files can be derived by reading the comments in the file and reading Russell Owen's paper on coordinate conversions. 

The file blank.dat is a template for generating new files. Use only the section relevant to the kind of data file you are creating.
