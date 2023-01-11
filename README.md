# ipm_cppy
# Test module for ipm.cppy

The method gives result with 0.1 average error on 97% probability in well-defined (x_i >= 0, A_i >= b >= 0) inequality constraint problems.

## !!!It is advised to limit the tested problems number on 500 due to memory allocation issue!!!

Be sure that python and scipy package is installed to your machine

For testing problemsFileName.json from problems folder:

  1. Assign {problemsFileName}.json to the problemsFileName variable in the test.py
    
  2. Run:
  ```
    python test.py
  ```
Generate new problems by running:
  ```
    python problems.py
  ```

# References:
## [Lecture 17: Interior Point Methods](https://www.cs.princeton.edu/courses/archive/fall18/cos521/Lectures/lec17.pdf)
## [Lecture 17 — October 28, 2014](http://people.seas.harvard.edu/~cs224/fall14/lec/lec17.pdf)

### Other links:
#### [Introduction to Interior Point Methods](https://www.tu-ilmenau.de/fileadmin/Bereiche/IA/prozessoptimierung/vorlesungsskripte/abebe_geletu/IPM_Slides.pdf)
#### [12. Interior-point methods](https://web.stanford.edu/class/ee364a/lectures/barrier.pdf)
#### [Chapter 14 Linear Programming: Interior-Point Methods](https://pages.cs.wisc.edu/~swright/726/handouts/ip_h.pdf)
#### [Interior Point Methods for Linear Programming](https://www.maths.ed.ac.uk/hall/NATCOR_2014/IPMforLP.pdf)
#### [Interior Point Methods and Linear Programming](https://faculty.ksu.edu.sa/sites/default/files/Interior%20Point%20Methods%20and%20Linear%20Programming.pdf)
#### [Interior-Point Methods for Linear Optimization](http://s3.amazonaws.com/mitsloan-php/wp-faculty/sites/30/2016/12/15031751/Interior-Point-Methods-for-Linear-Optimization.pdf)
#### [Chapter 10 Interior-Point Methods for Linear Programming](https://people.inf.ethz.ch/fukudak/lect/opt2011/aopt11note4.pdf)
#### [Interior Methods for Nonlinear Optimization∗](https://people.kth.se/~andersf/doc/sirev41494.pdf)
#### [C_fakepathOptimal_Abdullayev(muh)_(2022_Umumi).docx](http://lms.adnsu.az/adnsuEducation/upl?neuron=932FC97AD7D41A63484CAB8B43699CEF&action=downloadDocument&fileId=1493847)
