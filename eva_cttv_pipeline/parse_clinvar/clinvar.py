# ./clinvar.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-08-15 16:51:55.248593 by PyXB version 1.2.5 using Python 3.6.2.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a95dc0cc-81d1-11e7-bb31-14109fd615bd')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: typeStatus
class typeStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeStatus')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 17, 1)
    _Documentation = None
typeStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeStatus, enum_prefix=None)
typeStatus.current = typeStatus._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
typeStatus.completed_and_retired = typeStatus._CF_enumeration.addEnumeration(unicode_value='completed and retired', tag='completed_and_retired')
typeStatus.delete = typeStatus._CF_enumeration.addEnumeration(unicode_value='delete', tag='delete')
typeStatus.in_development = typeStatus._CF_enumeration.addEnumeration(unicode_value='in development', tag='in_development')
typeStatus.reclassified = typeStatus._CF_enumeration.addEnumeration(unicode_value='reclassified', tag='reclassified')
typeStatus.reject = typeStatus._CF_enumeration.addEnumeration(unicode_value='reject', tag='reject')
typeStatus.secondary = typeStatus._CF_enumeration.addEnumeration(unicode_value='secondary', tag='secondary')
typeStatus.suppressed = typeStatus._CF_enumeration.addEnumeration(unicode_value='suppressed', tag='suppressed')
typeStatus.under_review = typeStatus._CF_enumeration.addEnumeration(unicode_value='under review', tag='under_review')
typeStatus._InitializeFacetMap(typeStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeStatus', typeStatus)
_module_typeBindings.typeStatus = typeStatus

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 44, 11)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.HGVS_genomic_top_level = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, top level', tag='HGVS_genomic_top_level')
STD_ANON.HGVS_genomic_top_level_previous = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, top level, previous', tag='HGVS_genomic_top_level_previous')
STD_ANON.HGVS_genomic_top_level_other = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, top level, other', tag='HGVS_genomic_top_level_other')
STD_ANON.HGVS_genomic_RefSeqGene = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, RefSeqGene', tag='HGVS_genomic_RefSeqGene')
STD_ANON.HGVS_genomic_LRG = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, LRG', tag='HGVS_genomic_LRG')
STD_ANON.HGVS_genomic = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic', tag='HGVS_genomic')
STD_ANON.HGVS_coding_RefSeq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, coding, RefSeq', tag='HGVS_coding_RefSeq')
STD_ANON.HGVS_coding_LRG = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, coding, LRG', tag='HGVS_coding_LRG')
STD_ANON.HGVS_coding = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, coding', tag='HGVS_coding')
STD_ANON.HGVS_incomplete = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, incomplete', tag='HGVS_incomplete')
STD_ANON.HGVS_previous = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, previous', tag='HGVS_previous')
STD_ANON.HGVS_protein = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, protein', tag='HGVS_protein')
STD_ANON.HGVS_protein_RefSeq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, protein, RefSeq', tag='HGVS_protein_RefSeq')
STD_ANON.HGVS_non_coding = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, non-coding', tag='HGVS_non_coding')
STD_ANON.HGVS_non_validated = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, non-validated', tag='HGVS_non_validated')
STD_ANON.HGVS_RNA = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, RNA', tag='HGVS_RNA')
STD_ANON.HGVS_legacy = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, legacy', tag='HGVS_legacy')
STD_ANON.HGVS_uncertain = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS, uncertain', tag='HGVS_uncertain')
STD_ANON.HGVS = STD_ANON._CF_enumeration.addEnumeration(unicode_value='HGVS', tag='HGVS')
STD_ANON.NonHGVS = STD_ANON._CF_enumeration.addEnumeration(unicode_value='NonHGVS', tag='NonHGVS')
STD_ANON.Location = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Location', tag='Location')
STD_ANON.MiscellaneousDescription = STD_ANON._CF_enumeration.addEnumeration(unicode_value='MiscellaneousDescription', tag='MiscellaneousDescription')
STD_ANON.Description = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Description', tag='Description')
STD_ANON.FunctionalConsequence = STD_ANON._CF_enumeration.addEnumeration(unicode_value='FunctionalConsequence', tag='FunctionalConsequence')
STD_ANON.MolecularConsequence = STD_ANON._CF_enumeration.addEnumeration(unicode_value='MolecularConsequence', tag='MolecularConsequence')
STD_ANON.ProteinChange1LetterCode = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ProteinChange1LetterCode', tag='ProteinChange1LetterCode')
STD_ANON.ProteinChange3LetterCode = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ProteinChange3LetterCode', tag='ProteinChange3LetterCode')
STD_ANON.ActivityLevel = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ActivityLevel', tag='ActivityLevel')
STD_ANON.GlobalMinorAlleleFrequency = STD_ANON._CF_enumeration.addEnumeration(unicode_value='GlobalMinorAlleleFrequency', tag='GlobalMinorAlleleFrequency')
STD_ANON.AlleleFrequency = STD_ANON._CF_enumeration.addEnumeration(unicode_value='AlleleFrequency', tag='AlleleFrequency')
STD_ANON.Suspect = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Suspect', tag='Suspect')
STD_ANON.Allelic_Variant_previous = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Allelic Variant, previous', tag='Allelic_Variant_previous')
STD_ANON.acceptor_splice_site = STD_ANON._CF_enumeration.addEnumeration(unicode_value='acceptor splice site', tag='acceptor_splice_site')
STD_ANON.donor_splice_site = STD_ANON._CF_enumeration.addEnumeration(unicode_value='donor splice site', tag='donor_splice_site')
STD_ANON.nucleotide_change = STD_ANON._CF_enumeration.addEnumeration(unicode_value='nucleotide change', tag='nucleotide_change')
STD_ANON.protein_change_historical = STD_ANON._CF_enumeration.addEnumeration(unicode_value='protein change, historical', tag='protein_change_historical')
STD_ANON.transcript_variant = STD_ANON._CF_enumeration.addEnumeration(unicode_value='transcript variant', tag='transcript_variant')
STD_ANON.AbsoluteCopyNumber = STD_ANON._CF_enumeration.addEnumeration(unicode_value='AbsoluteCopyNumber', tag='AbsoluteCopyNumber')
STD_ANON.ReferenceCopyNumber = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ReferenceCopyNumber', tag='ReferenceCopyNumber')
STD_ANON.CopyNumberTuple = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CopyNumberTuple', tag='CopyNumberTuple')
STD_ANON.COSMIC = STD_ANON._CF_enumeration.addEnumeration(unicode_value='COSMIC', tag='COSMIC')
STD_ANON.SubmitterVariantId = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SubmitterVariantId', tag='SubmitterVariantId')
STD_ANON.ISCNCoordinates = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ISCNCoordinates', tag='ISCNCoordinates')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 133, 14)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.HGVS = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='HGVS', tag='HGVS')
STD_ANON_.genotype = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='genotype', tag='genotype')
STD_ANON_.Haploinsufficiency = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Haploinsufficiency', tag='Haploinsufficiency')
STD_ANON_.Triplosensitivity = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Triplosensitivity', tag='Triplosensitivity')
STD_ANON_.gene_relationships = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='gene relationships', tag='gene_relationships')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 157, 6)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.variant_in_gene = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='variant in gene', tag='variant_in_gene')
STD_ANON_2.co_occurring_variant = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='co-occurring variant', tag='co_occurring_variant')
STD_ANON_2.within_single_gene = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='within single gene', tag='within_single_gene')
STD_ANON_2.within_multiple_genes_by_overlap = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='within multiple genes by overlap', tag='within_multiple_genes_by_overlap')
STD_ANON_2.genes_overlapped_by_variant = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='genes overlapped by variant', tag='genes_overlapped_by_variant')
STD_ANON_2.near_gene_upstream = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='near gene, upstream', tag='near_gene_upstream')
STD_ANON_2.near_gene_downstream = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='near gene, downstream', tag='near_gene_downstream')
STD_ANON_2.asserted_but_not_computed = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='asserted, but not computed', tag='asserted_but_not_computed')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 179, 3)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.Gene = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Gene', tag='Gene')
STD_ANON_3.Variation = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Variation', tag='Variation')
STD_ANON_3.Insertion = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Insertion', tag='Insertion')
STD_ANON_3.Deletion = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Deletion', tag='Deletion')
STD_ANON_3.single_nucleotide_variant = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='single nucleotide variant', tag='single_nucleotide_variant')
STD_ANON_3.Indel = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Indel', tag='Indel')
STD_ANON_3.Duplication = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Duplication', tag='Duplication')
STD_ANON_3.Tandem_duplication = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Tandem duplication', tag='Tandem_duplication')
STD_ANON_3.Structural_variant = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Structural variant', tag='Structural_variant')
STD_ANON_3.copy_number_gain = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='copy number gain', tag='copy_number_gain')
STD_ANON_3.copy_number_loss = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='copy number loss', tag='copy_number_loss')
STD_ANON_3.protein_only = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='protein only', tag='protein_only')
STD_ANON_3.Microsatellite = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Microsatellite', tag='Microsatellite')
STD_ANON_3.fusion = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='fusion', tag='fusion')
STD_ANON_3.Inversion = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Inversion', tag='Inversion')
STD_ANON_3.Translocation = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Translocation', tag='Translocation')
STD_ANON_3.QTL = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='QTL', tag='QTL')
STD_ANON_3.Complex = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Complex', tag='Complex')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 292, 3)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.laboratory = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='laboratory', tag='laboratory')
STD_ANON_4.locus_specific_database_LSDB = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='locus-specific database (LSDB)', tag='locus_specific_database_LSDB')
STD_ANON_4.consortium = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='consortium', tag='consortium')
STD_ANON_4.resource = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='resource', tag='resource')
STD_ANON_4.other = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 306, 4)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.current = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
STD_ANON_5.replaced = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='replaced', tag='replaced')
STD_ANON_5.removed = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='removed', tag='removed')
STD_ANON_5.not_current = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='not current', tag='not_current')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 403, 6)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.RCV = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='RCV', tag='RCV')
STD_ANON_6.SCV = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='SCV', tag='SCV')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 428, 4)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.current = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
STD_ANON_7.replaced = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='replaced', tag='replaced')
STD_ANON_7.removed = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='removed', tag='removed')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 474, 11)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.ModeOfInheritance = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='ModeOfInheritance', tag='ModeOfInheritance')
STD_ANON_8.Penetrance = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Penetrance', tag='Penetrance')
STD_ANON_8.AgeOfOnset = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='AgeOfOnset', tag='AgeOfOnset')
STD_ANON_8.Severity = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Severity', tag='Severity')
STD_ANON_8.ClinicalSignificanceHistory = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='ClinicalSignificanceHistory', tag='ClinicalSignificanceHistory')
STD_ANON_8.SeverityDescription = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='SeverityDescription', tag='SeverityDescription')
STD_ANON_8.AssertionMethod = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='AssertionMethod', tag='AssertionMethod')
STD_ANON_8.TestingLaboratory = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='TestingLaboratory', tag='TestingLaboratory')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 538, 6)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.RCV = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='RCV', tag='RCV')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 548, 4)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.current = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
STD_ANON_10.replaced = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='replaced', tag='replaced')
STD_ANON_10.removed = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='removed', tag='removed')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 584, 11)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.ModeOfInheritance = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='ModeOfInheritance', tag='ModeOfInheritance')
STD_ANON_11.Penetrance = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='Penetrance', tag='Penetrance')
STD_ANON_11.AgeOfOnset = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='AgeOfOnset', tag='AgeOfOnset')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 626, 8)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.Description = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='Description', tag='Description')
STD_ANON_12.MolecularConsequence = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='MolecularConsequence', tag='MolecularConsequence')
STD_ANON_12.HGVS = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS', tag='HGVS')
STD_ANON_12.HGVS_genomic_top_level = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, top level', tag='HGVS_genomic_top_level')
STD_ANON_12.HGVS_genomic_top_level_previous = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, top level, previous', tag='HGVS_genomic_top_level_previous')
STD_ANON_12.HGVS_genomic_top_level_other = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, top level, other', tag='HGVS_genomic_top_level_other')
STD_ANON_12.HGVS_genomic_RefSeqGene = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, RefSeqGene', tag='HGVS_genomic_RefSeqGene')
STD_ANON_12.HGVS_genomic_LRG = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, genomic, LRG', tag='HGVS_genomic_LRG')
STD_ANON_12.HGVS_coding_RefSeq = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, coding, RefSeq', tag='HGVS_coding_RefSeq')
STD_ANON_12.HGVS_coding_LRG = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, coding, LRG', tag='HGVS_coding_LRG')
STD_ANON_12.HGVS_coding = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, coding', tag='HGVS_coding')
STD_ANON_12.HGVS_RNA = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, RNA', tag='HGVS_RNA')
STD_ANON_12.HGVS_previous = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, previous', tag='HGVS_previous')
STD_ANON_12.HGVS_protein = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, protein', tag='HGVS_protein')
STD_ANON_12.HGVS_protein_RefSeq = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, protein, RefSeq', tag='HGVS_protein_RefSeq')
STD_ANON_12.HGVS_nucleotide = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, nucleotide', tag='HGVS_nucleotide')
STD_ANON_12.HGVS_non_validated = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, non-validated', tag='HGVS_non_validated')
STD_ANON_12.HGVS_uncertain = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='HGVS, uncertain', tag='HGVS_uncertain')
STD_ANON_12.FunctionalConsequence = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='FunctionalConsequence', tag='FunctionalConsequence')
STD_ANON_12.ISCNCoordinates = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='ISCNCoordinates', tag='ISCNCoordinates')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 672, 3)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.Gene = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Gene', tag='Gene')
STD_ANON_13.Variant = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Variant', tag='Variant')
STD_ANON_13.gene_variant = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='gene-variant', tag='gene_variant')
STD_ANON_13.OMIM_record = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='OMIM record', tag='OMIM_record')
STD_ANON_13.Haplotype = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Haplotype', tag='Haplotype')
STD_ANON_13.Phase_unknown = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Phase unknown', tag='Phase_unknown')
STD_ANON_13.Distinct_chromosomes = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Distinct chromosomes', tag='Distinct_chromosomes')
STD_ANON_13.CompoundHeterozygote = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='CompoundHeterozygote', tag='CompoundHeterozygote')
STD_ANON_13.Diplotype = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Diplotype', tag='Diplotype')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 702, 3)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.CompoundHeterozygote = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='CompoundHeterozygote', tag='CompoundHeterozygote')
STD_ANON_14.Diplotype = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='Diplotype', tag='Diplotype')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 744, 3)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.Disease = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='Disease', tag='Disease')
STD_ANON_15.DrugResponse = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='DrugResponse', tag='DrugResponse')
STD_ANON_15.Finding = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='Finding', tag='Finding')
STD_ANON_15.PhenotypeInstruction = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='PhenotypeInstruction', tag='PhenotypeInstruction')
STD_ANON_15.TraitChoice = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='TraitChoice', tag='TraitChoice')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 806, 6)
    _Documentation = None
STD_ANON_16._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_16, enum_prefix=None)
STD_ANON_16.phenocopy = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='phenocopy', tag='phenocopy')
STD_ANON_16.Subphenotype = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='Subphenotype', tag='Subphenotype')
STD_ANON_16.DrugResponseAndDisease = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='DrugResponseAndDisease', tag='DrugResponseAndDisease')
STD_ANON_16.co_occurring_condition = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='co-occurring condition', tag='co_occurring_condition')
STD_ANON_16.Finding_member = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='Finding member', tag='Finding_member')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_enumeration)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 825, 3)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.Disease = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='Disease', tag='Disease')
STD_ANON_17.DrugResponse = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='DrugResponse', tag='DrugResponse')
STD_ANON_17.BloodGroup = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='BloodGroup', tag='BloodGroup')
STD_ANON_17.Finding = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='Finding', tag='Finding')
STD_ANON_17.NamedProteinVariant = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='NamedProteinVariant', tag='NamedProteinVariant')
STD_ANON_17.PhenotypeInstruction = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='PhenotypeInstruction', tag='PhenotypeInstruction')
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 872, 3)
    _Documentation = None
STD_ANON_18._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_18, enum_prefix=None)
STD_ANON_18.Disease = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='Disease', tag='Disease')
STD_ANON_18.DrugResponse = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='DrugResponse', tag='DrugResponse')
STD_ANON_18.Finding = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='Finding', tag='Finding')
STD_ANON_18.PhenotypeInstruction = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='PhenotypeInstruction', tag='PhenotypeInstruction')
STD_ANON_18.TraitChoice = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='TraitChoice', tag='TraitChoice')
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_enumeration)
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 936, 6)
    _Documentation = None
STD_ANON_19._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_19, enum_prefix=None)
STD_ANON_19.phenocopy = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='phenocopy', tag='phenocopy')
STD_ANON_19.Subphenotype = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Subphenotype', tag='Subphenotype')
STD_ANON_19.DrugResponseAndDisease = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='DrugResponseAndDisease', tag='DrugResponseAndDisease')
STD_ANON_19.co_occurring_condition = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='co-occurring condition', tag='co_occurring_condition')
STD_ANON_19.Finding_member = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='Finding member', tag='Finding_member')
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_enumeration)
_module_typeBindings.STD_ANON_19 = STD_ANON_19

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 955, 3)
    _Documentation = None
STD_ANON_20._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_20, enum_prefix=None)
STD_ANON_20.Disease = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='Disease', tag='Disease')
STD_ANON_20.DrugResponse = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='DrugResponse', tag='DrugResponse')
STD_ANON_20.BloodGroup = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='BloodGroup', tag='BloodGroup')
STD_ANON_20.Finding = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='Finding', tag='Finding')
STD_ANON_20.NamedProteinVariant = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='NamedProteinVariant', tag='NamedProteinVariant')
STD_ANON_20.PhenotypeInstruction = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='PhenotypeInstruction', tag='PhenotypeInstruction')
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_enumeration)
_module_typeBindings.STD_ANON_20 = STD_ANON_20

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1038, 4)
    _Documentation = None
STD_ANON_21._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_21, enum_prefix=None)
STD_ANON_21.number_of_occurrences = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='number of occurrences', tag='number_of_occurrences')
STD_ANON_21.p_value = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='p value', tag='p_value')
STD_ANON_21.odds_ratio = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='odds ratio', tag='odds_ratio')
STD_ANON_21.variant_call = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='variant call', tag='variant_call')
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_enumeration)
_module_typeBindings.STD_ANON_21 = STD_ANON_21

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1060, 4)
    _Documentation = None
STD_ANON_22._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_22, enum_prefix=None)
STD_ANON_22.submitter_generated = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='submitter-generated', tag='submitter_generated')
STD_ANON_22.data_mining = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='data mining', tag='data_mining')
STD_ANON_22.data_review = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='data review', tag='data_review')
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_enumeration)
_module_typeBindings.STD_ANON_22 = STD_ANON_22

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1077, 11)
    _Documentation = None
STD_ANON_23._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_23, enum_prefix=None)
STD_ANON_23.Location = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='Location', tag='Location')
STD_ANON_23.ControlsAppropriate = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='ControlsAppropriate', tag='ControlsAppropriate')
STD_ANON_23.MethodAppropriate = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='MethodAppropriate', tag='MethodAppropriate')
STD_ANON_23.TestName = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='TestName', tag='TestName')
STD_ANON_23.StructVarMethodType = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='StructVarMethodType', tag='StructVarMethodType')
STD_ANON_23.ProbeAccession = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='ProbeAccession', tag='ProbeAccession')
STD_ANON_23.TestingLaboratory = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='TestingLaboratory', tag='TestingLaboratory')
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_enumeration)
_module_typeBindings.STD_ANON_23 = STD_ANON_23

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1121, 9)
    _Documentation = None
