#!/usr/bin/python

"""Script to automatize a serie of Resp Gaussian calculations : take a log file as input """
"""and perform a serie of single points calculations --- March 2006 """
"""Takes 1 argument (ligand_name)                                   """

"""The name of the output is fixed to be : ligand_method_basis_scrf(0/1).opt.log"""
"""We assume that the name of Gaussian optimization logfile is ligand.opt.log   """
"""This could be indeed useful for the second script                            """

# We need several options 
import os
import re
from optparse import OptionParser
parser=OptionParser()

# the name of ligand geometry file w/o extension 
parser.add_option("-n", "--ligand", dest="lig", help="Name of ligand geom file without extension",metavar="FILE")

(options,args)=parser.parse_args()
lig=options.lig
geomfile=lig+'_geom'

# 8 calculations, for all combinations 

for level in ('mp2','scf','b3lyp'):
  for basis in ('6-31G*','cc-pVTZ'):
    for scrf in (0,1):
      # we read the common initial file 
      file=open('input.resp','r')
      intext=file.readlines()
      file.close()
      outtext=[]
      for line in intext:
        line=line.replace('LEVEL',level)
        line=line.replace('BASIS',basis)
        if scrf:
          line=line.replace('SCRF','scrf=(solvent=water)')
          input_gaussian=lig+'_'+level+'_'+basis+'_'+'scrf1'
          sub_gaussian=lig+'_'+level+'_'+basis+'_'+'scrf1'+'.sub'
          output_gaussian=lig+'_'+level+'_'+basis+'_'+'scrf1'+'.log'
        else:
          line=line.replace('SCRF','  ')
          input_gaussian=lig+'_'+level+'_'+basis+'_'+'scrf0'
          sub_gaussian=lig+'_'+level+'_'+basis+'_'+'scrf0'+'.sub'
          output_gaussian=lig+'_'+level+'_'+basis+'_'+'scrf0'+'.log'
       
        outtext.append(line)

      outfile=open(input_gaussian,'w')  # tempory file w/o opt extension 
      outfile.writelines(outtext)
      outfile.close()
      outtext=[]

      os.system("cat %(input_gaussian)s %(geomfile)s > %(input_gaussian)s.opt" %vars())
      # The new input files are ready 
        
      # We have to edit an auxiliaire sub file (for the French Cluster) to submit the job 
      infile2=open('sub.resp','r')
      intext2=infile2.readlines()
      infile2.close()

      outtext=[]

      for line in intext2:
        line=line.replace('fichier_input',input_gaussian+'.opt')
        line=line.replace('fichier_output',output_gaussian)
        outtext.append(line)

      outfile=open(sub_gaussian,'w')
      outfile.writelines(outtext)
      outfile.close()


# The last step is to submit to queue:
DIR = '/.automount/home/home1/edumont/DATABASE/database_mol2'
# We don't want to run mp2_631G* scf_cc-pVTZ
os.system("rm -f *mp2_631G*.sub *scf_cc-pVTZ*.sub")
for f in os.listdir(DIR):
    if f.endswith('.sub'):
        os.system("qsub %(f)s" % vars())
#       print "Submitted script %(outfile)s to queue." % vars()

