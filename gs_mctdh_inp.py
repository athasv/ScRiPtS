# MCTDH ground state input generator
# Created by Julia Endicott
# July 2012
# Email: jsendico@uwaterloo.ca
import sys

try:
    file_name=sys.argv[1]
    opname=sys.argv[2]
    NM=int(sys.argv[3])
    states=int(sys.argv[4])
except:
    print "Proper usage is: python gs_mcthd_inp.py new filename op file name (without extensions) number NM number states"
    sys.exit()
with open(file_name+".inp",'w') as f:  #create file
    s="RUN-SECTION\n\
    name = "+file_name+" relaxation=0 \n\
    tfinal = 500.0   tout = 0.2   tpsi= 1.0\n\
    psi  auto=twice  steps  gridpop cross orben\n\
    title = single set\n\
    end-run-section\n\n\
    OPERATOR-SECTION\n\
    oppath = .\n\
    opname = "+opname+"\n\
    end-operator-section\n\n\
    SPF-BASIS-SECTION\n\
    multi-set\n"\
    +NM*("      v%02d      =  " +(states)*"1, "+"1\n") % tuple(range(1,NM+1))\
    +"end-spf-basis-section\n\n\
    PRIMITIVE-BASIS-SECTION\n"\
    +NM*"    v%02d    HO     30   0.0     1.0     1.0\n" % tuple(range(1,NM+1))\
    +"    el     el     %d\n"\
    "end-primitive-basis-section\n\n\
INTEGRATOR-SECTION\n\
CMF      = 1.0, 3.0d-3\n\
RK8/spf  = 1.0d-8, 0.1\n\
RRDAV/A  = 520, 1.0d-9  # 720, 1.0d-9  ## 760, 1.0d-9\n\
energyorb  eps_inv=1.d-9\n\
end-integrator-section\n\n\
INIT_WF-SECTION\n\
build\n\
  init_state=%d\n" % (states+1, states+1)\
    +NM*"    v%02d    HO     0.0   0.0     1.0     1.0\n" % tuple(range(1,NM+1))\
    +"end-build\n\
end-init_wf-section\n\n\
end-input" #create string 
    f.write(s) #write string to file