STD_ANON_24._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_24, enum_prefix=None)
STD_ANON_24.curation = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='curation', tag='curation')
STD_ANON_24.literature_only = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='literature only', tag='literature_only')
STD_ANON_24.reference_population = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='reference population', tag='reference_population')
STD_ANON_24.re_interpretation = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='re-interpretation', tag='re_interpretation')
STD_ANON_24.case_control = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='case-control', tag='case_control')
STD_ANON_24.clinical_testing = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='clinical testing', tag='clinical_testing')
STD_ANON_24.in_vitro = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='in vitro', tag='in_vitro')
STD_ANON_24.in_vivo = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='in vivo', tag='in_vivo')
STD_ANON_24.inferred_from_source = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='inferred from source', tag='inferred_from_source')
STD_ANON_24.research = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='research', tag='research')
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_enumeration)
_module_typeBindings.STD_ANON_24 = STD_ANON_24

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1156, 11)
    _Documentation = None
STD_ANON_25._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_25, enum_prefix=None)
STD_ANON_25.Description = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='Description', tag='Description')
STD_ANON_25.VariantAlleles = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='VariantAlleles', tag='VariantAlleles')
STD_ANON_25.SubjectsWithVariant = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='SubjectsWithVariant', tag='SubjectsWithVariant')
STD_ANON_25.SubjectsWithDifferentCausativeVariant = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='SubjectsWithDifferentCausativeVariant', tag='SubjectsWithDifferentCausativeVariant')
STD_ANON_25.VariantChromosomes = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='VariantChromosomes', tag='VariantChromosomes')
STD_ANON_25.IndependentObservations = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='IndependentObservations', tag='IndependentObservations')
STD_ANON_25.SingleHeterozygote = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='SingleHeterozygote', tag='SingleHeterozygote')
STD_ANON_25.CompoundHeterozygote = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='CompoundHeterozygote', tag='CompoundHeterozygote')
STD_ANON_25.Homozygote = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='Homozygote', tag='Homozygote')
STD_ANON_25.Hemizygote = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='Hemizygote', tag='Hemizygote')
STD_ANON_25.NumberMosaic = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='NumberMosaic', tag='NumberMosaic')
STD_ANON_25.ObservedUnspecified = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='ObservedUnspecified', tag='ObservedUnspecified')
STD_ANON_25.AlleleFrequency = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='AlleleFrequency', tag='AlleleFrequency')
STD_ANON_25.SecondaryFinding = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='SecondaryFinding', tag='SecondaryFinding')
STD_ANON_25.GenotypeAndMOIConsistent = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='GenotypeAndMOIConsistent', tag='GenotypeAndMOIConsistent')
STD_ANON_25.UnaffectedFamilyMemberWithCausativeVariant = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='UnaffectedFamilyMemberWithCausativeVariant', tag='UnaffectedFamilyMemberWithCausativeVariant')
STD_ANON_25.HetParentTransmitNormalAllele = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='HetParentTransmitNormalAllele', tag='HetParentTransmitNormalAllele')
STD_ANON_25.CosegregatingFamilies = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='CosegregatingFamilies', tag='CosegregatingFamilies')
STD_ANON_25.InformativeMeioses = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='InformativeMeioses', tag='InformativeMeioses')
STD_ANON_25.SampleLocalID = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='SampleLocalID', tag='SampleLocalID')
STD_ANON_25.FamilyHistory = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='FamilyHistory', tag='FamilyHistory')
STD_ANON_25.NumFamiliesWithVariant = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='NumFamiliesWithVariant', tag='NumFamiliesWithVariant')
STD_ANON_25.NumFamiliesWithSegregationObserved = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='NumFamiliesWithSegregationObserved', tag='NumFamiliesWithSegregationObserved')
STD_ANON_25.SegregationObserved = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='SegregationObserved', tag='SegregationObserved')
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_enumeration)
_module_typeBindings.STD_ANON_25 = STD_ANON_25

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1234, 4)
    _Documentation = None
STD_ANON_26._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_26, enum_prefix=None)
STD_ANON_26.germline = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='germline', tag='germline')
STD_ANON_26.somatic = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='somatic', tag='somatic')
STD_ANON_26.de_novo = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='de novo', tag='de_novo')
STD_ANON_26.unknown = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON_26.not_provided = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='not provided', tag='not_provided')
STD_ANON_26.inherited = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='inherited', tag='inherited')
STD_ANON_26.maternal = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='maternal', tag='maternal')
STD_ANON_26.paternal = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='paternal', tag='paternal')
STD_ANON_26.uniparental = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='uniparental', tag='uniparental')
STD_ANON_26.biparental = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='biparental', tag='biparental')
STD_ANON_26.not_reported = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='not-reported', tag='not_reported')
STD_ANON_26.tested_inconclusive = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='tested-inconclusive', tag='tested_inconclusive')
STD_ANON_26.not_applicable = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='not applicable', tag='not_applicable')
STD_ANON_26.experimentally_generated = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='experimentally generated', tag='experimentally_generated')
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_enumeration)
_module_typeBindings.STD_ANON_26 = STD_ANON_26

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1271, 8)
    _Documentation = None
STD_ANON_27._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_27, enum_prefix=None)
STD_ANON_27.days = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='days', tag='days')
STD_ANON_27.weeks = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='weeks', tag='weeks')
STD_ANON_27.months = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='months', tag='months')
STD_ANON_27.years = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='years', tag='years')
STD_ANON_27.weeks_gestation = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='weeks gestation', tag='weeks_gestation')
STD_ANON_27.months_gestation = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='months gestation', tag='months_gestation')
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_enumeration)
_module_typeBindings.STD_ANON_27 = STD_ANON_27

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1283, 8)
    _Documentation = None
STD_ANON_28._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_28, enum_prefix=None)
STD_ANON_28.minimum = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='minimum', tag='minimum')
STD_ANON_28.maximum = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='maximum', tag='maximum')
STD_ANON_28.single = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='single', tag='single')
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_enumeration)
_module_typeBindings.STD_ANON_28 = STD_ANON_28

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1297, 4)
    _Documentation = None
STD_ANON_29._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_29, enum_prefix=None)
STD_ANON_29.yes = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='yes', tag='yes')
STD_ANON_29.no = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='no', tag='no')
STD_ANON_29.not_provided = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='not provided', tag='not_provided')
STD_ANON_29.unknown = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON_29.not_applicable = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='not applicable', tag='not_applicable')
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_enumeration)
_module_typeBindings.STD_ANON_29 = STD_ANON_29

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1337, 4)
    _Documentation = None
STD_ANON_30._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_30, enum_prefix=None)
STD_ANON_30.male = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='male', tag='male')
STD_ANON_30.female = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='female', tag='female')
STD_ANON_30.mixed = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='mixed', tag='mixed')
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_enumeration)
_module_typeBindings.STD_ANON_30 = STD_ANON_30

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1352, 4)
    _Documentation = None
STD_ANON_31._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_31, enum_prefix=None)
STD_ANON_31.submitter_generated = STD_ANON_31._CF_enumeration.addEnumeration(unicode_value='submitter-generated', tag='submitter_generated')
STD_ANON_31.data_mining = STD_ANON_31._CF_enumeration.addEnumeration(unicode_value='data mining', tag='data_mining')
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_enumeration)
_module_typeBindings.STD_ANON_31 = STD_ANON_31

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1420, 4)
    _Documentation = None
STD_ANON_32._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_32, enum_prefix=None)
STD_ANON_32.cis = STD_ANON_32._CF_enumeration.addEnumeration(unicode_value='cis', tag='cis')
STD_ANON_32.trans = STD_ANON_32._CF_enumeration.addEnumeration(unicode_value='trans', tag='trans')
STD_ANON_32.unknown = STD_ANON_32._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_enumeration)
_module_typeBindings.STD_ANON_32 = STD_ANON_32

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1450, 3)
    _Documentation = None
STD_ANON_33._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_33, enum_prefix=None)
STD_ANON_33.Indication = STD_ANON_33._CF_enumeration.addEnumeration(unicode_value='Indication', tag='Indication')
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_enumeration)
_module_typeBindings.STD_ANON_33 = STD_ANON_33

# Atomic simple type: ReviewStatusType
class ReviewStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The values of review status are used to build the 'star ratings' 
			displayed on the ClinVar public site.  
			0 stars:  a conflict or not classified by submitter
			1 star: classified by single submitter
			2 stars: classified by multiple submitters
			3 stars: reviewed by expert panel
			4 stars: reviewed by professional society"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReviewStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1459, 1)
    _Documentation = "The values of review status are used to build the 'star ratings' \n\t\t\tdisplayed on the ClinVar public site.  \n\t\t\t0 stars:  a conflict or not classified by submitter\n\t\t\t1 star: classified by single submitter\n\t\t\t2 stars: classified by multiple submitters\n\t\t\t3 stars: reviewed by expert panel\n\t\t\t4 stars: reviewed by professional society"
ReviewStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReviewStatusType, enum_prefix=None)
ReviewStatusType.no_assertion_provided = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='no assertion provided', tag='no_assertion_provided')
ReviewStatusType.no_assertion_criteria_provided = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='no assertion criteria provided', tag='no_assertion_criteria_provided')
ReviewStatusType.criteria_provided_single_submitter = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='criteria provided, single submitter', tag='criteria_provided_single_submitter')
ReviewStatusType.criteria_provided_multiple_submitters_no_conflicts = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='criteria provided, multiple submitters, no conflicts', tag='criteria_provided_multiple_submitters_no_conflicts')
ReviewStatusType.criteria_provided_conflicting_interpretations = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='criteria provided, conflicting interpretations', tag='criteria_provided_conflicting_interpretations')
ReviewStatusType.reviewed_by_expert_panel = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='reviewed by expert panel', tag='reviewed_by_expert_panel')
ReviewStatusType.practice_guideline = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='practice guideline', tag='practice_guideline')
ReviewStatusType.classified_by_single_submitter = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='classified by single submitter', tag='classified_by_single_submitter')
ReviewStatusType.reviewed_by_professional_society = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='reviewed by professional society', tag='reviewed_by_professional_society')
ReviewStatusType.not_classified_by_submitter = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='not classified by submitter', tag='not_classified_by_submitter')
ReviewStatusType.classified_by_multiple_submitters = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value='classified by multiple submitters', tag='classified_by_multiple_submitters')
ReviewStatusType._InitializeFacetMap(ReviewStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReviewStatusType', ReviewStatusType)
_module_typeBindings.ReviewStatusType = ReviewStatusType

# Atomic simple type: AssertionTypeAttr
class AssertionTypeAttr (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssertionTypeAttr')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1484, 1)
    _Documentation = None
AssertionTypeAttr._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssertionTypeAttr, enum_prefix=None)
AssertionTypeAttr.variation_to_disease = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value='variation to disease', tag='variation_to_disease')
AssertionTypeAttr.variation_in_modifier_gene_to_disease = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value='variation in modifier gene to disease', tag='variation_in_modifier_gene_to_disease')
AssertionTypeAttr.confers_sensitivity = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value='confers sensitivity', tag='confers_sensitivity')
AssertionTypeAttr.confers_resistance = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value='confers resistance', tag='confers_resistance')
AssertionTypeAttr.variant_to_named_protein = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value='variant to named protein', tag='variant_to_named_protein')
AssertionTypeAttr._InitializeFacetMap(AssertionTypeAttr._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AssertionTypeAttr', AssertionTypeAttr)
_module_typeBindings.AssertionTypeAttr = AssertionTypeAttr

# Atomic simple type: CommentTypeList
class CommentTypeList (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommentTypeList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1494, 1)
    _Documentation = None
CommentTypeList._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CommentTypeList, enum_prefix=None)
CommentTypeList.public = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='public', tag='public')
CommentTypeList.ConvertedByNCBI = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='ConvertedByNCBI', tag='ConvertedByNCBI')
CommentTypeList.MissingFromAssembly = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='MissingFromAssembly', tag='MissingFromAssembly')
CommentTypeList.GenomicLocationNotEstablished = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='GenomicLocationNotEstablished', tag='GenomicLocationNotEstablished')
CommentTypeList.LocationOnGenomeAndProductNotAligned = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='LocationOnGenomeAndProductNotAligned', tag='LocationOnGenomeAndProductNotAligned')
CommentTypeList.DeletionComment = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='DeletionComment', tag='DeletionComment')
CommentTypeList.AssemblySpecificAlleleDefinition = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='AssemblySpecificAlleleDefinition', tag='AssemblySpecificAlleleDefinition')
CommentTypeList.AlignmentGapMakesAppearInconsistent = CommentTypeList._CF_enumeration.addEnumeration(unicode_value='AlignmentGapMakesAppearInconsistent', tag='AlignmentGapMakesAppearInconsistent')
CommentTypeList._InitializeFacetMap(CommentTypeList._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CommentTypeList', CommentTypeList)
_module_typeBindings.CommentTypeList = CommentTypeList

# Atomic simple type: SeverityType
class SeverityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SeverityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1507, 1)
    _Documentation = None
SeverityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SeverityType, enum_prefix=None)
SeverityType.mild = SeverityType._CF_enumeration.addEnumeration(unicode_value='mild', tag='mild')
SeverityType.moderate = SeverityType._CF_enumeration.addEnumeration(unicode_value='moderate', tag='moderate')
SeverityType.severe = SeverityType._CF_enumeration.addEnumeration(unicode_value='severe', tag='severe')
SeverityType._InitializeFacetMap(SeverityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SeverityType', SeverityType)
_module_typeBindings.SeverityType = SeverityType

# Atomic simple type: AssertionTypeAttrSCVonly
class AssertionTypeAttrSCVonly (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssertionTypeAttrSCVonly')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1515, 1)
    _Documentation = None
AssertionTypeAttrSCVonly._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssertionTypeAttrSCVonly, enum_prefix=None)
AssertionTypeAttrSCVonly.variation_to_included_disease = AssertionTypeAttrSCVonly._CF_enumeration.addEnumeration(unicode_value='variation to included disease', tag='variation_to_included_disease')
AssertionTypeAttrSCVonly._InitializeFacetMap(AssertionTypeAttrSCVonly._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AssertionTypeAttrSCVonly', AssertionTypeAttrSCVonly)
_module_typeBindings.AssertionTypeAttrSCVonly = AssertionTypeAttrSCVonly

# Atomic simple type: ZygosityType
class ZygosityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ZygosityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1539, 1)
    _Documentation = None
ZygosityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ZygosityType, enum_prefix=None)
ZygosityType.Homozygote = ZygosityType._CF_enumeration.addEnumeration(unicode_value='Homozygote', tag='Homozygote')
ZygosityType.SingleHeterozygote = ZygosityType._CF_enumeration.addEnumeration(unicode_value='SingleHeterozygote', tag='SingleHeterozygote')
ZygosityType.CompoundHeterozygote = ZygosityType._CF_enumeration.addEnumeration(unicode_value='CompoundHeterozygote', tag='CompoundHeterozygote')
ZygosityType.Hemizygote = ZygosityType._CF_enumeration.addEnumeration(unicode_value='Hemizygote', tag='Hemizygote')
ZygosityType.not_provided = ZygosityType._CF_enumeration.addEnumeration(unicode_value='not provided', tag='not_provided')
ZygosityType._InitializeFacetMap(ZygosityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ZygosityType', ZygosityType)
_module_typeBindings.ZygosityType = ZygosityType

# Atomic simple type: Methodtypelist
class Methodtypelist (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Methodtypelist')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1548, 1)
    _Documentation = None
Methodtypelist._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Methodtypelist, enum_prefix=None)
Methodtypelist.literature_only = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='literature only', tag='literature_only')
Methodtypelist.reference_population = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='reference population', tag='reference_population')
Methodtypelist.case_control = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='case-control', tag='case_control')
Methodtypelist.clinical_testing = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='clinical testing', tag='clinical_testing')
Methodtypelist.in_vitro = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='in vitro', tag='in_vitro')
Methodtypelist.in_vivo = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='in vivo', tag='in_vivo')
Methodtypelist.research = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='research', tag='research')
Methodtypelist.curation = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='curation', tag='curation')
Methodtypelist.not_provided = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='not provided', tag='not_provided')
Methodtypelist.provider_interpretation = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='provider interpretation', tag='provider_interpretation')
Methodtypelist.phenotyping_only = Methodtypelist._CF_enumeration.addEnumeration(unicode_value='phenotyping only', tag='phenotyping_only')
Methodtypelist._InitializeFacetMap(Methodtypelist._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Methodtypelist', Methodtypelist)
_module_typeBindings.Methodtypelist = Methodtypelist

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1588, 3)
    _Documentation = None
STD_ANON_34._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_34, enum_prefix=None)
STD_ANON_34.current = STD_ANON_34._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
STD_ANON_34.previous = STD_ANON_34._CF_enumeration.addEnumeration(unicode_value='previous', tag='previous')
STD_ANON_34._InitializeFacetMap(STD_ANON_34._CF_enumeration)
_module_typeBindings.STD_ANON_34 = STD_ANON_34

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1608, 3)
    _Documentation = None
STD_ANON_35._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_35._CF_pattern.addPattern(pattern='VCV[0-9]{9}')
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_pattern)
_module_typeBindings.STD_ANON_35 = STD_ANON_35

