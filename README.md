# Lattice based cryptography

Lattice-based cryptography is a new wave of primitives used for post-quantum cryptography.
For instance, public-key cryptography will theoretically fall because of Shor's algorithm. While lattice problems will be hard enough so even quantum computer could not crack them.

Lattices can be found in geometry and group theory. It is an infinite set of points in a space R with specific properties.

**Properties :**
- When you add or substract two points together, it produced another lattice point.
- Every lattice points are separated by a minimal distance
- Every point in the space is within some maximum distance of a lattice point

# Introduction to lattices

## Vectors

A vector can be considered as pair of number v = (a, b). You have two dimensional vector but we can also have three dimensional vector v = (a, b, c). And more.

Operations such as addition, substraction or multiplication works as follow :
- vector addition : Add two vectors and you get another vector <br/>
v = (a, b), w = (c, d) <br/>
**v + w = (a, b) + (c, d) = (a+c, b+d)**

- vector substraction : Substract two vectors and you get another vector <br/>
v = (a, b), w = (c, d) <br/>
**v - w = (a, b) - (c, d) = (a-c, b-d)**

- scalar multiplication : Multiply a vector and a scalar and it also gives you a vector <br/>
v = (a, b), a scalar N </br>
**v * N = (a * N, b * N)**

- dot product : Multiply two vectors and it produces a scalar <br/>
v = (a, b), w = (c, d). <br/>
**v * w = (a * c) + (b * d)**


### Exercice : 
1) Two dimensions vector : v = (3, 6) and w = (2, 4) <br/>
Solve this equation **v * (4 * v - w)**. <br/>
Hint : At the end you should get only one number.


### Correction :  
1) 4 * v = (4 * 3, 4 * 6) = (12, 24)
2) (12, 24) - w = (12, 24) - (2, 4) = (12-2, 24-4) = (10, 20)
3) v * (10, 20) = (3 * 10) + (6 * 20) = 30 + 120 = 150 <br/>
Result = 150

## Basis

TODO ...


# Real World application of Lattices

In 2016, the NIST launched the PQC challenge which intended to establish a new standard for post-quantum cryptography. Since the beginning, a lot of exciting algorithms have been submitted. But in the end a lot of them were compromised by cryptanalisys attack. Hopefully, lattices have gone through the challenge and has been standardized by the NIST. This means, lattices are in a good way for real world application.

The select algorithms are **Kyber** and **Dilithium**. Kyber is key encapsulation mechanism (KEM) and Dilithium a digital signature scheme (DSS).
Both formed the **CRYSTALS** (Cryptographic Suite for Algebraic Lattices"). Source :
https://pq-crystals.org/index.shtml <br/>


Note : This first standard doesn't mark the beginning of transition from current cryptography to post-quantum cryptography. It is only a first draw and years of experimentation are still on going. 