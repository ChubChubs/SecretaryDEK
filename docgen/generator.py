__author__ = 'masterbob'
#from .models import Fields, Doc
from docxtpl import DocxTemplate
from importlib import import_module
import time
import datetime
import os.path
import sys
from django.conf import settings


def gen_a_doc(doc_name, preparation_module = None, obj=None):
    """
    :param doc_name:
     It is a string, that contains a template name to render.
     Like if we have a report_template.docx than
     to the doc_name should be passed a string 'report_template'
     Nota Bene! There is to be a data-cooker. Called the same as the template
     For example: report_template.py
     And it has to contain a method context(), that returns
     a context dictionary for jinja2 rendering engine.
    :return:
    An file name located in TMP_DEST
    """
    if preparation_module is None:
        preparation_module = doc_name # WOODOO MAGIC !!!!
    DOC_TEMPLATES_DIR = getattr(settings, "DOC_TEMPLATES_DIR", None)
    DOC_CONTEXT_GEN_DIR = getattr(settings, "DOC_CONTEXT_GEN_DIR", None)
    PROJECT_ROOT = getattr(settings, "PROJECT_ROOT", None)
    TMP_DEST = getattr(settings, "TMP_DEST", None)
    TMP_URL = getattr(settings, "TMP_URL", None)

    doc = DocxTemplate(os.path.join(PROJECT_ROOT, os.path.join(DOC_TEMPLATES_DIR, doc_name+'.docx')))
    print(os.path.join(PROJECT_ROOT, os.path.join(DOC_CONTEXT_GEN_DIR, preparation_module)))
    context_getter = import_module(preparation_module)
    context = getattr(context_getter, "context")()
    doc.render(context)
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    completeName = os.path.join(TMP_DEST, doc_name+st+'.docx')
    doc.save(completeName)
    return TMP_URL + doc_name + st + '.docx'
    #getattr /home/masterbob/WORK/django/SecretaryDEK/doc_templates

def gen_many_docs(doc_name, preparation_module = None):
    """
    :param doc_name:
    :param preparation_module:
    :return:
    """

    if preparation_module is None:
        preparation_module = doc_name # WOODOO MAGIC !!!!
    DOC_TEMPLATES_DIR = getattr(settings, "DOC_TEMPLATES_DIR", None)
    DOC_CONTEXT_GEN_DIR = getattr(settings, "DOC_CONTEXT_GEN_DIR", None)
    PROJECT_ROOT = getattr(settings, "PROJECT_ROOT", None)
    TMP_DEST = getattr(settings, "TMP_DEST", None)
    TMP_URL = getattr(settings, "TMP_URL", None)

    doc = DocxTemplate(os.path.join(PROJECT_ROOT, os.path.join(DOC_TEMPLATES_DIR, doc_name+'.docx')))
    print(os.path.join(PROJECT_ROOT, os.path.join(DOC_CONTEXT_GEN_DIR, preparation_module)))
    context_getter = import_module(preparation_module)
    names, contexts = getattr(context_getter, "contexts")()
    print ("pong")
    print (names, contexts)
    print ("pong")
    ret = []
    for (name, context) in zip(names, contexts):
            print ("pong")
            print (name, context)
            print ("pong")
            doc.render(context)
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
            completeName = os.path.join(TMP_DEST, doc_name+name+st+'.docx')
            doc.save(completeName)
            ret.append(TMP_URL + doc_name +name+ st + '.docx')
    return ret