# Union simple type: AssertionTypeAttrSCV
# superclasses pyxb.binding.datatypes.anySimpleType
class AssertionTypeAttrSCV (pyxb.binding.basis.STD_union):

    """Simple type that is a union of AssertionTypeAttr, AssertionTypeAttrSCVonly."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssertionTypeAttrSCV')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1520, 1)
    _Documentation = None

    _MemberTypes = ( AssertionTypeAttr, AssertionTypeAttrSCVonly, )
AssertionTypeAttrSCV._CF_pattern = pyxb.binding.facets.CF_pattern()
AssertionTypeAttrSCV._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssertionTypeAttrSCV)
AssertionTypeAttrSCV.variation_to_disease = 'variation to disease'# originally AssertionTypeAttr.variation_to_disease
AssertionTypeAttrSCV.variation_in_modifier_gene_to_disease = 'variation in modifier gene to disease'# originally AssertionTypeAttr.variation_in_modifier_gene_to_disease
AssertionTypeAttrSCV.confers_sensitivity = 'confers sensitivity'# originally AssertionTypeAttr.confers_sensitivity
AssertionTypeAttrSCV.confers_resistance = 'confers resistance'# originally AssertionTypeAttr.confers_resistance
AssertionTypeAttrSCV.variant_to_named_protein = 'variant to named protein'# originally AssertionTypeAttr.variant_to_named_protein
AssertionTypeAttrSCV.variation_to_included_disease = 'variation to included disease'# originally AssertionTypeAttrSCVonly.variation_to_included_disease
AssertionTypeAttrSCV._InitializeFacetMap(AssertionTypeAttrSCV._CF_pattern,
   AssertionTypeAttrSCV._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AssertionTypeAttrSCV', AssertionTypeAttrSCV)
_module_typeBindings.AssertionTypeAttrSCV = AssertionTypeAttrSCV

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 36, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 38, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 101, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 102, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 103, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 126, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON__Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 128, 9), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON__Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 147, 9), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type CitationType with content type ELEMENT_ONLY
class CitationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CitationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CitationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 231, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_CitationType_ID', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 233, 3), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__AbsentNamespace0_CitationType_URL', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 247, 3), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element CitationText uses Python identifier CitationText
    __CitationText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CitationText'), 'CitationText', '__AbsentNamespace0_CitationType_CitationText', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 248, 3), )

    
    CitationText = property(__CitationText.value, __CitationText.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CitationType_Type', pyxb.binding.datatypes.string)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 250, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 250, 2)
    
    Type = property(__Type.value, __Type.set, None, "This maintained distinct from publication types in PubMed and established \n\t\t\t\t\tby GTR curators. The default is 'general'.")

    
    # Attribute Abbrev uses Python identifier Abbrev
    __Abbrev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Abbrev'), 'Abbrev', '__AbsentNamespace0_CitationType_Abbrev', pyxb.binding.datatypes.string)
    __Abbrev._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 256, 2)
    __Abbrev._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 256, 2)
    
    Abbrev = property(__Abbrev.value, __Abbrev.set, None, 'Corresponds to the abbreviation reported by GTR.')

    _ElementMap.update({
        __ID.name() : __ID,
        __URL.name() : __URL,
        __CitationText.name() : __CitationText
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Abbrev.name() : __Abbrev
    })
_module_typeBindings.CitationType = CitationType
Namespace.addCategoryObject('typeBinding', 'CitationType', CitationType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 234, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Source uses Python identifier Source
    __Source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__AbsentNamespace0_CTD_ANON_2_Source', pyxb.binding.datatypes.string, required=True)
    __Source._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 237, 7)
    __Source._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 237, 7)
    
    Source = property(__Source.value, __Source.set, None, 'If there is an identifier, what database\n\t\t\t\t\t\t\t\t\tprovides it.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Source.name() : __Source
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type PublicSetType with content type ELEMENT_ONLY
class PublicSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type PublicSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PublicSetType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 303, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarAssertion uses Python identifier ClinVarAssertion
    __ClinVarAssertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClinVarAssertion'), 'ClinVarAssertion', '__AbsentNamespace0_PublicSetType_ClinVarAssertion', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 10, 1), )

    
    ClinVarAssertion = property(__ClinVarAssertion.value, __ClinVarAssertion.set, None, None)

    
    # Element ReferenceClinVarAssertion uses Python identifier ReferenceClinVarAssertion
    __ReferenceClinVarAssertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceClinVarAssertion'), 'ReferenceClinVarAssertion', '__AbsentNamespace0_PublicSetType_ReferenceClinVarAssertion', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 16, 1), )

    
    ReferenceClinVarAssertion = property(__ReferenceClinVarAssertion.value, __ReferenceClinVarAssertion.set, None, None)

    
    # Element RecordStatus uses Python identifier RecordStatus
    __RecordStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RecordStatus'), 'RecordStatus', '__AbsentNamespace0_PublicSetType_RecordStatus', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 305, 3), )

    
    RecordStatus = property(__RecordStatus.value, __RecordStatus.set, None, None)

    
    # Element ReplacedBy uses Python identifier ReplacedBy
    __ReplacedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReplacedBy'), 'ReplacedBy', '__AbsentNamespace0_PublicSetType_ReplacedBy', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 315, 3), )

    
    ReplacedBy = property(__ReplacedBy.value, __ReplacedBy.set, None, None)

    
    # Element Replaces uses Python identifier Replaces
    __Replaces = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Replaces'), 'Replaces', '__AbsentNamespace0_PublicSetType_Replaces', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 316, 3), )

    
    Replaces = property(__Replaces.value, __Replaces.set, None, None)

    
    # Element Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Title'), 'Title', '__AbsentNamespace0_PublicSetType_Title', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 317, 3), )

    
    Title = property(__Title.value, __Title.set, None, 'The title is contructed from the concatenation of the description of the variation and the phenotype.\n\t\t\t\t\tIn the database it is extracted from the title of RCV accession')

    
    # Element DeletedSCVList uses Python identifier DeletedSCVList
    __DeletedSCVList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DeletedSCVList'), 'DeletedSCVList', '__AbsentNamespace0_PublicSetType_DeletedSCVList', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 331, 3), )

    
    DeletedSCVList = property(__DeletedSCVList.value, __DeletedSCVList.set, None, None)

    
    # Attribute DateLastUpdated uses Python identifier DateLastUpdated
    __DateLastUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateLastUpdated'), 'DateLastUpdated', '__AbsentNamespace0_PublicSetType_DateLastUpdated', pyxb.binding.datatypes.anySimpleType)
    __DateLastUpdated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 341, 2)
    __DateLastUpdated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 341, 2)
    
    DateLastUpdated = property(__DateLastUpdated.value, __DateLastUpdated.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_PublicSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __ClinVarAssertion.name() : __ClinVarAssertion,
        __ReferenceClinVarAssertion.name() : __ReferenceClinVarAssertion,
        __RecordStatus.name() : __RecordStatus,
        __ReplacedBy.name() : __ReplacedBy,
        __Replaces.name() : __Replaces,
        __Title.name() : __Title,
        __DeletedSCVList.name() : __DeletedSCVList
    })
    _AttributeMap.update({
        __DateLastUpdated.name() : __DateLastUpdated,
        __ID.name() : __ID
    })
_module_typeBindings.PublicSetType = PublicSetType
Namespace.addCategoryObject('typeBinding', 'PublicSetType', PublicSetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 332, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SCV uses Python identifier SCV
    __SCV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SCV'), 'SCV', '__AbsentNamespace0_CTD_ANON_3_SCV', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 334, 6), )

    
    SCV = property(__SCV.value, __SCV.set, None, None)

    _ElementMap.update({
        __SCV.name() : __SCV
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type typeDeletedSCV with content type ELEMENT_ONLY
class typeDeletedSCV (pyxb.binding.basis.complexTypeDefinition):
    """A structure to support reporting of an accession, its version, the date is was deleted and description of deletion"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeDeletedSCV')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 343, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Accession uses Python identifier Accession
    __Accession = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Accession'), 'Accession', '__AbsentNamespace0_typeDeletedSCV_Accession', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 348, 3), )

    
    Accession = property(__Accession.value, __Accession.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_typeDeletedSCV_Description', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 358, 3), )

    
    Description = property(__Description.value, __Description.set, None, None)

    _ElementMap.update({
        __Accession.name() : __Accession,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.typeDeletedSCV = typeDeletedSCV
Namespace.addCategoryObject('typeBinding', 'typeDeletedSCV', typeDeletedSCV)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 349, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_4_Version', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 352, 7)
    __Version._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 352, 7)
    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Attribute DateDeleted uses Python identifier DateDeleted
    __DateDeleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateDeleted'), 'DateDeleted', '__AbsentNamespace0_CTD_ANON_4_DateDeleted', pyxb.binding.datatypes.date, required=True)
    __DateDeleted._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 353, 7)
    __DateDeleted._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 353, 7)
    
    DateDeleted = property(__DateDeleted.value, __DateDeleted.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Version.name() : __Version,
        __DateDeleted.name() : __DateDeleted
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type ReleaseType with content type ELEMENT_ONLY
class ReleaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ReleaseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 362, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarSet uses Python identifier ClinVarSet
    __ClinVarSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClinVarSet'), 'ClinVarSet', '__AbsentNamespace0_ReleaseType_ClinVarSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 3, 1), )

    
    ClinVarSet = property(__ClinVarSet.value, __ClinVarSet.set, None, 'The ClinVarSet is used to group the aggregate record (RCV accession)\n\t\t\twith the submissions underlying it (SCV accessions) \n\t\t\t')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_ReleaseType_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 370, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 370, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Dated uses Python identifier Dated
    __Dated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Dated'), 'Dated', '__AbsentNamespace0_ReleaseType_Dated', pyxb.binding.datatypes.date, required=True)
    __Dated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 371, 2)
    __Dated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 371, 2)
    
    Dated = property(__Dated.value, __Dated.set, None, None)

    _ElementMap.update({
        __ClinVarSet.name() : __ClinVarSet
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Dated.name() : __Dated
    })
_module_typeBindings.ReleaseType = ReleaseType
Namespace.addCategoryObject('typeBinding', 'ReleaseType', ReleaseType)


# Complex type MeasureTraitType with content type ELEMENT_ONLY
class MeasureTraitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MeasureTraitType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureTraitType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 373, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarSubmissionID uses Python identifier ClinVarSubmissionID
    __ClinVarSubmissionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ClinVarSubmissionID'), 'ClinVarSubmissionID', '__AbsentNamespace0_MeasureTraitType_ClinVarSubmissionID', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 375, 3), )

    
    ClinVarSubmissionID = property(__ClinVarSubmissionID.value, __ClinVarSubmissionID.set, None, None)

    
    # Element ClinVarAccession uses Python identifier ClinVarAccession
    __ClinVarAccession = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ClinVarAccession'), 'ClinVarAccession', '__AbsentNamespace0_MeasureTraitType_ClinVarAccession', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 393, 3), )

    
    ClinVarAccession = property(__ClinVarAccession.value, __ClinVarAccession.set, None, None)

    
    # Element AdditionalSubmitters uses Python identifier AdditionalSubmitters
    __AdditionalSubmitters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AdditionalSubmitters'), 'AdditionalSubmitters', '__AbsentNamespace0_MeasureTraitType_AdditionalSubmitters', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 415, 3), )

    
    AdditionalSubmitters = property(__AdditionalSubmitters.value, __AdditionalSubmitters.set, None, 'Optional element used only if there are multiple submitters. When there are multiple, each is listed \n\t\t\t\t\t\tin this element. \n\t\t\t\t\t')

    
    # Element RecordStatus uses Python identifier RecordStatus
    __RecordStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RecordStatus'), 'RecordStatus', '__AbsentNamespace0_MeasureTraitType_RecordStatus', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 427, 3), )

    
    RecordStatus = property(__RecordStatus.value, __RecordStatus.set, None, None)

    
    # Element ClinicalSignificance uses Python identifier ClinicalSignificance
    __ClinicalSignificance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance'), 'ClinicalSignificance', '__AbsentNamespace0_MeasureTraitType_ClinicalSignificance', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 436, 3), )

    
    ClinicalSignificance = property(__ClinicalSignificance.value, __ClinicalSignificance.set, None, None)

    
    # Element CustomAssertionScore uses Python identifier CustomAssertionScore
    __CustomAssertionScore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CustomAssertionScore'), 'CustomAssertionScore', '__AbsentNamespace0_MeasureTraitType_CustomAssertionScore', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 437, 3), )

    
    CustomAssertionScore = property(__CustomAssertionScore.value, __CustomAssertionScore.set, None, '\n\t\t\t\t\t\tUsed to represent the scoring matrix a submitter may use to \n\t\t\t\t\t\tevaluate clinical signficance. \n\t\t\t\t\t')

    
    # Element Assertion uses Python identifier Assertion
    __Assertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assertion'), 'Assertion', '__AbsentNamespace0_MeasureTraitType_Assertion', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 453, 3), )

    
    Assertion = property(__Assertion.value, __Assertion.set, None, None)

    
    # Element ExternalID uses Python identifier ExternalID
    __ExternalID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ExternalID'), 'ExternalID', '__AbsentNamespace0_MeasureTraitType_ExternalID', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 454, 3), )

    
    ExternalID = property(__ExternalID.value, __ExternalID.set, None, 'XrefType is used to identify data source(s) and their identifiers.\n\t\t\t\t\tOptional because not all sources have an ID specific to the assertion. \n\t\t\t\t\t')

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_MeasureTraitType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 461, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, 'AttributeSet is a package to represent a unit of information,\n\t\t\t\t\t\tthe source(s) of that unit, identifiers representing that unit, and comments.\n\t\t\t\t ')

    
    # Element ObservedIn uses Python identifier ObservedIn
    __ObservedIn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ObservedIn'), 'ObservedIn', '__AbsentNamespace0_MeasureTraitType_ObservedIn', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 497, 3), )

    
    ObservedIn = property(__ObservedIn.value, __ObservedIn.set, None, None)

    
    # Element MeasureSet uses Python identifier MeasureSet
    __MeasureSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MeasureSet'), 'MeasureSet', '__AbsentNamespace0_MeasureTraitType_MeasureSet', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 499, 5), )

    
    MeasureSet = property(__MeasureSet.value, __MeasureSet.set, None, None)

    
    # Element GenotypeSet uses Python identifier GenotypeSet
    __GenotypeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GenotypeSet'), 'GenotypeSet', '__AbsentNamespace0_MeasureTraitType_GenotypeSet', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 500, 4), )

    
    GenotypeSet = property(__GenotypeSet.value, __GenotypeSet.set, None, None)

    
    # Element TraitSet uses Python identifier TraitSet
    __TraitSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TraitSet'), 'TraitSet', '__AbsentNamespace0_MeasureTraitType_TraitSet', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 502, 3), )

    
    TraitSet = property(__TraitSet.value, __TraitSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_MeasureTraitType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 503, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element StudyName uses Python identifier StudyName
    __StudyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StudyName'), 'StudyName', '__AbsentNamespace0_MeasureTraitType_StudyName', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 504, 3), )

    
    StudyName = property(__StudyName.value, __StudyName.set, None, None)

    
    # Element StudyDescription uses Python identifier StudyDescription
    __StudyDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StudyDescription'), 'StudyDescription', '__AbsentNamespace0_MeasureTraitType_StudyDescription', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 505, 3), )

    
    StudyDescription = property(__StudyDescription.value, __StudyDescription.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_MeasureTraitType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 506, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateCreated uses Python identifier DateCreated
    __DateCreated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateCreated'), 'DateCreated', '__AbsentNamespace0_MeasureTraitType_DateCreated', pyxb.binding.datatypes.date)
    __DateCreated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 508, 2)
    __DateCreated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 508, 2)
    
    DateCreated = property(__DateCreated.value, __DateCreated.set, None, None)

    
    # Attribute DateLastUpdated uses Python identifier DateLastUpdated
    __DateLastUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateLastUpdated'), 'DateLastUpdated', '__AbsentNamespace0_MeasureTraitType_DateLastUpdated', pyxb.binding.datatypes.date)
    __DateLastUpdated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 509, 2)
    __DateLastUpdated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 509, 2)
    
    DateLastUpdated = property(__DateLastUpdated.value, __DateLastUpdated.set, None, 'A modification date is independent of a version change. \n\t\t\t\tContent generated by NCBI may change without representing a change in the version.\n\t\t\t\t')

    
    # Attribute SubmissionDate uses Python identifier SubmissionDate
    __SubmissionDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SubmissionDate'), 'SubmissionDate', '__AbsentNamespace0_MeasureTraitType_SubmissionDate', pyxb.binding.datatypes.date)
    __SubmissionDate._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 516, 2)
    __SubmissionDate._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 516, 2)
    
    SubmissionDate = property(__SubmissionDate.value, __SubmissionDate.set, None, None)

    
    # Attribute SubmissionName uses Python identifier SubmissionName
    __SubmissionName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SubmissionName'), 'SubmissionName', '__AbsentNamespace0_MeasureTraitType_SubmissionName', pyxb.binding.datatypes.string)
    __SubmissionName._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 517, 2)
    __SubmissionName._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 517, 2)
    
    SubmissionName = property(__SubmissionName.value, __SubmissionName.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_MeasureTraitType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __ClinVarSubmissionID.name() : __ClinVarSubmissionID,
        __ClinVarAccession.name() : __ClinVarAccession,
        __AdditionalSubmitters.name() : __AdditionalSubmitters,
        __RecordStatus.name() : __RecordStatus,
        __ClinicalSignificance.name() : __ClinicalSignificance,
        __CustomAssertionScore.name() : __CustomAssertionScore,
        __Assertion.name() : __Assertion,
        __ExternalID.name() : __ExternalID,
        __AttributeSet.name() : __AttributeSet,
        __ObservedIn.name() : __ObservedIn,
        __MeasureSet.name() : __MeasureSet,
        __GenotypeSet.name() : __GenotypeSet,
        __TraitSet.name() : __TraitSet,
        __Citation.name() : __Citation,
        __StudyName.name() : __StudyName,
        __StudyDescription.name() : __StudyDescription,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateCreated.name() : __DateCreated,
        __DateLastUpdated.name() : __DateLastUpdated,
        __SubmissionDate.name() : __SubmissionDate,
        __SubmissionName.name() : __SubmissionName,
        __ID.name() : __ID
    })
