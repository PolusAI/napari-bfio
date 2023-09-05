"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the Reader specification, but your plugin may choose to
implement multiple readers or even other plugin contributions. see:
https://napari.org/stable/plugins/guides.html?#readers
"""
import os
import logging
import numpy as np

BIOFORMATS_EXT = [
    '.1sc',
    '.2fl',
    '.acff',
    '.afi',
    '.afm',
    '.aim',
    '.al3d',
    '.ali',
    '.am',
    '.amiramesh',
    '.apl',
    '.arf',
    '.avi',
    '.bif',
    '.bin',
    '.bip',
    '.bmp',
    '.btf',
    '.c01',
    '.cfg',
    '.ch5',
    '.cif',
    '.cr2',
    '.crw',
    '.cxd',
    '.dat',
    '.db',
    '.dcm',
    '.dib',
    '.dicom',
    '.dm2',
    '.dm3',
    '.dm4',
    '.dti',
    '.dv',
    '.eps',
    '.epsi',
    '.exp',
    '.fdf',
    '.fff',
    '.ffr',
    '.fits',
    '.flex',
    '.fli',
    '.frm',
    '.gel',
    '.gif',
    '.grey',
    '.h5',
    '.hdf',
    '.hdr',
    '.hed', 
    '.his',
    '.htd',
    '.hx', 
    '.i2i',
    '.ics',
    '.ids',
    '.im3',
    '.img',
    '.img', 
    '.ims',
    '.inr',
    '.ipl',
    '.ipm',
    '.ipw',
    '.j2k',
    '.jp2',
    '.jpeg',
    '.jpf',
    '.jpg',
    '.jpk',
    '.jpx',
    '.klb',
    '.l2d',
    '.labels',
    '.lei',
    '.lif',
    '.liff',
    '.lim',
    '.lms',
    '.lof',
    '.lsm',
    '.map',
    '.mdb',
    '.mea',
    '.mnc',
    '.mng',
    '.mod',
    '.mov',
    '.mrc',
    '.mrcs',
    '.mrw',
    '.msr',
    '.mtb',
    '.mvd2',
    '.naf',
    '.nd',
    '.nd2',
    '.ndpi',
    '.ndpis',
    '.nef',
    '.nhdr',
    '.nii',
    '.nii.gz',
    '.nrrd',
    '.obf',
    '.obsep',
    '.oib',
    '.oif',
    '.oir',
    '.omp2info',
    '.par',
    '.pbm',
    '.pcoraw',
    '.pcx',
    '.pds',
    '.pgm',
    '.pic',
    '.pict',
    '.png',
    '.pnl',
    '.ppm',
    '.pr3',
    '.ps',
    '.psd',
    '.qptiff',
    '.r3d', 
    '.raw',
    '.rcpnl',
    '.rec',
    '.res',
    '.scn',
    '.sdt',
    '.seq',
    '.sif',
    '.sld',
    '.sldy',
    '.sm2',
    '.sm3',
    '.spc',
    '.spe',
    '.spi',
    '.st',
    '.stk',
    '.stp',
    '.svs',
    '.sxm', 
    '.tf2',
    '.tf8',
    '.tfr',
    '.tga',
    '.tif',
    '.tif', 
    '.tiff',
    '.tnb',
    '.top',
    '.txt',
    '.v',
    '.vff',
    '.vms',
    '.vsi',
    '.vws',
    '.wat',
    '.wpi',
    '.xdce',
    '.xlef',
    '.xqd',
    '.xqf',
    '.xv',
    '.xys',
    '.zfp',
    '.zfr',
    '.zvi',
]

def is_type_supported(path):
    if path.endswith(".ome.tiff"):
        return True
    elif path.endswith(".ome.tif"):
        return True
    elif path.endswith(".ome.zarr"):
        return True
    else:
        file_ext = os.path.splitext(path)[1]
        if file_ext in BIOFORMATS_EXT:
            return True
        else:
            return False

def napari_get_reader(path):
    """A basic implementation of a Reader contribution.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """
    if isinstance(path, list):
        # reader plugins may be handed single path, or a list of paths.
        # if it is a list, it is assumed to be an image stack...
        # so we are only going to look at the first file.
        path = path[0]

    # # if we know we cannot read the file, we immediately return None.
    if not is_type_supported(path):
        return None

    # otherwise we return the *function* that can read ``path``.
    return reader_function


def reader_function(path):
    """Take a path or list of paths and return a list of LayerData tuples.

    Readers are expected to return data as a list of tuples, where each tuple
    is (data, [add_kwargs, [layer_type]]), "add_kwargs" and "layer_type" are
    both optional.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    layer_data : list of tuples
        A list of LayerData tuples where each tuple in the list contains
        (data, metadata, layer_type), where data is a numpy array, metadata is
        a dict of keyword arguments for the corresponding viewer.add_* method
        in napari, and layer_type is a lower-case string naming the type of
        layer. Both "meta", and "layer_type" are optional. napari will
        default to layer_type=="image" if not provided
    """
    # handle both a string and a list of strings
    paths = [path] if isinstance(path, str) else path
    # load all files into array
    layer_data = []
    from bfio import BioReader # import as late as possible
    for _path in paths:
        file_ext = os.path.splitext(path)[1]
        if not (_path.endswith(".ome.zarr") or _path.endswith(".ome.tiff") or _path.endswith(".ome.tif")): 
            try:
                import bioformats_jar
            except ModuleNotFoundError:
                file_ext_wo_dot = file_ext.lstrip(".")
                logging.error("The bioformats_jar Python package is not present. "
                        + f"*.{file_ext_wo_dot} file reading is supported by bioformats-jar Python package."
                        + f"Install bioformats-jar using pip or do 'pip install bfio[all]'"      
                        )     
                # loading dummy data of [[0,0],[0,0]]
                layer_data.append(( np.squeeze(np.zeros(shape=(2,2))),{}))                        
                continue
        br = BioReader(_path)
        layer_data.append((np.squeeze(br.read()), {"metadata":br.metadata}))
    
    return layer_data
