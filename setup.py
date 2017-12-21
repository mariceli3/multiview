import os
from distutils.core import setup


def configuration(parent_package='', top_path=None):
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)

    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('multiview')
    config.add_subpackage('doc')

    return config


SCIPY_MIN_VERSION = '0.13.3'
NUMPY_MIN_VERSION = '1.8.2'
extra_setuptools_args = dict(
    zip_safe=False,  # the package can run out of an .egg file
    include_package_data=True,
    extras_require={
        'alldeps': (
            'numpy >= {0}'.format(NUMPY_MIN_VERSION),
            'scipy >= {0}'.format(SCIPY_MIN_VERSION),
        ),
    },
)


setup(
    name="multiview",
    packages=["multiview", "examples", "multiview.tests"],
    version="1.0",
    description="Multiview clustering and dimensionality reduction",
    author="María Araceli Burgueño Caballero",
    author_email="mburgueno@uoc.edu",
    url="https://github.com/mariceli3/multiview",
    download_url="https://github.com/mariceli3/multiview/dist/multiview-1.0.tar.gz",
    keywords=["multiview", "clustering", "dimensionality reduction"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    long_description="""
    Multiview clustering and dimensionality reduction
    -------------------------------------------------
    The ``multiview`` package provides multiview methods to work with
    multiview data (datasets with several data matrices from the same
    samples). It contains methods for multiview dimensionality reduction
    and methods for multiview clustering.

    Multiview dimensionality reduction
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Given a multiview dataset with ``v`` input data matrices,multiview
    dimensionality reduction methods produce a single, low-dimensional
    projection of the input data samples, trying to mantain as much of the
    original information as possible.

    Package ``multiview`` offers the function :doc:`mvmds` to perform multiview
    dimensionality reduction in a similar way than the multidimensional scaling
    method (cmdscale in R).

    Another dimensionality reduction function in this package is :doc:`mvtsne`,
    that extends ``tsne`` in R to multiview data.

    Multiview clustering
    ~~~~~~~~~~~~~~~~~~~~
    Given a multiview dataset with ``v`` input data matrices, multiview
    clustering methods produce a single clustering assignment, considering
    the information from all the input views.
    Package ``multiview`` offers the function :doc:`mvsc` to perform multiview
    spectral clustering. It is an extension to spectral clustering
    (``kernlab::specc`` in R) to multiview datasets.
    """
)