_module_typeBindings.MeasureTraitType = MeasureTraitType
Namespace.addCategoryObject('typeBinding', 'MeasureTraitType', MeasureTraitType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 376, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute submitter uses Python identifier submitter
    __submitter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'submitter'), 'submitter', '__AbsentNamespace0_CTD_ANON_5_submitter', pyxb.binding.datatypes.string)
    __submitter._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 377, 5)
    __submitter._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 377, 5)
    
    submitter = property(__submitter.value, __submitter.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_CTD_ANON_5_title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 378, 5)
    __title._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 378, 5)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute localKey uses Python identifier localKey
    __localKey = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'localKey'), 'localKey', '__AbsentNamespace0_CTD_ANON_5_localKey', pyxb.binding.datatypes.string, required=True)
    __localKey._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 379, 5)
    __localKey._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 379, 5)
    
    localKey = property(__localKey.value, __localKey.set, None, 'Of primary use to submitters, to facilitate\n\t\t\t\t\t\t\tidentification of records corresponding to their submissions.\n\t\t\t\t\t\t\tIf not provided by a submitter, NCBI generates. If provided by submitter, \n\t\t\t\t\t\t\tthat is represented in localKeyIsSubmitted.\n\t\t\t\t\t\t\t')

    
    # Attribute submittedAssembly uses Python identifier submittedAssembly
    __submittedAssembly = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'submittedAssembly'), 'submittedAssembly', '__AbsentNamespace0_CTD_ANON_5_submittedAssembly', pyxb.binding.datatypes.string)
    __submittedAssembly._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 388, 5)
    __submittedAssembly._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 388, 5)
    
    submittedAssembly = property(__submittedAssembly.value, __submittedAssembly.set, None, None)

    
    # Attribute submitterDate uses Python identifier submitterDate
    __submitterDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'submitterDate'), 'submitterDate', '__AbsentNamespace0_CTD_ANON_5_submitterDate', pyxb.binding.datatypes.date)
    __submitterDate._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 389, 5)
    __submitterDate._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 389, 5)
    
    submitterDate = property(__submitterDate.value, __submitterDate.set, None, None)

    
    # Attribute localKeyIsSubmitted uses Python identifier localKeyIsSubmitted
    __localKeyIsSubmitted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'localKeyIsSubmitted'), 'localKeyIsSubmitted', '__AbsentNamespace0_CTD_ANON_5_localKeyIsSubmitted', pyxb.binding.datatypes.anySimpleType)
    __localKeyIsSubmitted._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 390, 5)
    __localKeyIsSubmitted._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 390, 5)
    
    localKeyIsSubmitted = property(__localKeyIsSubmitted.value, __localKeyIsSubmitted.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __submitter.name() : __submitter,
        __title.name() : __title,
        __localKey.name() : __localKey,
        __submittedAssembly.name() : __submittedAssembly,
        __submitterDate.name() : __submitterDate,
        __localKeyIsSubmitted.name() : __localKeyIsSubmitted
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Optional element used only if there are multiple submitters. When there are multiple, each is listed 
						in this element. 
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 421, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SubmitterDescription uses Python identifier SubmitterDescription
    __SubmitterDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SubmitterDescription'), 'SubmitterDescription', '__AbsentNamespace0_CTD_ANON_6_SubmitterDescription', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 423, 5), )

    
    SubmitterDescription = property(__SubmitterDescription.value, __SubmitterDescription.set, None, None)

    _ElementMap.update({
        __SubmitterDescription.name() : __SubmitterDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """
						Used to represent the scoring matrix a submitter may use to 
						evaluate clinical signficance. 
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 444, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_7_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 446, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_7_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 447, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_7_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 449, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 449, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__AbsentNamespace0_CTD_ANON_7_Value', pyxb.binding.datatypes.string)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 450, 5)
    __Value._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 450, 5)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Citation.name() : __Citation,
        __XRef.name() : __XRef
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Value.name() : __Value
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """AttributeSet is a package to represent a unit of information,
						the source(s) of that unit, identifiers representing that unit, and comments.
				 """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 467, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_8_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 469, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_8_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 491, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_8_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 492, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_8_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 493, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type ReferenceAssertionType with content type ELEMENT_ONLY
class ReferenceAssertionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ReferenceAssertionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceAssertionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 520, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarAccession uses Python identifier ClinVarAccession
    __ClinVarAccession = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ClinVarAccession'), 'ClinVarAccession', '__AbsentNamespace0_ReferenceAssertionType_ClinVarAccession', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 522, 3), )

    
    ClinVarAccession = property(__ClinVarAccession.value, __ClinVarAccession.set, None, None)

    
    # Element RecordStatus uses Python identifier RecordStatus
    __RecordStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RecordStatus'), 'RecordStatus', '__AbsentNamespace0_ReferenceAssertionType_RecordStatus', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 547, 3), )

    
    RecordStatus = property(__RecordStatus.value, __RecordStatus.set, None, None)

    
    # Element ClinicalSignificance uses Python identifier ClinicalSignificance
    __ClinicalSignificance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance'), 'ClinicalSignificance', '__AbsentNamespace0_ReferenceAssertionType_ClinicalSignificance', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 556, 3), )

    
    ClinicalSignificance = property(__ClinicalSignificance.value, __ClinicalSignificance.set, None, 'Either the value corresponding to the scoring system of the ACMG, or \n\t\t\t\t\ta value representing such concepts as drug response, risk factors, etc.')

    
    # Element Assertion uses Python identifier Assertion
    __Assertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assertion'), 'Assertion', '__AbsentNamespace0_ReferenceAssertionType_Assertion', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 562, 3), )

    
    Assertion = property(__Assertion.value, __Assertion.set, None, None)

    
    # Element ExternalID uses Python identifier ExternalID
    __ExternalID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ExternalID'), 'ExternalID', '__AbsentNamespace0_ReferenceAssertionType_ExternalID', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 563, 3), )

    
    ExternalID = property(__ExternalID.value, __ExternalID.set, None, 'Represents the public identifier a source may have for this record. \n\t\t\t\t\t')

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_ReferenceAssertionType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 569, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, 'Many concepts in the database are represented by what ClinVar terms an AttributeSet, \n\t\t\t\t\t\twhich is an open-ended structure providing the equivalent of a type of information, the value(s) for that data type, \n\t\t\t\t\t\tsubmitter(s), free text comment(s) describing that attribute, identifier(s) for that attribute, and \n\t\t\t\t\t\tcitation(s) related to that attribute.\n\t\t\t\t\t')

    
    # Element ObservedIn uses Python identifier ObservedIn
    __ObservedIn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ObservedIn'), 'ObservedIn', '__AbsentNamespace0_ReferenceAssertionType_ObservedIn', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 602, 3), )

    
    ObservedIn = property(__ObservedIn.value, __ObservedIn.set, None, None)

    
    # Element MeasureSet uses Python identifier MeasureSet
    __MeasureSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MeasureSet'), 'MeasureSet', '__AbsentNamespace0_ReferenceAssertionType_MeasureSet', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 604, 5), )

    
    MeasureSet = property(__MeasureSet.value, __MeasureSet.set, None, None)

    
    # Element GenotypeSet uses Python identifier GenotypeSet
    __GenotypeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GenotypeSet'), 'GenotypeSet', '__AbsentNamespace0_ReferenceAssertionType_GenotypeSet', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 605, 4), )

    
    GenotypeSet = property(__GenotypeSet.value, __GenotypeSet.set, None, None)

    
    # Element TraitSet uses Python identifier TraitSet
    __TraitSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TraitSet'), 'TraitSet', '__AbsentNamespace0_ReferenceAssertionType_TraitSet', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 607, 3), )

    
    TraitSet = property(__TraitSet.value, __TraitSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_ReferenceAssertionType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 608, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_ReferenceAssertionType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 609, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateCreated uses Python identifier DateCreated
    __DateCreated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateCreated'), 'DateCreated', '__AbsentNamespace0_ReferenceAssertionType_DateCreated', pyxb.binding.datatypes.date)
    __DateCreated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 611, 2)
    __DateCreated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 611, 2)
    
    DateCreated = property(__DateCreated.value, __DateCreated.set, None, None)

    
    # Attribute DateLastUpdated uses Python identifier DateLastUpdated
    __DateLastUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateLastUpdated'), 'DateLastUpdated', '__AbsentNamespace0_ReferenceAssertionType_DateLastUpdated', pyxb.binding.datatypes.date)
    __DateLastUpdated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 612, 2)
    __DateLastUpdated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 612, 2)
    
    DateLastUpdated = property(__DateLastUpdated.value, __DateLastUpdated.set, None, None)

    
    # Attribute SubmissionDate uses Python identifier SubmissionDate
    __SubmissionDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SubmissionDate'), 'SubmissionDate', '__AbsentNamespace0_ReferenceAssertionType_SubmissionDate', pyxb.binding.datatypes.date)
    __SubmissionDate._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 613, 2)
    __SubmissionDate._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 613, 2)
    
    SubmissionDate = property(__SubmissionDate.value, __SubmissionDate.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_ReferenceAssertionType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __ClinVarAccession.name() : __ClinVarAccession,
        __RecordStatus.name() : __RecordStatus,
        __ClinicalSignificance.name() : __ClinicalSignificance,
        __Assertion.name() : __Assertion,
        __ExternalID.name() : __ExternalID,
        __AttributeSet.name() : __AttributeSet,
        __ObservedIn.name() : __ObservedIn,
        __MeasureSet.name() : __MeasureSet,
        __GenotypeSet.name() : __GenotypeSet,
        __TraitSet.name() : __TraitSet,
        __Citation.name() : __Citation,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateCreated.name() : __DateCreated,
        __DateLastUpdated.name() : __DateLastUpdated,
        __SubmissionDate.name() : __SubmissionDate,
        __ID.name() : __ID
    })
_module_typeBindings.ReferenceAssertionType = ReferenceAssertionType
Namespace.addCategoryObject('typeBinding', 'ReferenceAssertionType', ReferenceAssertionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Many concepts in the database are represented by what ClinVar terms an AttributeSet, 
						which is an open-ended structure providing the equivalent of a type of information, the value(s) for that data type, 
						submitter(s), free text comment(s) describing that attribute, identifier(s) for that attribute, and 
						citation(s) related to that attribute.
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 577, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_9_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 579, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_9_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 596, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_9_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 597, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_9_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 598, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type MeasureSetAttributeSet with content type ELEMENT_ONLY
class MeasureSetAttributeSet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MeasureSetAttributeSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureSetAttributeSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 616, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_MeasureSetAttributeSet_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 618, 3), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_MeasureSetAttributeSet_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 656, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_MeasureSetAttributeSet_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 657, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_MeasureSetAttributeSet_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 658, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeasureSetAttributeSet = MeasureSetAttributeSet
Namespace.addCategoryObject('typeBinding', 'MeasureSetAttributeSet', MeasureSetAttributeSet)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 718, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_10_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 720, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_10_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 729, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_10_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 730, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_10_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 731, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, 'table_type = 38')

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 761, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_11_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 763, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_11_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 772, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_11_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 773, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_11_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 774, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 784, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_12_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 786, 9), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_12_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 795, 9), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_12_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 796, 9), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_12_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 797, 9), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 846, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_13_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 848, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_13_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 857, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_13_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 858, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_13_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 859, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, 'table_type = 38')

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 891, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_14_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 893, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_14_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 902, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_14_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 903, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_14_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 904, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 914, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_15_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 916, 9), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_15_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 925, 9), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_15_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 926, 9), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_15_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 927, 9), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type AttributeType with content type SIMPLE
class AttributeType (pyxb.binding.basis.complexTypeDefinition):
    """The attribute is a general element to represent a defined set of data
				qualified by an enumerated set of types. For each attribute element, the value will
				be a character string and is optional. Source shall be used to store identifiers for
				supplied data from source other than the submitter (e.g. SequenceOntology). The data
				submitted where Type="variation" shall be validated against sequence_alternation in
				Sequence Ontology http://www.sequenceontology.org/. This is to be a generic version
				of AttributeType and should be used with extension when it is used to specify Type
				and its enumerations. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 970, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute integerValue uses Python identifier integerValue
    __integerValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'integerValue'), 'integerValue', '__AbsentNamespace0_AttributeType_integerValue', pyxb.binding.datatypes.int)
    __integerValue._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 983, 4)
    __integerValue._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 983, 4)
    
    integerValue = property(__integerValue.value, __integerValue.set, None, None)

    
    # Attribute dateValue uses Python identifier dateValue
    __dateValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dateValue'), 'dateValue', '__AbsentNamespace0_AttributeType_dateValue', pyxb.binding.datatypes.date)
    __dateValue._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 984, 4)
    __dateValue._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 984, 4)
    
    dateValue = property(__dateValue.value, __dateValue.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __integerValue.name() : __integerValue,
        __dateValue.name() : __dateValue
    })
_module_typeBindings.AttributeType = AttributeType
Namespace.addCategoryObject('typeBinding', 'AttributeType', AttributeType)


# Complex type SetElementSetType with content type ELEMENT_ONLY
class SetElementSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SetElementSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SetElementSetType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 988, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ElementValue uses Python identifier ElementValue
    __ElementValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ElementValue'), 'ElementValue', '__AbsentNamespace0_SetElementSetType_ElementValue', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 990, 3), )

    
    ElementValue = property(__ElementValue.value, __ElementValue.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_SetElementSetType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 999, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_SetElementSetType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1000, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_SetElementSetType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1001, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __ElementValue.name() : __ElementValue,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SetElementSetType = SetElementSetType
Namespace.addCategoryObject('typeBinding', 'SetElementSetType', SetElementSetType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 991, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_16_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 994, 7)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 994, 7)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type SoftwareSet with content type EMPTY
class SoftwareSet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SoftwareSet with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1004, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_SoftwareSet_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1005, 2)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1005, 2)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_SoftwareSet_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1006, 2)
    __version._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1006, 2)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute purpose uses Python identifier purpose
    __purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'purpose'), 'purpose', '__AbsentNamespace0_SoftwareSet_purpose', pyxb.binding.datatypes.string)
    __purpose._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1007, 2)
    __purpose._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1007, 2)
    
    purpose = property(__purpose.value, __purpose.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __version.name() : __version,
        __purpose.name() : __purpose
    })
_module_typeBindings.SoftwareSet = SoftwareSet
Namespace.addCategoryObject('typeBinding', 'SoftwareSet', SoftwareSet)


