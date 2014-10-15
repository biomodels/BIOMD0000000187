# BIOMD0000000187: MODEL6655578762

## Installation

Download this repository, and install with distutils

`python setup.py install`

Or, install using pip

`pip install git+https://github.com/biomodels/BIOMD0000000187.git`

To install a specific version (in this example, from the 2014-09-16 BioModels release)

`pip install git+https://github.com/biomodels/BIOMD0000000187.git@20140916`


# Model Notes


Ibrahim2008 - Mitotic Spindle Assembly Checkpoint - Convey variant

The Mitotic Spindle Assembly Checkpoint ((M)SAC) is an evolutionary conserved
mechanism. This model incorporates the perspectives of three central control
pathways, namely Mad1/Mad2 induced Cdc20 sequestering based on the Template
Model, MCC formation, and APC inhibition. MCC:APC dissociation is described by
two alternatives models, namely the "Dissociation" and the "Convey" model
variants. Both these model are available in BioModels Database. This model
corresponds to the "Convey" variant.

This model is described in the article:

[In-silico modeling of the mitotic spindle assembly
checkpoint.](http://identifiers.org/pubmed/18253502)

Ibrahim B, Diekmann S, Schmitt E, Dittrich P

PLoS One. 2008 Feb 6;3(2):e1555.

Abstract:

BACKGROUND: The Mitotic Spindle Assembly Checkpoint ((M)SAC) is an
evolutionary conserved mechanism that ensures the correct segregation of
chromosomes by restraining cell cycle progression from entering anaphase until
all chromosomes have made proper bipolar attachments to the mitotic spindle.
Its malfunction can lead to cancer.

PRINCIPLE FINDINGS: We have constructed and validated for the human (M)SAC
mechanism an in silico dynamical model, integrating 11 proteins and complexes.
The model incorporates the perspectives of three central control pathways,
namely Mad1/Mad2 induced Cdc20 sequestering based on the Template Model, MCC
formation, and APC inhibition. Originating from the biochemical reactions for
the underlying molecular processes, non-linear ordinary differential equations
for the concentrations of 11 proteins and complexes of the (M)SAC are derived.
Most of the kinetic constants are taken from literature, the remaining four
unknown parameters are derived by an evolutionary optimization procedure for
an objective function describing the dynamics of the APC:Cdc20 complex.
MCC:APC dissociation is described by two alternatives, namely the
"Dissociation" and the "Convey" model variants. The attachment of the
kinetochore to microtubuli is simulated by a switching parameter silencing
those reactions which are stopped by the attachment. For both, the
Dissociation and the Convey variants, we compare two different scenarios
concerning the microtubule attachment dependent control of the dissociation
reaction. Our model is validated by simulation of ten perturbation
experiments.

CONCLUSION: Only in the controlled case, our models show (M)SAC behaviour at
meta- to anaphase transition in agreement with experimental observations. Our
simulations revealed that for (M)SAC activation, Cdc20 is not fully
sequestered; instead APC is inhibited by MCC binding.

This model describes the controlled dissociation variant of the mitotic
spindle assembly checkpoint. If the tool you use has problems with events, you
can uncomment the assignment rules for u and u_prime and comment out the list
of events.

In accordance with the authors due to typos in the original publication some
initial conditions and parameters were slightly changed in the model:  |
article | model  
---|---|---  
_[O-Mad2]_ | 1.5e-7 M | 1.3e-7 M  
_[BubR1:Bub3]_ | 1.30e-7 M | 1.27e-7 M  
_k -4 _ | 0.01 M -1 s -1 | 0.02 M -1 s -1  
_k -5 _ | 0.1 M -1 s -1 | 0.2 M -1 s -1  
  
This model is hosted on [BioModels Database](http://www.ebi.ac.uk/biomodels/)
and identified by:
[MODEL6655578762](http://identifiers.org/biomodels.db/MODEL6655578762) .

To cite BioModels Database, please use: [BioModels Database: An enhanced,
curated and annotated resource for published quantitative kinetic
models](http://identifiers.org/pubmed/20587024) .

To the extent possible under law, all copyright and related or neighbouring
rights to this encoded model have been dedicated to the public domain
worldwide. Please refer to [CC0 Public Domain
Dedication](http://creativecommons.org/publicdomain/zero/1.0/) for more
information.


