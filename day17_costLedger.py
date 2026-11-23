"""Theory of a cost ledger.

A cost ledger is a set of accounting records used to collect and classify the
costs of producing goods or providing services. It gives managers detailed
cost information that complements the summarized expense accounts in the
general ledger.

Common cost categories include:
- Direct materials: materials traceable to a product, job, or service.
- Direct labor: labor directly involved in production or delivery.
- Overhead: indirect costs, such as rent, utilities, and equipment upkeep.

Direct costs are assigned to the relevant cost object. Indirect costs are
collected and allocated using an appropriate cost driver, such as labor hours
or machine hours. Costs may be organized by job, process, department, or
activity, depending on the business.

Cost-ledger information helps calculate unit costs, prepare budgets, evaluate
actual performance against estimates, and inform pricing decisions. Regular
reconciliation with general-ledger control accounts supports accurate records.
Consistent, reasonable classification and allocation are essential because
cost information influences management decisions.
"""
'''files=[{"file":"a.pdf","cost":0.03}, 
    {"file":"b.pdf","cost":0.10}, 
    {"file":"c.pdf","cost":0.02}, 
       ]
total_spend=0
total_save=0
for f in files:
    if f["cost"] <= 0.05:
        print(f["file"],"- SEND - SPEND",f["cost"])
        total_spend=total_spend+ f["cost"]
    else:
        print(f["file"],"stop - save",f["cost"])
        total_save=total_save +f["cost"]

print("total_spend",total_spend)
print("total_save",total_save)'''


files=[{"file":"x.pdf","cost":0.01}, 
    {"file":"y.pdf","cost":0.08}, 
    {"file":"z.pdf","cost":0.04}, 
    {"file":"w.pdf","cost":0.12}, 
       ]
total_spend=0
total_save=0
for f in files:
    if f["cost"] <= 0.05:
        print(f["file"],"SEND - SPEND ",f["cost"])
        total_spend=total_spend+ f["cost"]
    else:
        print(f["file"],"STOP - SAVE",f["cost"])
        total_save=total_save+ f["cost"]
print("Total spend : ",total_spend)
print("Total save : ",total_save)