# Complex type SubmitterType with content type SIMPLE
class SubmitterType (pyxb.binding.basis.complexTypeDefinition):
    """A structure to support reportng the name of a submitter, its org_id, and whether primary or not
			"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubmitterType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1010, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute SubmitterName uses Python identifier SubmitterName
    __SubmitterName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SubmitterName'), 'SubmitterName', '__AbsentNamespace0_SubmitterType_SubmitterName', pyxb.binding.datatypes.string)
    __SubmitterName._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1017, 4)
    __SubmitterName._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1017, 4)
    
    SubmitterName = property(__SubmitterName.value, __SubmitterName.set, None, None)

    
    # Attribute OrgAbbreviation uses Python identifier OrgAbbreviation
    __OrgAbbreviation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'OrgAbbreviation'), 'OrgAbbreviation', '__AbsentNamespace0_SubmitterType_OrgAbbreviation', pyxb.binding.datatypes.string)
    __OrgAbbreviation._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1018, 4)
    __OrgAbbreviation._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1018, 4)
    
    OrgAbbreviation = property(__OrgAbbreviation.value, __OrgAbbreviation.set, None, None)

    
    # Attribute OrgID uses Python identifier OrgID
    __OrgID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'OrgID'), 'OrgID', '__AbsentNamespace0_SubmitterType_OrgID', pyxb.binding.datatypes.int)
    __OrgID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1019, 4)
    __OrgID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1019, 4)
    
    OrgID = property(__OrgID.value, __OrgID.set, None, None)

    
    # Attribute primary uses Python identifier primary
    __primary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'primary'), 'primary', '__AbsentNamespace0_SubmitterType_primary', pyxb.binding.datatypes.string)
    __primary._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1020, 4)
    __primary._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1020, 4)
    
    primary = property(__primary.value, __primary.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_SubmitterType_category', pyxb.binding.datatypes.string)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1021, 4)
    __category._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1021, 4)
    
    category = property(__category.value, __category.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __SubmitterName.name() : __SubmitterName,
        __OrgAbbreviation.name() : __OrgAbbreviation,
        __OrgID.name() : __OrgID,
        __primary.name() : __primary,
        __category.name() : __category
    })
_module_typeBindings.SubmitterType = SubmitterType
Namespace.addCategoryObject('typeBinding', 'SubmitterType', SubmitterType)


# Complex type MethodType with content type ELEMENT_ONLY
class MethodType (pyxb.binding.basis.complexTypeDefinition):
    """ Details of a method used to generate variant calls or predict/report
                functional consequence. The name of the platform should represent a sequencer or an
                array, e.g. sequencing or array , e.g. capillary, 454, Helicos, Solexa, SOLiD. This
                structure should also be used if the method is 'Curation'. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MethodType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1026, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NamePlatform uses Python identifier NamePlatform
    __NamePlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NamePlatform'), 'NamePlatform', '__AbsentNamespace0_MethodType_NamePlatform', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1034, 3), )

    
    NamePlatform = property(__NamePlatform.value, __NamePlatform.set, None, None)

    
    # Element TypePlatform uses Python identifier TypePlatform
    __TypePlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TypePlatform'), 'TypePlatform', '__AbsentNamespace0_MethodType_TypePlatform', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1035, 3), )

    
    TypePlatform = property(__TypePlatform.value, __TypePlatform.set, None, None)

    
    # Element Purpose uses Python identifier Purpose
    __Purpose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Purpose'), 'Purpose', '__AbsentNamespace0_MethodType_Purpose', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1036, 3), )

    
    Purpose = property(__Purpose.value, __Purpose.set, None, None)

    
    # Element ResultType uses Python identifier ResultType
    __ResultType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ResultType'), 'ResultType', '__AbsentNamespace0_MethodType_ResultType', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1037, 3), )

    
    ResultType = property(__ResultType.value, __ResultType.set, None, None)

    
    # Element MinReported uses Python identifier MinReported
    __MinReported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MinReported'), 'MinReported', '__AbsentNamespace0_MethodType_MinReported', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1047, 3), )

    
    MinReported = property(__MinReported.value, __MinReported.set, None, None)

    
    # Element MaxReported uses Python identifier MaxReported
    __MaxReported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MaxReported'), 'MaxReported', '__AbsentNamespace0_MethodType_MaxReported', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1048, 3), )

    
    MaxReported = property(__MaxReported.value, __MaxReported.set, None, None)

    
    # Element ReferenceStandard uses Python identifier ReferenceStandard
    __ReferenceStandard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReferenceStandard'), 'ReferenceStandard', '__AbsentNamespace0_MethodType_ReferenceStandard', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1049, 3), )

    
    ReferenceStandard = property(__ReferenceStandard.value, __ReferenceStandard.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_MethodType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1050, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_MethodType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1051, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_MethodType_Description', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1052, 3), )

    
    Description = property(__Description.value, __Description.set, None, ' Free text to enrich the description of the method and to\n                        provide information not captured in specific fields. ')

    
    # Element Software uses Python identifier Software
    __Software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Software'), 'Software', '__AbsentNamespace0_MethodType_Software', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1058, 3), )

    
    Software = property(__Software.value, __Software.set, None, None)

    
    # Element SourceType uses Python identifier SourceType
    __SourceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SourceType'), 'SourceType', '__AbsentNamespace0_MethodType_SourceType', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1059, 3), )

    
    SourceType = property(__SourceType.value, __SourceType.set, None, None)

    
    # Element MethodType uses Python identifier MethodType
    __MethodType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MethodType'), 'MethodType', '__AbsentNamespace0_MethodType_MethodType', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1068, 3), )

    
    MethodType = property(__MethodType.value, __MethodType.set, None, None)

    
    # Element MethodAttribute uses Python identifier MethodAttribute
    __MethodAttribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MethodAttribute'), 'MethodAttribute', '__AbsentNamespace0_MethodType_MethodAttribute', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1069, 3), )

    
    MethodAttribute = property(__MethodAttribute.value, __MethodAttribute.set, None, None)

    
    # Element MethodResult uses Python identifier MethodResult
    __MethodResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MethodResult'), 'MethodResult', '__AbsentNamespace0_MethodType_MethodResult', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1097, 3), )

    
    MethodResult = property(__MethodResult.value, __MethodResult.set, None, ' MethodResult is used to represent results specific to a particular method.\n                        An example is a method used to validate the the variant call; the MethodResult would be pass/fail/inconclusive')

    _ElementMap.update({
        __NamePlatform.name() : __NamePlatform,
        __TypePlatform.name() : __TypePlatform,
        __Purpose.name() : __Purpose,
        __ResultType.name() : __ResultType,
        __MinReported.name() : __MinReported,
        __MaxReported.name() : __MaxReported,
        __ReferenceStandard.name() : __ReferenceStandard,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Description.name() : __Description,
        __Software.name() : __Software,
        __SourceType.name() : __SourceType,
        __MethodType.name() : __MethodType,
        __MethodAttribute.name() : __MethodAttribute,
        __MethodResult.name() : __MethodResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MethodType = MethodType
Namespace.addCategoryObject('typeBinding', 'MethodType', MethodType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1070, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_17_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1072, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_17_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1093, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type ObservationSet with content type ELEMENT_ONLY
class ObservationSet (pyxb.binding.basis.complexTypeDefinition):
    """Documents in what populations or samples an allele or genotype has been observed 
				relative to the described trait. Summary observations can be registered per 
				submitted assertion, grouped by common citation, study type, origin, ethnicity, tissue, cell line,
				and species data. Not all options are valid per study type, but these will not be validated in the xsd.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObservationSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1105, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Sample uses Python identifier Sample
    __Sample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Sample'), 'Sample', '__AbsentNamespace0_ObservationSet_Sample', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1114, 3), )

    
    Sample = property(__Sample.value, __Sample.set, None, None)

    
    # Element Method uses Python identifier Method
    __Method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Method'), 'Method', '__AbsentNamespace0_ObservationSet_Method', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1115, 3), )

    
    Method = property(__Method.value, __Method.set, None, None)

    
    # Element ObservedData uses Python identifier ObservedData
    __ObservedData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ObservedData'), 'ObservedData', '__AbsentNamespace0_ObservationSet_ObservedData', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1141, 3), )

    
    ObservedData = property(__ObservedData.value, __ObservedData.set, None, 'This is an AttributeSet, there will be 1 attribute supported by optional citations, xrefs and comment. \n\t\t\t\t\t\tThere must be at least one ObservedData Set, but can be any number.\n\t\t\t\t\t\tFor each ObservedData set the Attribute will be either decimal or string depending on type. \n\t\t\t\t\t\tThe value will be stored here, but decimals will be entered to the database as a string.\n\t\t\t\t\t')

    
    # Element Co-occurrenceSet uses Python identifier Co_occurrenceSet
    __Co_occurrenceSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Co-occurrenceSet'), 'Co_occurrenceSet', '__AbsentNamespace0_ObservationSet_Co_occurrenceSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1199, 3), )

    
    Co_occurrenceSet = property(__Co_occurrenceSet.value, __Co_occurrenceSet.set, None, None)

    
    # Element TraitSet uses Python identifier TraitSet
    __TraitSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TraitSet'), 'TraitSet', '__AbsentNamespace0_ObservationSet_TraitSet', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1200, 3), )

    
    TraitSet = property(__TraitSet.value, __TraitSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_ObservationSet_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1201, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_ObservationSet_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1202, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_ObservationSet_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1203, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Sample.name() : __Sample,
        __Method.name() : __Method,
        __ObservedData.name() : __ObservedData,
        __Co_occurrenceSet.name() : __Co_occurrenceSet,
        __TraitSet.name() : __TraitSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ObservationSet = ObservationSet
Namespace.addCategoryObject('typeBinding', 'ObservationSet', ObservationSet)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """This is an AttributeSet, there will be 1 attribute supported by optional citations, xrefs and comment. 
						There must be at least one ObservedData Set, but can be any number.
						For each ObservedData set the Attribute will be either decimal or string depending on type. 
						The value will be stored here, but decimals will be entered to the database as a string.
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1149, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_18_Attribute', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1151, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Severity uses Python identifier Severity
    __Severity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Severity'), 'Severity', '__AbsentNamespace0_CTD_ANON_18_Severity', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1191, 6), )

    
    Severity = property(__Severity.value, __Severity.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_18_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1192, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_18_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1193, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_18_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1194, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_18_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Severity.name() : __Severity,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type FamilyInfo with content type ELEMENT_ONLY
class FamilyInfo (pyxb.binding.basis.complexTypeDefinition):
    """Structure to describe attributes of any family data in an observation.
				If the details of the number of families and the de-identified pedigree id are not available,
				use FamilyHistory to describe what type of family data is available.  Can also be used to report 'Yes' or 'No' 
				if there are no more details.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FamilyInfo')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1206, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element FamilyHistory uses Python identifier FamilyHistory
    __FamilyHistory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FamilyHistory'), 'FamilyHistory', '__AbsentNamespace0_FamilyInfo_FamilyHistory', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1215, 3), )

    
    FamilyHistory = property(__FamilyHistory.value, __FamilyHistory.set, None, None)

    
    # Attribute NumFamilies uses Python identifier NumFamilies
    __NumFamilies = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumFamilies'), 'NumFamilies', '__AbsentNamespace0_FamilyInfo_NumFamilies', pyxb.binding.datatypes.int)
    __NumFamilies._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1217, 2)
    __NumFamilies._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1217, 2)
    
    NumFamilies = property(__NumFamilies.value, __NumFamilies.set, None, None)

    
    # Attribute NumFamiliesWithVariant uses Python identifier NumFamiliesWithVariant
    __NumFamiliesWithVariant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumFamiliesWithVariant'), 'NumFamiliesWithVariant', '__AbsentNamespace0_FamilyInfo_NumFamiliesWithVariant', pyxb.binding.datatypes.int)
    __NumFamiliesWithVariant._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1218, 2)
    __NumFamiliesWithVariant._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1218, 2)
    
    NumFamiliesWithVariant = property(__NumFamiliesWithVariant.value, __NumFamiliesWithVariant.set, None, None)

    
    # Attribute NumFamiliesWithSegregationObserved uses Python identifier NumFamiliesWithSegregationObserved
    __NumFamiliesWithSegregationObserved = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumFamiliesWithSegregationObserved'), 'NumFamiliesWithSegregationObserved', '__AbsentNamespace0_FamilyInfo_NumFamiliesWithSegregationObserved', pyxb.binding.datatypes.int)
    __NumFamiliesWithSegregationObserved._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1219, 2)
    __NumFamiliesWithSegregationObserved._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1219, 2)
    
    NumFamiliesWithSegregationObserved = property(__NumFamiliesWithSegregationObserved.value, __NumFamiliesWithSegregationObserved.set, None, None)

    
    # Attribute PedigreeID uses Python identifier PedigreeID
    __PedigreeID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PedigreeID'), 'PedigreeID', '__AbsentNamespace0_FamilyInfo_PedigreeID', pyxb.binding.datatypes.string)
    __PedigreeID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1220, 2)
    __PedigreeID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1220, 2)
    
    PedigreeID = property(__PedigreeID.value, __PedigreeID.set, None, None)

    
    # Attribute SegregationObserved uses Python identifier SegregationObserved
    __SegregationObserved = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SegregationObserved'), 'SegregationObserved', '__AbsentNamespace0_FamilyInfo_SegregationObserved', pyxb.binding.datatypes.string)
    __SegregationObserved._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1221, 2)
    __SegregationObserved._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1221, 2)
    
    SegregationObserved = property(__SegregationObserved.value, __SegregationObserved.set, None, None)

    _ElementMap.update({
        __FamilyHistory.name() : __FamilyHistory
    })
    _AttributeMap.update({
        __NumFamilies.name() : __NumFamilies,
        __NumFamiliesWithVariant.name() : __NumFamiliesWithVariant,
        __NumFamiliesWithSegregationObserved.name() : __NumFamiliesWithSegregationObserved,
        __PedigreeID.name() : __PedigreeID,
        __SegregationObserved.name() : __SegregationObserved
    })
_module_typeBindings.FamilyInfo = FamilyInfo
Namespace.addCategoryObject('typeBinding', 'FamilyInfo', FamilyInfo)


# Complex type SampleType with content type ELEMENT_ONLY
class SampleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SampleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SampleType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1223, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SampleDescription uses Python identifier SampleDescription
    __SampleDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SampleDescription'), 'SampleDescription', '__AbsentNamespace0_SampleType_SampleDescription', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1225, 3), )

    
    SampleDescription = property(__SampleDescription.value, __SampleDescription.set, None, None)

    
    # Element Origin uses Python identifier Origin
    __Origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Origin'), 'Origin', '__AbsentNamespace0_SampleType_Origin', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1233, 3), )

    
    Origin = property(__Origin.value, __Origin.set, None, None)

    
    # Element Ethnicity uses Python identifier Ethnicity
    __Ethnicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Ethnicity'), 'Ethnicity', '__AbsentNamespace0_SampleType_Ethnicity', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1253, 3), )

    
    Ethnicity = property(__Ethnicity.value, __Ethnicity.set, None, None)

    
    # Element GeographicOrigin uses Python identifier GeographicOrigin
    __GeographicOrigin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GeographicOrigin'), 'GeographicOrigin', '__AbsentNamespace0_SampleType_GeographicOrigin', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1254, 3), )

    
    GeographicOrigin = property(__GeographicOrigin.value, __GeographicOrigin.set, None, None)

    
    # Element Tissue uses Python identifier Tissue
    __Tissue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Tissue'), 'Tissue', '__AbsentNamespace0_SampleType_Tissue', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1255, 3), )

    
    Tissue = property(__Tissue.value, __Tissue.set, None, None)

    
    # Element CellLine uses Python identifier CellLine
    __CellLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CellLine'), 'CellLine', '__AbsentNamespace0_SampleType_CellLine', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1256, 3), )

    
    CellLine = property(__CellLine.value, __CellLine.set, None, None)

    
    # Element Species uses Python identifier Species
    __Species = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Species'), 'Species', '__AbsentNamespace0_SampleType_Species', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1257, 3), )

    
    Species = property(__Species.value, __Species.set, None, None)

    
    # Element Age uses Python identifier Age
    __Age = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Age'), 'Age', '__AbsentNamespace0_SampleType_Age', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1266, 3), )

    
    Age = property(__Age.value, __Age.set, None, None)

    
    # Element Strain uses Python identifier Strain
    __Strain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Strain'), 'Strain', '__AbsentNamespace0_SampleType_Strain', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1295, 3), )

    
    Strain = property(__Strain.value, __Strain.set, None, None)

    
    # Element AffectedStatus uses Python identifier AffectedStatus
    __AffectedStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AffectedStatus'), 'AffectedStatus', '__AbsentNamespace0_SampleType_AffectedStatus', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1296, 3), )

    
    AffectedStatus = property(__AffectedStatus.value, __AffectedStatus.set, None, None)

    
    # Element NumberTested uses Python identifier NumberTested
    __NumberTested = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumberTested'), 'NumberTested', '__AbsentNamespace0_SampleType_NumberTested', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1307, 3), )

    
    NumberTested = property(__NumberTested.value, __NumberTested.set, None, 'Denominator, total individuals included in this observation\n\t\t\t\t\t\tset.')

    
    # Element NumberMales uses Python identifier NumberMales
    __NumberMales = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumberMales'), 'NumberMales', '__AbsentNamespace0_SampleType_NumberMales', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1313, 3), )

    
    NumberMales = property(__NumberMales.value, __NumberMales.set, None, 'Denominator, total males included in this observation\n\t\t\t\t\t\tset.')

    
    # Element NumberFemales uses Python identifier NumberFemales
    __NumberFemales = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumberFemales'), 'NumberFemales', '__AbsentNamespace0_SampleType_NumberFemales', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1319, 3), )

    
    NumberFemales = property(__NumberFemales.value, __NumberFemales.set, None, 'Denominator, total females included in this observation\n\t\t\t\t\t\tset.')

    
    # Element NumberChrTested uses Python identifier NumberChrTested
    __NumberChrTested = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NumberChrTested'), 'NumberChrTested', '__AbsentNamespace0_SampleType_NumberChrTested', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1325, 3), )

    
    NumberChrTested = property(__NumberChrTested.value, __NumberChrTested.set, None, 'Denominator, total number chromosomes tested. Number affected\n\t\t\t\t\t\tand unaffected are captured in the element\n\t\t\t\t\t\tNumberObserved.')

    
    # Element Gender uses Python identifier Gender
    __Gender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Gender'), 'Gender', '__AbsentNamespace0_SampleType_Gender', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1332, 3), )

    
    Gender = property(__Gender.value, __Gender.set, None, 'Gender should be used ONLY if explicit values are not available for number of males or females, and there is a need to indicate that the genders in the sample are known. \n                    ')

    
    # Element FamilyData uses Python identifier FamilyData
    __FamilyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FamilyData'), 'FamilyData', '__AbsentNamespace0_SampleType_FamilyData', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1345, 3), )

    
    FamilyData = property(__FamilyData.value, __FamilyData.set, None, None)

    
    # Element Proband uses Python identifier Proband
    __Proband = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Proband'), 'Proband', '__AbsentNamespace0_SampleType_Proband', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1346, 3), )

    
    Proband = property(__Proband.value, __Proband.set, None, None)

    
    # Element Indication uses Python identifier Indication
    __Indication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Indication'), 'Indication', '__AbsentNamespace0_SampleType_Indication', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1347, 3), )

    
    Indication = property(__Indication.value, __Indication.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_SampleType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1348, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_SampleType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1349, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_SampleType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1350, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element SourceType uses Python identifier SourceType
    __SourceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SourceType'), 'SourceType', '__AbsentNamespace0_SampleType_SourceType', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1351, 3), )

    
    SourceType = property(__SourceType.value, __SourceType.set, None, None)

    _ElementMap.update({
        __SampleDescription.name() : __SampleDescription,
        __Origin.name() : __Origin,
        __Ethnicity.name() : __Ethnicity,
        __GeographicOrigin.name() : __GeographicOrigin,
        __Tissue.name() : __Tissue,
        __CellLine.name() : __CellLine,
        __Species.name() : __Species,
        __Age.name() : __Age,
        __Strain.name() : __Strain,
        __AffectedStatus.name() : __AffectedStatus,
        __NumberTested.name() : __NumberTested,
        __NumberMales.name() : __NumberMales,
        __NumberFemales.name() : __NumberFemales,
        __NumberChrTested.name() : __NumberChrTested,
        __Gender.name() : __Gender,
        __FamilyData.name() : __FamilyData,
        __Proband.name() : __Proband,
        __Indication.name() : __Indication,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment,
        __SourceType.name() : __SourceType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SampleType = SampleType
Namespace.addCategoryObject('typeBinding', 'SampleType', SampleType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1226, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_CTD_ANON_19_Description', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1228, 6), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_19_Citation', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1229, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __Citation.name() : __Citation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1258, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute TaxonomyId uses Python identifier TaxonomyId
    __TaxonomyId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TaxonomyId'), 'TaxonomyId', '__AbsentNamespace0_CTD_ANON_20_TaxonomyId', pyxb.binding.datatypes.int)
    __TaxonomyId._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1261, 7)
    __TaxonomyId._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1261, 7)
    
    TaxonomyId = property(__TaxonomyId.value, __TaxonomyId.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __TaxonomyId.name() : __TaxonomyId
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type Co-occurrenceType with content type ELEMENT_ONLY
class Co_occurrenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Co-occurrenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Co-occurrenceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1361, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Zygosity uses Python identifier Zygosity
    __Zygosity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Zygosity'), 'Zygosity', '__AbsentNamespace0_Co_occurrenceType_Zygosity', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1366, 3), )

    
    Zygosity = property(__Zygosity.value, __Zygosity.set, None, None)

    
    # Element AlleleDescSet uses Python identifier AlleleDescSet
    __AlleleDescSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AlleleDescSet'), 'AlleleDescSet', '__AbsentNamespace0_Co_occurrenceType_AlleleDescSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1367, 3), )

    
    AlleleDescSet = property(__AlleleDescSet.value, __AlleleDescSet.set, None, None)

    
    # Element Count uses Python identifier Count
    __Count = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Count'), 'Count', '__AbsentNamespace0_Co_occurrenceType_Count', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1368, 3), )

    
    Count = property(__Count.value, __Count.set, None, None)

    _ElementMap.update({
        __Zygosity.name() : __Zygosity,
        __AlleleDescSet.name() : __AlleleDescSet,
        __Count.name() : __Count
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Co_occurrenceType = Co_occurrenceType
Namespace.addCategoryObject('typeBinding', 'Co-occurrenceType', Co_occurrenceType)


# Complex type ClinicalSignificanceType with content type ELEMENT_ONLY
class ClinicalSignificanceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ClinicalSignificanceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClinicalSignificanceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1371, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ReviewStatus uses Python identifier ReviewStatus
    __ReviewStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReviewStatus'), 'ReviewStatus', '__AbsentNamespace0_ClinicalSignificanceType_ReviewStatus', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1373, 3), )

    
    ReviewStatus = property(__ReviewStatus.value, __ReviewStatus.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_ClinicalSignificanceType_Description', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1374, 3), )

    
    Description = property(__Description.value, __Description.set, None, 'We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ')

    
    # Element Explanation uses Python identifier Explanation
    __Explanation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Explanation'), 'Explanation', '__AbsentNamespace0_ClinicalSignificanceType_Explanation', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1380, 3), )

    
    Explanation = property(__Explanation.value, __Explanation.set, None, "Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.")

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_ClinicalSignificanceType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1386, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_ClinicalSignificanceType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1387, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_ClinicalSignificanceType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1388, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateLastEvaluated uses Python identifier DateLastEvaluated
    __DateLastEvaluated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateLastEvaluated'), 'DateLastEvaluated', '__AbsentNamespace0_ClinicalSignificanceType_DateLastEvaluated', pyxb.binding.datatypes.date)
    __DateLastEvaluated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1390, 2)
    __DateLastEvaluated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1390, 2)
    
    DateLastEvaluated = property(__DateLastEvaluated.value, __DateLastEvaluated.set, None, None)

    _ElementMap.update({
        __ReviewStatus.name() : __ReviewStatus,
        __Description.name() : __Description,
        __Explanation.name() : __Explanation,
        __XRef.name() : __XRef,
        __Citation.name() : __Citation,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateLastEvaluated.name() : __DateLastEvaluated
    })
_module_typeBindings.ClinicalSignificanceType = ClinicalSignificanceType
Namespace.addCategoryObject('typeBinding', 'ClinicalSignificanceType', ClinicalSignificanceType)


# Complex type ClinicalSignificanceTypeSCV with content type ELEMENT_ONLY
class ClinicalSignificanceTypeSCV (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ClinicalSignificanceTypeSCV with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClinicalSignificanceTypeSCV')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1392, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ReviewStatus uses Python identifier ReviewStatus
    __ReviewStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReviewStatus'), 'ReviewStatus', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_ReviewStatus', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1394, 3), )

    
    ReviewStatus = property(__ReviewStatus.value, __ReviewStatus.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Description', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1395, 3), )

    
    Description = property(__Description.value, __Description.set, None, 'We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ')

    
    # Element Explanation uses Python identifier Explanation
    __Explanation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Explanation'), 'Explanation', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Explanation', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1401, 3), )

    
    Explanation = property(__Explanation.value, __Explanation.set, None, "Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.")

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1407, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1408, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1409, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateLastEvaluated uses Python identifier DateLastEvaluated
    __DateLastEvaluated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateLastEvaluated'), 'DateLastEvaluated', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_DateLastEvaluated', pyxb.binding.datatypes.date)
    __DateLastEvaluated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1411, 2)
    __DateLastEvaluated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1411, 2)
    
    DateLastEvaluated = property(__DateLastEvaluated.value, __DateLastEvaluated.set, None, None)

    _ElementMap.update({
        __ReviewStatus.name() : __ReviewStatus,
        __Description.name() : __Description,
        __Explanation.name() : __Explanation,
        __XRef.name() : __XRef,
        __Citation.name() : __Citation,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateLastEvaluated.name() : __DateLastEvaluated
    })
_module_typeBindings.ClinicalSignificanceTypeSCV = ClinicalSignificanceTypeSCV
Namespace.addCategoryObject('typeBinding', 'ClinicalSignificanceTypeSCV', ClinicalSignificanceTypeSCV)


# Complex type AlleleDescType with content type ELEMENT_ONLY
class AlleleDescType (pyxb.binding.basis.complexTypeDefinition):
    """This is to be used within co-occurrence set """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlleleDescType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1413, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_AlleleDescType_Name', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1418, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element RelativeOrientation uses Python identifier RelativeOrientation
    __RelativeOrientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RelativeOrientation'), 'RelativeOrientation', '__AbsentNamespace0_AlleleDescType_RelativeOrientation', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1419, 3), )

    
    RelativeOrientation = property(__RelativeOrientation.value, __RelativeOrientation.set, None, None)

    
    # Element Zygosity uses Python identifier Zygosity
    __Zygosity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Zygosity'), 'Zygosity', '__AbsentNamespace0_AlleleDescType_Zygosity', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1428, 3), )

    
    Zygosity = property(__Zygosity.value, __Zygosity.set, None, None)

    
    # Element ClinicalSignificance uses Python identifier ClinicalSignificance
    __ClinicalSignificance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance'), 'ClinicalSignificance', '__AbsentNamespace0_AlleleDescType_ClinicalSignificance', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1429, 3), )

    
    ClinicalSignificance = property(__ClinicalSignificance.value, __ClinicalSignificance.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __RelativeOrientation.name() : __RelativeOrientation,
        __Zygosity.name() : __Zygosity,
        __ClinicalSignificance.name() : __ClinicalSignificance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AlleleDescType = AlleleDescType
Namespace.addCategoryObject('typeBinding', 'AlleleDescType', AlleleDescType)


# Complex type MeasureType with content type ELEMENT_ONLY
class MeasureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MeasureType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 31, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_MeasureType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 33, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_MeasureType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 34, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_MeasureType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 35, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element CytogeneticLocation uses Python identifier CytogeneticLocation
    __CytogeneticLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CytogeneticLocation'), 'CytogeneticLocation', '__AbsentNamespace0_MeasureType_CytogeneticLocation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 107, 3), )

    
    CytogeneticLocation = property(__CytogeneticLocation.value, __CytogeneticLocation.set, None, 'Cytogenetic location is maintained\n\t\t\t\t\tindependent of sequence location.')

    
    # Element SequenceLocation uses Python identifier SequenceLocation
    __SequenceLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SequenceLocation'), 'SequenceLocation', '__AbsentNamespace0_MeasureType_SequenceLocation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 113, 3), )

    
    SequenceLocation = property(__SequenceLocation.value, __SequenceLocation.set, None, None)

    
    # Element MeasureRelationship uses Python identifier MeasureRelationship
    __MeasureRelationship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MeasureRelationship'), 'MeasureRelationship', '__AbsentNamespace0_MeasureType_MeasureRelationship', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 114, 3), )

    
    MeasureRelationship = property(__MeasureRelationship.value, __MeasureRelationship.set, None, 'MeasureRelationship is used to represent relationships between \n\t\t\t\t\t\tthe type of measure being represented, and other object.\n\t\t\t\t\t\tThis can be gene/variant, protein/gene, etc., as in when a variation is reported to be within a gene.\n\t\t\t\t\t')

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_MeasureType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 173, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_MeasureType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 174, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_MeasureType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 175, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__AbsentNamespace0_MeasureType_Source', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 176, 3), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_MeasureType_Type', _module_typeBindings.STD_ANON_3, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 178, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 178, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_MeasureType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __CytogeneticLocation.name() : __CytogeneticLocation,
        __SequenceLocation.name() : __SequenceLocation,
        __MeasureRelationship.name() : __MeasureRelationship,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.MeasureType = MeasureType
Namespace.addCategoryObject('typeBinding', 'MeasureType', MeasureType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_21 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 39, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_21_Type', _module_typeBindings.STD_ANON, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 42, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 42, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Change uses Python identifier Change
    __Change = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Change'), 'Change', '__AbsentNamespace0_CTD_ANON_21_Change', pyxb.binding.datatypes.anySimpleType)
    __Change._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 94, 10)
    __Change._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 94, 10)
    
    Change = property(__Change.value, __Change.set, None, None)

    
    # Attribute Accession uses Python identifier Accession
    __Accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Accession'), 'Accession', '__AbsentNamespace0_CTD_ANON_21_Accession', pyxb.binding.datatypes.string)
    __Accession._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 95, 10)
    __Accession._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 95, 10)
    
    Accession = property(__Accession.value, __Accession.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_21_Version', pyxb.binding.datatypes.positiveInteger)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 96, 10)
    __Version._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 96, 10)
    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Change.name() : __Change,
        __Accession.name() : __Accession,
        __Version.name() : __Version
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """MeasureRelationship is used to represent relationships between 
						the type of measure being represented, and other object.
						This can be gene/variant, protein/gene, etc., as in when a variation is reported to be within a gene.
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 121, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_CTD_ANON_22_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 123, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_CTD_ANON_22_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 124, 6), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_CTD_ANON_22_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 125, 6), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element SequenceLocation uses Python identifier SequenceLocation
    __SequenceLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SequenceLocation'), 'SequenceLocation', '__AbsentNamespace0_CTD_ANON_22_SequenceLocation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 151, 6), )

    
    SequenceLocation = property(__SequenceLocation.value, __SequenceLocation.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_22_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 152, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_22_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 153, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_22_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 154, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_22_Type', _module_typeBindings.STD_ANON_2, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 156, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 156, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_22_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __SequenceLocation.name() : __SequenceLocation,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_23 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 129, 10)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_23_Type', _module_typeBindings.STD_ANON_, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 132, 13)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 132, 13)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type XrefType with content type EMPTY
