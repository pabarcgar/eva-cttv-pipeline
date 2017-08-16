import clinvar
import json
from pyxb_encoder import PyxbEncoder

xml = open('singleRecord.xml').read()
ReleaseSet = clinvar.CreateFromDocument(xml)

# print(ReleaseSet.__dict__)
# print(type(ReleaseSet.ClinVarSet[0].ReferenceClinVarAssertion.ObservedIn))
print(ReleaseSet.ClinVarSet[0].ReferenceClinVarAssertion.ObservedIn[0].Method[0].MethodType)
print(type(ReleaseSet.ClinVarSet[0].ReferenceClinVarAssertion.ObservedIn[0].Method[0].MethodType))
for clinvar in ReleaseSet.ClinVarSet:
    print(json.dumps(clinvar, cls=PyxbEncoder))
# print(type(ReleaseSet.ClinVarSet[0].ReferenceClinVarAssertion.Assertion))
# print(type(ReleaseSet.ClinVarSet[0]))
# print(type(ReleaseSet))

# json.dumps(ReleaseSet.ClinVarSet[0])
