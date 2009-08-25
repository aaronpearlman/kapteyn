#  ==========================================================================
#                                Declarations
#  --------------------------------------------------------------------------

cdef extern from "wcslib/wcs.h":

   cdef struct pvcard:
      int i
      int m
      double value

   cdef struct pscard:
      int i
      int m
      char value[72]

   cdef struct wcsprm:
      int    flag
      int    naxis
      int    lng
      int    lat
      int    spec
      double *crpix
      double *pc
      double *cdelt
      double *crval
      double lonpole
      double latpole
      double restfrq
      double restwav
      pvcard *pv
      int    npv
      int    npvmax
      pscard *ps
      int    nps
      int    npsmax
      int    altlin
      double *cd
      double *crota
      char   (*ctype)[72]
      char   (*cunit)[72]
      char   specsys[72]
      char   lngtyp[8]
      double equinox

   cdef char *wcs_errmsg[]

   int wcsini(int, int, wcsprm *)
   int wcsset(wcsprm *)
   int wcsfree(wcsprm *)
   int wcss2p(wcsprm *, int ncoord, int nelem, double *world,
              double *phi, double *theta, double *imgcrd, double *pixcrd,
              int stat[])
   int wcsp2s(wcsprm *, int ncoord, int nelem, double *pixcrd,
              double *imgcrd, double *phi, double *theta, double *world,
              int stat[])
   int wcssub(int alloc, wcsprm *, int *nsub, int *axes, wcsprm *)
   int wcssptr(wcsprm *, int *i, char *ctype)
   int wcsprt(wcsprm *)
   int wcsmix(wcsprm *, int mixpix, int mixcel, double *vspan, double vstep,
              int viter, double *world, double *phi, double *theta,
              double *imgcrd, double *pixcrd)

cdef extern from "wcslib/wcsunits.h":
   int wcsutrn(int ctrl, char *unitstr)

cdef extern from "wcslib/wcsfix.h":
   int unitfix(int, wcsprm *)
   int celfix(wcsprm *)
   int spcfix(wcsprm *)
   cdef char *wcsfix_errmsg[]