class XrefType (pyxb.binding.basis.complexTypeDefinition):
    """This structure is used to represent how an object described in the submission relates to objects in other databases.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'XrefType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 204, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute DB uses Python identifier DB
    __DB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DB'), 'DB', '__AbsentNamespace0_XrefType_DB', pyxb.binding.datatypes.string, required=True)
    __DB._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 209, 2)
    __DB._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 209, 2)
    
    DB = property(__DB.value, __DB.set, None, 'The name of the database. When there is an overlap with sequence\n\t\t\t\tdatabases, that name is used.')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_XrefType_ID', pyxb.binding.datatypes.string, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 215, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 215, 2)
    
    ID = property(__ID.value, __ID.set, None, 'The identifier used by the database.  Being exported\n\t\t\t\tas a string even though internally the database has rules for defining\n\t\t\t\twhich datases use integer identifers.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_XrefType_Type', pyxb.binding.datatypes.string)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 222, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 222, 2)
    
    Type = property(__Type.value, __Type.set, None, 'Used to differentiate between different types of identifers\n\t\t\t\tthat a database may provide.')

    
    # Attribute URL uses Python identifier URL
    __URL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__AbsentNamespace0_XrefType_URL', pyxb.binding.datatypes.anyURI)
    __URL._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 228, 2)
    __URL._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 228, 2)
    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute Status uses Python identifier Status
    __Status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Status'), 'Status', '__AbsentNamespace0_XrefType_Status', _module_typeBindings.typeStatus, unicode_default='current')
    __Status._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 229, 2)
    __Status._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 229, 2)
    
    Status = property(__Status.value, __Status.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DB.name() : __DB,
        __ID.name() : __ID,
        __Type.name() : __Type,
        __URL.name() : __URL,
        __Status.name() : __Status
    })
_module_typeBindings.XrefType = XrefType
Namespace.addCategoryObject('typeBinding', 'XrefType', XrefType)


# Complex type CommentType with content type SIMPLE
class CommentType (pyxb.binding.basis.complexTypeDefinition):
    """A structure to support reporting unformatted content.
			"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 262, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute DataSource uses Python identifier DataSource
    __DataSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DataSource'), 'DataSource', '__AbsentNamespace0_CommentType_DataSource', pyxb.binding.datatypes.string)
    __DataSource._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 269, 4)
    __DataSource._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 269, 4)
    
    DataSource = property(__DataSource.value, __DataSource.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CommentType_Type', _module_typeBindings.CommentTypeList)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 270, 4)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 270, 4)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DataSource.name() : __DataSource,
        __Type.name() : __Type
    })
_module_typeBindings.CommentType = CommentType
Namespace.addCategoryObject('typeBinding', 'CommentType', CommentType)


# Complex type DataSourceType with content type EMPTY
class DataSourceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DataSourceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSourceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 276, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute DataSource uses Python identifier DataSource
    __DataSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DataSource'), 'DataSource', '__AbsentNamespace0_DataSourceType_DataSource', pyxb.binding.datatypes.string, required=True)
    __DataSource._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 277, 2)
    __DataSource._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 277, 2)
    
    DataSource = property(__DataSource.value, __DataSource.set, None, 'A standard term for the source of the information')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_DataSourceType_ID', pyxb.binding.datatypes.string)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 282, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 282, 2)
    
    ID = property(__ID.value, __ID.set, None, 'The identifier used by the data source')

    
    # Attribute SourceType uses Python identifier SourceType
    __SourceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SourceType'), 'SourceType', '__AbsentNamespace0_DataSourceType_SourceType', _module_typeBindings.STD_ANON_4)
    __SourceType._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 287, 2)
    __SourceType._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 287, 2)
    
    SourceType = property(__SourceType.value, __SourceType.set, None, 'Controlled terms to categorize the source of the\n\t\t\t\tinformation')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DataSource.name() : __DataSource,
        __ID.name() : __ID,
        __SourceType.name() : __SourceType
    })
_module_typeBindings.DataSourceType = DataSourceType
Namespace.addCategoryObject('typeBinding', 'DataSourceType', DataSourceType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 394, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Acc uses Python identifier Acc
    __Acc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Acc'), 'Acc', '__AbsentNamespace0_CTD_ANON_24_Acc', pyxb.binding.datatypes.string, required=True)
    __Acc._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 395, 5)
    __Acc._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 395, 5)
    
    Acc = property(__Acc.value, __Acc.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_24_Version', pyxb.binding.datatypes.integer, required=True)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 396, 5)
    __Version._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 396, 5)
    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_24_Type', _module_typeBindings.STD_ANON_6, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 397, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 397, 5)
    
    Type = property(__Type.value, __Type.set, None, "RCV accessions aggregate data from each submission.\n\t\t\t\t\t\t\t\tEach submission is assigned an accession of beginning with 'SCV'\n\t\t\t\t\t\t\t")

    
    # Attribute OrgID uses Python identifier OrgID
    __OrgID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'OrgID'), 'OrgID', '__AbsentNamespace0_CTD_ANON_24_OrgID', pyxb.binding.datatypes.int)
    __OrgID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 410, 5)
    __OrgID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 410, 5)
    
    OrgID = property(__OrgID.value, __OrgID.set, None, None)

    
    # Attribute OrgAbbreviation uses Python identifier OrgAbbreviation
    __OrgAbbreviation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'OrgAbbreviation'), 'OrgAbbreviation', '__AbsentNamespace0_CTD_ANON_24_OrgAbbreviation', pyxb.binding.datatypes.string)
    __OrgAbbreviation._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 411, 5)
    __OrgAbbreviation._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 411, 5)
    
    OrgAbbreviation = property(__OrgAbbreviation.value, __OrgAbbreviation.set, None, None)

    
    # Attribute DateUpdated uses Python identifier DateUpdated
    __DateUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateUpdated'), 'DateUpdated', '__AbsentNamespace0_CTD_ANON_24_DateUpdated', pyxb.binding.datatypes.date)
    __DateUpdated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 412, 5)
    __DateUpdated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 412, 5)
    
    DateUpdated = property(__DateUpdated.value, __DateUpdated.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Acc.name() : __Acc,
        __Version.name() : __Version,
        __Type.name() : __Type,
        __OrgID.name() : __OrgID,
        __OrgAbbreviation.name() : __OrgAbbreviation,
        __DateUpdated.name() : __DateUpdated
    })
_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_25 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 470, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_25_Type', _module_typeBindings.STD_ANON_8, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 473, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 473, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 523, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Acc uses Python identifier Acc
    __Acc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Acc'), 'Acc', '__AbsentNamespace0_CTD_ANON_26_Acc', pyxb.binding.datatypes.string, required=True)
    __Acc._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 524, 5)
    __Acc._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 524, 5)
    
    Acc = property(__Acc.value, __Acc.set, None, 'The accession assigned by ClinVar.')

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_26_Version', pyxb.binding.datatypes.integer, required=True)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 529, 5)
    __Version._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 529, 5)
    
    Version = property(__Version.value, __Version.set, None, 'A new version of an SCV accession is assigned with an update\n\t\t\t\t\t\t\tfrom the submitter.  A new version of an RCV accession is assigned when the\n\t\t\t\t\t\t\tset of ClinVarAssertions is changed, either by a change in version or by\n\t\t\t\t\t\t\taddition of a new submission.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_26_Type', _module_typeBindings.STD_ANON_9, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 537, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 537, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute DateUpdated uses Python identifier DateUpdated
    __DateUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateUpdated'), 'DateUpdated', '__AbsentNamespace0_CTD_ANON_26_DateUpdated', pyxb.binding.datatypes.date)
    __DateUpdated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 544, 5)
    __DateUpdated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 544, 5)
    
    DateUpdated = property(__DateUpdated.value, __DateUpdated.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Acc.name() : __Acc,
        __Version.name() : __Version,
        __Type.name() : __Type,
        __DateUpdated.name() : __DateUpdated
    })
_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_27 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 580, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_27_Type', _module_typeBindings.STD_ANON_11, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 583, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 583, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_28 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 619, 4)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_28_Type', _module_typeBindings.STD_ANON_12, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 622, 7)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 622, 7)
    
    Type = property(__Type.value, __Type.set, None, 'MGG-2713 added HGVS, Description, and MolecularConsequence for AttributeType because they are in the submission xsd.  Skipping Location, which is also in the submission xsd.  In the current set of submissions, (March 2017) only HGVS is used.  djh')

    
    # Attribute Change uses Python identifier Change
    __Change = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Change'), 'Change', '__AbsentNamespace0_CTD_ANON_28_Change', pyxb.binding.datatypes.anySimpleType)
    __Change._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 651, 7)
    __Change._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 651, 7)
    
    Change = property(__Change.value, __Change.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Change.name() : __Change
    })
_module_typeBindings.CTD_ANON_28 = CTD_ANON_28


# Complex type MeasureSetType with content type ELEMENT_ONLY
class MeasureSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MeasureSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureSetType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 661, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Measure uses Python identifier Measure
    __Measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Measure'), 'Measure', '__AbsentNamespace0_MeasureSetType_Measure', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 663, 4), )

    
    Measure = property(__Measure.value, __Measure.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_MeasureSetType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 664, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_MeasureSetType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 665, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_MeasureSetType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 666, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_MeasureSetType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 667, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_MeasureSetType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 668, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_MeasureSetType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 669, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_MeasureSetType_Type', _module_typeBindings.STD_ANON_13, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 671, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 671, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_MeasureSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute Acc uses Python identifier Acc
    __Acc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Acc'), 'Acc', '__AbsentNamespace0_MeasureSetType_Acc', _module_typeBindings.STD_ANON_35)
    __Acc._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1607, 2)
    __Acc._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1607, 2)
    
    Acc = property(__Acc.value, __Acc.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_MeasureSetType_Version', pyxb.binding.datatypes.unsignedInt)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1614, 2)
    __Version._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1614, 2)
    
    Version = property(__Version.value, __Version.set, None, None)

    _ElementMap.update({
        __Measure.name() : __Measure,
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID,
        __Acc.name() : __Acc,
        __Version.name() : __Version
    })
_module_typeBindings.MeasureSetType = MeasureSetType
Namespace.addCategoryObject('typeBinding', 'MeasureSetType', MeasureSetType)


# Complex type GenotypeSetType with content type ELEMENT_ONLY
class GenotypeSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GenotypeSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenotypeSetType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 691, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MeasureSet uses Python identifier MeasureSet
    __MeasureSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MeasureSet'), 'MeasureSet', '__AbsentNamespace0_GenotypeSetType_MeasureSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 693, 4), )

    
    MeasureSet = property(__MeasureSet.value, __MeasureSet.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_GenotypeSetType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 694, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_GenotypeSetType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 695, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_GenotypeSetType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 696, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_GenotypeSetType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 697, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_GenotypeSetType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 698, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_GenotypeSetType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 699, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_GenotypeSetType_Type', _module_typeBindings.STD_ANON_14, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 701, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 701, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_GenotypeSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute Acc uses Python identifier Acc
    __Acc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Acc'), 'Acc', '__AbsentNamespace0_GenotypeSetType_Acc', _module_typeBindings.STD_ANON_35)
    __Acc._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1607, 2)
    __Acc._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1607, 2)
    
    Acc = property(__Acc.value, __Acc.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_GenotypeSetType_Version', pyxb.binding.datatypes.unsignedInt)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1614, 2)
    __Version._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1614, 2)
    
    Version = property(__Version.value, __Version.set, None, None)

    _ElementMap.update({
        __MeasureSet.name() : __MeasureSet,
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID,
        __Acc.name() : __Acc,
        __Version.name() : __Version
    })
_module_typeBindings.GenotypeSetType = GenotypeSetType
Namespace.addCategoryObject('typeBinding', 'GenotypeSetType', GenotypeSetType)


# Complex type TraitSetType with content type ELEMENT_ONLY
class TraitSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TraitSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TraitSetType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 712, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Trait uses Python identifier Trait
    __Trait = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Trait'), 'Trait', '__AbsentNamespace0_TraitSetType_Trait', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 714, 3), )

    
    Trait = property(__Trait.value, __Trait.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_TraitSetType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 715, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_TraitSetType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 716, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_TraitSetType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 717, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_TraitSetType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 739, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_TraitSetType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 740, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_TraitSetType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 741, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_TraitSetType_Type', _module_typeBindings.STD_ANON_15, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 743, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 743, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_TraitSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Trait.name() : __Trait,
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.TraitSetType = TraitSetType
Namespace.addCategoryObject('typeBinding', 'TraitSetType', TraitSetType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_29 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 721, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_29_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 724, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 724, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_29 = CTD_ANON_29


# Complex type TraitType with content type ELEMENT_ONLY
class TraitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TraitType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TraitType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 756, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_TraitType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 758, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_TraitType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 759, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_TraitType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 760, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element TraitRelationship uses Python identifier TraitRelationship
    __TraitRelationship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TraitRelationship'), 'TraitRelationship', '__AbsentNamespace0_TraitType_TraitRelationship', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 778, 3), )

    
    TraitRelationship = property(__TraitRelationship.value, __TraitRelationship.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_TraitType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 819, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_TraitType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 820, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_TraitType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 821, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__AbsentNamespace0_TraitType_Source', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 822, 3), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_TraitType_Type', _module_typeBindings.STD_ANON_17, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 824, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 824, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_TraitType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __TraitRelationship.name() : __TraitRelationship,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.TraitType = TraitType
Namespace.addCategoryObject('typeBinding', 'TraitType', TraitType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_30 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 764, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_30_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 767, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 767, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_30 = CTD_ANON_30


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 779, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_CTD_ANON_31_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 781, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_CTD_ANON_31_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 782, 6), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_CTD_ANON_31_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 783, 6), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_31_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 801, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_31_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 802, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__AbsentNamespace0_CTD_ANON_31_Source', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 803, 6), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_31_Type', _module_typeBindings.STD_ANON_16, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 805, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 805, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_31_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.CTD_ANON_31 = CTD_ANON_31


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_32 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 787, 10)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_32_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 790, 13)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 790, 13)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_32 = CTD_ANON_32


# Complex type ClinAsserTraitSetType with content type ELEMENT_ONLY
class ClinAsserTraitSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ClinAsserTraitSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClinAsserTraitSetType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 840, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Trait uses Python identifier Trait
    __Trait = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Trait'), 'Trait', '__AbsentNamespace0_ClinAsserTraitSetType_Trait', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 842, 3), )

    
    Trait = property(__Trait.value, __Trait.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_ClinAsserTraitSetType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 843, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_ClinAsserTraitSetType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 844, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_ClinAsserTraitSetType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 845, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_ClinAsserTraitSetType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 867, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_ClinAsserTraitSetType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 868, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_ClinAsserTraitSetType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 869, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_ClinAsserTraitSetType_Type', _module_typeBindings.STD_ANON_18, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 871, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 871, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute DateLastEvaluated uses Python identifier DateLastEvaluated
    __DateLastEvaluated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateLastEvaluated'), 'DateLastEvaluated', '__AbsentNamespace0_ClinAsserTraitSetType_DateLastEvaluated', pyxb.binding.datatypes.date)
    __DateLastEvaluated._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 882, 2)
    __DateLastEvaluated._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 882, 2)
    
    DateLastEvaluated = property(__DateLastEvaluated.value, __DateLastEvaluated.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_ClinAsserTraitSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Trait.name() : __Trait,
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __DateLastEvaluated.name() : __DateLastEvaluated,
        __ID.name() : __ID
    })
