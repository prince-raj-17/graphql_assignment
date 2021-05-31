from django.db.models import fields
import graphene
from graphene_django import DjangoObjectType
from .models import Bank, Branch


class BankType(DjangoObjectType):
   class Meta:
       model = Bank
       fields = ("id","name","branches")
    
class BranchType(DjangoObjectType):
   class Meta:
        model = Branch
       
class Query(graphene.ObjectType):
    all_branch = graphene.List(BranchType)
    all_banks = graphene.List(BankType)
    bank_by_name = graphene.List(BankType,name=graphene.String(required=True))

    def resolve_all_branch(root, info):
        return Branch.objects.select_related('bank').all()
    
    def resolve_all_banks(root,info):
        return Bank.objects.prefetch_related('branches').all()
    
    def resolve_bank_by_name(root,info,name):
        return Bank.objects.filter(name=name)

schema = graphene.Schema(query=Query)

    
    