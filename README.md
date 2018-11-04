# GAN-for-Spectroscopic-Data

Note: This is a partial work of CS289A final project.

### Motivation
Synthetic data are routinely used in a nearly all scientific disciplines. These data are often produced through simulations that are expensive both computationally and in
cost. While these simulations are necessary in many cases, for example in creating estimated responses for proposed systems, in some applications, one may simply wish to augment existing
datasets. In these cases, it would be useful to be able to generate new data from existing data that are representative of typical measurements.

Adversarial learning is an exciting and active field of machine learning research. GANs have recently received attention for their ability to generate
novel data. In this work, we examine the effectiveness of GANs in generating synthetic scientific data.

### Real Data of Single Crystal Band Struction
Angle-resolved photoemission Spectroscopy (ARPES) is a powerful tool to investigate the electronic structure of a material. The electrons 
are photoemitted by a pulsed laser beam in an ultra-high vacuum chamber, and their kinetic energy can be calculated by the time-of-flight 
measurements. By accumulating the photoelectron counts at interested momentum, one can obtain an energy dispersion curve (EDC), which is a
plot of photoelectron intensity as a function of binding energy (EB). (This is the spectroscopic data that we will play with.) Hence, a full electronic band
structure of a material can be mapped out by changing the sample rotational angle.

### Model
We use the Least Squares GAN consisting of a generator with three fully-connected layers, and a discriminator with two fully-connected layers, with ReLU
activation functions between layers. The Adadelta optimization is selected for training with no requirement of tuning hyperparameters
and is robust to noisy gradient information. To evaluate the network for our data, the network has been written in Keras. We can verify the
performance of the generator by doing PCA separately on the genuine and synthetic data.