_module_typeBindings.ClinAsserTraitSetType = ClinAsserTraitSetType
Namespace.addCategoryObject('typeBinding', 'ClinAsserTraitSetType', ClinAsserTraitSetType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_33 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 849, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_33_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 852, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 852, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_33 = CTD_ANON_33


# Complex type ClinAsserTraitType with content type ELEMENT_ONLY
class ClinAsserTraitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ClinAsserTraitType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClinAsserTraitType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 886, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_ClinAsserTraitType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 888, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_ClinAsserTraitType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 889, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_ClinAsserTraitType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 890, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element TraitRelationship uses Python identifier TraitRelationship
    __TraitRelationship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TraitRelationship'), 'TraitRelationship', '__AbsentNamespace0_ClinAsserTraitType_TraitRelationship', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 908, 3), )

    
    TraitRelationship = property(__TraitRelationship.value, __TraitRelationship.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_ClinAsserTraitType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 949, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_ClinAsserTraitType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 950, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_ClinAsserTraitType_Comment', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 951, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__AbsentNamespace0_ClinAsserTraitType_Source', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 952, 3), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_ClinAsserTraitType_Type', _module_typeBindings.STD_ANON_20, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 954, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 954, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_ClinAsserTraitType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __TraitRelationship.name() : __TraitRelationship,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.ClinAsserTraitType = ClinAsserTraitType
Namespace.addCategoryObject('typeBinding', 'ClinAsserTraitType', ClinAsserTraitType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_34 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 894, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_34_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 897, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 897, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_34 = CTD_ANON_34


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 909, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_CTD_ANON_35_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 911, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_CTD_ANON_35_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 912, 6), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_CTD_ANON_35_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 913, 6), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_35_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 931, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_35_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 932, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__AbsentNamespace0_CTD_ANON_35_Source', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 933, 6), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_35_Type', _module_typeBindings.STD_ANON_19, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 935, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 935, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_35_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.CTD_ANON_35 = CTD_ANON_35


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_36 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 917, 10)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_36_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 920, 13)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 920, 13)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_36 = CTD_ANON_36


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_37 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1073, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_37_Type', _module_typeBindings.STD_ANON_23, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1076, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1076, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_37 = CTD_ANON_37


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (MethodType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1116, 4)
    _ElementMap = MethodType._ElementMap.copy()
    _AttributeMap = MethodType._AttributeMap.copy()
    # Base type is MethodType
    
    # Element NamePlatform (NamePlatform) inherited from MethodType
    
    # Element TypePlatform (TypePlatform) inherited from MethodType
    
    # Element Purpose (Purpose) inherited from MethodType
    
    # Element ResultType (ResultType) inherited from MethodType
    
    # Element MinReported (MinReported) inherited from MethodType
    
    # Element MaxReported (MaxReported) inherited from MethodType
    
    # Element ReferenceStandard (ReferenceStandard) inherited from MethodType
    
    # Element Citation (Citation) inherited from MethodType
    
    # Element XRef (XRef) inherited from MethodType
    
    # Element Description (Description) inherited from MethodType
    
    # Element Software (Software) inherited from MethodType
    
    # Element SourceType (SourceType) inherited from MethodType
    
    # Element MethodType (MethodType) inherited from MethodType
    
    # Element MethodAttribute (MethodAttribute) inherited from MethodType
    
    # Element MethodResult (MethodResult) inherited from MethodType
    
    # Element Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_38_Type', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1120, 8), )

    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Type.name() : __Type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_38 = CTD_ANON_38


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_39 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1152, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_39_Type', _module_typeBindings.STD_ANON_25, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1155, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1155, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_39 = CTD_ANON_39


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.int
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1267, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.int
    
    # Attribute age_unit uses Python identifier age_unit
    __age_unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'age_unit'), 'age_unit', '__AbsentNamespace0_CTD_ANON_40_age_unit', _module_typeBindings.STD_ANON_27, required=True)
    __age_unit._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1270, 7)
    __age_unit._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1270, 7)
    
    age_unit = property(__age_unit.value, __age_unit.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_40_Type', _module_typeBindings.STD_ANON_28, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1282, 7)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1282, 7)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __age_unit.name() : __age_unit,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_40 = CTD_ANON_40


# Complex type IndicationType with content type ELEMENT_ONLY
class IndicationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type IndicationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndicationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1433, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Trait uses Python identifier Trait
    __Trait = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Trait'), 'Trait', '__AbsentNamespace0_IndicationType_Trait', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1435, 3), )

    
    Trait = property(__Trait.value, __Trait.set, None, 'Represent the value for the test indication as a name of a\n\t\t\t\t\t\ttrait.                     ')

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__AbsentNamespace0_IndicationType_Name', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1441, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Symbol'), 'Symbol', '__AbsentNamespace0_IndicationType_Symbol', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1442, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_IndicationType_AttributeSet', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1443, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Citation'), 'Citation', '__AbsentNamespace0_IndicationType_Citation', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1445, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XRef'), 'XRef', '__AbsentNamespace0_IndicationType_XRef', True, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1446, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Comment'), 'Comment', '__AbsentNamespace0_IndicationType_Comment', False, pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1447, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_IndicationType_Type', _module_typeBindings.STD_ANON_33, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1449, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1449, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__AbsentNamespace0_IndicationType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1604, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Trait.name() : __Trait,
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
_module_typeBindings.IndicationType = IndicationType
Namespace.addCategoryObject('typeBinding', 'IndicationType', IndicationType)


# Complex type AssertionTypeRCV with content type EMPTY
class AssertionTypeRCV (pyxb.binding.basis.complexTypeDefinition):
    """Assertion is used to represent the type of relationship between the trait set and the measure set. This is stored in
						GTR.clinvar.measure_trait.relat_type.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssertionTypeRCV')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1523, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_AssertionTypeRCV_Type', _module_typeBindings.AssertionTypeAttr, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1529, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1529, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.AssertionTypeRCV = AssertionTypeRCV
Namespace.addCategoryObject('typeBinding', 'AssertionTypeRCV', AssertionTypeRCV)


# Complex type SequenceLocationType with content type EMPTY
class SequenceLocationType (pyxb.binding.basis.complexTypeDefinition):
    """Used to report the assembly, chromosome, and location of the measure."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequenceLocationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1564, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Assembly uses Python identifier Assembly
    __Assembly = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Assembly'), 'Assembly', '__AbsentNamespace0_SequenceLocationType_Assembly', pyxb.binding.datatypes.string, required=True)
    __Assembly._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1571, 2)
    __Assembly._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1571, 2)
    
    Assembly = property(__Assembly.value, __Assembly.set, None, None)

    
    # Attribute Chr uses Python identifier Chr
    __Chr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Chr'), 'Chr', '__AbsentNamespace0_SequenceLocationType_Chr', pyxb.binding.datatypes.string, required=True)
    __Chr._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1572, 2)
    __Chr._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1572, 2)
    
    Chr = property(__Chr.value, __Chr.set, None, None)

    
    # Attribute Accession uses Python identifier Accession
    __Accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Accession'), 'Accession', '__AbsentNamespace0_SequenceLocationType_Accession', pyxb.binding.datatypes.string)
    __Accession._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1573, 2)
    __Accession._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1573, 2)
    
    Accession = property(__Accession.value, __Accession.set, None, None)

    
    # Attribute outerStart uses Python identifier outerStart
    __outerStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outerStart'), 'outerStart', '__AbsentNamespace0_SequenceLocationType_outerStart', pyxb.binding.datatypes.nonNegativeInteger)
    __outerStart._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1574, 2)
    __outerStart._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1574, 2)
    
    outerStart = property(__outerStart.value, __outerStart.set, None, None)

    
    # Attribute innerStart uses Python identifier innerStart
    __innerStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'innerStart'), 'innerStart', '__AbsentNamespace0_SequenceLocationType_innerStart', pyxb.binding.datatypes.nonNegativeInteger)
    __innerStart._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1575, 2)
    __innerStart._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1575, 2)
    
    innerStart = property(__innerStart.value, __innerStart.set, None, None)

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__AbsentNamespace0_SequenceLocationType_start', pyxb.binding.datatypes.nonNegativeInteger)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1576, 2)
    __start._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1576, 2)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute stop uses Python identifier stop
    __stop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_SequenceLocationType_stop', pyxb.binding.datatypes.positiveInteger)
    __stop._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1577, 2)
    __stop._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1577, 2)
    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Attribute innerStop uses Python identifier innerStop
    __innerStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'innerStop'), 'innerStop', '__AbsentNamespace0_SequenceLocationType_innerStop', pyxb.binding.datatypes.positiveInteger)
    __innerStop._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1578, 2)
    __innerStop._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1578, 2)
    
    innerStop = property(__innerStop.value, __innerStop.set, None, None)

    
    # Attribute outerStop uses Python identifier outerStop
    __outerStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'outerStop'), 'outerStop', '__AbsentNamespace0_SequenceLocationType_outerStop', pyxb.binding.datatypes.positiveInteger)
    __outerStop._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1579, 2)
    __outerStop._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1579, 2)
    
    outerStop = property(__outerStop.value, __outerStop.set, None, None)

    
    # Attribute display_start uses Python identifier display_start
    __display_start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'display_start'), 'display_start', '__AbsentNamespace0_SequenceLocationType_display_start', pyxb.binding.datatypes.nonNegativeInteger)
    __display_start._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1580, 2)
    __display_start._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1580, 2)
    
    display_start = property(__display_start.value, __display_start.set, None, None)

    
    # Attribute display_stop uses Python identifier display_stop
    __display_stop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'display_stop'), 'display_stop', '__AbsentNamespace0_SequenceLocationType_display_stop', pyxb.binding.datatypes.positiveInteger)
    __display_stop._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1581, 2)
    __display_stop._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1581, 2)
    
    display_stop = property(__display_stop.value, __display_stop.set, None, None)

    
    # Attribute Strand uses Python identifier Strand
    __Strand = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Strand'), 'Strand', '__AbsentNamespace0_SequenceLocationType_Strand', pyxb.binding.datatypes.string)
    __Strand._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1582, 2)
    __Strand._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1582, 2)
    
    Strand = property(__Strand.value, __Strand.set, None, None)

    
    # Attribute variantLength uses Python identifier variantLength
    __variantLength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variantLength'), 'variantLength', '__AbsentNamespace0_SequenceLocationType_variantLength', pyxb.binding.datatypes.positiveInteger)
    __variantLength._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1583, 2)
    __variantLength._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1583, 2)
    
    variantLength = property(__variantLength.value, __variantLength.set, None, None)

    
    # Attribute referenceAllele uses Python identifier referenceAllele
    __referenceAllele = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referenceAllele'), 'referenceAllele', '__AbsentNamespace0_SequenceLocationType_referenceAllele', pyxb.binding.datatypes.string)
    __referenceAllele._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1584, 2)
    __referenceAllele._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1584, 2)
    
    referenceAllele = property(__referenceAllele.value, __referenceAllele.set, None, None)

    
    # Attribute alternateAllele uses Python identifier alternateAllele
    __alternateAllele = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alternateAllele'), 'alternateAllele', '__AbsentNamespace0_SequenceLocationType_alternateAllele', pyxb.binding.datatypes.string)
    __alternateAllele._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1585, 2)
    __alternateAllele._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1585, 2)
    
    alternateAllele = property(__alternateAllele.value, __alternateAllele.set, None, None)

    
    # Attribute AssemblyAccessionVersion uses Python identifier AssemblyAccessionVersion
    __AssemblyAccessionVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'AssemblyAccessionVersion'), 'AssemblyAccessionVersion', '__AbsentNamespace0_SequenceLocationType_AssemblyAccessionVersion', pyxb.binding.datatypes.string)
    __AssemblyAccessionVersion._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1586, 2)
    __AssemblyAccessionVersion._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1586, 2)
    
    AssemblyAccessionVersion = property(__AssemblyAccessionVersion.value, __AssemblyAccessionVersion.set, None, None)

    
    # Attribute AssemblyStatus uses Python identifier AssemblyStatus
    __AssemblyStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'AssemblyStatus'), 'AssemblyStatus', '__AbsentNamespace0_SequenceLocationType_AssemblyStatus', _module_typeBindings.STD_ANON_34)
    __AssemblyStatus._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1587, 2)
    __AssemblyStatus._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1587, 2)
    
    AssemblyStatus = property(__AssemblyStatus.value, __AssemblyStatus.set, None, None)

    
    # Attribute positionVCF uses Python identifier positionVCF
    __positionVCF = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positionVCF'), 'positionVCF', '__AbsentNamespace0_SequenceLocationType_positionVCF', pyxb.binding.datatypes.nonNegativeInteger)
    __positionVCF._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1595, 2)
    __positionVCF._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1595, 2)
    
    positionVCF = property(__positionVCF.value, __positionVCF.set, None, None)

    
    # Attribute referenceAlleleVCF uses Python identifier referenceAlleleVCF
    __referenceAlleleVCF = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referenceAlleleVCF'), 'referenceAlleleVCF', '__AbsentNamespace0_SequenceLocationType_referenceAlleleVCF', pyxb.binding.datatypes.string)
    __referenceAlleleVCF._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1596, 2)
    __referenceAlleleVCF._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1596, 2)
    
    referenceAlleleVCF = property(__referenceAlleleVCF.value, __referenceAlleleVCF.set, None, None)

    
    # Attribute alternateAlleleVCF uses Python identifier alternateAlleleVCF
    __alternateAlleleVCF = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alternateAlleleVCF'), 'alternateAlleleVCF', '__AbsentNamespace0_SequenceLocationType_alternateAlleleVCF', pyxb.binding.datatypes.string)
    __alternateAlleleVCF._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1597, 2)
    __alternateAlleleVCF._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1597, 2)
    
    alternateAlleleVCF = property(__alternateAlleleVCF.value, __alternateAlleleVCF.set, None, None)

    
    # Attribute forDisplayLength uses Python identifier forDisplayLength
    __forDisplayLength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'forDisplayLength'), 'forDisplayLength', '__AbsentNamespace0_SequenceLocationType_forDisplayLength', pyxb.binding.datatypes.boolean)
    __forDisplayLength._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1598, 2)
    __forDisplayLength._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1598, 2)
    
    forDisplayLength = property(__forDisplayLength.value, __forDisplayLength.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Assembly.name() : __Assembly,
        __Chr.name() : __Chr,
        __Accession.name() : __Accession,
        __outerStart.name() : __outerStart,
        __innerStart.name() : __innerStart,
        __start.name() : __start,
        __stop.name() : __stop,
        __innerStop.name() : __innerStop,
        __outerStop.name() : __outerStop,
        __display_start.name() : __display_start,
        __display_stop.name() : __display_stop,
        __Strand.name() : __Strand,
        __variantLength.name() : __variantLength,
        __referenceAllele.name() : __referenceAllele,
        __alternateAllele.name() : __alternateAllele,
        __AssemblyAccessionVersion.name() : __AssemblyAccessionVersion,
        __AssemblyStatus.name() : __AssemblyStatus,
        __positionVCF.name() : __positionVCF,
        __referenceAlleleVCF.name() : __referenceAlleleVCF,
        __alternateAlleleVCF.name() : __alternateAlleleVCF,
        __forDisplayLength.name() : __forDisplayLength
    })
_module_typeBindings.SequenceLocationType = SequenceLocationType
Namespace.addCategoryObject('typeBinding', 'SequenceLocationType', SequenceLocationType)


# Complex type AssertionTypeSCV with content type EMPTY
class AssertionTypeSCV (pyxb.binding.basis.complexTypeDefinition):
    """Assertion is used to represent the type of relationship between the trait set and the measure set. This is stored in
						GTR.clinvar.measure_trait.relat_type.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssertionTypeSCV')
    _XSDLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1531, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_AssertionTypeSCV_Type', _module_typeBindings.AssertionTypeAttrSCV, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1537, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1537, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.AssertionTypeSCV = AssertionTypeSCV
Namespace.addCategoryObject('typeBinding', 'AssertionTypeSCV', AssertionTypeSCV)


ReleaseSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReleaseSet'), ReleaseType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 2, 8))
Namespace.addCategoryObject('elementBinding', ReleaseSet.name().localName(), ReleaseSet)

ClinVarSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClinVarSet'), PublicSetType, documentation='The ClinVarSet is used to group the aggregate record (RCV accession)\n\t\t\twith the submissions underlying it (SCV accessions) \n\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 3, 1))
Namespace.addCategoryObject('elementBinding', ClinVarSet.name().localName(), ClinVarSet)

ClinVarAssertion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClinVarAssertion'), MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', ClinVarAssertion.name().localName(), ClinVarAssertion)

ReferenceClinVarAssertion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceClinVarAssertion'), ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', ReferenceClinVarAssertion.name().localName(), ReferenceClinVarAssertion)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_21, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 38, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 101, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 102, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 103, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 101, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 102, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 103, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 38, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 101, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 102, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 103, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_23, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 128, 9)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 147, 9)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 147, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 128, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 147, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ID'), CTD_ANON_2, scope=CitationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 233, 3)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), pyxb.binding.datatypes.anyURI, scope=CitationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 247, 3)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CitationText'), pyxb.binding.datatypes.string, scope=CitationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 248, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 233, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 247, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 248, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, 'ID')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 233, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 247, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, 'CitationText')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 248, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CitationType._Automaton = _BuildAutomaton_2()




PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClinVarAssertion'), MeasureTraitType, scope=PublicSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 10, 1)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceClinVarAssertion'), ReferenceAssertionType, scope=PublicSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 16, 1)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RecordStatus'), STD_ANON_5, scope=PublicSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 305, 3), unicode_default='current'))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReplacedBy'), pyxb.binding.datatypes.string, scope=PublicSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 315, 3)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Replaces'), pyxb.binding.datatypes.string, scope=PublicSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 316, 3)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Title'), pyxb.binding.datatypes.string, scope=PublicSetType, documentation='The title is contructed from the concatenation of the description of the variation and the phenotype.\n\t\t\t\t\tIn the database it is extracted from the title of RCV accession', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 317, 3)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DeletedSCVList'), CTD_ANON_3, scope=PublicSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 331, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 315, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 316, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 317, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 323, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 331, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'RecordStatus')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 305, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'ReplacedBy')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 315, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Replaces')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 316, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Title')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 317, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceClinVarAssertion')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 323, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClinVarAssertion')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 330, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'DeletedSCVList')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 331, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PublicSetType._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SCV'), typeDeletedSCV, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 334, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'SCV')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 334, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




typeDeletedSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Accession'), CTD_ANON_4, scope=typeDeletedSCV, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 348, 3)))

typeDeletedSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, scope=typeDeletedSCV, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 358, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 358, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(typeDeletedSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'Accession')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 348, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(typeDeletedSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 358, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
typeDeletedSCV._Automaton = _BuildAutomaton_5()




ReleaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClinVarSet'), PublicSetType, scope=ReleaseType, documentation='The ClinVarSet is used to group the aggregate record (RCV accession)\n\t\t\twith the submissions underlying it (SCV accessions) \n\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 3, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReleaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClinVarSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 364, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReleaseType._Automaton = _BuildAutomaton_6()




MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ClinVarSubmissionID'), CTD_ANON_5, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 375, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ClinVarAccession'), CTD_ANON_24, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 393, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AdditionalSubmitters'), CTD_ANON_6, scope=MeasureTraitType, documentation='Optional element used only if there are multiple submitters. When there are multiple, each is listed \n\t\t\t\t\t\tin this element. \n\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 415, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RecordStatus'), STD_ANON_7, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 427, 3), unicode_default='current'))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance'), ClinicalSignificanceTypeSCV, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 436, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CustomAssertionScore'), CTD_ANON_7, scope=MeasureTraitType, documentation='\n\t\t\t\t\t\tUsed to represent the scoring matrix a submitter may use to \n\t\t\t\t\t\tevaluate clinical signficance. \n\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 437, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assertion'), AssertionTypeSCV, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 453, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ExternalID'), XrefType, scope=MeasureTraitType, documentation='XrefType is used to identify data source(s) and their identifiers.\n\t\t\t\t\tOptional because not all sources have an ID specific to the assertion. \n\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 454, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_8, scope=MeasureTraitType, documentation='AttributeSet is a package to represent a unit of information,\n\t\t\t\t\t\tthe source(s) of that unit, identifiers representing that unit, and comments.\n\t\t\t\t ', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 461, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ObservedIn'), ObservationSet, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 497, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MeasureSet'), MeasureSetType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 499, 5)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GenotypeSet'), GenotypeSetType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 500, 4)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TraitSet'), ClinAsserTraitSetType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 502, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 503, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StudyName'), pyxb.binding.datatypes.string, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 504, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StudyDescription'), pyxb.binding.datatypes.string, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 505, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 506, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 415, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 437, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 454, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 461, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 503, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 504, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 505, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 506, 3))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'ClinVarSubmissionID')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 375, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'ClinVarAccession')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 393, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'AdditionalSubmitters')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 415, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'RecordStatus')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 427, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 436, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'CustomAssertionScore')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 437, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Assertion')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 453, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'ExternalID')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 454, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 461, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'ObservedIn')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 497, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'MeasureSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 499, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'GenotypeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 500, 4))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'TraitSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 502, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 503, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'StudyName')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 504, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'StudyDescription')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 505, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 506, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasureTraitType._Automaton = _BuildAutomaton_7()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SubmitterDescription'), SubmitterType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 423, 5)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'SubmitterDescription')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 423, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_8()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 446, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 447, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 446, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 447, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 446, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 447, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_9()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_25, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 469, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 491, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 492, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 493, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 491, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 492, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 493, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 469, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 491, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 492, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 493, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_10()




ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ClinVarAccession'), CTD_ANON_26, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 522, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RecordStatus'), STD_ANON_10, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 547, 3), unicode_default='current'))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance'), ClinicalSignificanceType, scope=ReferenceAssertionType, documentation='Either the value corresponding to the scoring system of the ACMG, or \n\t\t\t\t\ta value representing such concepts as drug response, risk factors, etc.', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 556, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assertion'), AssertionTypeRCV, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 562, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ExternalID'), XrefType, scope=ReferenceAssertionType, documentation='Represents the public identifier a source may have for this record. \n\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 563, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_9, scope=ReferenceAssertionType, documentation='Many concepts in the database are represented by what ClinVar terms an AttributeSet, \n\t\t\t\t\t\twhich is an open-ended structure providing the equivalent of a type of information, the value(s) for that data type, \n\t\t\t\t\t\tsubmitter(s), free text comment(s) describing that attribute, identifier(s) for that attribute, and \n\t\t\t\t\t\tcitation(s) related to that attribute.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 569, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ObservedIn'), ObservationSet, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 602, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MeasureSet'), MeasureSetType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 604, 5)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GenotypeSet'), GenotypeSetType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 605, 4)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TraitSet'), TraitSetType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 607, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 608, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 609, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 556, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 563, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 569, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 602, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 608, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 609, 3))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ClinVarAccession')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 522, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'RecordStatus')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 547, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 556, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'Assertion')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 562, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ExternalID')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 563, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 569, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ObservedIn')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 602, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'MeasureSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 604, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'GenotypeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 605, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'TraitSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 607, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 608, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 609, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferenceAssertionType._Automaton = _BuildAutomaton_11()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_27, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 579, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 596, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 597, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 598, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 596, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 597, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 598, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 596, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 597, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 598, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_12()




MeasureSetAttributeSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_28, scope=MeasureSetAttributeSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 618, 3)))

MeasureSetAttributeSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=MeasureSetAttributeSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 656, 3)))

MeasureSetAttributeSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=MeasureSetAttributeSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 657, 3)))

MeasureSetAttributeSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=MeasureSetAttributeSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 658, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 656, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 657, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 658, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasureSetAttributeSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 618, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetAttributeSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 656, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetAttributeSet._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 657, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetAttributeSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 658, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasureSetAttributeSet._Automaton = _BuildAutomaton_13()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_29, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 720, 6)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 729, 6)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 730, 6)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_10, documentation='table_type = 38', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 731, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 729, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 730, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 731, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 720, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 729, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 730, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 731, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_14()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_30, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 763, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 772, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 773, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 774, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 772, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 773, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 774, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 763, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 772, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 773, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 774, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_15()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_32, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 786, 9)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 795, 9)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 796, 9)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 797, 9)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 795, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 796, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 797, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 786, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 795, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 796, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 797, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_16()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_33, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 848, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 857, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 858, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_13, documentation='table_type = 38', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 859, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 857, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 858, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 859, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 848, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 857, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 858, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 859, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_17()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_34, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 893, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 902, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 903, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 904, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 902, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 903, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 904, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 893, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 902, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 903, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 904, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_18()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_36, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 916, 9)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 925, 9)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 926, 9)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 927, 9)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 925, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 926, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 927, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 916, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 925, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 926, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 927, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_19()




SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ElementValue'), CTD_ANON_16, scope=SetElementSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 990, 3)))

SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=SetElementSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 999, 3)))

SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=SetElementSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1000, 3)))

SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=SetElementSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1001, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 999, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1000, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1001, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'ElementValue')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 990, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 999, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1000, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1001, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SetElementSetType._Automaton = _BuildAutomaton_20()




MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NamePlatform'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1034, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TypePlatform'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1035, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Purpose'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1036, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ResultType'), STD_ANON_21, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1037, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MinReported'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1047, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MaxReported'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1048, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReferenceStandard'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1049, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1050, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1051, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, scope=MethodType, documentation=' Free text to enrich the description of the method and to\n                        provide information not captured in specific fields. ', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1052, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Software'), SoftwareSet, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1058, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SourceType'), STD_ANON_22, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1059, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MethodType'), Methodtypelist, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1068, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MethodAttribute'), CTD_ANON_17, scope=MethodType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1069, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MethodResult'), AttributeType, scope=MethodType, documentation=' MethodResult is used to represent results specific to a particular method.\n                        An example is a method used to validate the the variant call; the MethodResult would be pass/fail/inconclusive', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1097, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1034, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1035, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1036, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1037, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1047, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1048, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1049, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1050, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1051, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1052, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1058, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1059, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1069, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1097, 3))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'NamePlatform')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1034, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'TypePlatform')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1035, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'Purpose')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1036, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'ResultType')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1037, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'MinReported')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1047, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'MaxReported')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1048, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'ReferenceStandard')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1049, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1050, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1051, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1052, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'Software')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1058, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'SourceType')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1059, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'MethodType')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1068, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'MethodAttribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1069, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, 'MethodResult')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1097, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MethodType._Automaton = _BuildAutomaton_21()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_37, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1072, 6)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1093, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1093, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1072, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1093, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_22()




ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Sample'), SampleType, scope=ObservationSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1114, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Method'), CTD_ANON_38, scope=ObservationSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1115, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ObservedData'), CTD_ANON_18, scope=ObservationSet, documentation='This is an AttributeSet, there will be 1 attribute supported by optional citations, xrefs and comment. \n\t\t\t\t\t\tThere must be at least one ObservedData Set, but can be any number.\n\t\t\t\t\t\tFor each ObservedData set the Attribute will be either decimal or string depending on type. \n\t\t\t\t\t\tThe value will be stored here, but decimals will be entered to the database as a string.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1141, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Co-occurrenceSet'), Co_occurrenceType, scope=ObservationSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1199, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TraitSet'), ClinAsserTraitSetType, scope=ObservationSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1200, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=ObservationSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1201, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=ObservationSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1202, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=ObservationSet, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1203, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1115, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1199, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1200, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1201, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1202, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1203, 3))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Sample')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1114, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Method')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1115, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'ObservedData')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1141, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Co-occurrenceSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1199, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'TraitSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1200, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1201, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1202, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1203, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationSet._Automaton = _BuildAutomaton_23()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Attribute'), CTD_ANON_39, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1151, 6)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Severity'), SeverityType, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1191, 6)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1192, 6)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1193, 6)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1194, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1191, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1192, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1193, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1194, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'Attribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1151, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'Severity')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1191, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1192, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1193, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1194, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_24()




FamilyInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FamilyHistory'), pyxb.binding.datatypes.string, scope=FamilyInfo, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1215, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1215, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FamilyInfo._UseForTag(pyxb.namespace.ExpandedName(None, 'FamilyHistory')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1215, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FamilyInfo._Automaton = _BuildAutomaton_25()




SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SampleDescription'), CTD_ANON_19, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1225, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Origin'), STD_ANON_26, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1233, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Ethnicity'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1253, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GeographicOrigin'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1254, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Tissue'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1255, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CellLine'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1256, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Species'), CTD_ANON_20, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1257, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Age'), CTD_ANON_40, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1266, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Strain'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1295, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AffectedStatus'), STD_ANON_29, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1296, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumberTested'), pyxb.binding.datatypes.int, scope=SampleType, documentation='Denominator, total individuals included in this observation\n\t\t\t\t\t\tset.', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1307, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumberMales'), pyxb.binding.datatypes.int, scope=SampleType, documentation='Denominator, total males included in this observation\n\t\t\t\t\t\tset.', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1313, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumberFemales'), pyxb.binding.datatypes.int, scope=SampleType, documentation='Denominator, total females included in this observation\n\t\t\t\t\t\tset.', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1319, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NumberChrTested'), pyxb.binding.datatypes.int, scope=SampleType, documentation='Denominator, total number chromosomes tested. Number affected\n\t\t\t\t\t\tand unaffected are captured in the element\n\t\t\t\t\t\tNumberObserved.', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1325, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Gender'), STD_ANON_30, scope=SampleType, documentation='Gender should be used ONLY if explicit values are not available for number of males or females, and there is a need to indicate that the genders in the sample are known. \n                    ', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1332, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FamilyData'), FamilyInfo, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1345, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Proband'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1346, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Indication'), IndicationType, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1347, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1348, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1349, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1350, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SourceType'), STD_ANON_31, scope=SampleType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1351, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1225, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1253, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1254, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1255, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1256, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1257, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1266, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1295, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1307, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1313, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1319, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1325, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1332, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1345, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1346, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1347, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1348, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1349, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1350, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1351, 3))
    counters.add(cc_19)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'SampleDescription')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1225, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Origin')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1233, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Ethnicity')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1253, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'GeographicOrigin')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1254, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Tissue')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1255, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'CellLine')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1256, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Species')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1257, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Age')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1266, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Strain')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1295, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'AffectedStatus')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1296, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'NumberTested')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1307, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'NumberMales')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1313, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'NumberFemales')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1319, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'NumberChrTested')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1325, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Gender')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1332, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'FamilyData')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1345, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Proband')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1346, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Indication')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1347, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1348, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1349, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1350, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, 'SourceType')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1351, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_21._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SampleType._Automaton = _BuildAutomaton_26()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), CommentType, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1228, 6)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1229, 6)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1228, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1229, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1228, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1229, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_27()




Co_occurrenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Zygosity'), ZygosityType, scope=Co_occurrenceType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1366, 3)))

Co_occurrenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AlleleDescSet'), AlleleDescType, scope=Co_occurrenceType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1367, 3)))

Co_occurrenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Count'), pyxb.binding.datatypes.int, scope=Co_occurrenceType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1368, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1366, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1367, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1368, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Co_occurrenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'Zygosity')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1366, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Co_occurrenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'AlleleDescSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1367, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Co_occurrenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'Count')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1368, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Co_occurrenceType._Automaton = _BuildAutomaton_28()




ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReviewStatus'), ReviewStatusType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1373, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, scope=ClinicalSignificanceType, documentation='We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1374, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Explanation'), CommentType, scope=ClinicalSignificanceType, documentation="Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.", location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1380, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1386, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1387, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1388, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1373, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1374, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1380, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1386, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1387, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1388, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, 'ReviewStatus')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1373, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1374, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, 'Explanation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1380, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1386, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1387, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1388, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClinicalSignificanceType._Automaton = _BuildAutomaton_29()




ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReviewStatus'), ReviewStatusType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1394, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Description'), pyxb.binding.datatypes.string, scope=ClinicalSignificanceTypeSCV, documentation='We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1395, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Explanation'), CommentType, scope=ClinicalSignificanceTypeSCV, documentation="Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.", location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1401, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1407, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1408, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1409, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1394, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1395, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1401, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1407, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1408, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1409, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'ReviewStatus')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1394, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1395, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'Explanation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1401, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1407, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1408, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1409, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClinicalSignificanceTypeSCV._Automaton = _BuildAutomaton_30()




AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), pyxb.binding.datatypes.string, scope=AlleleDescType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1418, 3)))

AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RelativeOrientation'), STD_ANON_32, scope=AlleleDescType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1419, 3)))

AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Zygosity'), ZygosityType, scope=AlleleDescType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1428, 3)))

AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance'), ClinicalSignificanceType, scope=AlleleDescType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1429, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1419, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1428, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1429, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1418, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, 'RelativeOrientation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1419, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, 'Zygosity')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1428, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, 'ClinicalSignificance')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1429, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AlleleDescType._Automaton = _BuildAutomaton_31()




MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 33, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 34, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 35, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CytogeneticLocation'), pyxb.binding.datatypes.string, scope=MeasureType, documentation='Cytogenetic location is maintained\n\t\t\t\t\tindependent of sequence location.', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 107, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SequenceLocation'), SequenceLocationType, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 113, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MeasureRelationship'), CTD_ANON_22, scope=MeasureType, documentation='MeasureRelationship is used to represent relationships between \n\t\t\t\t\t\tthe type of measure being represented, and other object.\n\t\t\t\t\t\tThis can be gene/variant, protein/gene, etc., as in when a variation is reported to be within a gene.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 114, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 173, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 174, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 175, 3)))

MeasureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Source'), DataSourceType, scope=MeasureType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 176, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 33, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 34, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 35, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 107, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 113, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 114, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 173, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 174, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 175, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 176, 3))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 33, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 34, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 35, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'CytogeneticLocation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 107, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'SequenceLocation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 113, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'MeasureRelationship')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 114, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 173, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 174, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 175, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(MeasureType._UseForTag(pyxb.namespace.ExpandedName(None, 'Source')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 176, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MeasureType._Automaton = _BuildAutomaton_32()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 123, 6)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 124, 6)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 125, 6)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SequenceLocation'), SequenceLocationType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 151, 6)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 152, 6)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 153, 6)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 154, 6)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 123, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 124, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 125, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 151, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 152, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 153, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 154, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 123, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 124, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 125, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'SequenceLocation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 151, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 152, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 153, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 154, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_33()




MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Measure'), MeasureType, scope=MeasureSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 663, 4)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=MeasureSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 664, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=MeasureSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 665, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), MeasureSetAttributeSet, scope=MeasureSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 666, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=MeasureSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 667, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=MeasureSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 668, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=MeasureSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 669, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 664, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 665, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 666, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 667, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 668, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 669, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Measure')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 663, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 664, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 665, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 666, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 667, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 668, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 669, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasureSetType._Automaton = _BuildAutomaton_34()




GenotypeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MeasureSet'), MeasureSetType, scope=GenotypeSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 693, 4)))

GenotypeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=GenotypeSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 694, 3)))

GenotypeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=GenotypeSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 695, 3)))

GenotypeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), MeasureSetAttributeSet, scope=GenotypeSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 696, 3)))

GenotypeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=GenotypeSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 697, 3)))

GenotypeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=GenotypeSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 698, 3)))

GenotypeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=GenotypeSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 699, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 694, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 695, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 696, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 697, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 698, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 699, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenotypeSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'MeasureSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 693, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenotypeSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 694, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenotypeSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 695, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GenotypeSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 696, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GenotypeSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 697, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(GenotypeSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 698, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(GenotypeSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 699, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenotypeSetType._Automaton = _BuildAutomaton_35()




TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Trait'), TraitType, scope=TraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 714, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=TraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 715, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=TraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 716, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_10, scope=TraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 717, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=TraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 739, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=TraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 740, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=TraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 741, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 715, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 716, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 717, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 739, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 740, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 741, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Trait')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 714, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 715, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 716, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 717, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 739, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 740, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 741, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TraitSetType._Automaton = _BuildAutomaton_36()




TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 758, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 759, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_11, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 760, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TraitRelationship'), CTD_ANON_31, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 778, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 819, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 820, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 821, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Source'), DataSourceType, scope=TraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 822, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 759, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 760, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 778, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 819, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 820, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 821, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 822, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 758, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 759, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 760, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'TraitRelationship')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 778, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 819, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 820, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 821, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Source')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 822, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TraitType._Automaton = _BuildAutomaton_37()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 781, 6)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 782, 6)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_12, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 783, 6)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 801, 6)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 802, 6)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Source'), DataSourceType, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 803, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 781, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 782, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 783, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 801, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 802, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 803, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 781, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 782, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 783, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 801, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 802, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'Source')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 803, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_38()




ClinAsserTraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Trait'), ClinAsserTraitType, scope=ClinAsserTraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 842, 3)))

ClinAsserTraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=ClinAsserTraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 843, 3)))

ClinAsserTraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=ClinAsserTraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 844, 3)))

ClinAsserTraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_13, scope=ClinAsserTraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 845, 3)))

ClinAsserTraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=ClinAsserTraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 867, 3)))

ClinAsserTraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=ClinAsserTraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 868, 3)))

ClinAsserTraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=ClinAsserTraitSetType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 869, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 843, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 844, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 845, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 867, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 868, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 869, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Trait')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 842, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 843, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 844, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 845, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 867, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 868, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 869, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClinAsserTraitSetType._Automaton = _BuildAutomaton_39()




ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 888, 3)))

ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 889, 3)))

ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_14, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 890, 3)))

ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TraitRelationship'), CTD_ANON_35, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 908, 3)))

ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 949, 3)))

ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 950, 3)))

ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 951, 3)))

ClinAsserTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Source'), DataSourceType, scope=ClinAsserTraitType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 952, 3)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 888, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 889, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 890, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 908, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 949, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 950, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 951, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 952, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 888, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 889, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 890, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'TraitRelationship')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 908, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 949, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 950, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 951, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ClinAsserTraitType._UseForTag(pyxb.namespace.ExpandedName(None, 'Source')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 952, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClinAsserTraitType._Automaton = _BuildAutomaton_40()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 911, 6)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 912, 6)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), CTD_ANON_15, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 913, 6)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 931, 6)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 932, 6)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Source'), DataSourceType, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 933, 6)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 911, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 912, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 913, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 931, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 932, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 933, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 911, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 912, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 913, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 931, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 932, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'Source')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 933, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_41()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Type'), STD_ANON_24, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1120, 8)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1116, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1034, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1035, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1036, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1037, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1047, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1048, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1049, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1050, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1051, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1052, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1058, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1059, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1069, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1097, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1120, 8))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'NamePlatform')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1034, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'TypePlatform')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1035, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'Purpose')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1036, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'ResultType')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1037, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'MinReported')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1047, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'MaxReported')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1048, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'ReferenceStandard')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1049, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1050, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1051, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'Description')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1052, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'Software')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1058, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'SourceType')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1059, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'MethodType')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1068, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'MethodAttribute')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1069, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'MethodResult')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1097, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(None, 'Type')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1120, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_42()




IndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Trait'), ClinAsserTraitType, scope=IndicationType, documentation='Represent the value for the test indication as a name of a\n\t\t\t\t\t\ttrait.                     ', location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1435, 3)))

IndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Name'), SetElementSetType, scope=IndicationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1441, 3)))

IndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Symbol'), SetElementSetType, scope=IndicationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1442, 3)))

IndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AttributeSet'), AttributeType, scope=IndicationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1443, 3)))

IndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Citation'), CitationType, scope=IndicationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1445, 3)))

IndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XRef'), XrefType, scope=IndicationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1446, 3)))

IndicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Comment'), CommentType, scope=IndicationType, location=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1447, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1441, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1442, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1443, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1445, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1446, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1447, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IndicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'Trait')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1435, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IndicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'Name')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1441, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IndicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'Symbol')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1442, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IndicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'AttributeSet')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1443, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IndicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'Citation')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1445, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IndicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'XRef')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1446, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(IndicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'Comment')), pyxb.utils.utility.Location('/Users/pagarcia/work/clinvarNewSchema/june-2017/pythonSchema/pyxb/clinvar_public_1.47.xsd', 1447, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IndicationType._Automaton = _BuildAutomaton_43()

